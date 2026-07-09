---
name: html-video
description: >
  HTML→Video meta-layer for coding agents. Turn prompts, article links, or GitHub repos
  into multi-frame animated MP4 videos by letting agents pick rendering engines (Hyperframes,
  Remotion, Motion Canvas), fill curated templates, and render locally via headless Chromium
  + ffmpeg. Use whenever the user wants to create a video, animate HTML content, turn an
  article into a video explainer, generate a product promo, make data-visualization videos,
  or produce any motion content from HTML. Triggers when the task involves video generation,
  MP4 export, animated HTML, template-based video creation, or the user mentions making
  videos from links or prompts.

  **Trigger keywords**: 做视频, 生成视频, 动画, video, MP4, animate, HTML→video,
  article to video, link to video, data visualization video, product promo video,
  explainer video, template video, hyperframes, remotion render.
metadata:
  category: design
---

# html-video — HTML becomes video, on your laptop

Bring your local coding agent. Describe a video, or paste an article link / GitHub repo,
and the agent turns it into a multi-frame, fully animated video — then renders it to a
real MP4 right on your machine. One agent loop, pluggable rendering engines, a curated
template gallery, optional AI soundtrack.

---

## Prerequisites

| Requirement | Minimum | Check |
|-------------|---------|-------|
| **Node.js** | 20+ | `node --version` |
| **pnpm** | 9+ | `pnpm --version` |
| **ffmpeg** | Any recent | `ffmpeg -version` |
| **Chromium** | — | `npx playwright install chromium` |

---

## Setup

```bash
cd html-video
pnpm install
pnpm -r build
```

Verify the install:

```bash
node packages/cli/dist/bin.js doctor
```

---

## How it works

```
  prompt / link / repo
        │
        ▼
  ① source fetch        studio pulls the URL or repo server-side, flattens to Markdown
        │
        ▼
  ② agent loop          agent reads the material + picked template style, emits a
        │               content-graph (storyboard) + one HTML block per frame
        ▼
  ③ content-graph       multi-frame IR — nodes + edges, topo-sorted into frame order
        │
        ▼
  ④ per-frame HTML      each node becomes a self-contained animated HTML frame
        │
        ▼
  ⑤ engine render       headless Chromium records each frame → webm per frame
        │
        ▼
  ⑥ ffmpeg              each webm → mp4 (libx264), concat into one video
        │
        ▼
      your.mp4
```

---

## Usage patterns

### 1. Start the studio (interactive UI)

```bash
node packages/cli/dist/bin.js studio
# Opens at http://127.0.0.1:3071
```

In the studio: pick a template, chat with your agent, edit per-frame text,
add a soundtrack, and export MP4.

### 2. CLI: search templates

```bash
node packages/cli/dist/bin.js search-templates --intent "github stars race" --top 3
node packages/cli/dist/bin.js search-templates --intent "product promo 30s" --top 5
```

### 3. CLI: inspect a template

```bash
node packages/cli/dist/bin.js inspect-template --id frame-data-chart-nyt
```

### 4. CLI: create and render a project

```bash
# Create a project
node packages/cli/dist/bin.js project-create --name "my-video" --template frame-glitch-title

# Set variables
node packages/cli/dist/bin.js project-set-vars --project my-video --vars '{"title":"Hello World"}'

# Preview
node packages/cli/dist/bin.js project-preview --project my-video

# Render to MP4
node packages/cli/dist/bin.js project-render --project my-video
```

---

## Turn a link into a video

This is the primary use case: hand the agent a link, get a video back.

```
User:   做一个解读视频 https://mp.weixin.qq.com/s/…
Agent:  Reads the article → builds a multi-frame explainer from the real content
```

Supported sources:
- **Web article** → fetched and flattened to Markdown (WeChat 公众号 supported)
- **GitHub repo** → description, structure, and README pulled via public API
- **Just a prompt** → agent writes content from scratch

---

## Template gallery (21 templates)

Templates are organized by category:

