---
name: huashu-douyin-script
description: >
  抖音爆款脚本创作——从竞品视频拆解到脚本生成的完整流程：下载抖音视频→Gemini视频分析→
  爆款公式提炼→脚本+分镜生成→AI味审校。支持种草脚本和千川素材两类输出。
  Trigger keywords: 抖音脚本, 爆款拆解, 竞品分析, 带货脚本, 千川素材,
  种草脚本, 视频拆解, 抖音视频分析.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - WebFetch
  - WebSearch
metadata:
  category: content
  source: https://github.com/alchaincyf/huashu-skills (1.2k+ stars)
  author: 花叔
  version: "1.0.0"
---

# 抖音爆款脚本创作

> 基于 [huashu-skills](https://github.com/alchaincyf/huashu-skills) (1.2k+ stars)。

## 工作流程

1. 竞品视频下载（yt-dlp）
2. Gemini 7维度视频深度分析（钩子、节奏、话术、转化设计等）
3. 爆款公式自动提炼，按品类沉淀复用
4. 脚本+分镜生成
5. 内置广审合规检查

## 使用示例
```
分析这个抖音爆款视频，帮我写一个同类型的带货脚本
```

## 安装
```bash
git clone https://github.com/alchaincyf/huashu-skills.git ~/.claude/skills/huashu-skills/
```
