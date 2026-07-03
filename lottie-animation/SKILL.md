---
name: lottie-animation
description: >
  一句话让 Claude Code 生成轻量 Lottie 动画动效。内置 Prompt 优化层：在调用 text-to-lottie 生成前，
  自动基于五条心法（FPS/帧数、控制项、素材、缓动、镜头运动）优化你的 prompt，展示优化版让你修改确认后再生成。
  基于 diffusionstudio/lottie (YC F24)。Trigger keywords: Lottie 动画, Lottie animation, 生成动效,
  动画动效, text-to-lottie, 轻量动画, SVG 动画, 启动动画, 点赞动效, 微动效, motion graphics,
  做个小动画, 生成一个动画, 帮我做个动效, 生成 Lottie, lottie json, 矢量动效。
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - AskUserQuestion
metadata:
  category: design
  source: https://mp.weixin.qq.com/s/ML9w6_dT0yloK3GpZ3A_dA
  upstream-skill: diffusionstudio/lottie
  install-upstream: npx skills add diffusionstudio/lottie
  author: 逛逛 GitHub (公众号)
  version: "1.0.0"
  license: MIT
---

# Lottie 动画生成 + Prompt 优化层

> 用一句话让 Claude Code 生成轻量 Lottie 动画动效。内置 Prompt 优化层，确保每次生成前你的 prompt 都经过五条心法打磨。

## 背景：什么是 Lottie / text-to-lottie

**Lottie** 是 Airbnb 开源的一种矢量动效格式——本质是一份描述矢量动画的 JSON 文件，一份 JSON 多端适用（iOS / Android / Web）。你日常刷 App 看到的启动动画、点赞爱心、下拉刷新小人、空状态插画，十有八九都是它。

**text-to-lottie**（diffusionstudio，YC F24）解决了传统动效开发的核心痛点：
- **传统流程**：设计师 AE 做动效 → Bodymovin 导出 JSON → 开发接代码。链路长、改一帧都要回到源文件
- **text-to-lottie**：Agent 生成 Lottie JSON → 本地浏览器实时预览 → Agent 自己读播放状态 → 不满意再改，闭环极短

它配套了完整的播放器项目（Vite + SolidJS + Skia WASM 渲染），支持 live reload、逐帧审查（Agent 可以直接读当前第几帧/总帧数/在播哪个场景）。

**安装上游 skill**：`npx skills add diffusionstudio/lottie`

---

## 核心工作流：Prompt 优化 → 确认 → 生成

本 skill 在 text-to-lottie 之上增加了一个 **Prompt 优化层**。每次生成动画前，先优化你的 prompt，确认后再执行。

### 完整流程

```
用户描述想要的动效
       │
       ▼
┌──────────────────────┐
│ ① Prompt 分析与优化   │  基于五条心法，自动补全缺失信息
│    输出：优化版 prompt │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ ② 用户审阅            │  ← AskUserQuestion
│    · 确认：直接生成    │    展示优化版 prompt
│    · 修改：手动调整    │    等用户决定
│    · 取消：重新描述    │
└──────────┬───────────┘
           │
           ▼  (用户确认后)
┌──────────────────────┐
│ ③ 调用 text-to-lottie│  用最终 prompt 生成 Lottie 动画
│    生成 + 预览        │
└──────────────────────┘
```

---

## 五条 Prompt 优化心法

收到用户的动效需求后，按以下五条规则逐项检查和优化：

### 规则 1：指定 FPS 和总帧数

> "60 FPS，3 秒"、“30 FPS，2 秒循环”

- 如果用户没说帧率，默认补上 **60 FPS**
- 如果用户没说时长，根据动效复杂度推断：简单动效 2 秒，中等 3 秒，复杂 4-5 秒
- 如果是要循环播放的，加上 "loop"

### 规则 2：显式声明要哪些控制项

> 默认生成的动画通常只暴露背景色一个控制。你想要颜色、大小、透明度都能调，就直接说出来。

- **颜色**：主色、辅色、背景色、渐变方向
- **大小**：缩放比例、尺寸约束
- **透明度**：淡入淡出、闪烁
- **位置**：居中、偏移、跟随路径
- 如果用户没指定，根据动效内容合理推断并补上

