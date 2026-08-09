# HNU Thesis Format

[![CI](https://github.com/helloworldJL/hnu-thesis-format/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/helloworldJL/hnu-thesis-format/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-3776AB.svg)](#requirements)

Privacy-conscious formatting and validation helpers for **Hunan University academic doctoral dissertations** under the 2025 writing specification. The project turns repeatable document checks into a transparent local workflow; it does not replace institutional review or Microsoft Word inspection.

[中文文档](README.zh-CN.md) · [Rules and limits](docs/RULES_AND_LIMITATIONS.md) · [Privacy](docs/PRIVACY.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md)

> **Unofficial project.** This repository is not affiliated with, authorized by, sponsored by, or endorsed by Hunan University (HNU). Always follow the current instructions from your school and programme. Official PDFs and example files are **not redistributed** here.

## What it does

| Capability | What the tool can help with | What still needs a person |
| --- | --- | --- |
| Preflight validation | Checks common A4, margin, heading, abstract, keyword, reference, and structural signals | Whether all requirements apply to your programme and submission batch |
| Formatting pass | Applies a conservative baseline to recognised paragraph types, page geometry, and positively recognised scholarly tables | Existing headers and complex/ambiguous content; final visual integrity, section breaks, and pagination |
| Local reports | Produces redacted JSON and HTML findings plus counts by default | Any opt-in excerpt report and every artifact before sharing or archiving |
| Rule traceability | Links the project’s interpretation to publicly available rule sources | Resolving conflicts with your college, supervisor, or latest university notice |

The supported scope is `academic_phd`. Professional-degree templates, college-specific additions, submission-system requirements, and substantive writing are outside the formatter’s authority.

## Requirements

- Python 3.9 or later
- [`python-docx`](https://python-docx.readthedocs.io/)
- Microsoft Word (or the programme’s required renderer) for final visual review
- A private working copy of your own `.docx`

Install the pinned runtime dependency range in your preferred isolated environment, then verify that the same interpreter can import it:

```bash
python3 -m pip install -r requirements.txt
python3 -c "import docx; print(docx.__version__)"
```

Chinese and Latin font availability varies by operating system. Do not accept silent font substitution for a submission copy; open the result in the required Word environment and inspect it page by page.

## Install as a Codex skill

Clone this repository, then copy the skill directory into your Codex skills directory:

```bash
git clone https://github.com/helloworldJL/hnu-thesis-format.git
cd hnu-thesis-format
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R hnu-thesis-format "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart or refresh your Codex session if needed. The installed path is:

```text
${CODEX_HOME:-$HOME/.codex}/skills/hnu-thesis-format
```

You can then ask Codex to use `hnu-thesis-format` to validate a private copy. Do not place a real thesis, signatures, student identifiers, or confidential material in this public repository.

## Use locally

Work in the installed skill directory (or the repository’s `hnu-thesis-format/` directory). Use a copy, not your only manuscript.

```bash
cd "${CODEX_HOME:-$HOME/.codex}/skills/hnu-thesis-format"
mkdir -p reports output
python3 -m scripts.validate anonymous-thesis.docx \
  --thesis-type academic_phd \
  --json-report reports/validation.json \
  --html-report reports/validation.html
```

Apply the formatting pass to a separate output file, then validate that output:

```bash
mkdir -p .private
${EDITOR:-vi} .private/title.txt

python3 -m scripts.format_thesis anonymous-thesis.docx output/anonymous-thesis-formatted.docx \
  --thesis-type academic_phd \
  --title-file .private/title.txt \
  --json-report reports/formatting.json \
  --html-report reports/formatting.html

python3 -m scripts.validate output/anonymous-thesis-formatted.docx \
  --thesis-type academic_phd \
  --json-report reports/post-format-validation.json \
  --html-report reports/post-format-validation.html
```

`anonymous-thesis.docx` is only a safe placeholder name. Supply your own private document path. The repository ignores `.private/`; save the approved title there as UTF-8 plain text and pass it with `--title-file`. This avoids putting a real title in shell history or a process listing. The formatter refuses an input/output collision and refuses to replace an existing output unless you explicitly pass `--overwrite`; keep the input and output distinct.

## Reading reports

The JSON report is intended for tooling; the HTML report is intended for a local, human-readable review. By default, both use redacted locations and count-based statistics: they do not include the input path or document excerpts. A representative **synthetic** summary looks like this:

```json
{
  "issues": [
    {
      "category": "页面",
      "severity": "warning",
      "location": "Paragraph 12",
      "message": "A setting needs manual review"
    }
  ],
  "stats": {
    "paragraphs": 128,
    "sections": 3,
    "tables": 4,
    "thesis_type": "academic_phd"
  }
}
```

Treat every finding as a review prompt, not as a certification. In particular, no clean report can prove visual layout, bibliographic correctness, legal declaration text, signature validity, or acceptance by HNU.

## Safety and privacy model

This project is deliberately local-first:

- It makes no network request for your document and does not upload your manuscript.
- Keep source documents, generated DOCX files, JSON reports, and HTML reports in a private location.
- Default reports are redacted and count-based: they omit the input path and document excerpts. `--include-sensitive-details` deliberately adds short excerpts to issue locations; use it only for a private review and never share that report unchanged.
- Existing non-empty headers and complex or ambiguous content are preserved rather than forced into a guessed layout; inspect them in Word and treat them as manual-review items.
- Existing footnote numbering is preserved by default. Use `--humanities-footnotes` only after confirming that the page-restarted circled-Arabic rule applies to the dissertation.
- Never commit student numbers, personal names, supervisor or committee information, signatures, confidentiality markings, abstracts, or an actual thesis to a public fork or issue.
- Use synthetic filenames and examples in public discussions; see the [privacy guide](docs/PRIVACY.md).

## Rule sources

The maintained interpretation starts from the university’s 2025 notice, **Hunan University Graduate Thesis or Practice Outcome Writing Specification (HNU Graduate Affairs [2025] No. 17)**:

- [University notice page](https://arch.hnu.edu.cn/info/1339/5544.htm)
- [Official notice PDF](https://arch.hnu.edu.cn/__local/3/0A/1F/C26F685925C840FAF8C54833458_2C3C04AE_557E4.pdf)

These links are provided for verification only. They are controlled by their publisher and may change. The repository contains independently written operational guidance, not copies of official PDFs or templates. See [rules, hierarchy, and limitations](docs/RULES_AND_LIMITATIONS.md).

## Standards currentness

The 2025 HNU rule source cites **GB/T 7714-2015** for bibliographic references. The national registry marks [GB/T 7714-2015 as abolished](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=7FA63E9BBA56E60471AEDAEBDE44B14C) and lists [GB/T 7714-2025 as current from 2026-07-01](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=C6CE52E55AC09B9C79A20AEA77CEDD14). This tool does not rewrite bibliographic content and does not claim comprehensive GB/T 7714 compliance; confirm the current HNU and college rule before submission.

For physical quantities and units, the HNU source cites the 1986 GB 3100–3102 family. The registry lists 1993 replacements including [GB/T 3101-1993](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=6B20B8B934FD23161550CF80BEC0F507) and [GB/T 3102.1-1993](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=FAB825C0FA7292DB32BFC80F0BAA685C). The tool treats quantity/unit semantics as manual review, not national-standard certification.

## FAQ

### Does this produce a submission-ready thesis?

No. It supports a repeatable first pass. You must still compare against the current official requirements, programme-level instructions, and the final rendered Word document.

### Is this for master’s, professional, or practice-outcome templates?

No. The current supported automation target is the academic doctoral thesis path. Other types require a separately reviewed implementation.

### Can I share the HTML report with my supervisor?

The default report has no input path or document excerpt, but it is still a thesis-derived artifact and should stay in an approved private channel. If you used `--include-sensitive-details`, it contains short excerpts and must not be shared unchanged.

### Which reference and unit standard should I use?

Start with the current HNU and college instructions for your submission. HNU’s 2025 source refers to GB/T 7714-2015, while the national registry records GB/T 7714-2025 as the current replacement from 2026-07-01. The 1986 unit-standard family cited by HNU also has 1993 successors. The tool does not rewrite bibliographic data and does not certify quantity/unit semantics; verify both manually.

### Why are there no official PDF samples in this repository?

They are official source documents, not project assets. This project links to public rule sources and does not redistribute them.

## Roadmap

- [ ] Improve non-destructive handling of complex Word fields and section layouts
- [ ] Expand machine-readable rule traceability and manual-review prompts
- [ ] Extend tests and documentation for opt-in sensitive-report handling
- [ ] Add reviewed support paths only when official scope and test fixtures are available
- [ ] Continue compatibility testing against supported Python and `python-docx` versions

## Project documents

- [Changelog](CHANGELOG.md)
- [Contribution guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security policy](SECURITY.md)
- [Apache-2.0 license](LICENSE) and [notice](NOTICE)
- [Citation metadata](CITATION.cff)
- [Release verification record](docs/verification.md)
- [v1.0.1 documentation-integrity patch notes](docs/releases/v1.0.1.md)
- [v1.0.0 sanitized local verification evidence](docs/evidence/v1.0.0-local.md)
- [v1.0.0 sanitized command log](docs/evidence/v1.0.0-command-log.md)
- [v1.0.0 release notes](docs/releases/v1.0.0.md)

## Disclaimer

This is an independent, community-maintained utility. It is not an official HNU template, policy interpretation, or approval tool, and it is not affiliated with or endorsed by Hunan University. You remain responsible for the correctness, privacy, and final submission of your own work.
