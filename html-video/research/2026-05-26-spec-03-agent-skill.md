# RFC-03：Agent Skill 设计

> **Status**: Draft v0.1
> **Date**: 2026-05-26
> **Depends on**: [RFC-01](./2026-05-26-spec-01-engine-adapter.md), [RFC-02](./2026-05-26-spec-02-template-metadata.md)
> **Scope**: 本地 coding agent（Claude Code / Cursor / Codex / Gemini / OpenCode）通过 html-video 做视频的协议、CLI、决策逻辑

---

## 顶层架构

```
┌─────────────────────────────────────────────┐
│   coding agent (Claude Code / Cursor / ...) │
│   读 SKILL.md → 调 html-video CLI            │
└──────────────────┬──────────────────────────┘
                   │ stdio / shell
┌──────────────────▼──────────────────────────┐
│           html-video CLI                     │
│   ┌────────────────────────────────────┐     │
│   │  Command router                     │     │
│   │  - search-templates                 │     │
│   │  - inspect-template                 │     │
│   │  - render                           │     │
│   │  - preview                          │     │
│   │  - list-engines                     │     │
│   └────────────┬────────────────────────┘     │
└────────────────┼──────────────────────────────┘
                 │ in-process call
┌────────────────▼──────────────────────────────┐
│         @html-video/core                       │
│   - Template registry                          │
│   - Engine selector (capabilities-based)       │
│   - Render orchestrator                        │
└────────────────┬──────────────────────────────┘
                 │ dynamic import
┌────────────────▼──────────────────────────────┐
│   adapter-hyperframes / adapter-remotion /    │
│   adapter-motion-canvas / adapter-revideo      │
└────────────────────────────────────────────────┘
```

**关键约束**：agent 只跟 CLI 打交道，**不**直接 import 任何 npm 包，**不**直接调 engine adapter。所有跨语言隔离 + 决策逻辑收敛在 CLI 层。

---

## CLI Contract（v0.1）

### 全局 flags

```
--json              输出 JSON（agent 默认带）
--no-color          关 ANSI（agent 默认带）
--cwd <path>        项目工作目录（默认 process.cwd()）
--config <path>     html-video.config.json 路径（覆盖自动发现）
--verbose           打印决策依据（debug）
```

### `html-video list-engines`

列出本机可用 adapters + 各自 capabilities。

```bash
html-video list-engines --json
```

输出（节选）：

```json
{
  "engines": [
    {
      "id": "hyperframes",
      "name": "Hyperframes",
      "installed": true,
      "version": "0.4.2",
      "capabilities": { ... }
    },
    {
      "id": "remotion",
      "installed": false,
      "install_hint": "pnpm add -D remotion @remotion/renderer"
    }
  ]
}
```

### `html-video search-templates`

按 intent / tags / category 检索。输出已经按 RFC-02 流程排好序。

```bash
html-video search-templates \
  --intent "show our github stars growth over the past 24 months" \
  --aspect 16:9 \
  --license-allow Apache-2.0,MIT,CC0-1.0,CC-BY-4.0 \
  --top 5 \
  --json
```

输出：

```json
{
  "matches": [
    {
      "id": "data-bar-chart-race",
      "name": "Bar Chart Race",
      "engine": "motion-canvas",
      "engine_installed": true,
      "score": 0.91,
      "score_reason": "tags=chart,race,data-driven match intent; aspect 16:9 supported; Apache-2.0 ok",
      "preview_poster": "/path/to/preview.png",
      "best_for": ["GitHub stars race", "Sales ranking", "..."]
    },
    { ... }
  ],
  "filtered_out": [
    {
      "id": "logo-reveal-cinematic",
      "reason": "category=intro-outro doesn't match intent 'data growth'"
    }
  ]
}
```

### `html-video inspect-template`

返回某个 template 的完整 metadata，agent 借此了解需要哪些 inputs。

```bash
html-video inspect-template data-bar-chart-race --json
```

输出 = RFC-02 的 metadata + 一些 runtime info（resolved source path, cached preview URL...）

### `html-video render`

实际渲染。

```bash
html-video render \
  --template data-bar-chart-race \
  --vars-file vars.json \
  --format mp4 \
  --resolution 1920x1080 \
  --fps 60 \
  --duration auto \
  --output /tmp/out.mp4 \
  --json
```

输出（streaming JSON 或 final summary）：

```json
{
  "status": "ok",
  "output_path": "/tmp/out.mp4",
  "engine": "motion-canvas",
  "duration_sec": 14.5,
  "render_wall_clock_sec": 28.3,
  "file_size_mb": 12.4,
  "diagnostics": []
}
```

如果 streaming 模式（`--stream-progress`），每秒 emit 一行 NDJSON：

```ndjson
{"type":"progress","stage":"preparing","pct":5}
{"type":"progress","stage":"preparing","pct":10}
{"type":"progress","stage":"rendering","pct":12,"frame":108,"total_frames":870}
...
{"type":"progress","stage":"muxing","pct":97}
{"type":"done","status":"ok","output_path":"/tmp/out.mp4",...}
```

