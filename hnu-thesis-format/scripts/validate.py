from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass

from . import constants as C
from .report_html import write_html_report
from .safety import (UnsafeDocumentError, atomic_write_text, load_docx,
                     validate_output_paths)


@dataclass
class Issue:
    category: str
    severity: str
    location: str
    message: str
    rule: str
    fix: str = ""
    rule_id: str = ""


def _match(key, text):
    return re.match(C.REGEX[key], text)


def _location(index, paragraph, include_sensitive_details):
    location = "Paragraph {}".format(index + 1)
    if include_sensitive_details:
        excerpt = re.sub(r"\s+", " ", paragraph.text.strip())[:60]
        if excerpt:
            location += ": " + excerpt
    return location


def classify_paragraph(text):
    if _match("abstract_zh", text): return "abstract_title_zh"
    if _match("abstract_en", text): return "abstract_title_en"
    if _match("toc_title", text): return "toc_title"
    if _match("chapter", text): return "chapter"
    if _match("heading3", text): return "heading3"
    if _match("heading2", text): return "heading2"
    if _match("heading1", text): return "heading1"
    if _match("caption_table", text): return "caption_table"
    if _match("caption_figure", text): return "caption_figure"
    if _match("reference_item", text): return "reference"
    if any(_match(key, text) for key in ("conclusion", "reference_heading", "appendix", "achievements", "acknowledgements", "defense")):
        return "unnumbered_chapter"
    if _match("keywords_zh", text): return "keyword_zh"
    if _match("keywords_en", text): return "keyword_en"
    return None


def paragraph_section_indices(doc):
    indices = []
    section_index = 0
    for paragraph in doc.paragraphs:
        indices.append(section_index)
        ppr = paragraph._p.pPr
        if ppr is not None and ppr.sectPr is not None:
            section_index += 1
    return indices


def find_landmarks(doc):
    section_map = paragraph_section_indices(doc)
    result = {}
    for index, paragraph in enumerate(doc.paragraphs):
        text = paragraph.text.strip()
        if "abstract" not in result and _match("abstract_zh", text):
            result["abstract"] = (index, section_map[index])
        if "toc" not in result and _match("toc_title", text):
            result["toc"] = (index, section_map[index])
    for index, paragraph in enumerate(doc.paragraphs):
        text = paragraph.text.strip()
        section_index = section_map[index]
        after_toc = "toc" not in result or (index > result["toc"][0] and section_index > result["toc"][1])
        style_name = paragraph.style.name.lower() if paragraph.style is not None else ""
        if after_toc and not style_name.startswith("toc") and _match("chapter", text):
            result["main"] = (index, section_index)
            break
    return result


def check_page_geometry(doc, issues):
    for index, section in enumerate(doc.sections):
        location = "Section {}".format(index + 1)
        dimensions = (section.page_width, section.page_height)
        if any(value is None for value in dimensions):
            issues.append(Issue("页面", "error", location, "纸张尺寸为未显式设置或不受支持的值。", C.RULE_LOCATORS["page"], "在Word中显式设置A4纸张尺寸。"))
        elif any(abs(got - wanted) > 0.6 for got, wanted in zip(
                sorted(round(value.mm, 1) for value in dimensions), sorted((210.0, 297.0)))):
            issues.append(Issue("页面", "error", "Section {}".format(index + 1), "纸张尺寸不是A4。", C.RULE_LOCATORS["page"], "设置为210mm × 297mm。"))
        for label, value, wanted in (("上边距", section.top_margin, 25), ("下边距", section.bottom_margin, 25),
                                     ("左边距", section.left_margin, 30), ("右边距", section.right_margin, 30),
                                     ("页眉距边界", section.header_distance, 10), ("页脚距边界", section.footer_distance, 10)):
            if value is None:
                issues.append(Issue("页面", "error", location, "{}为未显式设置或不受支持的值。".format(label), C.RULE_LOCATORS["page"], "在Word中显式设置该项。"))
            elif abs(value.mm - wanted) > 0.6:
                issues.append(Issue("页面", "error", location, "{}不符合要求。".format(label), C.RULE_LOCATORS["page"], "运行formatter调整。"))


def check_structure(doc, issues):
    found = {key: False for key in C.REQUIRED_SECTIONS}
    for paragraph in doc.paragraphs:
        for key in found:
            if _match(key, paragraph.text.strip()): found[key] = True
    for key, label in C.REQUIRED_SECTIONS.items():
        if not found[key]:
            issues.append(Issue("结构", "error", label, "未识别到规定组成部分。", C.RULE_LOCATORS["structure"], "确认内容是否缺失或标题是否采用非标准写法。"))


def check_keywords(doc, issues, include_sensitive_details):
    for index, paragraph in enumerate(doc.paragraphs):
        text = paragraph.text.strip()
        if not (_match("keywords_zh", text) or _match("keywords_en", text)): continue
        rest = re.split(r"[:：]", text, maxsplit=1)
        terms = [term.strip() for term in re.split(r"[；;，,]", rest[-1]) if term.strip()]
        if not 3 <= len(terms) <= 6:
            issues.append(Issue("关键词", "warning", _location(index, paragraph, include_sensitive_details),
                                "检测到{}个关键词；官方口径为3–6个。".format(len(terms)), C.RULE_LOCATORS["keywords"], "核对中英文对应后调整。"))


