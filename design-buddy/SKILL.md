---
name: design-buddy
description: >
  视觉生产中台——19 种设计生产能力的总控路由元技能。覆盖图表·幻灯片·海报·Logo·
  品牌UI·公众号排版·故事板·文章配图·生成艺术·Gemini文生图等全视觉链路。
  从内容出发自动选择图表类型、风格系统和输出格式。
  与 Dog-Skills 现有设计技能（architecture-diagram/fireworks-tech-graph/
  huashu-slides/dog-poster/canvas-design/algorithmic-art/brand-workshop）
  互补协作。优先推荐已有 Dog-Skills，Design Buddy 补独有能力。
  Trigger keywords: 做图, 配图, 封面, 公众号排版, 幻灯片,
  信息图, 逻辑图, 故事板, Logo设计, 品牌UI, Gemini生图,
  文章配图, 小红书图片, 海报生成, 图表生成, 分镜,
  design diagram, chart, slide deck, logo, brand UI,
  wechat layout, storyboard, illustration, infographic.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - WebFetch
  - WebSearch
metadata:
  category: design
  source: https://github.com/SpaceZephyr/design-buddy (MIT)
  upstream-author: 空格的键盘 (SpaceZephyr)
  sub-skills: 19
  version: "1.0.0"
  license: MIT
---

# Design Buddy — 视觉生产中台

