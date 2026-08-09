# HNU Thesis Format

[![CI](https://github.com/helloworldJL/hnu-thesis-format/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/helloworldJL/hnu-thesis-format/actions/workflows/ci.yml)
[![许可证](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-3776AB.svg)](#运行环境)

面向**湖南大学学术学位博士学位论文**的本地格式检查与辅助排版工具，依据 2025 年撰写规范整理可重复执行的检查流程。它用于降低常见格式遗漏，不替代学校、学院或导师的审核，也不替代最终的 Word 渲染核查。

[English](README.md) · [规则与边界](docs/RULES_AND_LIMITATIONS.md) · [隐私说明](docs/PRIVACY.md) · [参与贡献](CONTRIBUTING.md) · [安全政策](SECURITY.md)

> **非官方项目。** 本仓库与湖南大学不存在隶属、授权、赞助或背书关系。请以学校、学院及当期送审要求为准。本仓库**不分发**任何官方 PDF 或示范文件。

## 能做什么，不能做什么

| 能力 | 工具可提供的帮助 | 仍需人工确认的事项 |
| --- | --- | --- |
| 格式预检 | 检查常见的 A4、页边距、标题、摘要、关键词、参考文献和结构信号 | 规则是否适用于你的学院、学科和送审批次 |
| 辅助排版 | 对可识别段落、页面以及被明确识别为学术表格的对象应用保守基线 | 既有页眉和复杂/歧义内容，以及版式完整性、分节和最终页码 |
| 本地报告 | 默认输出已脱敏的 JSON、HTML 问题记录与数量统计 | 启用摘录后的报告，以及所有对外分享或归档的产物 |
| 规则可追溯性 | 链接到公开的规范来源，并说明项目的解释边界 | 学院口径冲突及最新通知的裁定 |

当前自动化范围仅为 `academic_phd`。专业学位模板、学院附加要求、提交系统规则与论文内容写作均不在本工具的裁量范围内。

## 运行环境

- Python 3.9 或更高版本
- [`python-docx`](https://python-docx.readthedocs.io/)
- Microsoft Word（或项目要求的最终渲染环境）
- 仅在私密位置保存的个人 `.docx` 工作副本

建议在隔离环境中安装仓库限定的运行时依赖范围，并确认同一个解释器可以导入依赖：

```bash
python3 -m pip install -r requirements.txt
python3 -c "import docx; print(docx.__version__)"
```

不同操作系统的中文与西文字体可用性不同。提交版不能接受无提示的字体替换；请务必在要求的 Word 环境中逐页检查最终结果。

## 作为 Codex skill 安装

先克隆仓库，再把 skill 目录复制到 Codex skills 目录：

```bash
git clone https://github.com/helloworldJL/hnu-thesis-format.git
cd hnu-thesis-format
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R hnu-thesis-format "${CODEX_HOME:-$HOME/.codex}/skills/"
```

必要时重启或刷新 Codex 会话。安装后目录为：

```text
${CODEX_HOME:-$HOME/.codex}/skills/hnu-thesis-format
```

之后可让 Codex 使用 `hnu-thesis-format` 检查你的私密副本。不要把真实论文、签名、学号或涉密材料提交到公开仓库。

## 本地使用

在已安装的 skill 目录（或仓库中的 `hnu-thesis-format/` 目录）执行。请先复制论文，避免直接操作唯一原稿。

```bash
cd "${CODEX_HOME:-$HOME/.codex}/skills/hnu-thesis-format"
mkdir -p reports output
python3 -m scripts.validate anonymous-thesis.docx \
  --thesis-type academic_phd \
  --json-report reports/validation.json \
  --html-report reports/validation.html
```

将排版结果写入新文件，随后再次检查：

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

`anonymous-thesis.docx` 只是安全的示例名称，请替换为你自己私密工作副本的路径。仓库已忽略 `.private/`；请把已确认题名以 UTF-8 纯文本保存在该目录，再用 `--title-file` 传入。这样不会把真实题名写进 shell 历史或进程列表。格式化工具会拒绝输入输出路径相同的调用，也会拒绝覆盖已存在的输出文件，除非你明确传入 `--overwrite`；请始终保持输入和输出不同。

## 如何理解报告

JSON 便于自动化处理，HTML 便于本地人工阅读。二者默认使用脱敏位置和数量统计：不包含输入文件路径或论文摘录。以下只是**合成示例**，不包含真实论文信息：

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

每一条结果都应视为复核提示，而不是合格证明。即使报告没有错误，也无法证明视觉版式、参考文献著录、声明页文本、签名有效性或学校最终受理一定无误。

## 隐私与安全边界

本项目采取本地优先的处理方式：

- 不会为处理论文发起网络请求，也不会上传论文。
- 原始 DOCX、输出 DOCX、JSON 报告和 HTML 报告都应保存在私密位置。
- 默认报告已脱敏且以数量统计为主：不含输入路径和论文摘录。`--include-sensitive-details` 会有意在问题位置中加入短摘录，只能用于私密复核，不能原样分享。
- 非空既有页眉与复杂或歧义内容会被保留，不会强行猜测布局；请在 Word 中检查，并将其视为人工复核项。
- 既有脚注编号默认保持不变。只有确认论文适用逐页重编号的带圈阿拉伯数字规则后，才可使用 `--humanities-footnotes`。
- 不要把学号、姓名、导师或答辩委员信息、签名、密级标记、摘要或真实论文提交到公开 fork、issue 或讨论区。
- 公开交流请使用合成文件名和示例；详见[隐私说明](docs/PRIVACY.md)。

## 规则来源

项目的规则解释以湖南大学 2025 年通知《湖南大学研究生学位论文或实践成果撰写规范》（湖大研字〔2025〕17号）为主要来源：

- [学校通知页面](https://arch.hnu.edu.cn/info/1339/5544.htm)
- [官方通知 PDF](https://arch.hnu.edu.cn/__local/3/0A/1F/C26F685925C840FAF8C54833458_2C3C04AE_557E4.pdf)

链接仅用于核验，页面归发布方所有并可能调整。本仓库提供的是独立表述的操作性说明，并不复制官方 PDF 或模板。详情见[规则层级与限制](docs/RULES_AND_LIMITATIONS.md)。

## 标准时效提示

2025 年 HNU 规范来源对参考文献援引的是 **GB/T 7714-2015**。国家标准平台显示，[GB/T 7714-2015 已废止](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=7FA63E9BBA56E60471AEDAEBDE44B14C)，[GB/T 7714-2025 自 2026-07-01 起现行](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=C6CE52E55AC09B9C79A20AEA77CEDD14)。本工具不改写参考文献内容，也不声称全面符合 GB/T 7714；提交前请核对当期 HNU 与学院要求。

物理量和单位方面，HNU 来源引用 1986 年 GB 3100–3102 系列；国家标准平台列示 [GB/T 3101-1993](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=6B20B8B934FD23161550CF80BEC0F507) 和 [GB/T 3102.1-1993](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=FAB825C0FA7292DB32BFC80F0BAA685C) 等 1993 年替代标准。本工具只将量和单位语义列为人工复核项，不提供国家标准符合性认证。

## 常见问题

### 它能生成可以直接提交的论文吗？

不能。它只能提供可重复的第一轮辅助。你仍需对照当期官方要求、学院要求和最终 Word 渲染结果完成核验。

### 它支持硕士、专业学位或实践成果模板吗？

暂不支持。当前自动化目标仅为学术学位博士论文。其他类型必须在规范范围明确、测试材料完备后另行实现。

### 可以把 HTML 报告发给导师吗？

默认报告不含输入路径或论文摘录，但仍是论文派生产物，应只在获准的私密渠道中保存和发送。若启用了 `--include-sensitive-details`，报告会含有短摘录，不能原样分享。

### 参考文献和量单位应按哪个标准？

应先以你本次提交适用的 HNU 与学院最新要求为准。HNU 2025 年来源引用 GB/T 7714-2015，但国家标准平台记录 GB/T 7714-2025 已自 2026-07-01 起作为现行替代标准；其引用的 1986 年单位标准系列也已有 1993 年替代版本。本工具不会改写参考文献数据，也不会认证量和单位语义，必须人工核实。

### 为什么仓库里没有官方 PDF 示例？

官方文件不属于本项目资产。项目提供公开来源链接，不重新发布官方 PDF 或示范文件。

## 路线图

- [ ] 改进复杂 Word 域与分节布局的非破坏性处理
- [ ] 扩展机器可读的规则追溯与人工复核提示
- [ ] 扩展启用敏感报告选项的测试与文档
- [ ] 仅在规则范围明确且有测试样本时扩展支持路径
- [ ] 持续验证支持的 Python 与 `python-docx` 版本组合

## 项目文档

- [更新日志](CHANGELOG.md)
- [贡献指南](CONTRIBUTING.md)
- [行为准则](CODE_OF_CONDUCT.md)
- [安全政策](SECURITY.md)
- [Apache-2.0 许可证](LICENSE)与[声明](NOTICE)
- [引用元数据](CITATION.cff)
- [发布核验记录](docs/verification.md)
- [v1.0.1 发布文档完整性修复说明](docs/releases/v1.0.1.md)
- [v1.0.0 脱敏本地核验证据](docs/evidence/v1.0.0-local.md)
- [v1.0.0 脱敏命令日志](docs/evidence/v1.0.0-command-log.md)
- [v1.0.0 发布说明](docs/releases/v1.0.0.md)

## 免责声明

这是独立维护的社区工具，不是湖南大学官方模板、政策解释或审批工具，也未获得湖南大学隶属或背书。论文内容、隐私保护和最终提交结果均由使用者自行负责。