### 规则 3：能提供素材就别空着说

> AI 基于具体素材做出来的效果好得多。

- 用户提到了 SVG 路径？提取出来放进 prompt
- 用户提到了品牌 logo？提醒用户可以提供 SVG 文件
- 用户描述了具体形状？保留描述，补充"请基于以下形状生成：[描述]"
- 如果没有素材，用精确的几何描述替代模糊描述

### 规则 4：缓动函数术语化

> 说 ease-in、ease-out、ease-in-out，AI 听得懂。别光说"动画"。

- "慢慢开始" → `ease-in`
- "慢慢结束" → `ease-out`
- "平滑过渡" → `ease-in-out`
- "弹性效果" → `spring` 或 `bounce`
- "匀速" → `linear`
- 如果用户没指定，根据动效类型推荐合适的缓动

### 规则 5：镜头运动写入 prompt

> 专业动效很多靠镜头运动。推、拉、摇、移、变焦，写进 prompt 里，AI 会用 group 变换模拟出来。

- **推**：镜头推进，主体变大 → "zoom in / scale up"
- **拉**：镜头拉远，主体变小 → "zoom out / scale down"
- **摇**：水平旋转 → "pan horizontally / rotate Y"
- **移**：平移 → "translate / move from A to B"
- **变焦**：焦点切换 → "focus shift / blur to sharp"
- 如果用户描述了空间运动，翻译成镜头术语

---

## 优化版 Prompt 输出模板

每次优化后，用以下格式展示给用户：

```
## 🎯 优化版 Prompt

[经过五条心法优化后的完整 prompt]

---

### 📋 优化明细

| 规则 | 原始 | 优化后 |
|------|------|--------|
| 1. FPS/帧数 | [原始或"未指定"] | [优化后] |
| 2. 控制项 | [原始或"未指定"] | [优化后] |
| 3. 素材 | [原始或"未指定"] | [优化后] |
| 4. 缓动 | [原始或"未指定"] | [优化后] |
| 5. 镜头 | [原始或"未指定"] | [优化后] |

---

请选择：
1. ✅ **确认生成** — 用优化版 prompt 开始生成
2. ✏️ **我要修改** — 告诉我你想调整什么
3. ❌ **取消** — 重新描述需求
```

---

## 生成阶段

用户确认后，提示用户执行：

```
请在你的 Claude Code 终端中运行：
npx skills add diffusionstudio/lottie

然后用以下 prompt 生成动画：

[最终确认的 prompt]
```

如果 text-to-lottie skill 已安装，直接引导调用。

---

## 使用示例

### 示例 1：模糊需求 → 优化 → 生成

**用户**：帮我做一个心跳的动效。

**Skill 优化后**：
> 生成一个心跳动画 Lottie：一个心形图标以 60 FPS 循环缩放，模拟心跳节奏——快速放大（0.1s）→ 快速缩小（0.1s）→ 暂停（0.3s）→ 重复。使用 ease-in-out 缓动。心形颜色为红色 #FF2D55，背景透明。总时长 2 秒循环。允许控制心形颜色和缩放幅度。

### 示例 2：有素材的优化

**用户**：把桌面 hello.svg 做成动画。

**Skill 优化后**：
> 读取桌面的 hello.svg 路径，做成 Lottie 动画：沿路径自然方向逐笔揭示文字，套用 Apple 风格渐变（#007AFF → #00C7BE），ease-in-out 节奏，透明背景。60 FPS，3 秒。允许控制渐变起始色、线宽、动画速度。

### 示例 3：品牌动效

**用户**：苹果 logo 晃来晃去最后消失。

**Skill 优化后**：
> 制作一个 Lottie 动效：Apple logo 以弹簧物理效果左右晃动（振幅递减），最后跳一下（快速 scale up 1.2x）缩成一个点消失（scale to 0 + opacity to 0）。60 FPS，2.5 秒。使用 spring 缓动用于摇晃，ease-in 用于消失。深色背景 #1a1a1a。允许控制 logo 颜色、晃动强度、动画时长。
