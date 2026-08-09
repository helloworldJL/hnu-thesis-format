# Privacy guide

`hnu-thesis-format` is designed for local document processing, but a thesis and its formatted output remain sensitive. Treat them as private by default.

## Data boundary

The tool reads a document from the path you provide and writes outputs to paths you choose. It does not require a cloud account or document upload. Your operating system, editor, backup, sync client, terminal history, and Git configuration may independently retain copies or metadata.

## What must stay private

Do not publish, commit, paste into an issue, or include in a test fixture:

- names, student numbers, contact details, affiliations, or adviser/committee data;
- signatures, seals, secrecy classifications, defence dates, or submission records;
- a real title, abstract, full text, unpublished results, or references that identify the author’s work;
- document paths that disclose an account name, home directory, cloud drive, or private folder structure; or
- an opt-in sensitive-detail report that contains any of the above.

## Safe workflow

1. Keep the original and formatted DOCX files outside the cloned repository.
2. Use a neutral filename such as `anonymous-thesis.docx` in examples and screenshots.
3. Create the real dissertation title in a private, UTF-8 plain-text file and pass it with `--title-file`; do not put it on a command line with `--title`, in shell history, or in version control.
4. Write reports to a private directory and inspect them before sharing.
5. If you need help, reproduce the problem with a minimal synthetic DOCX and generic text.
6. Before a `git add`, inspect staged changes with `git diff --cached --check` and `git diff --cached`.

## Reports and logs

By default, JSON and HTML reports use fixed messages, rule locators, paragraph indices, and aggregate counts. They omit the input-document path and document excerpts. This default is designed for safer review, not as an authorization to publish a thesis-derived report.

`--include-sensitive-details` is an explicit private-review mode: it adds a short document excerpt to selected issue locations. Do not use that option for an artifact you will share, and do not publish its output. Keep every report in an approved private channel unless it has been independently reviewed for the intended audience.

## Official materials

Do not commit official PDFs, templates, sample files, logos, or rendered screenshots unless you have clear permission to redistribute them. Link to the authoritative public page instead. This keeps the repository focused on original tooling and avoids making unofficial copies of university materials.

## Responsible disclosure

If you find a path disclosure, sensitive-data leak, or unsafe crafted-DOCX behaviour, follow [SECURITY.md](../SECURITY.md). Use synthetic reproductions only.
