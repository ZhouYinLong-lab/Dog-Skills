---
name: huashu-prompt-save
description: >
  Prompt分类保存——自动识别Prompt类型（技术/内容/教学/产品/通用）并分类保存到对应目录，
  更新索引。Trigger keywords: 保存prompt, 记录prompt, 整理prompt, prompt save.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
metadata:
  category: tools
  source: https://github.com/alchaincyf/huashu-skills (1.2k+ stars)
  author: 花叔
  version: "1.0.0"
---

# Prompt分类保存

> 基于 [huashu-skills](https://github.com/alchaincyf/huashu-skills) (1.2k+ stars)。

## 核心功能

- 自动识别Prompt类型：技术/内容/教学/产品/通用
- 分类保存到对应目录
- 更新索引，便于检索复用

## 使用示例
```
保存这个prompt，分类到技术类
```

## 安装
```bash
git clone https://github.com/alchaincyf/huashu-skills.git ~/.claude/skills/huashu-skills/
```
