# CSS 高级技巧手册

> 来源: css-styling-expert (cin12211, MIT) + MDN + CSS-Tricks
> 整合现代 CSS 中最实用的高级技巧,供 Phase 3 代码生成时参考。

---

## 1. 布局技巧

### 容器查询 (Container Queries)

```css
/* 组件级响应式,不依赖视口 */
.card-container {
  container-type: inline-size;
  container-name: card;
}

@container card (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
  }
}
```

### 自适应网格 (无需媒体查询)

```css
/* 自动填充,最小250px */
.grid-auto {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}

/* Bento Grid — 不同大小 */
.bento {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 200px;
  gap: 1rem;
}
.bento > :nth-child(1) { grid-column: span 2; grid-row: span 2; }
.bento > :nth-child(2) { grid-column: span 1; grid-row: span 1; }
.bento > :nth-child(3) { grid-column: span 1; grid-row: span 2; }
```

### Subgrid (继承父网格)

```css
.parent {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
.child {
  display: grid;
  grid-column: span 3;
  grid-template-columns: subgrid; /* 对齐父级列 */
}
```

---

## 2. 排版技巧

### 文本平衡

```css
h1, h2, h3 {
  text-wrap: balance; /* 每行字数均匀 */
}

p {
  text-wrap: pretty; /* 防止孤行 */
}
```

### 流体排版 (clamp)

```css
/* 无需媒体查询的响应式字号 */
h1 {
  font-size: clamp(2rem, 5vw + 1rem, 4rem);
}

body {
  font-size: clamp(1rem, 0.5vw + 0.875rem, 1.125rem);
}
```

### 首字下沉

```css
.article p:first-of-type::first-letter {
  initial-letter: 3;
  font-weight: bold;
  margin-right: 0.5em;
}
```

---

## 3. 动画与交互

### 滚动驱动动画

```css
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.reveal {
  animation: fadeIn linear;
  animation-timeline: view();
  animation-range: entry 0% entry 80%;
}
```

### 视差滚动

```css
.parallax {
  transform: translateY(var(--scroll, 0));
  will-change: transform;
}
```

```js
// JS 配合
window.addEventListener('scroll', () => {
  document.documentElement.style.setProperty(
    '--scroll', `${window.scrollY * 0.5}px`
  );
});
```

### GPU 加速

```css
.smooth {
  will-change: transform;
  transform: translateZ(0);
  backface-visibility: hidden;
}
```

### Steps() 精灵动画 (来源: sprite-animation)

```css
.sprite {
  width: 100px;
  height: 100px;
  background: url(sprite-sheet.png);
  animation: play 1s steps(10) infinite;
}

@keyframes play {
  from { background-position: 0 0; }
  to { background-position: -1000px 0; }
}
```

---

## 4. 视觉效果

### 玻璃态 (Glassmorphism)

```css
.glass {
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
}
```

### 新粗野主义 (Neubrutalism)

```css
.brutal {
  border: 3px solid #000;
  box-shadow: 6px 6px 0 #000;
  border-radius: 0;
  transition: box-shadow 100ms, transform 100ms;
}
.brutal:hover {
  box-shadow: 3px 3px 0 #000;
  transform: translate(3px, 3px);
}
```

### 粘土态 (Claymorphism)

```css
.clay {
  background: #f0f0f0;
  border-radius: 24px;
  box-shadow:
    8px 8px 16px #d9d9d9,
    -8px -8px 16px #ffffff,
    inset 2px 2px 4px rgba(255,255,255,0.8),
    inset -2px -2px 4px rgba(0,0,0,0.05);
}
```

### 渐变文字

```css
.gradient-text {
  background: linear-gradient(135deg, #6366F1, #22D3EE);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
```

---

## 5. 交互反馈

### 悬浮卡片

```css
.card-hover {
  transition: transform 200ms ease, box-shadow 200ms ease;
}
.card-hover:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
}
```

### 按钮波纹

```css
.btn-ripple {
  position: relative;
  overflow: hidden;
}
.btn-ripple::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle, rgba(255,255,255,0.3) 10%, transparent 10%);
  transform: scale(10);
  opacity: 0;
  transition: transform 0.5s, opacity 0.5s;
}
.btn-ripple:active::after {
  transform: scale(0);
  opacity: 1;
  transition: 0s;
}
```

---

## 6. 可访问性与用户体验

### Focus visible (仅键盘用户)

```css
:focus:not(:focus-visible) {
  outline: none;
}
:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

### Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### prefers-color-scheme

```css
:root {
  color-scheme: light dark;
}
@media (prefers-color-scheme: dark) {
  /* 自动暗色模式 */
}
```

---

## 7. 现代选择器

```css
/* :has() — 父选择器 */
.card:has(img) { /* 有图片的卡片 */ }
.card:has(.sold-out) { opacity: 0.6; }

/* :is() — 减少重复 */
:is(h1, h2, h3) + p { margin-top: 0.5em; }

/* :where() — 零特异性 */
:where(.sidebar) a { color: blue; } /* 特异性=0,0,1 */

/* :nth-child() of — 条件筛选 */
:nth-child(2 of .highlighted) { background: yellow; }
```

---

## 8. 性能清单

- [ ] 使用 `content-visibility: auto` 延迟渲染屏外内容
- [ ] 图片使用 `loading="lazy"` + `decoding="async"`
- [ ] 动画使用 `transform` + `opacity` 组合
- [ ] 使用 `will-change` 但用完即删(不给浏览器留负担)
- [ ] CSS `@import` 避免使用(串行加载)
- [ ] 关键 CSS 内联在 `<head>` 中

---

*来源: css-styling-expert (cin12211/orca-q, MIT) + sprite-animation (nexu-io/open-design, MIT)*