> 19 种设计生产能力的总控路由。从内容出发，自动选择图表类型、风格、输出格式。
> 上游来源: [SpaceZephyr/design-buddy](https://github.com/SpaceZephyr/design-buddy) (MIT)，作者：空格的键盘

## 核心理念

```
不是让 AI 随机画一张"看起来还行"的图。
是先判断内容要表达什么，再选择合适的视觉结构、
画面比例、设计风格和输出格式。
```

---

## 路由总控

**优先级原则**：Dog-Skills 已有覆盖 → 优先推荐。Design Buddy 独有能力 → 作为补充。

### 路由表

| 用户输入特征 | 首选方案 (Dog-Skills) | Design Buddy 备选 | 说明 |
|-------------|----------------------|-------------------|------|
| "架构图" / "系统图" | **architecture-diagram** | space-architecture-diagram | Dog-Skills 更成熟（Quick/Deep双模式） |
| "流程图" / "ER图" / "时序图" | **fireworks-tech-graph** | space-chart-html-plus | Dog-Skills 8风格14类型 |
| Mermaid 图 | **fireworks-tech-graph** | space-mermaid-diagram | 均支持 |
| "做PPT" / "幻灯片" | **huashu-slides** / **humanize-ppt** | space-slide-deck | Dog-Skills 已覆盖；Design Buddy 独有 60+ 品牌自动匹配 |
| "海报" | **dog-poster** → 三子技能 | space-markdown-poster | Dog-Skills 路由更完整 |
| "Logo" / 品牌设计 | **brand-workshop** | space-logo-generator | Dog-Skills 三阶段品牌全案 |
| 品牌 UI / DESIGN.md | **dog-frontier** (58品牌) | space-brand-ui-design (62品牌) | 均支持 DESIGN.md 即插即用 |
| p5.js 生成艺术 | **algorithmic-art** | space-generative-art | Dog-Skills 官方出品 |
| 海报/静态艺术 | **canvas-design** | space-canvas-art | Dog-Skills 官方出品 |
| **文章→逻辑图** ⭐ | — | **text-logic-diagram** | Dog-Skills 独有独立技能 |
| **公众号富 HTML 排版** ⭐ | — | **space-wechat-layout** | 可复制到公众号编辑器 |
| **故事→分镜板** ⭐ | — | **space-storyboard-generator** | 故事→分镜表+图片 |
| **Gemini 文生图** ⭐ | — | **space-gemini-image** | 新后端 |
| **GPT-image-2 图表** ⭐ | — | **space-chart-image** | 图片格式图表 |
| **零代码创建生图 Skill** ⭐ | — | **space-image-skill-builder** | 元能力：创建自定义生图 Skill |
| 文章批量配图 | **huashu-image-upload** | space-image-studio / space-ai-article-illustration | Dog-Skills 已覆盖 |
| 小红书封面 | **huashu-xhs-image** | space-image-studio | Dog-Skills 已覆盖 |

⭐ = Design Buddy 独有能力，Dog-Skills 无直接覆盖。

---

## 19 个子技能总览

### 图表 & 架构图

| 子技能 | 能力 | 输出 |
|--------|------|------|
| `space-architecture-diagram` | 中文系统架构图/部署图/网络拓扑图 | HTML/SVG |
| `space-chart-html` | 流程图/架构图/ER图/旅程图等 10 类 | HTML |
| `space-chart-html-plus` | 35+ 类图表：技术/流程/战略/数据/信息展示 | HTML |
| `space-chart-image` | GPT-image-2 生成流程图/架构图/SWOT/路线图 | PNG |
| `space-mermaid-diagram` | 文本/工作流→Mermaid 图 | Mermaid/Markdown |
| `space-text-logic-diagram` | 论述性文章→递进/流程/循环/层次/对比/矩阵逻辑图 | HTML/SVG |

### 视觉 & 品牌

| 子技能 | 能力 | 输出 |
|--------|------|------|
| `space-gemini-image` | Gemini 文生图/图生图/多图参考生成 | 图片 |
| `space-gemini-article-illustration` | Markdown 文章批量配图并插入文档 | 图片+文章 |
| `space-image-studio` | GPT-image-2 总控工作室：封面/配图/图表/逻辑图 | PNG |
| `space-ai-article-illustration` | GPT-image-2/Gemini 文章批量配图 | PNG |
| `space-logo-generator` | 品牌 Logo 批量生成和方向探索 | Logo 图片 |
| `space-brand-ui-design` | 62 顶级品牌 DESIGN.md→匹配品牌风格 UI | HTML/React/Vue/CSS |
| `space-image-skill-builder` | 零代码创建自定义批量生图 Skill | 新 Skill 目录 |

### 页面 & 故事

| 子技能 | 能力 | 输出 |
|--------|------|------|
| `space-slide-deck` | Markdown→幻灯片，60+品牌匹配，可导出 PPTX/PDF | PNG+PPTX/PDF |
| `space-wechat-layout` | 公众号文章排版，可复制富 HTML 到编辑器 | HTML 预览页 |
| `space-markdown-poster` | Markdown→社交媒体分享海报 | PNG |
| `space-storyboard-generator` | 故事润色→分镜拆解→故事板生成 | 分镜表+图片 |
| `space-canvas-art` | 海报/静态艺术设计哲学与画布生成 | PNG/PDF/MD |
| `space-generative-art` | p5.js 生成艺术：粒子/流场/交互参数探索 | HTML/JS/MD |

---

## 四层工作架构

```
内容理解  →  读取内容，判断真正要表达的信息
视觉决策  →  选择图像类型·图表结构·平台比例·品牌规范·风格系统·输出媒介
资产生成  →  GPT-image-2·HTML/SVG·Mermaid·p5.js·Gemini·排版模板·本地脚本
交付整理  →  保存图片·HTML·PDF·Markdown，回写文章或生成批量文件
```

---

## 安装方式

### 本元技能

```bash
cp -r design-buddy/ ~/.claude/skills/design-buddy/
```

### 上游完整安装（获取所有 19 个子技能）

```bash
npx skills add SpaceZephyr/design-buddy
```

上游子技能遵循 `space-*` 命名规范。Dog-Skills 用户优先使用本生态内的设计技能，Design Buddy 作为独有能力的补充。

---

## 上游致谢

本元技能基于 [SpaceZephyr/design-buddy](https://github.com/SpaceZephyr/design-buddy) (MIT License)，作者：空格的键盘。

Dog-Skills 生态内协作：`architecture-diagram`（架构图）、`fireworks-tech-graph`（多风格图表）、`huashu-slides`（幻灯片）、`dog-poster`（海报路由）、`brand-workshop`（品牌设计）、`dog-frontier`（全链路前端）、`algorithmic-art`（生成艺术）、`canvas-design`（画布设计）、`text-logic-diagram`（文章→逻辑图）。
