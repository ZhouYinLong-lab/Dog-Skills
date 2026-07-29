---
name: huashu-image-upload
description: >
  文章配图一键生成并上传图床，自动插入Markdown链接。AI生成/公共领域/免费图库三层优先级。
  Trigger keywords: 配图, 插图, 上传图片, 文章配图, image upload.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
metadata:
  category: design
  source: https://github.com/alchaincyf/huashu-skills (1.2k+ stars)
  author: 花叔
  version: "1.0.0"
---

# 图片配图与上传

> 基于 [huashu-skills](https://github.com/alchaincyf/huashu-skills) (1.2k+ stars)。

## 核心功能

- 三层优先级：AI生成 / 公共领域 / 免费图库
- 自动上传ImgBB，返回永久Markdown链接
- 适合任何需要配图的写作场景

## 使用示例
```
给这篇文章自动配图并上传
```

## 安装
```bash
git clone https://github.com/alchaincyf/huashu-skills.git ~/.claude/skills/huashu-skills/
```
