---
name: hnu-thesis-format
description: Format, audit, or plan an academic doctoral dissertation for Hunan University under the 2025 writing rules. Use for doctoral thesis structure, bilingual front matter, page layout, headings, abstracts, citations, figures, tables, and submission-ready formatting checks; do not use for professional-degree practice reports.
---

# HNU academic doctoral dissertation format

Use this skill only for an academic doctoral dissertation. Treat the official
2025 rule as controlling; the supplied sample explains visual implementation
only. Do not extend a sample detail when the rule is silent.

## Work sequence

1. Confirm that the deliverable is an academic doctoral dissertation and whether
   it is Chinese or a permitted non-Chinese dissertation. If a college or a newer
   HNU/national rule applies, obtain it before formatting.
2. Read [rule-matrix.md](references/rule-matrix.md) for every applicable rule ID.
   Read [content-and-manual-rules.md](references/content-and-manual-rules.md) for
   structure and content, then [layout.md](references/layout.md) before touching
   document styles or sections.
3. Build or audit in this order: bilingual front matter, the single declaration/
   authorization page, bilingual abstracts, table of contents, body, references, appendices, degree-period
   achievements, acknowledgements, and committee-list page. Use placeholders for
   unknown personal or confidential fields.
4. Verify visible output after export to PDF: page size/margins, section starts,
   headers and page-number transitions, no orphaned headings, table/figure
   placement, and citation order. Record each checked rule ID and the rendered
   page(s).
5. Use [hnu-2015-citation-patterns.md](references/hnu-2015-citation-patterns.md) only as synthetic
   patterns reflecting the 2015 standard named in the HNU Rule. Before formatting
   real references, confirm the currently applicable HNU/college citation rule;
   never invent or repair a reference by guesswork.

## Required rule decisions

- Use the official keyword range: **3–6**, not the sample's 3–8 annotation.
- Require at least 50,000 Chinese characters for an academic doctoral thesis;
  obtain any stricter school/college requirement separately.
- Keep Chinese before English for the inner title page and abstract, with each
  English part starting a new page.
- Treat the conclusion as its own unnumbered chapter. Start every body chapter
  on a new page; keep body headings within 15 characters and free of punctuation.
- Apply sequential numeric in-text citations and a matching, hanging-indent
  reference list. Require at least 100 references, including at least 40 foreign-
  language references, unless a controlling newer rule says otherwise.

## Automation boundaries

Read [automation-safety.md](references/automation-safety.md) before running a
formatting macro, script, template transform, or batch audit. Automate reversible
style, section, numbering, and preflight work; do not automate authorship claims,
signatures, confidential classifications, committee data, factual results, or
submission.

## Bundled commands

Work from the skill root. Use a private copy and placeholder-relative paths;
never pass a real title with `--title`, because it can appear in process listings.

```sh
# Validate a private copy; reports are redacted by default.
python3 -m scripts.validate "./<private-copy>/input.docx" \
  --json-report "./<private-output>/validation.json" \
  --html-report "./<private-output>/validation.html"

# Format to a distinct output. Read the private title from a file.
python3 -m scripts.format_thesis "./<private-copy>/input.docx" \
  "./<private-output>/formatted.docx" \
  --title-file "./<private-copy>/title.txt" \
  --json-report "./<private-output>/format-report.json" \
  --html-report "./<private-output>/format-report.html"
```

Do not use `--overwrite` unless replacement is explicitly authorized. The
formatter revalidates its output, but the agent must then reopen the DOCX, export
it to PDF, and visually inspect the rendered pages under the work sequence.
Treat any nonzero status as a review/error condition; never claim submission
readiness from a script result. Preserve the document's footnote-numbering policy
unless the user has confirmed that the humanities rule applies; only then pass
`--humanities-footnotes`.

## Privacy and source handling

Read [privacy.md](references/privacy.md) before opening or sharing a thesis,
sample, or generated artifact. Do not reuse names, titles, identification numbers,
adviser details, institutions, committees, or other example data from source
files. Use neutral placeholders in public instructions and test files.

## Reference map

- [rule-matrix.md](references/rule-matrix.md) — stable rule IDs and exact PDF page locators.
- [content-and-manual-rules.md](references/content-and-manual-rules.md) — doctoral content and manual rules.
- [layout.md](references/layout.md) — page, type, header, pagination, and visual checks.
- [hnu-2015-citation-patterns.md](references/hnu-2015-citation-patterns.md) — synthetic patterns reflecting the HNU-2015 source rule.
- [sources.md](references/sources.md) — authority, provenance, and conflict resolution.
- [privacy.md](references/privacy.md) — publication-safe data handling.
