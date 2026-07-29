---
name: ljg-qa
description: >
  信息提问机——把文章/论文/书的核心观点抽成 Q-A 对。Question 切要害，
  Answer 简洁清晰有形式化收口。Trigger keywords: 问答, Q&A, QA, 提问,
  抽取问题, ljg-qa.
allowed-tools:
  - Read
  - Write
  - WebFetch
metadata:
  category: thinking
  source: https://github.com/lijigang/ljg-skills (6.5k+ stars)
  author: lijigang
  version: "1.0.0"
---

# ljg-qa: 问答提取

> 基于 [ljg-skills](https://github.com/lijigang/ljg-skills) (6.5k+ stars)。
> 不是 FAQ 生成器——是思想脚手架。

## 核心概念

把核心观点拆成「为什么—怎么—边界」的问答链。读者顺着 Q 走过去，每个 A 砸下来一枚钉子，复现作者整套推理。

## 使用示例
```
把这篇文章的核心观点抽成 Q&A 对
```

## 安装
```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.claude/skills/_upstream/ljg-skills/
```