def _range_text(doc, start_key, end_keys):
    collecting = False
    values = []
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if not collecting and _match(start_key, text):
            collecting = True
            continue
        if collecting and any(_match(key, text) for key in end_keys): break
        if collecting: values.append(text)
    return "\n".join(values)


def check_abstract(doc, issues, thesis_type):
    zh_text = _range_text(doc, "abstract_zh", ("keywords_zh", "abstract_en", "toc_title"))
    count = len(re.findall(r"[\u4e00-\u9fff]", zh_text))
    expected = C.THESIS_TYPES[thesis_type]["abstract_chars_about"]
    if count and count < expected // 2:
        issues.append(Issue("摘要", "info", "中文摘要", "中文摘要字符数明显低于约{}字的参考值。".format(expected), C.RULE_LOCATORS["abstract"], "人工复核摘要完整性。"))
    if re.search(r"[\[［]\d+[\]］]", zh_text):
        issues.append(Issue("摘要", "warning", "中文摘要", "摘要中检测到引用编号。", C.RULE_LOCATORS["abstract"], "人工核对并移除摘要引用编号。"))
    if re.search(r"(?:图|表)\s*\d|公式|式[（(]\d+", zh_text):
        issues.append(Issue("摘要", "warning", "中文摘要", "摘要中可能含图、表或公式引用。", C.RULE_LOCATORS["abstract"], "人工核对摘要内容。"))


def check_headings(doc, issues, include_sensitive_details):
    main_index = find_landmarks(doc).get("main", (len(doc.paragraphs), 0))[0]
    for index, paragraph in enumerate(doc.paragraphs):
        if index < main_index: continue
        text = paragraph.text.strip()
        if not _match("chapter", text): continue
        title = re.sub(r"^第\s*[0-9一二三四五六七八九十百]+\s*章\s*", "", text)
        location = _location(index, paragraph, include_sensitive_details)
        if len(re.sub(r"\s+", "", title)) > 15:
            issues.append(Issue("标题", "info", location, "章标题超过15字的一般建议。", C.RULE_LOCATORS["headings"], "由作者判断是否精简。"))
        if re.search(r"[，。！？；：,.!?;:]", title):
            issues.append(Issue("标题", "warning", location, "章标题含标点。", C.RULE_LOCATORS["headings"], "人工核对标题。"))
        if re.search(r"[\[［]\d+[\]］]", text):
            issues.append(Issue("标题", "error", location, "标题含参考文献标注。", C.RULE_LOCATORS["headings"], "将引文标注移至正文。"))


def check_numbering_boundaries(doc, issues):
    landmarks = find_landmarks(doc)
    if "abstract" not in landmarks or "main" not in landmarks:
        issues.append(Issue("页码", "warning", "Section boundaries", "无法同时识别中文摘要与正文第一章。", C.RULE_LOCATORS["numbering"], "人工确认分节与页码起点。"))
    elif landmarks["abstract"][1] == landmarks["main"][1]:
        issues.append(Issue("页码", "error", "Section {}".format(landmarks["abstract"][1] + 1), "中文摘要与正文第一章位于同一节，无法安全设置两套页码。", C.RULE_LOCATORS["numbering"], "在正文第一章前插入下一页分节符后重试。"))


def _reference_texts(doc):
    collecting = False
    refs = []
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if not collecting and _match("reference_heading", text): collecting = True; continue
        if collecting and any(_match(key, text) for key in ("appendix", "achievements", "acknowledgements", "defense")): break
        if collecting and _match("reference_item", text): refs.append(text)
    return refs


def check_counts(doc, issues, thesis_type):
    config = C.THESIS_TYPES[thesis_type]
    cjk = len(re.findall(r"[\u4e00-\u9fff]", "\n".join(p.text for p in doc.paragraphs)))
    if cjk < config["word_count_min"]:
        issues.append(Issue("字数", "info", "全文", "中文字符估算低于博士论文一般要求。", C.RULE_LOCATORS["structure"], "以Word字数统计和学院口径复核。"))
    refs = _reference_texts(doc)
    foreign = sum(len(re.findall(r"[A-Za-z]", ref)) >= 8 for ref in refs)
    if not refs:
        issues.append(Issue("参考文献", "error", "参考文献", "未识别到任何编号参考文献条目。", C.RULE_LOCATORS["references"], "确认参考文献表存在并采用[n]顺序编码，或核对非标准标题/编号。", "REFERENCE_ITEMS_MISSING"))
    elif len(refs) < config["reference_min"]:
        issues.append(Issue("参考文献", "warning", "参考文献", "参考文献数量低于{}篇。".format(config["reference_min"]), C.RULE_LOCATORS["references"], "补足或确认学院备案规则。"))
    if foreign < config["foreign_reference_min"]:
        issues.append(Issue("参考文献", "warning", "参考文献", "外文参考文献估算低于{}篇。".format(config["foreign_reference_min"]), C.RULE_LOCATORS["references"], "人工复核语种并补足。"))


