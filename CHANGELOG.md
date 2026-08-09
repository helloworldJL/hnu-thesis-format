# Changelog

All notable changes to this project are documented in this file. The project follows [Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-08-09

### Added

- Initial public release of the `hnu-thesis-format` Codex skill for the academic doctoral-thesis workflow.
- Local validation and conservative formatting command surface with redacted JSON and HTML reporting by default; sensitive excerpts require explicit opt-in.
- English and Simplified Chinese installation, usage, privacy-boundary, rule-source, limitation, and release guidance, plus English community, security, citation, and licensing files.
- Community health files and Apache-2.0 licensing for original project code and documentation.

### Safety

- Public examples use synthetic filenames and content only.
- Formatter title input supports a private UTF-8 `--title-file` as a safer alternative to command-line title text.
- Formatting is limited to recognised paragraph types and positively recognised scholarly tables; pre-existing headers and complex/uncertain content remain for manual review.
- Official source PDFs and official example documents are not bundled or redistributed.

[1.0.0]: https://github.com/helloworldJL/hnu-thesis-format/releases/tag/v1.0.0
