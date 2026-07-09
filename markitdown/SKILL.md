---
name: markitdown
description: >
  微软开源文档转换工具 MarkItDown — PDF/Word/PPT/Excel/HTML/EPUB/图片/音频 等 20+ 种格式
  一键转干净 Markdown。保留标题层级、列表、表格、链接，转出的 Markdown 人看得舒服、AI 读得顺畅。
  适用于 Obsidian 知识库入库、RAG 文档预处理、团队文档格式统一、AI 分析前预处理。
  Trigger keywords: markitdown, MarkItDown, 文档转换, PDF转Markdown, Word转Markdown,
  PPT转Markdown, 格式转换, 文档预处理, Obsidian导入, 知识库入库, RAG预处理,
  微软文档工具, 一键转markdown, 文件转markdown, document to markdown,
  convert PDF, convert Word, convert PPT, 音频转文字, OCR转markdown.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
metadata:
  category: tools
  source: https://github.com/microsoft/markitdown (MIT)
  author:
    original: Microsoft AutoGen Team
  version: "1.0.0"
  license: MIT
---

# MarkItDown — 微软开源文档转换神器

> 把任何文件转成干净 Markdown。16 万 GitHub Star，MIT 开源，微软维护。

## 一句话说清楚

MarkItDown 是微软 AutoGen 团队开源的 Python 工具，专做一件事：**把任何文件转成干净 Markdown**。

不是生硬抽文本。是完整保留标题层级、列表结构、表格、链接——转出来的 Markdown 人看得舒服，AI 读得顺畅。

## 支持格式

20+ 种，覆盖电脑里几乎所有文件类型：

| 类别 | 格式 |
|------|------|
| Office | Word (.docx)、PPT (.pptx)、Excel (.xlsx/.xls) |
| 文档 | PDF（含扫描件 OCR）、EPUB |
| 多媒体 | 图片（OCR + 元数据）、音频（语音转写） |
| 数据 | CSV、JSON、XML |
| 网页 | HTML |
| 黑科技 | ZIP 自动解压批量转、YouTube 链接扒字幕 |

---

## 安装

```bash
# 全量安装（推荐）
pip install 'markitdown[all]'

# 按需安装
pip install 'markitdown[pdf,docx,pptx]'
```

---

## 使用方法

### CLI 一行搞定（最简单）

```bash
markitdown 项目报告.pdf -o 输出.md
```

### Python 调用（3 行代码）

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("项目报告.pdf")
print(result.text_content)
```

### 进阶：接大模型做图像描述

PPT 里的图、扫描件里的照片，默认转不出来文字。接上 GPT-4o 让 AI 自动生成文字描述：

```python
from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI()
md = MarkItDown(llm_client=client, llm_model="gpt-4o")
result = md.convert("季度汇报.pptx")
print(result.text_content)
```

PPT 里的流程图、架构图——AI 自动生成文字描述嵌进 Markdown。带图的 PPT 转出来不再是「[图片]」占位符。

---

## Obsidian 最佳搭档

推荐工作流：

```
① 拖入文件 → ② MarkItDown 自动转 Markdown → ③ 写入 Obsidian vault
```

同事发来的 Word 周报、客户给的 PDF 方案、会议录音转写的文本——全部一键变成 Obsidian 里的双向链接就绪笔记。

如果搭了 RAG 知识库或用 AI 做文档分析，MarkItDown 是预处理第一步。**大模型读 Markdown 比读 PDF 省 Token、解析更准**——这是实测结果。

---

## 谁适合用

| ✅ 适合 | ❌ 不适合 |
|---------|-----------|
| Obsidian 用户：外部文档一键入库 | 需要高保真排版（出版级 PDF 还原） |
| RAG 开发者：文档预处理省 80% 清洗工作 | MarkItDown 目标是"让 AI 读懂"，不是"让人打印" |
| 职场人：统一团队文档格式、做 AI 摘要 | |
| 学生/研究者：课件转笔记、文献整理 | |

---

## 触发示例

- "帮我把这个 PDF 转成 Markdown"
- "我有几个 Word 文档要导入 Obsidian，帮我转一下"
- "把这个 PPT 转为 Markdown，里面的图用 GPT-4o 描述一下"
- "批量把文件夹里的所有 .docx 转为 .md"
- "用 MarkItDown 把会议录音转文字然后整理成笔记"
- "convert this PDF to markdown for my knowledge base"
- "预处理这些文档用于 RAG"

---

## 来源

- **开源项目**: [github.com/microsoft/markitdown](https://github.com/microsoft/markitdown)
- **作者**: Microsoft AutoGen Team
- **Star**: 160,000+
- **协议**: MIT
- **中文介绍**: 整理自微信公众号文章《16万Star的免费Obsidian入库转换神器：微软官方开源MarkItDown》
