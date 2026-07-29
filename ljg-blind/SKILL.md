---
name: ljg-blind
description: >
  盲区扫描——读取你与AI的历史对话，照出暴露的思维盲区（不是不懂的知识，
  是让某类真相一直看不见的思维习惯），精准定位后给出针对性补全建议。
  Trigger keywords: 盲区, 扫盲区, 思维盲区, 照盲区, 看看我的思维盲区,
  我昨天想漏了什么, blind spot, ljg-blind, 检查盲区.
allowed-tools:
  - Read
  - Write
  - Edit
metadata:
  category: thinking
  source: https://github.com/lijigang/ljg-skills (6.5k+ stars)
  author: lijigang
  version: "1.0.0"
---

# ljg-blind：盲区扫描

> 基于 [ljg-skills](https://github.com/lijigang/ljg-skills) (6.5k+ stars)。

## 盲区是什么

盲区不是知识缺口。是一种结构性的思维习惯，它让某一类真相对你系统性地不可见。证据不在"他说错了什么"——在他没往哪看，他在哪绕了，他默认了什么却从没检。

## 5种盲区信号

绕开点、空转框架、单一取景框、未检前提、相邻空缺

## 使用示例
```
扫描一下我最近的思维盲区
```

## 安装
```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.claude/skills/_upstream/ljg-skills/
```