### `html-video preview`

启 dev server 让用户在浏览器调（agent 调起后把 URL 推给用户）。

```bash
html-video preview --template data-bar-chart-race --vars-file vars.json --json
```

```json
{
  "url": "http://127.0.0.1:53219",
  "engine": "motion-canvas",
  "pid": 87234,
  "stop_command": "html-video preview-stop --pid 87234"
}
```

### `html-video doctor`

诊断本机环境。Agent 在用户首次启动 html-video 时**应该先跑这个**，把缺的依赖补全提示给用户。

```bash
html-video doctor --json
```

输出：

```json
{
  "status": "warning",
  "checks": [
    { "name": "node-version", "status": "ok", "value": "v20.10.0" },
    { "name": "ffmpeg", "status": "ok", "value": "ffmpeg version 7.0" },
    { "name": "chromium", "status": "ok" },
    { "name": "adapter-hyperframes", "status": "ok", "version": "0.4.2" },
    { "name": "adapter-remotion", "status": "missing", "install_hint": "pnpm add -D @html-video/adapter-remotion" }
  ]
}
```

---

## SKILL.md（Claude Code 版）

放置位置：`@html-video/agent-skill-claude-code/SKILL.md`，用户 install 后 symlink 到 `~/.claude/skills/html-video/`。

```markdown
---
name: html-video
description: |
  Generate HTML videos by orchestrating multiple rendering engines (Hyperframes,
  Remotion, Motion Canvas, Revideo) through a unified CLI. Pick the right engine
  per use case, fill template variables, render to MP4/WebM. Use when user asks
  to "create video", "render video", "make a video", "数据动画", "演示视频",
  "social short", or provides data/intent that fits a video format.
---

# html-video skill

You orchestrate the `html-video` CLI to generate videos. Never call engine
adapters directly — always go through the CLI.

## Initial check (run once per session)

```bash
html-video doctor --json
```

If `status` is `error` or critical adapters missing, surface install hints to
the user and stop. If `warning`, note the gap but proceed if user's intent
doesn't need the missing piece.

## Standard workflow

### 1. Understand intent

When user asks for a video, extract:
- **purpose** (data viz / social short / explainer / promo / ...)
- **input data** (if any — table, list, JSON, narrative)
- **aspect ratio** preference (16:9 / 9:16 / 1:1)
- **duration** target (if mentioned)
- **license needs** (commercial vs personal)

If any is unclear, ask **one batched question** before searching templates.

### 2. Search templates

```bash
html-video search-templates \
  --intent "<extracted purpose+data summary>" \
  --aspect <ratio> \
  --license-allow <comma-list> \
  --top 3 --json
```

Show the user **top 3** results with poster image and score reason. Let them pick.

### 3. Inspect chosen template

```bash
html-video inspect-template <id> --json
```

Read the `inputs.schema`. Compare with the data the user has provided.

- If user data already covers the schema → fill `vars.json`, skip to render
- If gaps → ask user **the missing fields only** (don't re-confirm what's
  already known)
- If user data needs reshaping (e.g. user gave CSV, schema wants JSON
  array-of-objects) → reshape silently, show before rendering

### 4. Optional preview

If template's `performance.reference_render` suggests render will take
> 30 seconds, offer a preview first:

```bash
html-video preview --template <id> --vars-file vars.json --json
```

Open the URL in the user's browser. After their OK, render.

### 5. Render

```bash
html-video render --template <id> --vars-file vars.json \
  --format mp4 --resolution 1920x1080 --fps 60 \
  --output ~/Desktop/<descriptive-name>.mp4 \
  --stream-progress --json
```

Surface progress to user every 25% (preparing / rendering 25% / 50% / 75% /
muxing / done). On done, paste the absolute output path.

### 6. On errors

- `engine-not-installed` → run `html-video doctor` and surface install hints
- `template-invalid` → re-inspect template, check vars match schema
- `render-failed` → read `diagnostics` array, propose fix, ask user before retry
- `render-timeout` → ask user if lower resolution / shorter duration is OK

## Anti-patterns (don't do these)

- ❌ Don't pick a template silently — always show top 3 with reasons
- ❌ Don't render a 60-second video without offering preview first
- ❌ Don't re-ask for vars the user already provided
- ❌ Don't fall back to a different engine on render failure without telling
  the user (the user might have license / aesthetic reasons for the choice)
- ❌ Don't write to engine-native files directly — only edit `vars.json`

## Quick reference

| Task | Command |
|---|---|
| Health check | `html-video doctor --json` |
| Find templates | `html-video search-templates --intent "..." --json` |
| Read template | `html-video inspect-template <id> --json` |
| Render | `html-video render --template <id> --vars-file vars.json --output <path> --json` |
| Preview | `html-video preview --template <id> --vars-file vars.json --json` |
| List engines | `html-video list-engines --json` |
```

---

## Cursor / Codex / Gemini variants

