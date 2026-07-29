# Performance

Transition specificity and GPU compositing hints.

## Transition Only What Changes

Never use `transition: all` or Tailwind's `transition` shorthand. Always specify exact properties.

```css
/* Good */
.button {
  transition-property: scale, background-color;
  transition-duration: 150ms;
  transition-timing-function: ease-out;
}

/* Bad */
.button { transition: all 150ms ease-out; }
```

```tsx
// Good — explicit properties
<button className="transition-[scale,background-color] duration-150 ease-out">

// Bad — transition all
<button className="transition duration-150 ease-out">

// Tailwind transition-transform covers: transform, translate, scale, rotate
<button className="transition-transform duration-150 ease-out">
```

## Use `will-change` Sparingly

Hints the browser to pre-promote an element to its own GPU compositing layer.

### Rules

```css
/* Good */
.animated-card { will-change: transform; }
.animated-card { will-change: transform, opacity; }

/* Bad — never use all */
.animated-card { will-change: all; }

/* Bad — properties that can't be GPU-composited */
.animated-card { will-change: background-color, padding; }
```

### Useful Properties

| Property | GPU-compositable | Worth using `will-change` |
|----------|-----------------|---------------------------|
| `transform` | Yes | Yes |
| `opacity` | Yes | Yes |
| `filter` (blur, brightness) | Yes | Yes |
| `clip-path` | Yes | Yes |
| `top`, `left`, `width`, `height` | No | No |
| `background`, `border`, `color` | No | No |

### When to Skip

Modern browsers optimize well on their own. Only add `will-change` when you notice first-frame stutter — Safari particularly benefits. Don't add preemptively to every animated element; each compositing layer costs memory.
