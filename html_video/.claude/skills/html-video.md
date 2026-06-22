---
name: html-video
description: HTML→Video meta-layer — turn HTML into MP4 video via coding agents. Studio at :3071, CLI tools for templates/doctor, 23 templates across hyperframes & remotion engines.
---

# html-video Skill

HTML→Video meta-layer for coding agents. Turn HTML templates, articles, or prompts into real MP4 videos using Hyperframes (headless Chromium + ffmpeg) or Remotion (React) rendering engines.

## Quick Reference

| Command | Description |
|---|---|
| `pnpm -r build` | Build all workspace packages |
| `node packages/cli/dist/bin.js studio` | Start the browser studio at http://127.0.0.1:3071 |
| `node packages/cli/dist/bin.js doctor` | Check installed agents, engines, templates |
| `node packages/cli/dist/bin.js search-templates --intent "<query>" --top N` | Search templates by intent |
| `pnpm typecheck` | TypeScript across all packages |
| `pnpm lint` | Biome linter |
| `pnpm format` | Auto-format all files |
| `pnpm test` | Run all tests |
| `pnpm --filter @html-video/cli smoke` | Run smoke test |

## Project Structure

```
packages/
├── core/                  Types, registries, orchestrator, MiniMax + ffmpeg audio
├── content-graph/         Multi-frame storyboard IR (nodes + edges, topo-sort)
├── runtime/               Agent runtime — detect / spawn / stream (14 agents)
├── adapter-hyperframes/   Hyperframes engine — Chromium + ffmpeg render
├── adapter-remotion/      Remotion engine — React-based render
├── cli/                   CLI + studio HTTP server + source fetching
├── project-studio/        Static studio assets
└── studio-next/           Browser studio UI (Vite-built)
templates/                 23 curated, license-clean video templates
research/                  RFCs and design specs
```

## Engines

- **Hyperframes** (default): HTML + CSS + GSAP, rendered via headless Chromium + ffmpeg
- **Remotion**: React components, rendered via `@remotion/renderer`

## Templates (23)

Categories: data-viz, title-card, hero, cinematic, VFX, outro, product-promo, explainer, editorial, kinetic-type

Key templates: `frame-data-chart-nyt`, `frame-glitch-title`, `frame-liquid-bg-hero`, `frame-product-promo`, `frame-decision-tree`, `frame-bold-poster`, `vfx-text-cursor`, `frame-data-rollup` (native Remotion)

## Development Workflow

1. **Build**: `pnpm -r build` — builds all packages in dependency order
2. **Type check**: `pnpm typecheck` — before committing
3. **Format**: `pnpm format` — auto-format with Biome
4. **Start studio**: `node packages/cli/dist/bin.js studio` — opens at :3071

## Port Allocation

Ports 3071–3079 reserved for html-video (T9 in nexu-io project space).

## Adding a Template

1. Create `templates/<id>/` with `template.html-video.yaml`, `source/index.html`, `SKILL.md`, `poster.svg`/`preview.png`
2. Follow RFC-07 provenance rules (three-layer attribution: origin → via_skill → transformation)
3. Build + verify: `pnpm -r build && node packages/cli/dist/bin.js search-templates --intent "your topic"`

## Key Files

- `CLAUDE.md` — internal working notes, session progress, design decisions
- `CONTRIBUTING.md` — contribution guide
- `ATTRIBUTIONS.md` — template attributions
- `research/` — RFCs for engine adapter spec, template metadata, content-graph, provenance
