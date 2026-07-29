---
name: ljg-present
description: >
  演讲铸造器——把orgmode/markdown outline 1:1铸成单文件离线HTML。
  支持black/red/yellow、hacker、hacker-dark三种主题。
  Trigger keywords: 讲这个, present, 做成演讲, slides, 标语流, 宣言体,
  slogan, manifesto, ljg-present.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
metadata:
  category: design
  source: https://github.com/lijigang/ljg-skills (6.5k+ stars)
  author: lijigang
  version: "1.0.0"
---

# ljg-present：演讲铸造器

> 基于 [ljg-skills](https://github.com/lijigang/ljg-skills) (6.5k+ stars)。
> 把 outline 铸成舞台。内容由作者决定，skill 只决定它如何被看见。

## 核心契约

**Outline 是真理，Skill 是渲染器。** 单文件离线HTML，自动处理标题封面、多行密度布局、表格、ASCII、LaTeX、自适应与翻页笔。

## 使用示例
```
把这个outline铸成演讲 slides
```

## 安装
```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.claude/skills/_upstream/ljg-skills/
```
