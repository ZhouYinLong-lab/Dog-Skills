---
name: dog-poster
description: >
  海报设计工作室元技能(Dog-Poster)——上游通过风格询问确定你的需求，下游自动路由到最合适的
  海报生成器：(1) 信息图风 → article-poster，(2) 通用设计风 → canvas-design，
  (3) 手工拼贴艺术风 → torn-paper-collage-poster。三个子技能各有所长，
  本技能负责帮你选对工具。
  Trigger keywords: 海报设计, 做海报, 海报, poster, 设计海报, 生成海报,
  dog-poster, poster studio, 海报工作室, 帮我做海报, 宣传海报, 活动海报, 信息图海报,
  拼贴海报, 我要做海报, create a poster, design a poster, Dog-Poster。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
  - AskUserQuestion
  - WebFetch
metadata:
  category: design
  source: composite (article-poster + canvas-design + torn-paper-collage-poster)
  version: "1.0.0"
  license: MIT
---

# Dog-Poster — 海报设计工作室

> 先问你要什么风格，再帮你选对工具。三个海报子技能各有所长，本技能帮你做选择。

## 上游：风格询问与路由

收到海报需求时，先通过以下问题确定风格方向：

```
┌─────────────────────────────────────────────────────────────┐
│               Dog-Poster — 上游路由                          │
│                                                              │
│  ① 你的内容来源是什么？                                       │
│     A. 一篇文章/链接 → 提取要点做信息图                       │
│     B. 一个活动/产品 → 需要宣传海报                           │
│     C. 追求艺术感 → 想要独特的手工质感                        │
│                                                              │
│  ② 你想要的视觉风格？                                         │
│     A. 数据可视化·信息图 —— 要点提炼+图表+知识卡片            │
│     B. 通用设计·活动海报 —— 干净专业·高分辨率可印刷           │
│     C. 手工拼贴·Zine风   —— 撕纸·邮票·胶带·复印机纹理        │
│                                                              │
│  ③ 在什么平台使用？                                           │
│     A. 社交媒体（小红书/公众号/Twitter）→ 竖版/方版            │
│     B. 印刷张贴 → 高分辨率 A3/A4                              │
│     C. Slack/内部沟通 → 轻量快速                              │
└─────────────────────────────────────────────────────────────┘
```

## 下游：路由到子技能

```
你的回答 → 自动匹配
    │
    ├── 内容来源=文章 / 风格=信息图
    │       → article-poster
    │       → 文章URL→要点提取→数据可视化海报
    │
    ├── 风格=通用设计 / 需要印刷
    │       → canvas-design
    │       → 自然语言→高分辨率PNG/PDF海报
    │
    └── 风格=手工拼贴 / 艺术感
            → torn-paper-collage-poster
            → 撕纸层叠+邮票+胶带+复印机纹理
```

## 三个子技能速览

| 子技能 | 一句话 | 输入 | 输出 |
|--------|--------|------|------|
| **article-poster** | 文章→信息图海报 | URL 或文本 | 数据可视化风海报 |
| **canvas-design** | 程序化通用海报 | 自然语言描述 | 高分辨率 PNG/PDF |
| **torn-paper-collage-poster** | 手工拼贴艺术海报 | 主题描述 | 撕纸拼贴风海报 |

## 安装

```bash
# 三个子技能各自独立安装
npx skills add MagicCube/agentara --skill article-poster -y -g
/plugin install example-skills@anthropic-agent-skills  # canvas-design
npx skills add MagicCube/agentara --skill torn-paper-collage-poster -y -g
```

## 使用方式

对 Claude Code 说：

| 你说 | 路由到 |
|------|--------|
| "把这篇文章做成信息图海报" | → article-poster |
| "帮我设计一张产品发布会的海报" | → canvas-design |
| "做一张独立音乐演出的拼贴海报" | → torn-paper-collage-poster |
| "帮我做海报"（没说风格） | → 三连问帮你选 |

## 三个都试试？

不确定选哪个时，可以说：

> "同一个主题，帮我用三种风格各做一张海报，我对比看看"

三个子技能会并行生成：信息图版 + 通用设计版 + 手工拼贴版。
