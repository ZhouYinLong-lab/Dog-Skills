---
name: huashu-info-search
description: >
  信息搜索与知识管理——多渠道搜索新产品/新技术，交叉验证后自动存入知识库。
  信息源优先级管理（官方>科技媒体>社区），自动过滤过时信息。
  Trigger keywords: 最新信息, 新产品, 搜索资料, 查资料, 了解XX, info search.
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

# 信息搜索与知识管理

> 基于 [huashu-skills](https://github.com/alchaincyf/huashu-skills) (1.2k+ stars)。

## 核心功能

- 多渠道搜索 + 交叉验证
- 信息源优先级：官方 > 科技媒体 > 社区
- 自动过滤过时信息（忽略2025年前的百度/知乎结果）
- 可靠信息自动保存到 `_knowledge_base`

## 使用示例
```
搜索一下Claude Code最新版本的新功能
```

## 安装
```bash
git clone https://github.com/alchaincyf/huashu-skills.git ~/.claude/skills/huashu-skills/
```
