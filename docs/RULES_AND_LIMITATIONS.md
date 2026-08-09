# Rules, hierarchy, and limitations

## Authority hierarchy

This repository is an implementation aid, not a source of institutional authority. When requirements differ, use the following order:

1. a newer applicable national, Ministry of Education, or HNU rule;
2. the controlling 2025 HNU rule PDF;
3. an approved college-level rule or disciplinary convention where the HNU rule permits it; then
4. a supplied layout sample, only for visual interpretation and never as a substitute for the rule; then
5. this project’s documented interpretation and generated review prompts.

The primary public rule source used for this project is the 2025 Hunan University notice **“Hunan University Graduate Thesis or Practice Outcome Writing Specification” (HNU Graduate Affairs [2025] No. 17)**:

- [Notice page](https://arch.hnu.edu.cn/info/1339/5544.htm)
- [Official PDF](https://arch.hnu.edu.cn/__local/3/0A/1F/C26F685925C840FAF8C54833458_2C3C04AE_557E4.pdf)

The links are for checking the current source. The project does not redistribute the PDFs, examples, templates, logo assets, or other official materials.

## Standard-currentness caveat

The 2025 HNU source cites GB/T 7714-2015. The national registry records [GB/T 7714-2015 as abolished](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=7FA63E9BBA56E60471AEDAEBDE44B14C) and [GB/T 7714-2025 as current from 2026-07-01](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=C6CE52E55AC09B9C79A20AEA77CEDD14). The tool does not rewrite bibliographic content and makes no claim of comprehensive GB/T 7714 compliance. Before submission, obtain the current HNU/college position on which citation standard governs your document.

The HNU source also cites the 1986 GB 3100–3102 quantity-and-unit family. The national registry identifies 1993 replacements including [GB/T 3101-1993](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=6B20B8B934FD23161550CF80BEC0F507) and [GB/T 3102.1-1993](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=FAB825C0FA7292DB32BFC80F0BAA685C). The tool treats physical quantity and unit semantics as manual review only, not national-standard certification.

## Supported target

The automated command surface is designed for the `academic_phd` workflow. It applies conservative formatting only to recognised paragraph types and positively recognised scholarly tables. It is not a general template generator and does not claim support for professional degrees, master’s dissertations, practice-outcome reports, or a particular college’s custom cover and submission requirements.

## What automation cannot decide

The tool cannot authoritatively determine:

- whether a source rule is current or applies to your programme;
- whether abstract languages are semantically equivalent;
- bibliographic completeness or correctness under GB/T 7714 or another applicable citation standard;
- final cover, declaration, confidentiality, signature, binding, or submission-system compliance;
- layout involving fields, drawings, text boxes, equations, complex tables, tracked changes, template-specific XML, or pre-existing non-empty headers and footers; or
- whether the rendered document has page-break, line-wrap, font-substitution, overlap, or clipping defects.

The formatter preserves existing non-empty headers and complex/uncertain content rather than guessing a rewrite. Treat those areas as report-only/manual review, run the tool on a copy, preserve the original, then inspect the resulting DOCX in the required Word environment. Escalate conflicts to the authorized school or programme contact rather than changing a document based only on automation.

## Change discipline

Rule changes need a publicly verifiable source, a precise locator, a declared scope, and a synthetic test. If the source is ambiguous, the project should prefer an explicit manual-review prompt over an irreversible rewrite.
