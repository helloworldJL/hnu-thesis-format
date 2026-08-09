# Safe automation boundary

Automate formatting only after preserving the input and producing an output copy.
Use a dry-run or change log whenever the tool supports it. Reopen the output and
render it to PDF for visual verification.

## Current implementation may automate

- Apply A4 geometry, margins, header/footer distance, paragraph spacing, and
  fonts to existing document sections and recognized paragraphs.
- Apply named style/hierarchy mappings; format recognized scholarly data tables.
- Fill only empty headers/footers and set page-number fields/formats in existing,
  unambiguous sections.
- Produce read-only counts and lint findings for heading length, punctuation,
  citation sequence, reference/keyword counts, and unresolved placeholders.

## Manual unless an independently reviewed tool proves otherwise

- Insert section breaks, create or move section boundaries, or infer a missing
  Roman-to-Arabic pagination boundary.
- Regenerate a table of contents or relabel equations, tables, or figures.
- Certify any layout, bibliographic, units/symbols, content, or submission rule.

## Require human-confirmed input

- Classification/security level, submission and defense dates, author/adviser
  fields, degree-period achievements, committee roster, and any affiliation.
- Abstract/content accuracy, findings, innovation claims, source metadata, figure
  permissions, and reference correctness.
- The official declaration text, handwritten signatures, and any scanned signature.

## Never automate

- Inventing, copying, drawing, inserting, or reusing a signature.
- Fabricating a committee, adviser, result, achievement, citation, classification,
  institutional field, or compliance claim.
- Altering the official declaration text, uploading a dissertation, sending it for
  printing, or submitting it to HNU.

## Report privacy

Default reports omit local source paths and document excerpts. The
`--include-sensitive-details` option is opt-in and private-only; use it only for
an authorized private output, because it may include short document excerpts.

## Layout guardrails

- Put the authorized thesis title, not a copied university label, in even-page
  headers. Never infer header content from a sample page that conflicts with the
  Rule.
- Apply three-line-table automation to scholarly data tables only. Exclude the
  factual defense committee list and similar administrative records.
- Keep a table caption with the table below it. For a figure caption below an
  image, use a container/anchoring method that keeps image and caption together;
  do not blindly apply a caption `keep-with-next` rule that binds it to body text.
- Treat degree labels and attachment labels in a sample as placeholders; populate
  final fields only from authorized private data.

## Required verification record

For each formatting run, retain the input/output filenames, tool/version, date,
changed style/section properties, rendered-PDF page checks, and failed checks.
Report an unverified rule as unverified, never as passed.
