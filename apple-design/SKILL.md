---
name: apple-design
description: >
  Apple 设计哲学蒸馏——将 WWDC 流体界面设计原则翻译为 Web 端的 CSS/JS 实现。
  16 条原则覆盖：直接操作·弹簧物理·中断性·速度传递·动量投影·橡皮筋边界·
  材质与景深·排版·无障碍。适用于构建"像原生一样流畅"的 Web 交互体验。
  Trigger keywords: Apple风格, 苹果设计, iOS动效, 流体界面,
  fluid interface, Apple design, spring animation, 像iOS一样丝滑,
  rubber-banding, 橡皮筋效果, 原生感, native-like,
  Apple质感, 毛玻璃效果, backdrop-filter, 苹果排版,
  San Francisco字体, 中断式动画, 手势动画, momentum scroll,
  fluid gesture, 苹果风格抽屉, 苹果风格弹窗, apple design system.
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
  upstream-author: Emil Kowalski (Vercel → Linear)
  inspiration: WWDC 2018 "Designing Fluid Interfaces" by Apple
  version: "1.0.0"
  license: MIT
---

# Apple Design — 苹果设计哲学（Web 实现版）

> 把 Apple 的流体界面哲学翻译成 Web 开发者能直接用的 CSS 和 JavaScript。
> 核心信条：**"界面之所以感觉'活着'，是因为运动始终从当前值开始，继承用户的速度，投射动量向前，并在任何瞬间都能被抓住和逆转。"**
> 上游来源：[emilkowalski/skills](https://github.com/emilkowalski/skills) (MIT, 4500+ ⭐)

---

## 设计哲学总览

```
Apple 流体界面的 16 条原则:

  感知层 (用户感觉到什么)
  ├─ 1. 即时响应 — 消灭延迟
  ├─ 2. 直接操作 — 1:1 跟随
  ├─ 3. 中断性   — 任何瞬间可逆转
  └─ 4. 行为而非动画 — 用弹簧不用关键帧

  物理层 (如何做到)
  ├─ 5. 速度传递   — 手势结束→动画开始，无缝衔接
  ├─ 6. 动量投影   — 预测自然停止位置
  ├─ 7. 橡皮筋边界 — 渐进阻力，非硬停
  ├─ 8. 空间一致性 — 进场退场沿同一路径
  └─ 9. 帧级流畅   — 只用 transform+opacity

  视觉层 (看起来怎样)
  ├─ 10. 材质与景深 — backdrop-filter + 动态模糊
  ├─ 11. 排版      — 光学字号 + 动态字重
  ├─ 12. 色彩      — 语义色彩 + 深色模式
  └─ 13. 触觉反馈 — 按下→缩放→释放

  包容层 (对所有人)
  ├─ 14. 减少动效   — prefers-reduced-motion
  ├─ 15. 减少透明度 — prefers-reduced-transparency
  └─ 16. 增强对比度 — prefers-contrast
```

---

## 原则 1：即时响应 — 消灭延迟

> "在 `pointerdown` 时响应，不是在 `click` 时。"

```css
/* ✅ 100ms 内的即时反馈 */
.button:active {
  transform: scale(0.97);
  transition: transform 100ms ease-out;
}

/* ❌ 等到 click 事件才反应 = 有可感知的延迟 */
```

### 交互事件优先级

| 事件 | 响应时间目标 | 用途 |
|------|------------|------|
| `pointerdown` | 即时（0-50ms） | 按钮按下、卡片选中 |
| `pointermove` | 每帧（~16ms） | 拖拽、滑动 |
| `click` | 不用于视觉反馈 | 仅用于逻辑提交 |
| 300ms tap delay | **必须消除** | 用 `touch-action: manipulation` |

```css
/* 消除移动端 300ms 点击延迟 */
button, a, [role="button"] {
  touch-action: manipulation;
}
```

---

## 原则 2：直接操作 — 1:1 跟随

> "界面必须像真实物体一样'粘'在手指上。"

```js
// ✅ 使用 setPointerCapture，手指移出元素边界后仍能跟踪
element.addEventListener('pointerdown', (e) => {
  element.setPointerCapture(e.pointerId);
  // 记录起始位置和速度历史
});

// 跟踪最近 5 帧的速度（非仅当前位置）
const velocityHistory = [];
element.addEventListener('pointermove', (e) => {
  velocityHistory.push({
    x: e.movementX,
    y: e.movementY,
    time: performance.now()
  });
  if (velocityHistory.length > 5) velocityHistory.shift();
  
  // 立即更新元素位置（1:1 跟随，无延迟）
  element.style.transform = `translate(${currentX}px, ${currentY}px)`;
});
```

**铁律**：拖拽过程中不使用任何动画/过渡——元素必须 1:1 跟随手指。

---

## 原则 3：中断性 — 最重要的原则

> "每一个动画都必须在飞行途中被重定向。"

```
❌ CSS @keyframes — 无法中断
   一旦开始，必须播放完毕。用户新输入被忽略。

⚠️ CSS transitions — 部分可中断
   改变目标值时从中断点平滑过渡，但缺乏物理感。

✅ Springs — 天生可中断
   弹簧始终从"当前值"开始，天然支持任意时刻重定向。
```

### 什么该用什么

| 场景 | 推荐方案 | 原因 |
|------|---------|------|
| 手势驱动 UI（Drawer/Sheet/卡片滑动） | **Spring** | 需要继承速度、可中断、物理真实 |
| 弹出层（Popover/Dropdown/Tooltip） | **CSS transition** | 简单够用，可中断 |
| 纯装饰动画（背景渐变/呼吸灯） | **@keyframes** | 不需要交互，无所谓 |
| 页面切换 | **Spring 或 transition** | 取决于是否需要手势驱动 |

### Spring 动画配置

```js
import { animate } from 'motion'; // 或 framer-motion

// 默认阻尼弹簧（无弹性，最常用）
animate(el, { y: 0 }, {
  type: 'spring',
  bounce: 0,      // 阻尼比 = 1.0，临界的
  duration: 0.4   // 响应时间（非固定时长）
});

// 仅拖拽松手时有轻微弹性
animate(el, { y: target }, {
  type: 'spring',
  bounce: 0.2,
  duration: 0.4
});
```

### Apple 的两参数弹簧模型

| 参数 | 含义 | 推荐范围 |
|------|------|---------|
| **Damping Ratio** （阻尼比） | 控制过冲：1.0=无弹性, <1.0=有弹性 | 0.8-1.0 |
| **Response** （响应时间，秒） | 到达目标的速度（非固定duration） | 0.3-0.6s |

| 交互 | Damping | Response |
|------|---------|----------|
| 移动/重定位 | 1.0 | 0.4 |
| 旋转 | 0.8 | 0.4 |
| Drawer/Sheet | 0.8 | 0.3 |
| 滚动回弹 | 1.0 | 0.5 |

---

## 原则 4：行为而非动画 — 用弹簧

> "如果一个动效看起来像动画但表现得像物理，它就是弹簧。"

区分"动画思维"和"物理思维"：

| 动画思维 ❌ | 物理思维 ✅ |
|-----------|-----------|
| "这个元素在 300ms 内从 A 移动到 B" | "这个元素受到一个力，推向目标位置" |
| 固定时长，不可中断 | 基于物理，天生可中断 |
| `transition: transform 300ms` | `spring({ bounce: 0, duration: 0.4 })` |
| 松手后突然跳变 | 松手后继承速度平滑过渡 |

---

## 原则 5：速度传递

> "手势结束 → 弹簧开始，必须无缝继承手指的速度。"

```js
// 在 pointerup 时计算手指速度
element.addEventListener('pointerup', (e) => {
  const lastEvent = velocityHistory[velocityHistory.length - 1];
  const firstEvent = velocityHistory[0];
  const dt = lastEvent.time - firstEvent.time;
  
  const velocityX = (lastEvent.x - firstEvent.x) / dt * 1000; // px/s
  const velocityY = (lastEvent.y - firstEvent.y) / dt * 1000;
  
  // 将速度传递给弹簧
  animate(el, {
    x: targetX,
    y: targetY
  }, {
    type: 'spring',
    bounce: 0.2,
    duration: 0.4,
    velocity: velocityX  // Motion 库直接接收 px/s
  });
});
```

**铁律**：松手位置 + 松手速度 → 弹簧目标 → 无缝。任何可见的"跳变"都是 bug。

---

## 原则 6：动量投影

> "不要从松手位置吸附到最近边界。用速度预测元素会自然停在哪里，再吸附到最近的 snap point。"

```js
// Apple 的指数衰减动量投影公式
function project(initialVelocity, decelerationRate = 0.998) {
  return (initialVelocity / 1000) * decelerationRate / (1 - decelerationRate);
}

// 使用
const projectedStop = currentPosition + project(releaseVelocity);
const target = nearestSnapPoint(projectedStop, snapPoints);
```

| 场景 | Deceleration Rate |
|------|-------------------|
| 快速轻扫（flick） | 0.998（Apple 默认） |
| 慢速拖动 | 0.995 |
| 分页滑动 | 0.999（几乎无摩擦） |

---

## 原则 7：橡皮筋边界（Soft Boundaries）

> "边界不是硬墙，是越来越强的橡皮筋。"

```js
// Apple 的橡皮筋阻力函数
function rubberband(overshoot, dimension, constant = 0.55) {
  return (overshoot * dimension * constant) / (dimension + constant * Math.abs(overshoot));
}

// 应用示例
const maxScroll = contentHeight - containerHeight;
if (scrollY > maxScroll) {
  const overshoot = scrollY - maxScroll;
  visualOffset = maxScroll + rubberband(overshoot, containerHeight);
}
```

视觉表现：
```
正常滚动: ████████████░░  范围内线性
过冲区域: ██████████████▓  阻力越来越大的橡皮筋
松手回弹: ██████████████░░ ← spring 弹回边界内
```

---

## 原则 8：空间一致性

> "元素从哪来，就回哪去。"

```css
/* ✅ 下拉菜单从触发它的按钮展开，也收回那个位置 */
.dropdown {
  transform-origin: var(--trigger-x) var(--trigger-y);
  /* 不是 transform-origin: center; ← 错误！ */
}

/* ✅ 进场和退场沿同一路径 */
.sheet-enter  { transform: translateY(100%); }
.sheet-exit   { transform: translateY(100%); }
/* 出场是进场的继续，而非镜像反转 */
```

---

## 原则 9：帧级流畅

> "让每一帧都在 16ms 内完成。"

```css
/* ✅ 可动的属性 */
.animated {
  will-change: transform, opacity;
  /* 提前告知浏览器，让它在合成器线程上准备 */
}

/* ✅ 动画结束后清理 */
.animated.animation-done {
  will-change: auto;
}
```

每帧位置变化控制在感知阈值以下：
- 平移: < 1px/frame（60fps 下 < 60px/s）
- 缩放: < 0.5%/frame
- 旋转: < 0.5°/frame
- 透明度: < 5%/frame

---

## 原则 10：材质与景深

> "浮起来的元素要有空间感——模糊 + 半透明 + 阴影。"

```css
/* iOS 风格的工具栏 */
.toolbar {
  background: rgba(255, 255, 255, 0.72);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-top: 0.5px solid rgba(255, 255, 255, 0.4);
}

/* 深色模式 */
@media (prefers-color-scheme: dark) {
  .toolbar {
    background: rgba(30, 30, 30, 0.72);
    backdrop-filter: blur(20px) saturate(180%);
    border-top: 0.5px solid rgba(255, 255, 255, 0.1);
  }
}
```

### 材质层级系统

| 层级 | 背景透明度 | backdrop-filter blur | 阴影 | 场景 |
|------|-----------|---------------------|------|------|
| L0 背景 | 不透明 | 无 | 无 | 主内容区 |
| L1 浮层 | 0.72 | 20px | 0 2px 8px rgba(0,0,0,0.08) | 卡片 |
| L2 弹出 | 0.85 | 30px | 0 4px 16px rgba(0,0,0,0.12) | 弹窗/Sheet |
| L3 模态 | 0.92 | 40px | 0 8px 32px rgba(0,0,0,0.16) | Modal |
| L4 系统 | 0.95 | 50px | 0 16px 48px rgba(0,0,0,0.20) | 系统级覆盖 |

```css
/* 动态材质：弹出时 blur 和 scale 同步动画 */
.modal {
  backdrop-filter: blur(0px);
  transform: scale(0.95);
  transition: backdrop-filter 400ms ease-out,
              transform 400ms ease-out;
}
.modal.open {
  backdrop-filter: blur(40px);
  transform: scale(1);
}
```

### 滚动边缘渐变

```css
/* 用渐变遮罩替代硬分界线 */
.scroll-container {
  --fade-size: 20px;
  mask-image: linear-gradient(
    to bottom,
    transparent 0%,
    black var(--fade-size),
    black calc(100% - var(--fade-size)),
    transparent 100%
  );
  -webkit-mask-image: linear-gradient(
    to bottom,
    transparent 0%,
    black var(--fade-size),
    black calc(100% - var(--fade-size)),
    transparent 100%
  );
}
```

---

## 原则 11：排版

> "字号越大，字间距越紧；字号越小，字间距越松。"

```css
:root {
  /* Apple 的设计标记 */
  --font-ui: 'system-ui', -apple-system, BlinkMacSystemFont, 'SF Pro Text',
             'Segoe UI', Roboto, sans-serif;
  --font-display: 'SF Pro Display', 'system-ui', -apple-system, sans-serif;
  --font-mono: 'SF Mono', 'SFMono-Regular', 'Consolas', 'Liberation Mono',
              'Menlo', monospace;
}

/* 基础排版规则 */
body {
  font-family: var(--font-ui);
  font-optical-sizing: auto;        /* 让浏览器根据字号自动微调字形 */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-rendering: optimizeLegibility;
}

/* 字间距：大字紧、小字松 */
.large-title  { letter-spacing: -0.02em; }  /* 34pt → -2% */
.title-1      { letter-spacing: -0.01em; }  /* 28pt → -1% */
.title-2      { letter-spacing: -0.005em; } /* 22pt → -0.5% */
.headline     { letter-spacing: 0; }        /* 17pt → 0 */
.body         { letter-spacing: 0.005em; }  /* 15pt → +0.5% */
.caption      { letter-spacing: 0.01em; }   /* 12pt → +1% */

/* 行高：大字紧、小字松 */
.large-title  { line-height: 1.1; }
.title-1      { line-height: 1.15; }
.headline     { line-height: 1.3; }
.body         { line-height: 1.5; }
.caption      { line-height: 1.6; }

/* 动态字重 */
@supports (font-variation-settings: 'wght' 400) {
  .sf-pro {
    font-family: 'SF Pro Display', 'system-ui', sans-serif;
    font-variation-settings: 'wght' 400;
  }
}
```

### 布局单位

```
❌ 不要用 px 固定布局
✅ 用 rem / em / vw / vh / % 构建可伸缩的排版系统

html { font-size: 62.5%; }  /* 1rem = 10px，便于计算 */
/* Apple 实际用 17pt = 17px 作为根字号基准 */
```

---

## 原则 12：色彩 — 语义与动态

```css
:root {
  /* Apple 的语义色彩系统 */
  --color-label: rgba(0, 0, 0, 0.85);
  --color-secondary-label: rgba(0, 0, 0, 0.55);
  --color-tertiary-label: rgba(0, 0, 0, 0.25);
  --color-placeholder-text: rgba(0, 0, 0, 0.25);

  --color-system-fill: rgba(120, 120, 128, 0.2);
  --color-secondary-system-fill: rgba(120, 120, 128, 0.16);

  --color-separator: rgba(60, 60, 67, 0.12);
  --color-opaque-separator: rgba(60, 60, 67, 0.36);

  /* 强调色 */
  --color-tint: #007AFF;       /* iOS Blue */
  --color-tint-hover: #0056CC;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-label: rgba(255, 255, 255, 0.85);
    --color-secondary-label: rgba(255, 255, 255, 0.55);
    --color-tertiary-label: rgba(255, 255, 255, 0.25);
    --color-separator: rgba(84, 84, 88, 0.6);
    --color-tint: #0A84FF;
  }
}
```

**关键**：不要用 `#000` 或 `#FFF` 纯色。Apple 的全系统颜色都带透明度，让底层内容透出。

---

## 原则 13：触觉反馈 — 按下→缩放→释放

```css
/* Apple 风格的三段式按钮反馈 */
.btn {
  transform: scale(1);
  transition: transform 100ms ease-out;
}

/* 按下：缩小 */
.btn:active {
  transform: scale(0.97);
  transition: transform 50ms ease-out;
}

/* 释放：弹回（如果使用 spring） */
/* CSS transition 会在 pointerup 时自动回弹 */
```

```js
// 释放时的弹簧回弹（更有质感）
btn.addEventListener('pointerup', () => {
  animate(btn, { scale: 1 }, {
    type: 'spring',
    bounce: 0.5,      // 给释放加一点弹性
    duration: 0.3
  });
});
```

---

## 原则 14-16：无障碍 — 三种动效偏好

```css
/* 14. 减少动效 */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
  
  .sheet, .modal, .drawer {
    transition: opacity 200ms ease;
    transform: none !important;
  }
}

/* 15. 减少透明度（对有视觉障碍的用户） */
@media (prefers-reduced-transparency: reduce) {
  .toolbar {
    background: var(--color-background-solid, white);
    backdrop-filter: none;
  }
  .modal {
    background: var(--color-background-solid, white);
    backdrop-filter: none;
  }
}

/* 16. 增强对比度 */
@media (prefers-contrast: more) {
  .card {
    border: 2px solid var(--color-label);
  }
  .separator {
    background: var(--color-label);
  }
}
```

**铁律**：响应这三个媒体查询不是"加分项"，是基础要求。

---

## CSS 技艺速查

### 现代 CSS 入场动画

```css
/* 使用 @starting-style（Chrome 117+）做声明式入场 */
.popover {
  transform: scale(1);
  opacity: 1;
  transition: transform 200ms ease-out,
              opacity 200ms ease-out;

  @starting-style {
    transform: scale(0.95);
    opacity: 0;
  }
}
/* 无需 JS，元素插入 DOM 时自动播放入场动画 */
```

### Clip-path 揭示动画

```css
/* 替代 height 动画的展开效果 */
.collapsible {
  clip-path: inset(0 0 0 0);
  transition: clip-path 300ms ease-out;
}
.collapsible.collapsed {
  clip-path: inset(0 0 100% 0);
}

/* Tab 内容切换 */
.tab-panel {
  clip-path: inset(0 0 0 0);
  transition: clip-path 250ms ease-in-out;
}
.tab-panel.exit-left {
  clip-path: inset(0 100% 0 0);
}
```

### 模糊桥接（Blur Bridge）

```js
// 当两个状态差异太大无法自然过渡时，
// 在过渡中段加一层 blur 来掩盖视觉跳跃
const el = document.querySelector('.transitioning');
el.style.filter = 'blur(4px)';
el.style.opacity = '0.5';

await animate(el, { /* 状态切换 */ }, { duration: 0.2 });

el.style.filter = 'blur(0px)';
el.style.opacity = '1';
```

---

## 安装方式

### Claude Code

```bash
cp -r apple-design/ ~/.claude/skills/apple-design/
```

### 上游安装（获取 Emil 完整设计工程技能集）

```bash
npx skills add emilkowalski/skills
```

本 skill 专注于 Apple 设计哲学的 Web 实现，与 `animation-craft`（动画工艺元技能）互补使用。

---

## 与 Dog-Skills 生态的协作

```
apple-design          →  设计哲学层（"Apple 怎么做？"）
animation-craft       →  工艺执行层（"怎么写才对？"）
dog-frontier          →  全链路工程（"怎么把一切串起来？"）
ui-ux-pro-max         →  风格数据库（"还有什么风格可选？"）
```

**典型协作流程**：
1. 用户："帮我做一个 iOS 风格的底部抽屉"
2. `apple-design` → 提供原则：弹簧物理、速度传递、材质层级
3. `animation-craft` Phase 2 → 生成具体代码（参数：damping 0.8, response 0.3）
4. `animation-craft` Phase 3 → 审查代码是否通过 10 条标准

---

## 触发示例

- "帮我做一个像 iOS 那样的底部弹出抽屉"
- "这个弹窗动画不够 Apple，帮我优化"
- "给这个列表加上 iOS 风格的橡皮筋回弹"
- "做一个 Apple 风格的毛玻璃导航栏"
- "按 Apple 设计规范审查一下这个页面的动效"
- "create an iOS-style fluid gesture for this card"
- "把这段拖拽代码改成 Apple 的流体交互风格"
- "这个 Modal 的进出动画太生硬了，按 Apple 标准重写"
- "帮我用 SF Pro 的排版规范重新设置这个页面的字体"

---

## 上游致谢

本 skill 基于 [Emil Kowalski 的 apple-design skill](https://github.com/emilkowalski/skills) (MIT License)，核心灵感来自：
- WWDC 2018: [Designing Fluid Interfaces](https://developer.apple.com/videos/play/wwdc2018/803/) — Apple 官方流体界面设计原则
- WWDC 2023: [Design dynamic Live Activities](https://developer.apple.com/videos/play/wwdc2023/) — 材质与动画更新
- Emil Kowalski 的 Web 端翻译和工程实践（Sonner, Vaul, animations.dev）
