# Release verification record / 发布核验记录

This is the completed evidence-oriented release record for `v1.0.0`. Results are bound to the verified implementation candidate and linked artifacts below; later documentation-only release commits must retain a green `CI` run before tagging.

本文档是 `v1.0.0` 已完成的证据化发布核验记录。结果绑定到下列已核验实现候选提交与证据；后续仅修改文档的发布提交在打标签前仍须保持 `CI` 绿色。

## Release identity / 发布标识

| Field / 字段 | Value / 值 |
| --- | --- |
| Version / 版本 | `v1.0.0` |
| Release date / 发布日期 | `2026-08-09` |
| Verified implementation candidate / 已核验实现候选提交 | [`0417ba8a1ed5d6dc5758b3eeaeb02e2fbbb10e38`](https://github.com/helloworldJL/hnu-thesis-format/commit/0417ba8a1ed5d6dc5758b3eeaeb02e2fbbb10e38) |
| Release owner / 发布负责人 | [`@helloworldJL`](https://github.com/helloworldJL) |
| Verification completed at / 核验完成时间 | `2026-08-09 20:00 CST` |
| Evidence directory / 证据目录 | [`docs/evidence/`](evidence/) |

## Required commands / 必跑命令

Run from the repository root. Record the command, exit status, and a non-empty captured result for every applicable row. The public [sanitized command log](evidence/v1.0.0-command-log.md) replaces private paths with placeholders; complete raw logs remain private. Do not substitute an inferred result for an execution result.

请在仓库根目录运行。每个适用条目都必须记录命令、退出状态和非空结果。公开的[脱敏命令日志](evidence/v1.0.0-command-log.md)以占位符替换私密路径；完整原始日志保持私密。不得以推断结果代替实际执行结果。

| Check category / 核验类别 | Invocation / 调用命令 | Expected observable / 预期可观察结果 | Status / 状态 | Evidence path / 证据路径 |
| --- | --- | --- | --- | --- |
| Repository status / 仓库状态 | `git status --short` | Release changes are known and no unintended sensitive files are staged | **PASS**, exit `0`; clean after candidate commit | [Candidate commit](https://github.com/helloworldJL/hnu-thesis-format/commit/0417ba8a1ed5d6dc5758b3eeaeb02e2fbbb10e38) |
| Python test suite / Python 测试 | `python -m pytest -q` | Exit code `0`; all collected tests pass | **PASS**, 17 passed | [Local evidence](evidence/v1.0.0-local.md#automated-gates--自动化门槛) |
| Synthetic validator privacy regression / 合成校验器隐私回归 | `python -m pytest -q tests/test_validation_cli.py` | Exit code `0`; pytest creates temporary synthetic DOCX/report artifacts and verifies default reports contain neither the input path nor the injected private marker | **PASS**, 2 passed | [Local evidence](evidence/v1.0.0-local.md#synthetic-workflow--合成工作流) |
| Public release scan / 公开发布扫描 | `python tests/release_scan.py` | Exit code `0`; output is `Public release scan passed.` | **PASS**, exit `0` | [Local evidence](evidence/v1.0.0-local.md#automated-gates--自动化门槛) |
| Formatter entry point / 格式化器入口 | `(cd hnu-thesis-format && python -m scripts.format_thesis --help)` | Exit code `0`; usage lists mutually exclusive `--title` and UTF-8 `--title-file` inputs | **PASS**, exit `0` | [Candidate CI checks](https://github.com/helloworldJL/hnu-thesis-format/commit/0417ba8a1ed5d6dc5758b3eeaeb02e2fbbb10e38/checks) |
| Validator entry point / 校验器入口 | `(cd hnu-thesis-format && python -m scripts.validate --help)` | Exit code `0`; usage lists `--json-report`, `--html-report`, and opt-in `--include-sensitive-details` | **PASS**, exit `0` | [Candidate CI checks](https://github.com/helloworldJL/hnu-thesis-format/commit/0417ba8a1ed5d6dc5758b3eeaeb02e2fbbb10e38/checks) |
| CI workflow / CI 工作流 | GitHub Actions workflow named `CI` in `.github/workflows/ci.yml` on the verified implementation candidate | Green runs for Ubuntu and macOS on Python 3.9 and 3.12 | **PASS**, four jobs green | [Candidate CI checks](https://github.com/helloworldJL/hnu-thesis-format/commit/0417ba8a1ed5d6dc5758b3eeaeb02e2fbbb10e38/checks) |

The pytest suite creates synthetic DOCX files in pytest-managed temporary directories; it does not rely on a committed real-thesis fixture. If a repository command or fixture arrangement differs at release time, update this table to the exact executed command; do not silently omit the row.

The sanitized local DOCX/PDF/HTML inspection log is published at [`docs/evidence/v1.0.0-local.md`](evidence/v1.0.0-local.md), with command outputs at [`docs/evidence/v1.0.0-command-log.md`](evidence/v1.0.0-command-log.md); private source artifacts, absolute paths, raw logs, and screenshots are intentionally not published.

如果发布时仓库命令或 fixture 名称不同，请把本表改为实际执行的精确命令；不得静默省略条目。

脱敏的本地 DOCX/PDF/HTML 检查日志见 [`docs/evidence/v1.0.0-local.md`](evidence/v1.0.0-local.md)，命令输出见 [`docs/evidence/v1.0.0-command-log.md`](evidence/v1.0.0-command-log.md)；私密源产物、绝对路径、原始日志与截图不会公开。

## Artifact inspection / 产物检查

| Artifact / 产物 | Required inspection / 必查项 | Result / 结果 | Evidence path / 证据路径 |
| --- | --- | --- | --- |
| Pytest temporary JSON/HTML reports | Created from synthetic input; default report contains no input path or document excerpt | **PASS**; source path, input filename, excerpt, and synthetic title absent | [Synthetic workflow](evidence/v1.0.0-local.md#synthetic-workflow--合成工作流) |
| Formatter title file | Private UTF-8 plain-text title file; not committed, not an output path, and passed with `--title-file` rather than a real `--title` command-line value | **PASS**; ignored private file used | [Synthetic workflow](evidence/v1.0.0-local.md#synthetic-workflow--合成工作流) |
| Rendered synthetic DOCX/PDF | Formatter output is non-empty and distinct from its synthetic input; page size, margins, page-number transition, headers, recognised scholarly tables, and no clipping/overlap checked manually | **PASS**; 12-page A4 PDF opened and inspected | [Rendered-document review](evidence/v1.0.0-local.md#rendered-document-review--渲染文档检查) |
| Public tree | Contains no official PDF/template/logo/screenshot and no personal or confidential source artifact | **PASS**; Git candidate scan and independent privacy review clean | [Automated gates](evidence/v1.0.0-local.md#automated-gates--自动化门槛) |

## Release gates / 发布门槛

- [x] All applicable command rows have an actual exit status and captured artifact path.
- [x] All generated artifacts named above were opened or parsed, not merely assumed to exist.
- [x] No report intended for sharing used `--include-sensitive-details`.
- [x] The CI workflow named `CI` is green for the candidate commit.
- [x] Documentation has been read against the final repository layout and command surface.
- [x] The privacy scan found no real thesis material, personal identifiers, local absolute paths, official PDFs, or official template assets.
- [x] The release notes at [`docs/releases/v1.0.0.md`](releases/v1.0.0.md) contain actual evidence.

## Approval / 批准

| Role / 角色 | Name or handle / 姓名或账号 | Date / 日期 | Decision / 结论 |
| --- | --- | --- | --- |
| Release owner / 发布负责人 | [`@helloworldJL`](https://github.com/helloworldJL) | `2026-08-09` | **APPROVE / 批准** |
| Final verifier / 最终复核人 | Codex release QA and independent review lanes | `2026-08-09` | **APPROVE / 批准** |

This record is complete. Tag only a commit whose final `CI` run is green and whose public Git tree still passes the release scan.

本记录已完成。仅可为最终 `CI` 绿色且公开 Git 树仍通过发布扫描的提交打标签。