def add_manual_notes(issues):
    notes = (("内容", "题目、摘要中英文一致性、术语、量和单位需人工复核。"),
             ("声明", "声明文字与手写签名有效性需人工复核。"),
             ("图表公式", "图表技术内容、公式换行及物理量斜体需人工复核。"),
             ("装订", "单面起页、空白背面和装订要求仅作人工复核。"))
    for category, message in notes:
        issues.append(Issue(category, "info", "人工复核", message, C.RULE_LOCATORS["manual"], "导出PDF后逐页检查。"))
    issues.append(Issue("参考文献", "warning", "规范版本", "HNU 2025文件引用的GB/T 7714-2015已由2026年7月1日实施的GB/T 7714-2025全部代替；本工具仅检查安全的顺序编码基础特征，不声称完成现行标准合规审查。", C.RULE_LOCATORS["standards_currentness"], "提交前确认研究生院和学院当前适用口径。", "STANDARD_CURRENTNESS_GBT7714"))
    issues.append(Issue("量和单位", "info", "规范版本", "HNU文件中的GB3100-3102-86引文具有历史性；国家标准平台列示1993版替代关系，本工具不自动判定量和单位的完整合规性。", C.RULE_LOCATORS["standards_currentness"], "按当前学校要求和现行国家标准人工复核。", "STANDARD_CURRENTNESS_UNITS"))
    issues.append(Issue("页眉", "info", "人工复核", "页眉双线按示范文件视觉尺寸采用上粗下细的约1.5pt/0.75pt效果；官方正文中的“15磅”存在明显歧义。", C.RULE_LOCATORS["numbering"], "在Word或导出PDF中目视核对双线方向与粗细。", "HEADER_BORDER_VISUAL_CHECK"))


def collect_stats(doc, thesis_type):
    refs = _reference_texts(doc)
    return {"paragraphs": len(doc.paragraphs), "sections": len(doc.sections), "tables": len(doc.tables),
            "cjk_chars_approx": len(re.findall(r"[\u4e00-\u9fff]", "\n".join(p.text for p in doc.paragraphs))),
            "reference_count": len(refs), "foreign_reference_count_approx": sum(len(re.findall(r"[A-Za-z]", r)) >= 8 for r in refs),
            "thesis_type": thesis_type}


def validate_document(doc, thesis_type=C.THESIS_TYPE, include_sensitive_details=False):
    if thesis_type not in C.THESIS_TYPES: raise ValueError("Unsupported thesis type")
    issues = []
    check_page_geometry(doc, issues); check_structure(doc, issues)
    check_keywords(doc, issues, include_sensitive_details); check_abstract(doc, issues, thesis_type)
    check_headings(doc, issues, include_sensitive_details); check_numbering_boundaries(doc, issues)
    check_counts(doc, issues, thesis_type); add_manual_notes(issues)
    return issues


def validate_path(path, thesis_type=C.THESIS_TYPE, include_sensitive_details=False):
    doc = load_docx(path)
    return validate_document(doc, thesis_type, include_sensitive_details), collect_stats(doc, thesis_type)


def format_text_report(issues):
    return "\n".join("[{0.severity}] {0.category} - {0.location}: {0.message} ({0.rule})".format(issue) for issue in issues) or "未发现脚本可检测的问题。"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate an HNU 2025 academic doctoral dissertation DOCX without modifying it.")
    parser.add_argument("docx"); parser.add_argument("--thesis-type", default=C.THESIS_TYPE, choices=sorted(C.THESIS_TYPES))
    parser.add_argument("--html-report"); parser.add_argument("--json-report")
    parser.add_argument("--overwrite", action="store_true", help="Replace only the explicitly requested report outputs.")
    parser.add_argument("--report-language", choices=("zh", "en", "bilingual"), default="bilingual")
    parser.add_argument("--include-sensitive-details", action="store_true", help="Include short document excerpts in report locations.")
    args = parser.parse_args(argv)
    try:
        validate_output_paths((args.docx,), (args.html_report, args.json_report), args.overwrite)
        issues, stats = validate_path(args.docx, args.thesis_type, args.include_sensitive_details)
        payload = {"schema_version": 1, "thesis_type": args.thesis_type, "sources": list(C.SOURCES),
                   "issues": [asdict(issue) for issue in issues], "stats": stats}
        if args.json_report:
            atomic_write_text(args.json_report, json.dumps(payload, ensure_ascii=False, indent=2), args.overwrite)
        if args.html_report:
            write_html_report(issues, args.html_report, overwrite=args.overwrite,
                              thesis_type=args.thesis_type, stats=stats, language=args.report_language)
    except (UnsafeDocumentError, OSError, ValueError) as exc:
        parser.error(str(exc))
    print(format_text_report(issues))
    return 1 if any(issue.severity == "error" for issue in issues) else 0


if __name__ == "__main__":
    raise SystemExit(main())
