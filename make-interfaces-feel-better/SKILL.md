---
name: make-interfaces-feel-better
description: >
  UI polish skill — 16 design engineering principles for making interfaces feel polished and professional.
  Covers typography, surfaces, animations, and performance. Triggers on UI review, design details,
  "make it feel better", "feels off", 界面打磨, UI细节, border radius, shadows, stagger animations,
  enter/exit transitions, optical alignment, font smoothing, tabular numbers, image outlines.
metadata:
  category: design
---

# Details That Make Interfaces Feel Better

Great interfaces rarely come from a single thing. It's usually a collection of small details that compound into a great experience. Apply these principles when building or reviewing UI code.

## Quick Reference

| Category | Reference | When to Use |
|----------|-----------|-------------|
| Typography | [typography.md](references/typography.md) | Text wrapping, font smoothing, tabular numbers |
| Surfaces | [surfaces.md](references/surfaces.md) | Border radius, optical alignment, shadows, image outlines, hit areas |
| Animations | [animations.md](references/animations.md) | Interruptible animations, enter/exit transitions, icon animations, scale on press |
| Performance | [performance.md](references/performance.md) | Transition specificity, `will-change` usage |

## Core Principles

### 1. Concentric Border Radius
`outerRadius = innerRadius + padding`. Mismatched radii on nested elements is the most common thing that makes interfaces feel off.

### 2. Optical Over Geometric Alignment
When geometric centering looks off, align optically. Buttons with icons need manual adjustment — `icon-side padding = text-side padding - 2px`.

### 3. Shadows Over Borders
Layer multiple transparent `box-shadow` values for natural depth. Shadows adapt to any background; solid borders don't.

### 4. Interruptible Animations
Use CSS transitions for interactive state changes — they can be interrupted mid-animation. Reserve keyframes for staged sequences that run once.

### 5. Split and Stagger Enter Animations
Don't animate a single container. Break content into semantic chunks and stagger each with ~100ms delay.

### 6. Subtle Exit Animations
Use a small fixed `translateY(-12px)` instead of full height. Exits should be softer and shorter than enters.

### 7. Contextual Icon Animations
Animate icons with `opacity`, `scale` (0.25→1), and `blur` (4px→0). Use spring with bounce=0 if Motion available; CSS cross-fade if not.

### 8. Font Smoothing
Apply `-webkit-font-smoothing: antialiased` on macOS for crisper text.

### 9. Tabular Numbers
Use `font-variant-numeric: tabular-nums` for dynamically updating numbers to prevent layout shift.

### 10. Text Wrapping
`text-wrap: balance` on headings (≤6 lines). `text-wrap: pretty` on body text to avoid orphans.

### 11. Image Outlines
Add `1px` outline: pure black `rgba(0,0,0,0.1)` in light mode, pure white `rgba(255,255,255,0.1)` in dark mode. Never use tinted neutrals.

### 12. Scale on Press
`scale(0.96)` on click gives buttons tactile feedback. Never below `0.95`. Add `static` prop to disable when distracting.

### 13. Skip Animation on Page Load
`initial={false}` on `AnimatePresence` for default-state elements. Verify it doesn't break intentional entrance animations.

### 14. Never Use `transition: all`
Always specify exact properties. Tailwind: `transition-transform` or `transition-[scale,opacity]`.

### 15. Use `will-change` Sparingly
Only for `transform`, `opacity`, `filter` — GPU-compositable properties. Never `will-change: all`. Only add when you notice first-frame stutter.

### 16. Minimum Hit Area
44×44px for touch/mobile, ≥40×40px for dense desktop. Extend with pseudo-element. Never let two hit areas overlap.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Same border radius on parent and child | `outerRadius = innerRadius + padding` |
| Icons look off-center | Adjust optically with padding or fix SVG |
| Hard borders between sections | Use layered `box-shadow` with transparency |
| Jarring enter/exit animations | Split, stagger, and keep exits subtle |
| Numbers cause layout shift | Apply `tabular-nums` |
| Heavy text on macOS | Apply `antialiased` to root |
| Animation plays on page load | Add `initial={false}` to `AnimatePresence` |
| `transition: all` | Specify exact properties |
| First-frame animation stutter | Add `will-change: transform` (sparingly) |
| Tiny hit areas | Extend with pseudo-element to 44×44px |

## Review Output Format

Always present changes as a markdown table with **Before** and **After** columns. Group by principle with a heading. Only include principles where changes were made — omit empty tables.

### Example

#### Concentric border radius
| Before | After |
|--------|-------|
| `rounded-xl` on card + `rounded-xl` on inner button (`p-2`) | `rounded-2xl` on card, `rounded-lg` on inner button |

#### Scale on press
| Before | After |
|--------|-------|
| `<button className="...">` | Added `active:scale-[0.96] transition-transform` |

## Review Checklist

- [ ] Nested rounded elements use concentric border radius
- [ ] Icons are optically centered, not just geometrically
- [ ] Shadows used instead of borders where appropriate
- [ ] Enter animations are split and staggered
- [ ] Exit animations are subtle
- [ ] Dynamic numbers use `tabular-nums`
- [ ] Font smoothing is applied
- [ ] Headings use `text-wrap: balance`
- [ ] Images have subtle outlines (pure black/white, not tinted)
- [ ] Buttons use `scale(0.96)` on press where appropriate
- [ ] `AnimatePresence` uses `initial={false}` for default-state elements
- [ ] No `transition: all` — only specific properties
- [ ] `will-change` only on `transform`/`opacity`/`filter`, never `all`
- [ ] Interactive elements have ≥44×44px hit areas (touch) or ≥40×40px (desktop)