| Category | Templates |
|----------|-----------|
| **Data Viz** | frame-data-chart-nyt, frame-pentagram-stat, frame-data-rollup |
| **Titles & VFX** | frame-glitch-title, vfx-text-cursor, frame-bold-poster |
| **Heroes & Cinematics** | frame-liquid-bg-hero, frame-light-leak-cinema, frame-electric-studio |
| **Product Promos** | frame-bold-signal, frame-creative-voltage, frame-build-minimal |
| **Outros** | frame-logo-outro |
| **Explainer Scaffolds** | frame-takram-organic |

Browse all 21 templates in the studio gallery (`/api/templates`).

---

## Multi-frame videos (content-graph)

For videos with multiple scenes, the agent produces a **content-graph**:

```json
{
  "nodes": [
    { "id": "intro", "kind": "text", "label": "Opening title" },
    { "id": "data1", "kind": "data", "label": "Key stat #1" },
    { "id": "outro", "kind": "entity", "label": "Logo end card" }
  ],
  "edges": [
    { "from": "intro", "to": "data1", "kind": "sequence" },
    { "from": "data1", "to": "outro", "kind": "sequence" }
  ]
}
```

Each node becomes one frame (self-contained animated HTML). The studio lets you
reorder frames, edit text inline, and re-render individual frames.

Single-frame videos take a fast path that skips the content-graph entirely.

---

## AI Soundtrack

In **Settings → Audio**, add a MiniMax API key. Then in the **Soundtrack** panel:

- **Background music** — describe a mood (e.g. "calm cinematic ambient, slow build")
- **Narration** — type a script for TTS

Both are mixed into the exported MP4 via ffmpeg (music ducked under voice).

---

## Supported agents (14 backends)

Auto-detected on `PATH`; switchable from the studio's top bar:

Open Design (Vela) · Windsurf CLI · Trae CLI · Claude Code · Cursor Agent ·
Codex CLI · Gemini CLI · Grok Build · Qwen Code · OpenCode · GitHub Copilot CLI ·
Aider · Hermes · Anthropic Messages API

---

## Architecture

```
packages/
├── core/                  Project / Asset / ContentGraph types, registries, orchestrator
├── content-graph/         Multi-frame storyboard IR (nodes + edges, topo-sort)
├── runtime/               Agent runtime — detect / spawn / stream (14 backends)
├── adapter-hyperframes/   Hyperframes engine adapter — real render via Chromium + ffmpeg
├── adapter-remotion/      Remotion engine adapter — React-based compositions
├── cli/                   `html-video` command + studio HTTP server + source fetching
└── project-studio/        Browser studio UI (chat, templates, frames, soundtrack, export)
templates/                 21 curated, license-clean video templates
research/                  RFCs (engine adapter / template metadata / agent skill / content-graph)
```

---

## Rendering engines

| Engine | Status | Paradigm |
|--------|--------|----------|
| **Hyperframes** | ✅ Shipped (default) | HTML + CSS + GSAP, headless Chromium + ffmpeg |
| **Remotion** | ✅ Native support | React components, `spring()` / `interpolate()` animations |
| **Motion Canvas / Revideo** | 🗺️ Planned | TypeScript generators on canvas |
| **Manim** | 🗺️ Researching | Math / 3D first |

The engine adapter interface is pluggable — swap engines without changing the
storyboard or the agent workflow.

---

## Key constraints

- **Always render to verify** — studio iframe previews use cached fonts; only exported
  MP4 shows the real render output. FOUT (flash of unstyled text) only visible in MP4.
- **Multi-frame concat** — when mixing frames from different engines, use concat FILTER
  (not demuxer) to rebuild the timeline correctly.
- **Duration control** — use `durationMode: 'explicit'` for multi-frame exports to
  prevent the engine from auto-extending frame durations.
- **License-clean templates only** — every template has SPDX license + provenance trail
  (origin / via_skill / transformation). No template ships without clear permissive license.

---

## Related projects

| Project | Relationship |
|---------|-------------|
| [Open Design](https://github.com/nexu-io/open-design) | Sister project — design-agent meta-layer |
| [HTML Anything](https://github.com/nexu-io/html-anything) | Sister project — HTML for static deliverables |
| [Hyperframes](https://github.com/heygen-com/hyperframes) | The default shipped engine adapter |

---

## License

Apache-2.0