不重写一遍。用 [`@html-video/agent-skill-claude-code`](#) 作为 master，**自动 transpile** 成：

- `@html-video/agent-skill-cursor` —— `.cursor/rules/html-video.mdc` 形式
- `@html-video/agent-skill-codex` —— `~/.codex/skills/html-video.md`
- `@html-video/agent-skill-gemini` —— `~/.gemini/agents/html-video.toml`
- `@html-video/agent-skill-opencode` —— OD 项目内 `.opencode/skills/html-video/`

transpile 工具藏在 `tools/skill-transpile/`，CI 跑。所有变体共享 SKILL.md 的 prose，只换 frontmatter / file 命名。

---

## Engine 选择逻辑（agent 不必懂细节，但放这里供 review）

CLI 内部决策伪码：

```ts
function selectEngineForTemplate(template, userPrefs, installedEngines) {
  // Stage 0: template 已经声明 engine，必须用这个 engine 的 adapter
  const targetEngine = template.engine;
  const adapter = installedEngines.find(e => e.id === targetEngine);

  if (!adapter) {
    return {
      ok: false,
      reason: `Template requires ${targetEngine} but it's not installed`,
      install_hint: `pnpm add -D @html-video/adapter-${targetEngine}`
    };
  }

  // Stage 1: validate template against adapter capabilities
  const validation = adapter.validate(template);
  if (!validation.ok) {
    return { ok: false, reason: validation.errors[0].message };
  }

  // Stage 2: license filter
  if (userPrefs.commercial && template.license.commercial_use === false) {
    return { ok: false, reason: 'Template not licensed for commercial use' };
  }

  // Stage 3: aspect / format / fps 兼容
  if (userPrefs.format && !adapter.capabilities.outputFormats.includes(userPrefs.format)) {
    return { ok: false, reason: `Engine ${targetEngine} doesn't support ${userPrefs.format}` };
  }

  return { ok: true, adapter };
}
```

注意：**v0.1 不做 cross-engine fallback**（一个 template 只对应一个 engine）。如果 agent 想"换 engine 试试"，让它重新 search-templates 选另一个 template id。

---

## 监控 / 遥测（可选）

`html-video.config.json` 可加：

```json
{
  "telemetry": {
    "enabled": false,
    "endpoint": "https://html-video.nexu.io/telemetry"
  }
}
```

默认 **off**。开了后只发匿名渲染统计（template id, engine, duration, success/fail），**不**发用户 vars 内容。Apache-2.0 + 显式 opt-in 是底线。

---

## 用户交互范例（实际对话）

```
User: 帮我做个视频，展示 OD 仓库 GitHub stars 25 天涨 5 万的曲线

Agent (内部跑 search):
  → html-video search-templates --intent "github stars growth over time" --aspect 16:9 --top 3 --json

Agent (回应用户):
  我找到 3 个匹配的模板，你想用哪个？

  1. **Bar Chart Race** ★★★ (Motion Canvas)
     [poster.png]
     适合：rankings 对比 / 多 entity 演变
     时长：5-60s 可调
     License: Apache-2.0

  2. **Line Chart Animation** ★★ (Hyperframes)
     [poster.png]
     适合：单指标随时间演变（你这个场景）
     时长：3-30s
     License: Apache-2.0

  3. **Number Counter Reveal** ★ (Hyperframes)
     [poster.png]
     适合：单数字爆炸式 reveal
     时长：3-10s

User: 第二个

Agent: 我看了 Line Chart 模板需要这些数据：
  - data: 时间序列 (date + value)
  - title: 标题（≤80字）
  - y_axis_label: Y 轴标签

  你的 25 天数据我能帮你拉，但 GitHub API 翻页限制可能不全，要不要我用 growth-dashboard 已 backfill 的数据？

User: 用 dashboard 的

Agent (调 growth-dashboard 的 SQLite 拉数据 → 整成 JSON → 渲染):
  好。Title 我用 "Open Design GitHub Stars · 25 Days to 50K"，
  y 轴 "Stars (cumulative)"。开始渲染...

  [progress 25% / 50% / 75%]

  ✅ 渲染完成
  /Users/joey/Desktop/od-stars-50k-race.mp4 (1920×1080, 14.5s, 12 MB)
```

---

## Open Questions（v0.2 待定）

1. **Skill 之间的协作**：html-video skill 想调 growth-dashboard 的数据 → 是直接读 SQLite 还是走 cross-skill MCP？v0.1 让 agent 自己 bridge
2. **Multi-shot 工作流**：用户说"做个视频，60 秒，前 10 秒 logo reveal、中间 40 秒 chart race、最后 10 秒 CTA" → 需要 timeline composer skill。v0.2+ 才考虑
3. **缓存层**：相同 template + 相同 vars 多次 render 是否复用？倾向加 content-hash cache，但 v0.1 先不做
4. **OpenCode 集成**：OD 用 opencode 跑 agent；html-video 是否也注入 opencode skill registry？等 OD client 那边的 skill 接入接口稳定再做
