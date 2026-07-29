---
name: ppt-master
description: >
  AI 从任意文档（PDF/Word/Markdown/URL）生成真正可编辑的 .pptx 文件——原生 PowerPoint 形状、
  图表和动画（DrawingML），不是截图拼凑的假 PPT。内置 20 套模板（Anthropic 风、麦肯锡风、
  Google 风、学术答辩风等），支持多尺寸输出（16:9/4:3/小红书竖版/A4），6000+ Tabler 图标库 +
  33 种图表模板，演讲者备注可转语音旁白（90+ 语言）并导出 MP4 视频。数据本地运行，不上传云端。
  Trigger keywords: 做PPT, 生成PPT, PPT, PowerPoint, 幻灯片, 演示文稿, 生成幻灯片,
  文档转PPT, PDF转PPT, Word转PPT, Markdown转PPT, 答辩PPT, 组会PPT, 投资人Pitch,
  学术PPT, 商务PPT, ppt-master, ppt master, make a PPT, create PowerPoint,
  generate slides, 帮我做PPT, 生成一个PPT, 做一份演示文稿, 做presentation,
  make a presentation, 转成PPT, 导出PPTX.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Agent
  - TaskCreate
  - WebFetch
metadata:
  category: content
  source: https://github.com/hugohe3/ppt-master
  install: /plugin install ppt-master@ppt-master
  version: "1.0.0"
  license: MIT
---

# PPT Master — AI 生成真正可编辑的 PowerPoint

> 27,000+ GitHub Star · MIT 开源 · 不是截图拼凑，每个文本框、形状、图表都能独立编辑

PPT Master 是 Hugo He 开发的 Claude Code Skill，将任意文档（PDF、Word、Markdown、网页链接）自动生成**真正可编辑的 .pptx 文件**——底层用的是 DrawingML（PowerPoint 原生矢量格式），每个元素都可以在 PowerPoint 里独立点击编辑，和手写的一样。

## 和"截图流"PPT 工具的区别

```
截图流工具                          PPT Master
┌─────────────────────┐           ┌─────────────────────┐
│ AI 生成一堆 PNG 图片  │           │ AI 生成 SVG 设计稿    │
│ 塞进 PPT 当背景       │           │ Python → DrawingML   │
│ ❌ 改不了文字          │           │ ✅ 每个元素独立可编辑  │
│ ❌ 调不了颜色          │           │ ✅ 原生形状+图表+动画 │
│ ❌ 换不了图表数据       │           │ ✅ 图表数据可修改     │
└─────────────────────┘           └─────────────────────┘
```

技术路线：`输入文档 → AI 生成 SVG（设计稿）→ Python 转换 SVG → DrawingML → 输出原生可编辑 .pptx`。SVG 和 DrawingML 本质同源（2D 矢量格式），转换是"方言翻译"而非格式跨越。

## 核心能力

### 🎨 20 套内置模板

Anthropic 风 · 麦肯锡风 · Google 风 · 学术答辩风 · 科技创业风 · 极简风 · 渐变风 · 复古风 · 更多——覆盖商业、学术、科技全场景。

### 📐 多尺寸输出

16:9 宽屏 · 4:3 标准 · 小红书竖版 3:4 · 朋友圈 1:1 · A4 打印 · 自定义尺寸。

### 🖼️ 内置资源库

- **6000+ Tabler 图标**：无需外部下载，按需自动引用
- **33 种图表模板**：柱状图、折线图、饼图、雷达图、甘特图、流程图等

### 🎬 原生动画 & 动效

两层动画系统，均为 DrawingML 原生对象，可自由编辑：

| 层级 | 说明 | 默认 |
|------|------|------|
| **页面过渡** (Slide Transitions) | 淡入淡出等页面切换效果 | ✅ 开启 |
| **元素入场** (Entrance Animations) | 逐元素飞入、淡入等 | ❌ 关闭，`-a auto` 开启 |

三种触发方式：
- **`on-click`** — 点击触发，适合现场演讲
- **`after-previous`** — 自动播放，适合旁白配音/视频导出
- **`with-previous`** — 并行展示

### 🎙️ 旁白转语音 + 导出视频

演讲者备注 → AI 语音旁白（90+ 语言）→ 嵌入 PPTX → PowerPoint 一键导出 MP4 视频。动画自动切到 `after-previous` 模式配合旁白节奏。

### 🔒 本地运行

所有处理在本地完成，文档不离开你的电脑。仅消耗模型 API token 费用，无其他成本。

## 安装

### 方式一：Claude Code 插件（推荐）

```bash
# 在 Claude Code 中执行：
/plugin marketplace add hugohe3/ppt-master
/plugin install ppt-master@ppt-master
```

### 方式二：跨 Agent CLI

```bash
npx skills add hugohe3/ppt-master
```

### 环境依赖

```bash
pip install -r requirements.txt   # Python 3.10+
```

## 使用方式

```
"帮我把这份 PDF 做成 PPT，麦肯锡风，10 页以内"
"把这篇 Markdown 文档转成学术答辩风格的幻灯片"
"用这个 Word 文档生成一份投资人 Pitch，16:9，带动画"
"给这个网页链接做一份小红书竖版 PPT"
"给这份 PPT 加上演讲旁白，导出 MP4"
```

## 动画开启方式

```bash
-a auto                    # AI 根据内容语义自动分配动画
# 或通过 animations.json 精细控制每个元素的动画
```

> **设计哲学**：作者刻意默认关闭元素动画——用户反馈自动动画显得"突兀"和"AI 味太重"。需要时按需开启，与 Dog-Skills 的反「AI 味」理念一致。

## 性能参考

| 页数 | 预计生成时间 | 推荐模型 |
|------|-------------|----------|
| 5 页 | ~5-10 分钟 | Claude Sonnet |
| 10 页 | ~10-20 分钟 | Claude Opus（推荐） |
| 20+ 页 | ~30+ 分钟 | Claude Opus，分批生成 |

## 最佳搭配

- **humanize-ppt**：先用 humanize-ppt 做演讲结构设计（AST 大纲+演讲体检），再用 ppt-master 渲染成可编辑 .pptx
- **baoyu-skills**：需要配图时，用 baoyu-image-gen 生成插图再嵌入 PPT
- **markitdown**：先把 PDF/Word 转成干净 Markdown，再喂给 ppt-master，效果更好
- **theme-factory**：用主题工厂生成品牌配色方案，作为 ppt-master 的自定义模板参考

## 局限

- 需要 Python 3.10+ 环境（非纯浏览器方案）
- 10 页 PPT 约 10-20 分钟，非秒级生成
- 无可视化拖拽界面，全程通过对话操作
- 图表是静态形状，不绑定 Excel 动态数据
