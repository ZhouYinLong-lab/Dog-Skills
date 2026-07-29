---
name: huashu-research
description: >
  结构化网络调研——先建文件再搜索，每搜一轮就保存一轮，确保调研成果增量持久化，
  不怕会话截断丢失。阶段摘要+最终简报双层输出。
  Trigger keywords: 调研, 搜索资料, 帮我查一下, 了解一下, 最新信息, research.
allowed-tools:
  - Read
  - Write
  - Bash
  - WebFetch
  - WebSearch
metadata:
  category: thinking
  source: https://github.com/alchaincyf/huashu-skills (1.2k+ stars)
  author: 花叔
  version: "1.0.0"
---

# 结构化调研

> 基于 [huashu-skills](https://github.com/alchaincyf/huashu-skills) (1.2k+ stars)。

## 核心机制

- **增量持久化**：先建文件再搜索，每搜一轮保存一轮
- **双层输出**：阶段摘要 + 最终简报
- 适合需要多轮搜索的深度调研

## 使用示例
```
调研一下2025年AI编程工具的市场格局
```

## 安装
```bash
git clone https://github.com/alchaincyf/huashu-skills.git ~/.claude/skills/huashu-skills/
```
