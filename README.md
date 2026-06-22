# Dog-Skills

> A collection of Claude skills for AI-assisted development workflows.

Skills are installable prompt bundles for [Claude](https://claude.ai) (Cowork / Claude Code). Each skill teaches Claude a specialized workflow so you don't have to re-explain it every time.

---

## Installation

### Method 1: Install from `.skill` file

Download the `.skill` file and drag it into Claude Code's chat window — it auto-installs to `~/.claude/skills/`.

### Method 2: Manual copy

```bash
mkdir -p ~/.claude/skills
cp -r cc-dispatch ~/.claude/skills/cc-dispatch
cp -r tutor ~/.claude/skills/exam-tutor
cp -r html_video ~/.claude/skills/html-video
```

### Verification

```bash
ls ~/.claude/skills/
# cc-dispatch/  exam-tutor/  html-video/
```

Once installed, skills trigger automatically when Claude detects a matching task — no special command needed.

### Trigger examples

| Skill | Try saying... |
|-------|---------------|
| `cc-dispatch` | "拆一个 Task Package 给 Claude Code" / "验收这份完成报告" |
| `exam-tutor` | "帮我生成第5章复习资料" / "分析往年卷的高频考点" / "为这道题写一份习题讲解" |
| `html-video` | "把这篇文章做成视频" / "用这个 GitHub 仓库生成一个介绍视频" / "做一个产品宣传动画" |

---

## Skills

### `cc-dispatch` — Codex × Claude Code Collaboration Protocol

**Purpose**: Saves Codex quota by turning the Codex ↔ Claude Code relationship into a structured ticket system rather than a back-and-forth conversation.

**Workflow**:

```
Codex (PM)  ──[Task Package]──▶  Claude Code (Executor)
                                        │
Codex (QA)  ◀──[Completion Report]──────┘
```

Codex acts as product manager: it decomposes requirements into a structured **Task Package** with explicit acceptance criteria and hands it off to Claude Code. Claude Code executes and returns a structured **Completion Report** with per-criterion PASS/FAIL status. Codex reviews the report and either accepts or generates an incremental Change Request.

**Why it saves quota**: Precise task packages mean Claude Code executes correctly on the first attempt — no clarification loops. Structured reports mean Codex verifies acceptance without re-reading all diffs — no unnecessary back-and-forth.

**Key components**:

- **Task Package template** — Task ID, context (file paths, not pasted code), numbered requirements, constraints, verifiable acceptance criteria, test commands
- **Completion Report format** — Status (DONE / PARTIAL / BLOCKED), modified files table, AC checklist with PASS/FAIL, test output, deviations
- **Acceptance framework** — 4-step review checklist, ACCEPT declaration format, Change Request format (incremental, references original Task ID)
- **Quality checklist** — Pre-flight self-check before handing off a task package

**Install**: Download `cc-dispatch.skill` and drag it into Claude Code.

---

### `exam-review-generator` — 期末复习资料生成器

**Purpose**: Generates structured exam review materials — chapter-by-chapter tutorials and exercise class handouts — by analyzing textbook PDFs, past exam papers, and answer keys. Identifies high-frequency topics, classifies content (keep / compress / remove) with evidence, and produces quality-audited markdown output.

**Two operating modes**:

| Mode | Trigger | Output |
|------|---------|--------|
| **Lightweight** | Single knowledge point, one exercise, pure topic analysis | Single `.md` file |
| **Complete** | Full chapter or multi-chapter generation | Tutorials + exercise classes + audit files + images |

**Complete mode workflow** (6 phases):

```
Phase 0: Inventory       →  List source materials, confirm scope
Phase 1: Topic Analysis  →  Map past paper questions to chapters/knowledge points
                            Classify: keep / compress-keep / remove (with evidence)
Phase 2: Tutorial Gen    →  Per-chapter tutorials with structured template
                            (exam summary → knowledge structure → deep dives → 
                             question types → self-check checklist)
Phase 3: Exercise Class  →  Group past paper questions by topic, detailed walkthroughs
Phase 4: Quality Gates   →  12-item checklist (format, images, coverage, evidence,
                            explanations, audit files) — no report until all pass
Phase 5: Report          →  Structured completion report with open issues
```

**Output structure per chapter**:

```
output/
├── tutorials/chXX.md              # Structured tutorial with exam relevance analysis
├── exercise_classes/chXX.md       # Exercise class with detailed walkthroughs
├── assets/chXX/                   # Locally cropped images (no full-page screenshots)
└── audit/
    ├── past_paper_topic_map.csv   # Every past question → chapter/knowledge point
    ├── chXX_coverage.csv          # Per-section keep/compress/remove decisions
    ├── chXX_md_check.txt          # Markdown format self-check
    ├── chXX_text_quality_check.txt # Content quality self-check
    └── chXX_image_audit.csv       # Per-image quality audit (if images used)
```

**Subject adaptation**: Defaults to math (calculus, linear algebra). References guide for circuits/electronics, physics, CS, and chemistry/biology with subject-specific writing requirements.

**Key design principles**:
- Evidence-driven: every keep/remove decision backed by past paper question numbers
- Student-centric: every formula explained in plain language with "why", "when", and "common mistakes"
- Image quality enforced: local crops only, full-page screenshots rejected
- Strict gating: 12-item quality checklist must pass before chapter is declared complete

**Install**: Download `exam-tutor.skill` and drag it into Claude Code.

---

### `html-video` — HTML→Video Meta-Layer for Coding Agents

**Purpose**: Turn prompts, article links, or GitHub repos into multi-frame animated MP4 videos by letting coding agents pick rendering engines, fill curated templates, and render locally via headless Chromium + ffmpeg.

**How it works**:

```
  prompt / link / repo
        │
        ▼
  ① source fetch        studio pulls the URL or repo server-side
        │
        ▼
  ② agent loop          agent reads the material + template style, emits a
        │               content-graph (storyboard) + one HTML block per frame
        ▼
  ③ engine render       headless Chromium records animated HTML → webm
        │
        ▼
  ④ ffmpeg              each webm → mp4 (libx264), concat into one video
        │
        ▼
      your.mp4
```

**Key features**:

- **14 coding agent backends** — Open Design (Vela), Windsurf CLI, Trae CLI, Claude Code, Cursor, Codex, Gemini, Grok, Qwen, OpenCode, Copilot, Aider, Hermes, Anthropic API — auto-detected and switchable
- **21 curated templates** — data viz (NYT-style charts), title cards & VFX, heroes & cinematics, product promos, outros, explainer scaffolds — all license-clean with provenance trail
- **Article / repo → video** — paste a URL or GitHub repo; studio fetches content server-side (WeChat 公众号 supported) and builds the video from real content
- **Multi-frame storyboards** — content-graph drives multi-scene videos; edit per-frame text inline, reorder, re-render
- **AI soundtrack** — optional background music + narration via MiniMax, mixed into the exported MP4
- **Pluggable engines** — Hyperframes (shipped), Remotion (native support), with Motion Canvas/Revideo and Manim on the roadmap
- **Real MP4 render** — headless Chromium + ffmpeg (libx264), locally — no cloud render, no per-clip fee
- **Apache-2.0** — no per-render fees, no seat caps

**Quick start**:

```bash
cd html_video
pnpm install && pnpm -r build
node packages/cli/dist/bin.js studio    # opens at http://127.0.0.1:3071
```

**Studio workflow**: pick a template → chat with your agent → edit per-frame text → add soundtrack → export MP4.

**CLI utilities**:

```bash
node packages/cli/dist/bin.js doctor
node packages/cli/dist/bin.js search-templates --intent "data chart" --top 3
node packages/cli/dist/bin.js project-create --name "my-video" --template frame-glitch-title
```

**Prerequisites**: Node.js 20+, pnpm 9+, ffmpeg, Chromium (Playwright).

**Install**: Download `html-video.skill` and drag it into Claude Code.

---

## Adding Skills

Each skill lives in its own directory with a `SKILL.md` file. To contribute:

1. Create `your-skill-name/SKILL.md` with YAML frontmatter (`name`, `description`)
2. Package with `python scripts/package_skill.py your-skill-name/`
3. Submit a PR with the directory and the `.skill` file

---

*Built with the Claude skill-creator workflow.*
