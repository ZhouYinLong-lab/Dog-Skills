# Dog-Skills

A collection of Claude Code skills for AI-assisted development workflows. Each skill lives in its own top-level directory with a `SKILL.md` file at its root.

## Repository structure

```
skill-directory/
├── SKILL.md          # Required: YAML frontmatter (name, description) + markdown body
├── README.md         # Optional: skill-level documentation
├── LICENSE           # Optional
├── ATTRIBUTIONS.md   # Required for derived works
├── references/       # Optional: supporting materials
├── scripts/          # Optional: automation scripts
└── ...
```

Pre-built `.skill` files live in `dist/`.

## Adding a skill

### Quick: just the directory

1. Create `your-skill-name/SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: your-skill-name
   description: >
     What this skill does. Trigger keywords: keyword1, keyword2, 中文关键词.
   metadata:
     category: development  # ← REQUIRED: see categories below
   ---
   # Your Skill Title
   ```
2. Run the sync workflow to update the root README (see below).

### Workflow: sync skill to README

After creating or copying a skill directory, run:

```
/workflow sync-skill-readme { skillDir: "your-skill-name/" }
```

This workflow updates the root `README.md` in **4 sections**:
1. **Installation** (Method 2) — adds `cp -r` command
2. **Verification** — adds entry to `ls` output
3. **Trigger examples table** — adds row with example prompts
4. **Skills section** — adds full `### \`name\` — Title` entry

#### Optional args

| Arg | Default | Description |
|-----|---------|-------------|
| `skillDir` | *(required)* | Path to skill directory, e.g. `"my-skill/"` |
| `name` | from SKILL.md | Override skill name |
| `title` | from SKILL.md | Override human-readable title |
| `triggerExamples` | derived from description | Examples for trigger table: `"试试这个" / "try this"` |
| `installName` | same as `name` | Directory name in `~/.claude/skills/` |
| `installCmd` | auto-generated | Install command for the Skills section |
| `shortDescription` | from SKILL.md | One-line purpose description |
| `category` | from SKILL.md metadata | Skill category key (see categories below) |

#### Example: full invocation

```
/workflow sync-skill-readme {
  skillDir: "tutor/",
  installName: "exam-tutor",
  triggerExamples: "帮我生成复习资料" / "analyze past exams",
  installCmd: "Download `dist/exam-tutor.skill` and drag it into Claude Code."
}
```

## Skill Categories

Every skill must belong to exactly one category. The category is stored in `SKILL.md` frontmatter under `metadata.category`.

| Category Key | Icon | Name | Description |
|-------------|------|------|-------------|
| `thinking` | 🧠 | Thinking & Research | Deep research, first-principles thinking, persona distillation, learning methods |
| `development` | 💻 | Development | Code review, collaboration protocols, site cloning, IDE bridges |
| `design` | 🎨 | Design & Frontend | UI/UX design systems, anti-AI-taste design, animations, HTML→video |
| `content` | 📝 | Content & Writing | AI text humanization, slide decks, diagrams, translation, social content |
| `learning` | 📚 | Learning & Teaching | Exam review generators, tutorial generators, course creation |
| `business` | 💼 | Business & Strategy | Business diagnostics, decision frameworks, benchmark analysis |
| `tools` | 🔍 | Tools & Discovery | Skill discovery, reading assistants, IM bridges, utilities |

## README conventions

The root `README.md` is organized into **category sections** (see above). Within each category, skills are listed in **alphabetical order**. When adding a new skill:

1. Determine the correct category from the SKILL.md metadata
2. Add the skill entry to the correct category section in alphabetical order
3. Update all 4 sub-sections within that category: Installation, Verification, Trigger Table, Skills Detail

Some skills use different source directory names vs install names:
- `tutor/` → installs as `exam-tutor`
- `nuwa-skill/` → installs as `nuwa`
- `html_video/` → installs as `html-video`
- `claude-to-im-skill/` → installs as `claude-to-im`
- `vercel-labs-skills/` → installs as `find-skills`
- `last30days-skill/` → installs as `last30days`
- `ui-ux-pro-max-skill/` → installs as `ui-ux-pro-max`

## Plugin-based skills

Some skills in this repo are wrappers/guides for Claude Code plugins. These use `/plugin install` instead of `cp -r`:

- `superpowers/` → `/plugin install superpowers@claude-plugins-official`
- `planning-with-files/` → `/plugin install planning-with-files@claude-plugin-directory`
- `code-review/` → `/plugin install code-review@claude-plugin-directory`
- `code-simplifier/` → `/plugin install code-simplifier@claude-plugin-directory`
- `webapp-testing/` → `/plugin install webapp-testing@claude-plugin-directory`
- `mcp-builder/` → `/plugin install mcp-builder@claude-plugin-directory`

These skill directories serve as documentation and trigger-awareness wrappers — when a user's request matches the trigger keywords, Claude Code will suggest the appropriate plugin.

## README special sections

The root `README.md` has two special sections beyond the skill catalog:

- **Usage Workflow**: New project setup guide, daily development pipeline, and maintenance cycle
- **Skill Combination Recommendations**: Tiered skill bundles for different project types (starter, full pipeline, frontend, large project)

## Skill conventions

- **Bilingual**: Most skills have Chinese + English names, descriptions, and trigger keywords
- **Attribution**: Derived works require `ATTRIBUTIONS.md` crediting original authors
- **Frontmatter**: Every `SKILL.md` starts with `---`-delimited YAML containing `name` and `description`
- **Licenses**: Vary per skill — MIT, MIT-0, Apache-2.0, CC BY-NC 4.0
