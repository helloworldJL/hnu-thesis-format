# Contributing

Thank you for improving `hnu-thesis-format`. Contributions should make the tool safer, more transparent, and easier to verify without turning it into an unofficial authority on HNU policy.

## Before you start

- Read [the rules and limitations](docs/RULES_AND_LIMITATIONS.md) and [privacy guide](docs/PRIVACY.md).
- Open an issue first for a material rule interpretation, scope expansion, or API change.
- Work from publicly verifiable sources. Link to the authoritative notice or standard; do not upload official PDFs, protected templates, or screenshots unless you have explicit redistribution permission.
- Never include a real thesis, student identifier, name, adviser/committee information, signature, confidential marking, or local absolute path in a commit, issue, fixture, or screenshot.

## Development expectations

1. Create a focused branch and keep the change narrow.
2. Add or update a synthetic test fixture when behaviour changes.
3. Run the relevant tests and report the exact command and result in the pull request.
4. Update documentation and the changelog when users will observe a change.
5. Preserve manual-review boundaries. A validator warning is not a policy decision, and a formatter must not silently rewrite uncertain content.

## Rule changes

For a rule-related pull request, state:

- the rule source, issuer, publication date, and stable URL;
- the precise section or page locator;
- whether the source is mandatory, illustrative, or programme-specific;
- the expected machine behaviour and the required manual check;
- the effect on existing documents and reports.

When sources conflict, do not guess. Document the conflict, retain the safer manual-review boundary, and request maintainer review.

## Pull request checklist

- [ ] I used only synthetic/public-safe examples.
- [ ] I did not add official PDFs, templates, logos, or screenshots without permission.
- [ ] I avoided real-person data, thesis text, and absolute local paths.
- [ ] I added or updated appropriate tests and ran them locally.
- [ ] I documented any new dependency, compatibility constraint, or manual-review requirement.
- [ ] I accept the project’s Apache-2.0 license for my original contribution.

## Code of Conduct

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). Report security-sensitive issues through the process in [SECURITY.md], not through a public issue.
