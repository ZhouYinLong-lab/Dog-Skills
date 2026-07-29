---
name: huashu-wechat-image
description: >
  公众号配图工作流——生成封面图（2.35:1）、正文插图（16:9/4:3）、信息图。
  两条路径：AI生成（Gemini视觉创意型）和HTML渲染（文字精确型）。
  先提案后生成，3种推荐风格按文章类型匹配。Trigger keywords: 公众号配图,
  公众号封面, 文章配图, 正文插图, 公众号图片, wechat image.
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

# 公众号配图工作流

> 基于 [huashu-skills](https://github.com/alchaincyf/huashu-skills) (1.2k+ stars)。
> 核心原则：先提案，后生成。

## 核心能力

- **封面图**（2.35:1）、**正文插图**（16:9/4:3）、**信息图**
- **两条路径**：AI生成（视觉创意型）/ HTML渲染（文字精确型）
- 3种推荐风格按文章类型匹配
- 自动上传ImgBB获取永久链接

## 使用示例
```
给这篇公众号文章生成封面图和正文配图
```

## 安装
```bash
git clone https://github.com/alchaincyf/huashu-skills.git ~/.claude/skills/huashu-skills/
```
