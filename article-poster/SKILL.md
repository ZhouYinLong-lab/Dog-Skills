---
name: article-poster
description: >
  文章→信息图海报——从文章 URL/文本自动生成精美信息图海报，适合社交媒体传播。
  Trigger keywords: 文章海报, 信息图, article poster, infographic,
  公众号海报, 小红书配图, 内容海报, 知识卡片, blog to poster。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Agent
  - WebFetch
  - WebSearch
metadata:
  category: design
  source: MagicCube/agentara
  version: "1.0.0"
  license: MIT
---

# Article Poster — 文章→信息图海报

> 从文章链接或文本自动生成精美信息图海报。

## 核心能力

- **自动提取关键信息**：从 URL/文本中提取核心观点
- **信息图布局**：数据可视化 + 要点提炼 + 金句高亮
- **多平台适配**：小红书竖版、公众号横版、Twitter 卡片
- **风格可选**：极简、科技、文艺、商务

## 安装

```bash
npx skills add MagicCube/agentara --skill article-poster -y -g
```

## 触发示例

- "把这篇博客做成信息图海报"
- "这篇文章的核心观点做成一张长图"
- "帮我做一个知识卡片发小红书"
