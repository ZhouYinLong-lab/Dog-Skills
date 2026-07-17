---
name: animation-craft
description: >
  动画工艺元技能——整合术语转换(animation-vocabulary)、设计工程(emil-design-eng)、
  质量审查(review-animations)三阶段流水线。把模糊的动效需求变成精确的动画代码，
  再经过10条硬标准审查，输出 Before→After→Why 优化建议。
  解决 AI 生成动画"生硬、缓动不对、时长不合理"的常见问题。
  Trigger keywords: 动画审查, 动效优化, animation review, 动画不自然,
  动效太生硬, animation craft, 动画质量, 动效术语, 缓动函数,
  动画时长, prefers-reduced-motion, 动画质感, 微交互动效,
  animation quality, motion design review, 动画不够丝滑,
  这个动画怪怪的, 动效帮我看看, review my animations,
  CSS动画优化, spring animation, 弹性动画, 阻尼动画.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
metadata:
  category: design
  source: https://github.com/emilkowalski/skills (MIT)
  upstream-author: Emil Kowalski (Vercel → Linear, Sonner/Vaul author)
  version: "1.0.0"
  license: MIT
---

# Animation Craft — 动画工艺元技能

> 整合 Emil Kowalski 三件套为一站式动画工艺流水线。AI 写的动画代码不够好？用这套规则让它变好。
> 上游来源：[emilkowalski/skills](https://github.com/emilkowalski/skills) (MIT, 4500+ ⭐)

## 核心理念

```
"AI 不会自动写出有审美的动画——它需要一套工艺规则。
 这套规则 = 精确的术语 + 正确的物理参数 + 严格的审查标准。"
                                                  — Emil Kowalski
```

动画工艺的三个层次，缺一不可：
- **说对词** → AI 才能理解你要什么（词汇层）
- **做对事** → AI 才能产出正确的代码（工程层）
- **验质量** → 确保输出达到工艺标准（审查层）

---

## 工作流程总览

```
用户描述动效需求
       │
       ▼
┌─────────────────────────────────┐
│ Phase 1: Vocabulary 术语转换     │
│ 模糊感觉 → 精确动画术语         │
│ "弹出来" → spring scale-in      │
│ "一个个出来" → staggered reveal  │
└──────────┬──────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│ Phase 2: Design-Eng 设计工程    │
│ 按工艺规则生成/优化动画代码      │
│ 时长·缓动·GPU属性·无障碍        │
└──────────┬──────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│ Phase 3: Review 质量审查        │
│ 10条硬标准逐项审查              │
│ 输出 Before → After → Why       │
└─────────────────────────────────┘
```

### 路由逻辑

根据用户输入自动判断从哪个阶段进入：

| 用户说什么 | 从哪开始 |
|-----------|----------|
| "这个动效叫什么？" / "用什么术语描述这个效果？" | Phase 1 → 2 → 3（完整流程） |
| "帮我写一个弹窗动画" / "做一个下拉菜单的动效" | Phase 1（快速术语确认）→ Phase 2 |
| "审查一下这个组件的动画" / "这个动效怪怪的" | Phase 3（直接审查） |
| "优化这段动画代码" | Phase 2（优化已有代码）→ Phase 3 |

---

## Phase 1: Vocabulary — 术语转换

> **目标**：把"模糊的感觉"翻译成"精确的动画术语"，让 AI 准确理解你的意图。

### 为什么这一步至关重要

同样的动画需求，用不同方式描述，AI 的输出质量天差地别：

| ❌ 模糊描述 | ✅ 精确术语 | AI 理解差异 |
|------------|------------|------------|
| "弹出来" | spring scale-in with ease-out | 模糊→随机实现 / 精确→可预测的弹性缩放 |
| "一个个出来" | staggered entrance, 50ms delay per item | 模糊→可能同时出现 / 精确→明确逐个延迟 |
| "页面切换" | shared element transition | 模糊→简单fade / 精确→元素在页面间持续变形 |
| "菜单展开" | origin-aware scale-in from trigger | 模糊→从屏幕中心缩放 / 精确→从触发按钮位置缩放 |
| "列表滚动" | rubber-banding at boundary | 模糊→硬边界停止 / 精确→iOS风格弹性过冲 |
| "卡片出现" | scale(0.95→1) + opacity(0→1), ease-out, 200ms | 模糊→可能从scale(0)开始(无体积感) |

### 术语词汇表

#### 入场/出场 (Enter/Exit)

| 感觉描述 | 精确术语 | 推荐参数 |
|---------|---------|---------|
| "淡入" | fade in | opacity 0→1, 150-300ms |
| "滑入" | slide in | translateY(10px→0) + opacity, ease-out |
| "弹入" | spring scale-in | scale(0.95→1), spring, bounce: 0-0.2 |
| "放大出现" | scale-up reveal | scale + opacity, transform-origin: trigger |
| "从触发位置展开" | origin-aware scale-in | transform-origin 动态设置 |

#### 序列动画 (Sequencing)

| 感觉描述 | 精确术语 | 推荐参数 |
|---------|---------|---------|
| "一个个出来" | staggered entrance | 30-80ms delay per item |
| "依次展开" | sequential reveal | cascade, 50-100ms stagger |
| "波浪效果" | wave animation | stagger + translateY, 正弦分布延迟 |

#### 状态切换 (State Transitions)

| 感觉描述 | 精确术语 | 推荐参数 |
|---------|---------|---------|
| "页面切换" | shared element transition | FLIP 动画模式 |
| "列表重排" | layout animation | spring, bounce: 0 |
| "展开/收起" | collapse/expand | height auto→0, 或用 clip-path inset |
| "切换Tab" | tab transition | clip-path inset + fade |

#### 反馈 (Feedback)

| 感觉描述 | 精确术语 | 推荐参数 |
|---------|---------|---------|
| "按下有反应" | press feedback | scale(0.97), 100ms ease-out |
| "点击涟漪" | ripple effect | radial-gradient expand + fade |
| "拉到顶弹一下" | rubber-banding | 过冲 + spring 回弹 |
| "摇晃表示错误" | shake | translateX(±5px), 3-4次, 300ms |

#### 缓动 (Easing)

| 感觉描述 | 精确术语 | CSS / JS |
|---------|---------|---------|
| "慢慢开始" | ease-in | `cubic-bezier(0.4, 0, 1, 1)` |
| "慢慢结束" | ease-out | `cubic-bezier(0, 0, 0.2, 1)` |
| "平滑过渡" | ease-in-out | `cubic-bezier(0.4, 0, 0.2, 1)` |
| "弹性效果" | spring / bounce | `spring({ bounce: 0.2 })` |
| "匀速" | linear | `cubic-bezier(0, 0, 1, 1)` |
| "iOS抽屉" | drawer easing | `cubic-bezier(0.32, 0.72, 0, 1)` |
| "惯性滚动" | momentum / decay | deceleration rate 0.998 |

#### 滚动 (Scroll)

| 感觉描述 | 精确术语 | 推荐实现 |
|---------|---------|---------|
| "视差" | parallax | translateY 反向, 速率比 0.5-0.8 |
| "滚动到边界弹一下" | rubber-banding | 渐进阻力函数 |
| "吸附" | snap scroll | CSS scroll-snap |
| "滚动触发动画" | scroll-driven animation | CSS animation-timeline: scroll() |

### Phase 1 输出模板

```
## 🏷️ 术语翻译

**原始需求**: [用户原话]
**翻译结果**: [精确术语1] + [精确术语2] + [精确术语3]

**推荐参数**:
- 动画类型: [类型]
- 缓动: [easing]
- 时长: [duration]ms
- 属性: [只列 transform/opacity]

是否按此理解继续生成代码？
```

---

## Phase 2: Design-Eng — 设计工程规则

> **目标**：生成/优化动画代码，确保每一行动画都符合工艺标准。

### 规则 1：动画时长控制

| UI 元素 | 推荐时长 | 原因 |
|---------|---------|------|
| 按钮按下反馈 | 100-160ms | 高频操作，需即时响应 |
| Tooltip 出现 | 125-200ms | 辅助信息，不能干扰 |
| 下拉菜单展开 | 150-250ms | 需感知但不拖沓 |
| 弹窗/Modal 进入 | 200-500ms | 需建立空间感 |
| Drawer/Sheet 滑出 | 250-400ms | 需跟随手势节奏 |
| 页面切换 | 300-500ms | 需传达导航方向 |
| Toast 通知 | 200-300ms 进入, 3-5s 停留 | 信息传递优先 |

**铁律**：UI 动画不超过 **300ms**，除非是大面积布局变化（Modal/Drawer/页面切换）。

### 规则 2：缓动函数选择

```
入场动画 → ease-out (cubic-bezier(0, 0, 0.2, 1))
  元素从无到有，快速进入后平稳落位。用户等待的是结果，不是过程。

出场动画 → ease-in (cubic-bezier(0.4, 0, 1, 1))
  元素从有到无，快速启动后缓慢消失。用户已不需要它，让它快走。

状态切换 → ease-in-out (cubic-bezier(0.4, 0, 0.2, 1))
  元素在原地变形，对称的开始和结束。

弹性交互 → spring (bounce: 0-0.2)
  直接操作（拖拽/滑动），需要物理真实感。
```

**铁律**：UI 动画**禁止**使用 `ease-in` 作为入场缓动——它会让人感觉界面卡顿。

### 规则 3：只动画 GPU 友好属性

```
✅ 始终动画:
  - transform (translate, scale, rotate, skew)
  - opacity

❌ 绝不动画:
  - width, height → 触发 layout，掉帧
  - top, left, right, bottom → 触发 layout
  - margin, padding → 触发 layout
  - border-width → 触发 paint

⚠️ 谨慎使用:
  - box-shadow → 触发 paint，低端设备卡
  - filter: blur() → 触发 paint，只在必要时用
  - background-color → 触发 paint，时长需控制在150ms内
```

替代方案：
- 需要"展开"效果？→ 用 `transform: scaleY()` 替代 `height` 动画
- 需要"位移"？→ 用 `transform: translate()` 替代 `top/left`
- 需要"淡入+模糊"？→ 用 `opacity` + 预设模糊静态层

### 规则 4：弹出层必须从触发位置展开

```css
/* ❌ 错误：从屏幕中心弹出 */
.popover {
  animation: scaleIn 200ms ease-out;
  transform-origin: center; /* 没有空间感 */
}

/* ✅ 正确：从触发元素位置弹出 */
.popover {
  animation: scaleIn 200ms ease-out;
  transform-origin: var(--trigger-x) var(--trigger-y); /* 动态计算 */
}
```

适用场景：Popover、Dropdown Menu、Context Menu、Tooltip、Sheet。

### 规则 5：入场从 scale(0.95) 开始，不是 scale(0)

```css
/* ❌ 错误：无体积感的缩放 */
@keyframes badEntrance {
  from { transform: scale(0); opacity: 0; }
  /* 元素凭空产生，没有物质感 */
}

/* ✅ 正确：有体积感的缩放 */
@keyframes goodEntrance {
  from { transform: scale(0.95); opacity: 0; }
  to   { transform: scale(1); opacity: 1; }
  /* 元素始终存在体积，视觉自然 */
}
```

### 规则 6：自定义缓动曲线优于内置 easing

```css
:root {
  /* 内置 easing 通常不理想，改用精确 cubic-bezier */
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
  --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
  --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

### 规则 7：弹簧物理参数指南

使用 spring 动画时的推荐参数（Framer Motion / Motion 等库）：

| 交互类型 | Damping Ratio | Response (s) | Bounce |
|---------|---------------|-------------|--------|
| 移动/重定位 | 1.0 | 0.4 | 0 |
| 旋转 | 0.8 | 0.4 | 0 |
| Drawer/Sheet | 0.8 | 0.3 | 0 |
| 拖拽松手（慢速） | 1.0 | 0.4 | 0 |
| 拖拽甩出（快速） | 0.8 | 0.3 | 0.2 |

```js
// 默认：无弹性的阻尼弹簧（最常用）
animate(el, { y: 0 }, { type: 'spring', bounce: 0, duration: 0.4 });

// 仅手势松手时有轻微弹性
animate(el, { y: target }, { type: 'spring', bounce: 0.2, duration: 0.4 });
```

### 规则 8：中断性 — 动画必须可重定向

```
CSS transition 的优势：可中断
  - 在 transition 运行时更新目标值，动画从中断点平滑重定向到新目标
  - 适用于：hover 状态、下拉菜单、悬浮卡片

CSS @keyframes 的劣势：不可中断
  - 已开始的 keyframe 无法被用户交互中断
  - 避免用于：交互式 UI 元素（除非是纯装饰性的）

Spring 的优势：天生可中断
  - spring 始终从当前值开始，天然支持中断
  - 适用于：手势驱动的 UI、拖拽、滑动
```

**铁律**：交互式 UI 元素**禁止**使用 `@keyframes` 做入场/出场。用 CSS transition 或 spring。

### 规则 9：进场和出场不对称

```css
/* ✅ 好的设计：非对称 */
.menu-enter  { animation: slideDown 200ms ease-out; }    /* 从上方展开 */
.menu-exit   { animation: fadeOut 150ms ease-in; }       /* 直接淡出 */

/* ❌ 坏的设计：镜像反转 */
.menu-enter  { animation: slideDown 200ms ease-out; }
.menu-exit   { animation: slideUp 200ms ease-in; }       /* 完全反向 = 无聊 */
```

为什么？进场是"建立空间关系"，出场是"清除已不需要的元素"——两个时刻的用户心智完全不同。

### 规则 10：无障碍 — 尊重用户动效偏好

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
  
  /* 但保留微妙的透明度变化（不涉及空间位移） */
  .toast { transition: opacity 200ms ease; }
}
```

额外考虑：
```css
/* 减少透明度（对有视觉障碍的用户） */
@media (prefers-reduced-transparency: reduce) {
  .toolbar { background: white; backdrop-filter: none; }
}

/* 增强对比度 */
@media (prefers-contrast: more) {
  .card { border: 2px solid currentColor; }
}
```

---

## Phase 3: Review — 10 条审查硬标准

> **目标**：逐条审查动画代码，每一条必须是"通过"而非"差不多"。输出 Before → After → Why。

### 审查清单

| # | 标准 | 检查方法 | 严重程度 |
|---|------|---------|---------|
| 1 | **动画有目的** | 这个动画是在反馈/解释/装饰？还是纯粹"炫"？ | 🔴 阻断 |
| 2 | **频率匹配** | 高频操作（每天几十次）→ 极短或无动画；低频（onboarding）→ 可更丰富 | 🔴 阻断 |
| 3 | **缓动正确** | 入场=ease-out, 出场=ease-in, 状态=ease-in-out。没有 UI 用 ease-in 入场 | 🔴 阻断 |
| 4 | **时长 ≤ 300ms** | 除了 Modal/Drawer/页面切换，所有 UI 动画都检查时长 | 🟡 严重 |
| 5 | **transform-origin 正确** | Popover/Dropdown 的 transform-origin 指向触发元素，非默认 center | 🟡 严重 |
| 6 | **可中断** | 交互式元素不使用 @keyframes；动画进行中可以响应新的用户输入 | 🟡 严重 |
| 7 | **只用 transform + opacity** | 检查是否动画了 width/height/top/left/margin 等 layout 属性 | 🔴 阻断 |
| 8 | **无障碍** | prefers-reduced-motion 处理正确；键盘操作不触发大型动画 | 🟡 严重 |
| 9 | **进场≠出场镜像** | 进入和退出使用不同的动画，而非简单反转 | 🟢 建议 |
| 10 | **整体统一** | 所有动画属于同一套缓动和时长体系，而非散乱混搭 | 🟢 建议 |

### 审查输出格式

对每个问题，用 Before → After → Why 三段式输出：

```
## 🔍 动画审查报告

### 问题 #1: 弹窗使用 ease-in 入场
**严重程度**: 🔴 阻断

**Before**:
```css
.modal { animation: modalIn 300ms ease-in; }
```

**After**:
```css
.modal { animation: modalIn 300ms ease-out; }
```

**Why**: ease-in 在开始阶段缓慢，让用户感觉"界面卡住了才反应过来"。
入场动画应用 ease-out——快速启动、平稳落位，用户感知的是结果而非过程。
```

### 常见问题速查

| 现象 | 根因 | 修复 |
|------|------|------|
| "动画感觉拖沓" | 用了 ease-in 且时长 >300ms | 改为 ease-out, ≤250ms |
| "弹窗从奇怪的地方出来" | transform-origin 是默认 center | 动态设为触发元素位置 |
| "列表展开时卡顿" | 动画了 height 属性 | 改用 scaleY + clip-path |
| "缩放没有体积感" | 从 scale(0) 开始 | 改为 scale(0.95) |
| "松手后元素跳变" | 没有速度传递 | 用 spring 继承手势速度 |
| "低端机动画掉帧" | 动画了 box-shadow/filter | 改用 opacity 淡入替代 |
| "transition: all 300ms" | 所有属性都在过渡 | 明确列出 transition-property |
| "键盘操作触发了大动画" | 未检查 reduced-motion | 用媒体查询移除动画 |

---

## 安装方式

### Claude Code

```bash
cp -r animation-craft/ ~/.claude/skills/animation-craft/
```

### 上游安装（获取 Emil 原始三件套）

```bash
npx skills add emilkowalski/skills
```

本 skill 为元技能包装层，整合并增强了上游三个技能的协作流程。

---

## 触发示例

### Phase 1 触发（术语转换）
- "这个弹出效果叫什么术语？"
- "怎么描述'卡片依次滑入'这个动画？"
- "iOS 那种拉到顶弹一下的效果怎么说？"

### Phase 2 触发（设计工程）
- "帮我写一个下拉菜单的展开动画"
- "做一个弹窗的入场动效"
- "给这个按钮加按下反馈"

### Phase 3 触发（质量审查）
- "审查一下这个组件的动画"
- "这个动效怎么感觉怪怪的，帮我看看"
- "review my animations for quality"
- "检查这个页面的动效是否合规"
- "这个动画在低端机上卡，帮我诊断"

### 完整流程触发
- "帮我做一个有质感的弹窗动画"
- "设计一套 Toast 通知的动效系统"
- "优化整个项目的动画体验"

---

## 上游致谢

本 skill 基于 [Emil Kowalski 的 skills 仓库](https://github.com/emilkowalski/skills) (MIT License)，整合了以下三个上游技能：

| 上游技能 | 在本 skill 中的角色 |
|---------|-------------------|
| `animation-vocabulary` | Phase 1: 术语转换 |
| `emil-design-eng` | Phase 2: 设计工程规则 |
| `review-animations` | Phase 3: 10条审查标准 |

Emil Kowalski 是 Sonner (React toast)、Vaul (React drawer) 的作者，前 Vercel 设计工程师，现 Linear Web 团队成员。他的设计工程哲学浓缩在这三个技能中。
