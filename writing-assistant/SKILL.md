---
name: writing-assistant
description: >
  结构化写作助手——从大纲到草稿到润色到发表前审查，覆盖完整写作流程。
  适用于博客、备忘录、论文、报告等各类文体。
  Trigger keywords: 写作助手, writing assistant, 帮我写, 写文章,
  写博客, 写报告, 润色, 修改文章, 大纲, draft, 写稿。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
  - WebFetch
  - WebSearch
metadata:
  category: content
  source: lyndonkl/claude
  version: "1.0.0"
  license: MIT
---

# Writing Assistant — 结构化写作助手

> 大纲→草稿→润色→发表前审查，覆盖完整写作流程。

## 写作流程

```
Outline → Draft → Revise → Pre-publish Gate
   │         │        │            │
 结构骨架   内容填充  语言润色    最终审查
```

## 核心能力

- **结构化写作**：从零到终稿的全流程
- **多文体支持**：博客、备忘录、论文、报告、Newsletter
- **风格适配**：正式/半正式/随性，按场景调整
- **发表前审查**：逻辑一致性、读者视角、可读性检查

## 安装

```bash
# 来自 lyndonkl/claude 仓库
git clone https://github.com/lyndonkl/claude.git /tmp/lyndonkl-claude
cp -r /tmp/lyndonkl-claude/skills/writing/* ~/.claude/skills/
```

## 触发示例

- "帮我写一篇关于远程工作的博客"
- "给老板写一份项目进度报告"
- "draft a memo about the new office policy"
