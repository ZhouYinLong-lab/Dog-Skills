---
name: huashu-xhs-image
description: >
  小红书配图工作流——先出2-3个设计提案，选定后生成。默认AI生成（Gemini），
  精确数据表格用HTML兜底。两条路径并行出图对比，中文文字渲染验证+设计评分。
  Trigger keywords: 小红书配图, 小红书封面, 小红书图片, 做张小红书图,
  笔记配图, xhs image.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - WebFetch
metadata:
  category: design
  source: https://github.com/alchaincyf/huashu-skills (1.2k+ stars)
  author: 花叔
  version: "1.0.0"
---

# 小红书配图工作流

> 基于 [huashu-skills](https://github.com/alchaincyf/huashu-skills) (1.2k+ stars)。
> 核心原则：先提案，后生成。

## 核心能力

- 先出2-3个设计提案，选定后生成
- 两条路径并行出图对比（AI生成 + HTML渲染）
- 中文文字渲染验证 + 设计评分
- 默认AI生成，精确数据表格用HTML兜底

## 使用示例
```
帮我给这篇小红书笔记生成配图
```

## 安装
```bash
git clone https://github.com/alchaincyf/huashu-skills.git ~/.claude/skills/huashu-skills/
```
