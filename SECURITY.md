# Security Policy

## Supported versions

Security fixes are applied to the latest released version and the `main` branch. Older releases may not receive patches.

## Reporting a vulnerability

Please do **not** publish a public issue for a suspected vulnerability, data-exposure risk, malicious-document handling problem, or report-redaction failure.

Use GitHub’s private vulnerability-reporting feature for this repository when available. If it is unavailable, contact the repository owner through the private contact route shown on the repository profile and include “hnu-thesis-format security report” in the subject.

Include, where safe:

- a concise description of the impact;
- affected version or commit;
- reproduction steps using a synthetic document only;
- the expected and observed behaviour; and
- any suggested mitigation.

Do not attach a real thesis, document containing personal information, signature image, student identifier, confidential marking, or an official source document that you cannot redistribute.

We will acknowledge reports as soon as practicable, investigate privately, and coordinate a fix and disclosure timeline with the reporter when a vulnerability is confirmed.

## Scope

Examples of in-scope reports include unintended local-file disclosure, unsafe handling of crafted DOCX packages, report data leakage, dependency vulnerabilities, and code paths that overwrite an input document unexpectedly. Formatting disagreements or requests for additional institution-specific rules belong in a normal issue unless they create a security or privacy risk.
