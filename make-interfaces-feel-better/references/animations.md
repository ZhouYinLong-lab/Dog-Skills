# Animations

Interruptible animations, enter/exit transitions, and contextual icon animations.

## Interruptible Animations

| | CSS Transitions | CSS Keyframe Animations |
|---|---|---|
| **Behavior** | Interpolate toward latest state | Run on a fixed timeline |
| **Interruptible** | Yes — retargets mid-animation | No — restarts from beginning |
| **Use for** | Interactive state changes (hover, toggle, open/close) | Staged sequences that run once (enter, loading) |
| **Duration** | Adapts to remaining distance | Fixed regardless of state |

**Rule:** Always prefer CSS transitions for interactive elements. Reserve keyframes for one-shot sequences.

```css
/* Good — interruptible transition */
.drawer { transform: translateX(-100%); transition: transform 200ms ease-out; }
.drawer.open { transform: translateX(0); }
/* Clicking mid-animation smoothly reverses */

/* Bad — keyframe for interactive element */
.drawer.open { animation: slideIn 200ms ease-out forwards; }
/* Closing mid-animation snaps or restarts */
```

## Enter Animations: Split and Stagger

1. **Split** into logical groups (title, description, buttons)
2. **Stagger** with ~100ms delay between groups
3. **For titles**, consider splitting into words with ~80ms stagger
4. **Combine** `opacity`, `blur`, and `translateY` for the enter effect

```tsx
// Motion (Framer Motion) — staggered enter
<motion.div
  initial="hidden" animate="visible"
  variants={{ visible: { transition: { staggerChildren: 0.1 } } }}
>
  <motion.h1 variants={{
    hidden: { opacity: 0, y: 12, filter: "blur(4px)" },
    visible: { opacity: 1, y: 0, filter: "blur(0px)" },
  }}>Welcome</motion.h1>
  <motion.p variants={{
    hidden: { opacity: 0, y: 12, filter: "blur(4px)" },
    visible: { opacity: 1, y: 0, filter: "blur(0px)" },
  }}>Description</motion.p>
</motion.div>
```

### CSS-Only Stagger

```css
.stagger-item { opacity: 0; transform: translateY(12px); filter: blur(4px); animation: fadeInUp 400ms ease-out forwards; }
.stagger-item:nth-child(1) { animation-delay: 0ms; }
.stagger-item:nth-child(2) { animation-delay: 100ms; }
.stagger-item:nth-child(3) { animation-delay: 200ms; }

@keyframes fadeInUp {
  to { opacity: 1; transform: translateY(0); filter: blur(0); }
}
```

## Exit Animations

Exits should be softer and shorter than enters. Use small fixed `translateY(-12px)` instead of full height.

```tsx
<motion.div exit={{
  opacity: 0, y: -12, filter: "blur(4px)",
  transition: { duration: 0.15, ease: "easeIn" },
}}>
  {content}
</motion.div>
```

- Exit duration: ~150ms (shorter than enter's ~300ms)
- Keep directional movement to indicate where element went
- Don't remove exit animations entirely — subtle motion preserves context

## Contextual Icon Animations

Animate icons with `opacity`, `scale`, and `blur` instead of toggling visibility.

**Fixed values (do not deviate):**
- `scale`: `0.25` → `1` (never `0.5` or `0.6`)
- `opacity`: `0` → `1`
- `filter`: `"blur(4px)"` → `"blur(0px)"`
- `transition`: `{ type: "spring", duration: 0.3, bounce: 0 }` — **bounce must always be `0`**

### Motion Example

```tsx
<AnimatePresence mode="popLayout">
  <motion.span
    key={isActive ? "active" : "inactive"}
    initial={{ opacity: 0, scale: 0.25, filter: "blur(4px)" }}
    animate={{ opacity: 1, scale: 1, filter: "blur(0px)" }}
    exit={{ opacity: 0, scale: 0.25, filter: "blur(4px)" }}
    transition={{ type: "spring", duration: 0.3, bounce: 0 }}
  >
    <Icon />
  </motion.span>
</AnimatePresence>
```

### CSS Cross-Fade (No Motion Library)

Keep both icons in DOM, one absolute-positioned. Toggling state cross-fades them with `cubic-bezier(0.2, 0, 0, 1)`.

**Rule:** Check `package.json` for `motion` or `framer-motion`. If present, use Motion approach. If not, use CSS cross-fade — don't add a dependency just for icon transitions.

### When to Animate Icons

| Animate | Don't animate |
|---------|---------------|
| Icons on hover (action buttons) | Static navigation icons |
| State change icons (play→pause, like→liked) | Decorative icons |
| Icons in contextual toolbars | Icons always visible |
| Loading/success indicators | Icon labels (text next to icon) |

## Scale on Press

`scale(0.96)` on click. Never below `0.95`. Add `static` prop to disable when distracting.

```css
.button { transition-property: scale; transition-duration: 150ms; transition-timing-function: ease-out; }
.button:active { scale: 0.96; }
```

```tsx
// Tailwind
<button className="transition-transform duration-150 ease-out active:scale-[0.96]">

// Static prop pattern
const tapScale = "active:not-disabled:scale-[0.96]";
function Button({ static: isStatic, className, children, ...props }) {
  return <button className={cn("transition-transform duration-150 ease-out", !isStatic && tapScale, className)} {...props}>{children}</button>;
}
```

## Skip Animation on Page Load

`initial={false}` on `AnimatePresence` prevents enter animations on first render.

```tsx
// Good — no animation on mount, only on state change
<AnimatePresence initial={false} mode="popLayout">
  <motion.span key={state} initial={...} animate={...} exit={...}>
    <Icon />
  </motion.span>
</AnimatePresence>
```

Works for: icon swaps, toggles, tabs, segmented controls. Don't use when component relies on `initial` for a first-time enter animation (staggered hero, loading state).
