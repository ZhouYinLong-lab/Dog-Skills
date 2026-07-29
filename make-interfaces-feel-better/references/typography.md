# Typography

Typography rendering details that make interfaces feel better.

## Text Wrapping

### text-wrap: balance

Distributes text evenly across lines, preventing orphaned words on headings and short text blocks. **Only works on blocks of 6 lines or fewer** (Chromium) or 10 lines or fewer (Firefox) — the balancing algorithm is computationally expensive, so browsers limit it to short text.

```css
h1, h2, h3 { text-wrap: balance; }
```

**Tailwind:** `text-balance`

### text-wrap: pretty

Prevents orphaned words (a single word dangling on the last line) by adjusting line breaks throughout the paragraph. Unlike `balance`, it doesn't try to equalize line lengths — it just ensures the last line isn't embarrassingly short. Works on text of any length.

This should be your **default for short-to-medium text** — paragraphs, descriptions, captions, list items, card text. For very long text (10+ lines), skip both `pretty` and `balance`.

```css
p, li, figcaption, blockquote { text-wrap: pretty; }
```

**Tailwind:** `text-pretty`

### When to Use Which

| Scenario | Use |
|----------|-----|
| Headings (h1-h3) | `text-wrap: balance` |
| Hero text, taglines | `text-wrap: balance` |
| Body paragraphs, descriptions | `text-wrap: pretty` |
| List items, captions | `text-wrap: pretty` |
| Long articles (10+ lines) | Browser default (skip) |

## Font Smoothing

On macOS, browsers render text with subpixel antialiasing by default, which can make thin weights look heavier.

```css
:root {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

This is particularly important for:
- Light font weights (300, 400) on dark backgrounds
- Design systems where text crispness matters
- Interfaces where text is the primary element

**Tailwind:** `antialiased` class on the root element.

## Tabular Numbers

When numbers update dynamically (counters, timers, prices), proportional-width digits cause layout shift as values change.

```css
.numbers {
  font-variant-numeric: tabular-nums;
}
```

**Tailwind:** `tabular-nums`

Apply to: animated counters, timers/stopwatches, price displays, stat cards, any dynamically updating number.
