from __future__ import annotations

import html
from collections import defaultdict
from pathlib import Path

from . import constants as C
from .safety import atomic_write_text

LABELS = {
    "zh": {
        "scope": "适用范围", "sources": "规范来源", "statistics": "统计",
        "issues": "问题清单", "severity": "等级", "category": "类别",
        "location": "位置", "message": "说明", "rule": "规则与定位", "fix": "建议",
        "error": "错误", "warning": "提醒", "info": "人工复核", "none": "未发现脚本可检测的问题",
    },
    "en": {
        "scope": "Scope", "sources": "Official sources", "statistics": "Statistics",
        "issues": "Findings", "severity": "Severity", "category": "Category",
        "location": "Location", "message": "Finding", "rule": "Rule and locator", "fix": "Suggested action",
        "error": "Error", "warning": "Warning", "info": "Manual review", "none": "No machine-detectable issues found",
    },
}


def _esc(value):
    return html.escape(str(value), quote=True)


def _label(language, key):
    if language == "bilingual":
        return LABELS["zh"][key] + " / " + LABELS["en"][key]
    return LABELS[language][key]


def build_html_report(issues, *, title="HNU 2025 Doctoral Thesis Format Report",
                      thesis_type=C.THESIS_TYPE, stats=None, language="bilingual"):
    if language not in {"zh", "en", "bilingual"}:
        raise ValueError("language must be zh, en, or bilingual")
    config = C.THESIS_TYPES[thesis_type]
    stats = stats or {}
    grouped = defaultdict(list)
    for issue in issues:
        grouped[issue.severity].append(issue)
    rows = []
    for severity in ("error", "warning", "info"):
        for issue in grouped[severity]:
            rows.append("<tr class='{0}'><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td></tr>".format(
                _esc(severity), _esc(_label(language, severity)), _esc(issue.category),
                _esc(issue.location), _esc(issue.message), _esc(issue.rule), _esc(issue.fix)))
    if not rows:
        rows.append("<tr><td colspan='6' class='empty'>{}</td></tr>".format(_esc(_label(language, "none"))))
    stats_items = "".join("<li><span>{}</span><b>{}</b></li>".format(_esc(k), _esc(v)) for k, v in stats.items())
    source_language = "en" if language == "en" else "zh"
    source_items = "".join("<li><a href='{url}'>{label}</a></li>".format(
        url=_esc(source["url"]), label=_esc(source["label_" + source_language])) for source in C.SOURCES)
    scope = config["doc_label_en"] if language == "en" else config["doc_label"]
    return """<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><title>{title}</title>
<style>
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC",sans-serif;margin:32px;color:#222;line-height:1.5}}
h1{{font-size:24px;margin:0 0 8px}}h2{{font-size:18px;margin-top:26px;border-bottom:1px solid #ddd;padding-bottom:6px}}
.meta{{color:#666}}.cards{{display:flex;gap:12px;flex-wrap:wrap;margin:18px 0}}.card{{border:1px solid #ddd;border-radius:6px;padding:10px 16px}}
.card b{{display:block;font-size:24px}}.error b,tr.error td:first-child{{color:#b42318}}.warning b,tr.warning td:first-child{{color:#9a6700}}.info b,tr.info td:first-child{{color:#175cd3}}
table{{width:100%;border-collapse:collapse}}th,td{{border:1px solid #ddd;padding:8px;vertical-align:top}}th{{background:#f4f4f4;text-align:left}}
ul.stats{{list-style:none;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:8px}}
ul.stats li{{border:1px solid #ddd;padding:8px;min-width:0}}
ul.stats span{{display:block;color:#666}}ul.stats span,ul.stats b{{overflow-wrap:anywhere;word-break:break-word}}
</style></head><body><h1>{title}</h1><div class="meta">湖大研字〔2025〕17号 · {scope_label}: {scope}</div>
<div class="cards">{cards}</div><h2>{sources_label}</h2><ul>{sources}</ul>
<h2>{stats_label}</h2><ul class="stats">{stats}</ul><h2>{issues_label}</h2>
<table><thead><tr>{headers}</tr></thead><tbody>{rows}</tbody></table></body></html>""".format(
        lang="en" if language == "en" else "zh-CN", title=_esc(title), scope_label=_esc(_label(language, "scope")),
        scope=_esc(scope), cards="".join("<div class='card {0}'><span>{1}</span><b>{2}</b></div>".format(
            severity, _esc(_label(language, severity)), len(grouped[severity])) for severity in ("error", "warning", "info")),
        sources_label=_esc(_label(language, "sources")), sources=source_items,
        stats_label=_esc(_label(language, "statistics")), stats=stats_items or "<li>-</li>",
        issues_label=_esc(_label(language, "issues")), headers="".join("<th>{}</th>".format(_esc(_label(language, key)))
            for key in ("severity", "category", "location", "message", "rule", "fix")), rows="".join(rows))


def write_html_report(issues, output_path, overwrite=False, **kwargs):
    path = Path(output_path)
    return atomic_write_text(path, build_html_report(issues, **kwargs), overwrite)
