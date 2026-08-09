from __future__ import annotations

THESIS_TYPE = "academic_phd"

THESIS_TYPES = {
    THESIS_TYPE: {
        "doc_label": "博士学位论文",
        "doc_label_en": "Academic doctoral dissertation",
        "header_odd": "湖南大学博士学位论文",
        "reference_min": 100,
        "foreign_reference_min": 40,
        "word_count_min": 50_000,
        "abstract_chars_about": 1_200,
    }
}

SOURCES = (
    {
        "id": "official-2025-17",
        "label_zh": "《湖南大学研究生学位论文或实践成果撰写规范》（湖大研字〔2025〕17号），PDF第2–22页",
        "label_en": "HNU Graduate Thesis or Practice Outcome Writing Standard (HNU Graduate Document [2025] No. 17), PDF pp. 2–22",
        "url": "https://arch.hnu.edu.cn/__local/3/0A/1F/C26F685925C840FAF8C54833458_2C3C04AE_557E4.pdf",
    },
    {
        "id": "samr-gbt-7714-2015",
        "label_zh": "全国标准信息公共服务平台：GB/T 7714-2015（已废止）",
        "label_en": "SAMR National Standards platform: GB/T 7714-2015 (abolished)",
        "url": "https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=7FA63E9BBA56E60471AEDAEBDE44B14C",
    },
    {
        "id": "samr-gbt-7714-2025",
        "label_zh": "全国标准信息公共服务平台：GB/T 7714-2025（2026年7月1日实施，全部代替GB/T 7714-2015）",
        "label_en": "SAMR National Standards platform: GB/T 7714-2025 (effective 1 July 2026; replaces GB/T 7714-2015)",
        "url": "https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=C6CE52E55AC09B9C79A20AEA77CEDD14",
    },
    {
        "id": "samr-gbt-3101-1993",
        "label_zh": "全国标准信息公共服务平台：GB/T 3101-1993（代替1986版）",
        "label_en": "SAMR National Standards platform: GB/T 3101-1993 (replaces the 1986 edition)",
        "url": "https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=6B20B8B934FD23161550CF80BEC0F507",
    },
    {
        "id": "samr-gbt-3102-1-1993",
        "label_zh": "全国标准信息公共服务平台：GB/T 3102.1-1993（代替1986版）",
        "label_en": "SAMR National Standards platform: GB/T 3102.1-1993 (replaces the 1986 edition)",
        "url": "https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=FAB825C0FA7292DB32BFC80F0BAA685C",
    },
)

RULE_LOCATORS = {
    "structure": "湖大研字〔2025〕17号，PDF第2–4页",
    "abstract": "湖大研字〔2025〕17号，PDF第4、10页",
    "keywords": "湖大研字〔2025〕17号，PDF第4页；示范文件PDF第11页",
    "headings": "湖大研字〔2025〕17号，PDF第9、19页",
    "references": "湖大研字〔2025〕17号，PDF第7、14–16、19页",
    "page": "湖大研字〔2025〕17号，PDF第18–19页",
    "numbering": "湖大研字〔2025〕17号，PDF第19页；示范文件PDF第11–13页",
    "tables": "湖大研字〔2025〕17号，PDF第13页",
    "footnotes": "湖大研字〔2025〕17号，PDF第12、19页",
    "manual": "湖大研字〔2025〕17号，PDF第2–22页",
    "standards_currentness": "湖大研字〔2025〕17号，PDF第14、17页；全国标准信息公共服务平台",
}

FONT_HEITI = "黑体"
FONT_SONGTI = "宋体"
FONT_LATIN = "Times New Roman"

PAGE = {
    "width_mm": 210.0,
    "height_mm": 297.0,
    "margin_top_mm": 25.0,
    "margin_bottom_mm": 25.0,
    "margin_left_mm": 30.0,
    "margin_right_mm": 30.0,
    "header_distance_mm": 10.0,
    "footer_distance_mm": 10.0,
}

HEADER = {"font_cn": FONT_SONGTI, "font_latin": FONT_LATIN, "pt": 9.0,
          "border_val": "thickThinSmallGap", "border_size_eighths": 12}
FOOTER = {"font_cn": FONT_LATIN, "font_latin": FONT_LATIN, "pt": 9.0}
TABLE = {"top_bottom_border_size_eighths": 12, "middle_border_size_eighths": 6}
KEYWORDS = {"official_min": 3, "official_max": 6, "sample_note_max": 8}

