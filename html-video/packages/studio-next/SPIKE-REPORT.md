# Spike report — hyperframes/studio integration (2026-05-29)

Verdict: **plan A (rebuild html-video studio on top of hf NLELayout) costs
several weeks, not one. Pivot to plan B — keep the current vanilla studio,
borrow the small leaf components.**

## What we tried

`packages/studio-next/` is a Vite + React 19 app that imports
`@hyperframes/studio` 0.6.52 from npm, then attempts:

1. Mount `<Player directUrl={...}>` pointing at an existing frame served
   by the production studio (`http://127.0.0.1:3071/preview/<id>/frame/<nid>`).
2. Bind `useElementPicker(iframeRef)` to the player's iframe.
3. Toggle pick mode + click an element in the loaded frame.

## What works

- **Vite imports `@hyperframes/studio` cleanly.** No transpiler tweaks needed.
- **`SourceEditor` (CodeMirror 6 wrapper for HTML/CSS/JS)** renders and edits
  out of the box — confirmed in the earlier two-pane spike.
- **`hyperframes` runtime auto-injection** is real: hf Player polls the iframe
  every 200ms, detects `__timelines` (GSAP) or absence and injects an IIFE
  shim. Our agent-generated frames are valid hosts for this.
- **Pure utility exports** (`applyPatch`, `parseStyleString`,
  `mergeStyleIntoTag`, `findElementBlock`, `EaseCurveEditor`) are pure logic
  and drop in.

## What blocks plan A

- **`Player.directUrl` is a fallback, not the canonical entry.** Source
  reads `const src = directUrl || /api/projects/${projectId}/preview`.
  In practice the player still expects the surrounding hf studio backend:
  - serves `/api/projects/:id/composition` returning a composition.json
  - hosts the runtime IIFE on a same-origin path
  - implements asset / file APIs (`/api/projects/:id/files/...`) that the
    runtime calls back to fetch nested compositions
  Pointing `directUrl` at our `/preview/:id/frame/:nodeId` request loads
  the frame's HTML, but the runtime then tries to call back into a hf
  backend that doesn't exist, and the picker's postMessage handshake
  (`{ source: "hf-parent", type: "control", action: "enable-pick-mode" }`)
  is answered by nothing.

- **`useElementPicker` only works behind hf Player.** The iframe must be
  the same one the player has injected its runtime into. Our own iframe
  can't be substituted.

- **`NLELayout` reads from hf's Composition + FileManager + TimelineElement
  model**, which are concepts we don't map onto. Our ContentGraph nodes are
  N independent full-bleed HTML pages; hf's Composition is one timeline
  with multiple layers / clips on shared tracks.

- **The NLE shows a single composition's timeline, not "N storyboard
  cards"**. We'd have to either:
  - shoehorn each frame into a separate hf composition (and the NLE
    becomes a per-frame editor with no inter-frame view), or
  - flatten our N frames into one hf composition with N sequential layers
    (and lose the per-frame `data-hv-text` editing model)

Both choices wreck the v0.8 phase-driven flow.

## What we can still take

| component | status | what we'd use it for |
|-----------|--------|---------------------|
| `SourceEditor` (CodeMirror 6) | ✅ drop-in | Right-pane "Source" tab next to Frame text |
| `EaseCurveEditor` | ✅ drop-in | Future motion-curve picker on per-element edits |
| `applyPatch` + `parseStyleString` + `mergeStyleIntoTag` + `findElementBlock` | ✅ drop-in | Programmatic edits to frame HTML (used by an inline element picker we control) |
| Their styling tokens (`tailwind-preset.ts`) | ⚠️ would need React anyway | Visual consistency if we go React |
| `Player` / `Timeline` / `NLELayout` | ❌ requires hf backend | n/a |
| `useElementPicker` | ❌ requires hf runtime contract | n/a |

## Recommended path (plan B)

1. **Production studio stays vanilla JS at port 3071.** No React migration.
2. **Right-pane gets a "Source" tab** that wraps `SourceEditor` from
   `@hyperframes/studio`. Joey can edit the active frame's HTML directly
   in CodeMirror with HTML/CSS/JS syntax + autocomplete. Save via
   `PUT /api/projects/:id/frames/:nodeId/raw-html` (already exists).
3. **Click-to-edit text overlay stays our hand-rolled one** (commit
   `e17af19` / `5046fa5`). It already works without postMessage and
   without hf runtime.
4. **`packages/studio-next` becomes a permanent home** for any React-only
   borrowable hf widget (EaseCurveEditor etc), exposed back into the
   vanilla studio via an `<iframe>` portal or a tiny standalone bundle.
   No need to React-migrate the main app.
5. **If we ever want NLE-style editing**, the path is to ship our own
   timeline UI on top of our existing frames[] model — not to reshape our
   model to fit hf's.

## Out of scope for this report

- Alternatives like Remotion / Motion Canvas / Revideo as backend (we're a
  meta-aggregator anyway — they're future).
- Building a hf-compatible backend so `Player` works as designed. Doable
  but ~1 week, and the resulting integration still won't surface our
  5-phase chat or ContentGraph — it's a parallel UI for editing one
  composition at a time.
