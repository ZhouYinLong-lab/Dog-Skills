---
name: ljg-card
description: >
  内容铸卡——将内容转化为PNG视觉卡片。7种模具：长阅读卡(-l)、信息图(-i)、
  多卡片(-m)、视觉笔记(-v)、漫画(-c)、白板(-w)、大字碑刻图(-b,1080×1440)。
  Trigger keywords: 铸, cast, 做成图, 做成卡片, 做成信息图, 视觉笔记,
  sketchnote, 漫画, comic, 白板, whiteboard, 大字, 小红书卡片, ljg-card.
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

# ljg-card: 铸

> 基于 [ljg-skills](https://github.com/lijigang/ljg-skills) (6.5k+ stars)。
> 内容进去，PNG 出来。模具决定形状。

## 7种模具

| 参数 | 模具 | 说明 |
|------|------|------|
| `-l` | 长阅读卡 | 默认，适合深度内容 |
| `-i` | 信息图 | 数据/流程可视化 |
| `-m` | 多卡片 | 1080×1440 系列卡片 |
| `-v` | 视觉笔记 | 杂志+档案布局 |
| `-c` | 漫画 | 日式黑白漫画风 |
| `-w` | 白板 | 马克笔风格板布局 |
| `-b` | 大字碑刻图 | 1080×1440，适合小红书 |

## 使用示例
```
把这段话铸成一张信息图
```

## 安装
```bash
git clone https://github.com/lijigang/ljg-skills.git ~/.claude/skills/_upstream/ljg-skills/
```