STYLE_SPECS = {
    "chapter": dict(font_cn=FONT_HEITI, font_latin=FONT_LATIN, pt=18.0,
                    alignment="center", space_before_pt=10.0, space_after_pt=30.0,
                    line_spacing_pt=20.0, first_line_indent_pt=0.0,
                    keep_with_next=True, page_break_before=True),
    "unnumbered_chapter": dict(font_cn=FONT_HEITI, font_latin=FONT_LATIN, pt=18.0,
                               alignment="center", space_before_pt=10.0, space_after_pt=30.0,
                               line_spacing_pt=20.0, first_line_indent_pt=0.0,
                               keep_with_next=True, page_break_before=True),
    "heading1": dict(font_cn=FONT_HEITI, font_latin=FONT_LATIN, pt=15.0,
                     alignment="left", space_before_pt=12.0, space_after_pt=12.0,
                     line_spacing_pt=20.0, first_line_indent_pt=0.0, keep_with_next=True),
    "heading2": dict(font_cn=FONT_HEITI, font_latin=FONT_LATIN, pt=14.0,
                     alignment="left", space_before_pt=6.0, space_after_pt=6.0,
                     line_spacing_pt=20.0, first_line_indent_pt=0.0, keep_with_next=True),
    "heading3": dict(font_cn=FONT_HEITI, font_latin=FONT_LATIN, pt=12.0,
                     alignment="left", space_before_pt=6.0, space_after_pt=6.0,
                     line_spacing_pt=20.0, first_line_indent_pt=0.0, keep_with_next=True),
    "body": dict(font_cn=FONT_SONGTI, font_latin=FONT_LATIN, pt=12.0,
                 alignment="justify", space_before_pt=0.0, space_after_pt=0.0,
                 line_spacing_pt=20.0, first_line_indent_pt=24.0),
    "abstract_title_zh": dict(font_cn=FONT_HEITI, font_latin=FONT_LATIN, pt=18.0,
                              alignment="center", space_before_pt=10.0, space_after_pt=30.0,
                              line_spacing_pt=20.0, first_line_indent_pt=0.0, keep_with_next=True),
    "abstract_title_en": dict(font_cn=FONT_LATIN, font_latin=FONT_LATIN, pt=18.0,
                              alignment="center", space_before_pt=10.0, space_after_pt=30.0,
                              line_spacing_pt=20.0, first_line_indent_pt=0.0, keep_with_next=True),
    "keyword_zh": dict(font_cn=FONT_HEITI, font_latin=FONT_LATIN, pt=12.0,
                       alignment="left", space_before_pt=20.0, space_after_pt=0.0,
                       line_spacing_pt=20.0, first_line_indent_pt=0.0),
    "keyword_en": dict(font_cn=FONT_LATIN, font_latin=FONT_LATIN, pt=12.0,
                       alignment="left", space_before_pt=20.0, space_after_pt=0.0,
                       line_spacing_pt=20.0, first_line_indent_pt=0.0),
    "toc_title": dict(font_cn=FONT_HEITI, font_latin=FONT_LATIN, pt=18.0,
                      alignment="center", space_before_pt=10.0, space_after_pt=30.0,
                      line_spacing_pt=20.0, first_line_indent_pt=0.0, keep_with_next=True),
    "toc_level1": dict(font_cn=FONT_HEITI, font_latin=FONT_LATIN, pt=12.0,
                       alignment="left", space_before_pt=0.0, space_after_pt=0.0,
                       line_spacing_pt=20.0, first_line_indent_pt=0.0),
    "caption_table": dict(font_cn=FONT_HEITI, font_latin=FONT_LATIN, pt=10.5,
                          alignment="center", space_before_pt=0.0, space_after_pt=6.0,
                          line_spacing_pt=20.0, first_line_indent_pt=0.0, keep_with_next=True),
    "caption_figure": dict(font_cn=FONT_HEITI, font_latin=FONT_LATIN, pt=10.5,
                           alignment="center", space_before_pt=6.0, space_after_pt=0.0,
                           line_spacing_pt=20.0, first_line_indent_pt=0.0),
    "reference": dict(font_cn=FONT_SONGTI, font_latin=FONT_LATIN, pt=12.0,
                      alignment="justify", space_before_pt=0.0, space_after_pt=0.0,
                      line_spacing_pt=20.0, first_line_indent_pt=0.0,
                      hanging_indent_pt=24.0),
}

REGEX = {
    "abstract_zh": r"^摘\s*要$", "abstract_en": r"^Abstract$",
    "keywords_zh": r"^关键词\s*[:：]", "keywords_en": r"^Key\s+Words?\s*[:：]",
    "toc_title": r"^目\s*录$",
    "chapter": r"^第\s*[0-9一二三四五六七八九十百]+\s*章(?:\s|$)",
    "heading1": r"^[0-9]+\.[0-9]+\s+", "heading2": r"^[0-9]+\.[0-9]+\.[0-9]+\s+",
    "heading3": r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\s+",
    "caption_table": r"^表\s*[0-9A-Z]+\.[0-9]+[\s　]", "caption_figure": r"^图\s*[0-9A-Z]+\.[0-9]+[\s　]",
    "reference_heading": r"^参考文献$", "reference_item": r"^\s*[\[［]\s*\d+\s*[\]］]",
    "appendix": r"^附录\s*[A-ZＡ-Ｚ]", "conclusion": r"^结\s*论$",
    "achievements": r"^攻读学位期间的学术或实践成果$", "acknowledgements": r"^致\s*谢$",
    "defense": r"^答辩委员会名单$", "originality_declaration": r"^学位论文原创性声明$",
    "copyright_authorization": r"^学位论文版权使用授权书$",
}

REQUIRED_SECTIONS = {
    "originality_declaration": "原创性声明", "copyright_authorization": "版权使用授权书",
    "abstract_zh": "中文摘要", "abstract_en": "英文摘要", "toc_title": "目录",
    "reference_heading": "参考文献", "achievements": "攻读学位期间的学术或实践成果",
    "acknowledgements": "致谢", "defense": "答辩委员会名单",
}
