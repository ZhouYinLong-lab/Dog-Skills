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

#### Example: full invocation

```
/workflow sync-skill-readme {
  skillDir: "tutor/",
  installName: "exam-tutor",
  triggerExamples: "帮我生成复习资料" / "analyze past exams",
  installCmd: "Download `dist/exam-tutor.skill` and drag it into Claude Code."
}
```

## README conventions

The root `README.md` maintains **alphabetical order** in all 4 skill-listing sections. When adding a new skill, entries go in their correct alphabetical position — not appended to the end.

Some skills use different source directory names vs install names:
- `tutor/` → installs as `exam-tutor`
- `nuwa-skill/` → installs as `nuwa`
- `html_video/` → installs as `html-video`

## Skill conventions

- **Bilingual**: Most skills have Chinese + English names, descriptions, and trigger keywords
- **Attribution**: Derived works require `ATTRIBUTIONS.md` crediting original authors
- **Frontmatter**: Every `SKILL.md` starts with `---`-delimited YAML containing `name` and `description`
- **Licenses**: Vary per skill — MIT, MIT-0, Apache-2.0, CC BY-NC 4.0
