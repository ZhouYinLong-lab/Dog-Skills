# Surfaces

Border radius, optical alignment, shadows, and image outlines.

## Concentric Border Radius

When nesting rounded elements, the outer radius must equal the inner radius plus the padding:

```
outerRadius = innerRadius + padding
```

This rule is most useful when nested surfaces are close together. If padding is larger than `24px`, treat the layers as separate surfaces and choose each radius independently.

```css
/* Good — concentric radii */
.card { border-radius: 20px; padding: 8px; }  /* 12 + 8 */
.card-inner { border-radius: 12px; }

/* Bad — same radius on both */
.card { border-radius: 12px; padding: 8px; }
.card-inner { border-radius: 12px; }
```

### Tailwind Example

```tsx
// Good — outer radius accounts for padding
<div className="rounded-2xl p-2">       {/* 16px radius, 8px padding */}
  <div className="rounded-lg">          {/* 8px radius = 16 - 8 ✓ */}
    ...
  </div>
</div>

// Bad — same radius on both
<div className="rounded-xl p-2">
  <div className="rounded-xl">          {/* same radius, looks off */}
    ...
  </div>
</div>
```

## Optical Alignment

### Buttons with Text + Icon

`icon-side padding = text-side padding - 2px`

```css
.button-with-icon {
  padding-left: 16px;
  padding-right: 14px; /* icon side = text side - 2px */
}
```

```tsx
// Tailwind
<button className="pl-4 pr-3.5 flex items-center gap-2">
  <span>Continue</span>
  <ArrowRightIcon />
</button>
```

### Play Button Triangles

Play icons are triangular — their geometric center is not their visual center. Shift slightly right:

```css
.play-button svg { margin-left: 2px; }
```

### Asymmetric Icons

The best fix is adjusting the SVG directly so no extra margin is needed. Fallback: adjust with margin (`ml-px`).

## Shadows Instead of Borders

For buttons, cards, and containers that use a border for depth, prefer `box-shadow`. Shadows adapt to any background via transparency; solid borders don't. **Do not apply to dividers** — those should stay as borders.

### Shadow as Border (Light Mode)

```css
:root {
  --shadow-border:
    0px 0px 0px 1px rgba(0, 0, 0, 0.06),
    0px 1px 2px -1px rgba(0, 0, 0, 0.06),
    0px 2px 4px 0px rgba(0, 0, 0, 0.04);
  --shadow-border-hover:
    0px 0px 0px 1px rgba(0, 0, 0, 0.08),
    0px 1px 2px -1px rgba(0, 0, 0, 0.08),
    0px 2px 4px 0px rgba(0, 0, 0, 0.06);
}
```

### Shadow as Border (Dark Mode)

```css
--shadow-border: 0 0 0 1px rgba(255, 255, 255, 0.08);
--shadow-border-hover: 0 0 0 1px rgba(255, 255, 255, 0.13);
```

### When to Use Shadows vs. Borders

| Use shadows | Use borders |
|-------------|-------------|
| Cards, containers with depth | Dividers between list items |
| Buttons with bordered styles | Table cell boundaries |
| Elevated elements (dropdowns, modals) | Form input outlines (accessibility) |
| Elements on varied backgrounds | Hairline separators in dense UI |

## Image Outlines

Add a subtle `1px` outline with low opacity for consistent depth.

### Color rules (non-negotiable)

- **Light mode**: pure black — `rgba(0, 0, 0, 0.1)`
- **Dark mode**: pure white — `rgba(255, 255, 255, 0.1)`
- Never use tinted neutrals (slate, zinc, `#0a0a0a`, `#f5f5f7`) — they read as dirt on the image edge.

```css
img {
  outline: 1px solid rgba(0, 0, 0, 0.1);
  outline-offset: -1px;
}
```

```tsx
// Tailwind
<img className="outline outline-1 -outline-offset-1 outline-black/10 dark:outline-white/10" src={src} alt={alt} />
```

**Why outline instead of border?** `outline` doesn't affect layout, and `outline-offset: -1px` keeps it inset.

## Minimum Hit Area

44×44px for touch/mobile, ≥40×40px for dense desktop. Extend with pseudo-element:

```css
.checkbox {
  position: relative;
  width: 20px;
  height: 20px;
}
.checkbox::after {
  content: "";
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 44px; height: 44px;
}
```

```tsx
// Tailwind
<button className="relative size-5 after:absolute after:top-1/2 after:left-1/2 after:size-11 after:-translate-1/2">
  <CheckIcon />
</button>
```

**Never let two hit areas overlap.** If the extended area collides with another element, shrink it — but keep it as large as possible without collision.
