---
name: scientific-writing-editor
description: >
  科学写作编辑——专为学术场景设计的写作助手。覆盖论文手稿、基金申请书、
  推荐信、审稿回复等学术文体，确保符合学术规范和期刊要求。
  Trigger keywords: 科学写作, 论文编辑, 学术写作, scientific writing,
  论文润色, 基金申请, grant writing, 审稿回复, 推荐信, manuscript,
  期刊投稿, 学术规范。
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

# Scientific Writing Editor — 科学写作编辑

> 专为学术场景设计的写作助手，覆盖论文、基金、推荐信等学术文体。

## 核心能力

- **论文手稿**：结构化编辑、逻辑流优化、术语一致性
- **基金申请书**：说服力增强、研究意义强化、预算合理性
- **推荐信**：学术/职业推荐信，突出关键品质
- **审稿回复**：逐条回复审稿意见，礼貌而坚定
- **期刊适配**：按特定期刊格式和规范调整

## 安装

```bash
git clone https://github.com/lyndonkl/claude.git /tmp/lyndonkl-claude
cp -r /tmp/lyndonkl-claude/skills/writing/* ~/.claude/skills/
```

## 触发示例

- "帮我润色这篇论文的方法论部分"
- "帮我写一封给博士生的推荐信"
- "回复审稿人第三条意见，注意语气礼貌"
