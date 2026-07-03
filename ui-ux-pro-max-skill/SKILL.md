---
name: ui-ux-pro-max
description: >
  AI-powered design intelligence toolkit for coding assistants【轻量独立版 · dog-frontier 已包含本技能】。
  Provides 67 UI styles, 161 color palettes, 57 font pairings, 25 chart types, 99 UX guidelines,
  and 161 industry-specific reasoning rules across 16 tech stacks (HTML+Tailwind,
  React, Next.js, shadcn/ui, Vue, Svelte, SwiftUI, Flutter, etc.). The v2.0 Design
  System Generator takes a project description and outputs a complete design system.
  只需设计推荐用本技能，需要全链路前端方案（含组件开发/品牌/动画）用 dog-frontier。
  Trigger keywords: UI design, UX, design system, color palette, font pairing,
  dashboard design, landing page, glassmorphism, minimalism, brutalism, neumorphism,
  Bento grid, shadcn/ui design, Tailwind design, UI风格, 设计系统, 配色, 字体搭配.
metadata:
  category: design
---

# UI UX Pro Max — Design Intelligence for AI Coding Agents

AI-powered design toolkit providing design recommendations and code generation
guidance across multiple platforms. 67 UI styles, 161 color palettes, 57 font
pairings, 25 chart types, 99 UX guidelines, 161 industry-specific rules.

Version 2.5.0. MIT License.

---

## Installation

```bash
npx uipro-cli init --ai <platform>
```

Supported platforms (18): Claude Code, Cursor, Windsurf, GitHub Copilot, Kiro,
Roo Code, KiloCode, Codex CLI, Qoder, Gemini CLI, Trae, OpenCode, Continue,
CodeBuddy, Droid (Factory), Warp, Augment, Antigravity, OpenClaw.

For Claude Code Plugin Marketplace:
```bash
claude plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
```

---

## What it provides

### 67 UI styles
Glassmorphism, Minimalism, Brutalism, Bento Grid, Neumorphism, AI-Native UI,
Spatial UI (VisionOS), and 60+ more, plus 8 landing page patterns and 10
BI/analytics dashboard styles.

### 161 color palettes
Industry-specific palettes aligned 1:1 to product categories (SaaS, healthcare,
e-commerce, fintech, education, entertainment, etc.).

### 57 font pairings
Curated typography combinations with Google Fonts import links.

### 25 chart types
Recommendations for data visualization in dashboards.

### 99 UX guidelines
Best practices, anti-patterns, and accessibility rules.

### 16 tech stacks
Stack-specific design guidelines for: HTML+Tailwind, React, Next.js, shadcn/ui,
Vue, Nuxt.js, Nuxt UI, Svelte, Astro, SwiftUI, React Native, Flutter,
Jetpack Compose, Angular, Laravel (Blade/Livewire/Inertia), JavaFX.

---

## Design System Generator (v2.0)

Take a project description → get a complete design system:

1. **Multi-domain search** across product categories, styles, palettes, patterns, typography
2. **BM25 ranking + anti-pattern filtering**
3. **Output**: pattern, style, colors, typography, effects, anti-patterns to avoid, pre-delivery checklist

Example: "build a landing page for a beauty spa" → warm color palette, elegant typography, soft glassmorphism effects, anti-patterns to avoid.

---

## Architecture

```
src/ui-ux-pro-max/          # Canonical data (CSVs, Python scripts, templates)
cli/                        # CLI installer
.claude/skills/             # Skill symlinks for Claude Code
.claude-plugin/             # Marketplace publishing config
```

---

## License

MIT
