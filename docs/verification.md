# Release verification record / 发布核验记录

This is the evidence-oriented release record for `v1.0.0`. It is a template, not a claim that a command has passed. Before creating a release, the release owner must replace every `PENDING` value with a captured result, artifact path, and reviewer/date where applicable.

本文档是 `v1.0.0` 的证据化发布核验记录。它是模板，不代表任何命令已经通过。创建发布前，发布负责人必须将每一个 `PENDING` 替换为实际结果、证据路径，以及适用时的复核人和日期。

## Release identity / 发布标识

| Field / 字段 | Value / 值 |
| --- | --- |
| Version / 版本 | `v1.0.0` |
| Planned release date / 计划发布日期 | `2026-08-09` |
| Commit / 提交 | `PENDING` |
| Release owner / 发布负责人 | `PENDING` |
| Verification completed at / 核验完成时间 | `PENDING` |
| Evidence directory / 证据目录 | `PENDING` |

## Required commands / 必跑命令

Run from the repository root. Record the complete command, exit status, and a non-empty captured log for every applicable row. Do not substitute an inferred result for an execution result.

请在仓库根目录运行。每个适用条目都必须记录完整命令、退出状态和非空日志。不得以推断结果代替实际执行结果。

| Check category / 核验类别 | Invocation / 调用命令 | Expected observable / 预期可观察结果 | Status / 状态 | Evidence path / 证据路径 |
| --- | --- | --- | --- | --- |
| Repository status / 仓库状态 | `git status --short` | Release changes are known and no unintended sensitive files are staged | `PENDING` | `PENDING` |
| Python test suite / Python 测试 | `python -m pytest -q` | Exit code `0`; all collected tests pass | `PENDING` | `PENDING` |
| Synthetic validator privacy regression / 合成校验器隐私回归 | `python -m pytest -q tests/test_validation_cli.py` | Exit code `0`; pytest creates temporary synthetic DOCX/report artifacts and verifies default reports contain neither the input path nor the injected private marker | `PENDING` | `PENDING` |
| Public release scan / 公开发布扫描 | `python tests/release_scan.py` | Exit code `0`; output is `Public release scan passed.` | `PENDING` | `PENDING` |
| Formatter entry point / 格式化器入口 | `(cd hnu-thesis-format && python -m scripts.format_thesis --help)` | Exit code `0`; usage lists mutually exclusive `--title` and UTF-8 `--title-file` inputs | `PENDING` | `PENDING` |
| Validator entry point / 校验器入口 | `(cd hnu-thesis-format && python -m scripts.validate --help)` | Exit code `0`; usage lists `--json-report`, `--html-report`, and opt-in `--include-sensitive-details` | `PENDING` | `PENDING` |
| CI workflow / CI 工作流 | GitHub Actions workflow named `CI` in `.github/workflows/ci.yml` on the release commit | Green runs for Ubuntu and macOS on Python 3.9 and 3.12 | `PENDING` | `PENDING` |

The pytest suite creates synthetic DOCX files in pytest-managed temporary directories; it does not rely on a committed real-thesis fixture. If a repository command or fixture arrangement differs at release time, update this table to the exact executed command; do not silently omit the row.

如果发布时仓库命令或 fixture 名称不同，请把本表改为实际执行的精确命令；不得静默省略条目。

## Artifact inspection / 产物检查

| Artifact / 产物 | Required inspection / 必查项 | Result / 结果 | Evidence path / 证据路径 |
| --- | --- | --- | --- |
| Pytest temporary JSON/HTML reports | Created from synthetic input; default report contains no input path or document excerpt | `PENDING` | `PENDING` |
| Formatter title file | Private UTF-8 plain-text title file; not committed, not an output path, and passed with `--title-file` rather than a real `--title` command-line value | `PENDING` | `PENDING` |
| Rendered synthetic DOCX/PDF | Formatter output is non-empty and distinct from its synthetic input; page size, margins, page-number transition, headers, recognised scholarly tables, and no clipping/overlap checked manually | `PENDING` | `PENDING` |
| Public tree | Contains no official PDF/template/logo/screenshot and no personal or confidential source artifact | `PENDING` | `PENDING` |

## Release gates / 发布门槛

- [ ] All applicable command rows have an actual exit status and captured artifact path.
- [ ] All generated artifacts named above were opened or parsed, not merely assumed to exist.
- [ ] No report intended for sharing used `--include-sensitive-details`; any private-review use of that flag was separately inspected.
- [ ] The CI workflow named `CI` is green for the candidate commit.
- [ ] Documentation has been read against the final repository layout and command surface.
- [ ] The privacy scan found no real thesis material, personal identifiers, local absolute paths, official PDFs, or official template assets.
- [ ] The release notes at [`docs/releases/v1.0.0.md`](releases/v1.0.0.md) have their verification section filled with actual evidence.

## Approval / 批准

| Role / 角色 | Name or handle / 姓名或账号 | Date / 日期 | Decision / 结论 |
| --- | --- | --- | --- |
| Release owner / 发布负责人 | `PENDING` | `PENDING` | `PENDING` |
| Final verifier / 最终复核人 | `PENDING` | `PENDING` | `PENDING` |

Do not publish while any required value remains `PENDING`.

任何必填项仍为 `PENDING` 时，不得发布。
