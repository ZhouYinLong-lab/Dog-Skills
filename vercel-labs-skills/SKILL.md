---
name: find-skills
description: >
  Helps users discover and install agent skills from the open skills ecosystem.
  When a user asks "how do I do X", "find a skill for X", "is there a skill
  that can...", or expresses interest in extending capabilities, this skill
  searches the skills.sh leaderboard and runs `npx skills find <query>` to
  locate relevant skills, verifies quality (install count, source reputation,
  GitHub stars), and offers to install. Use when users need to find skills
  for any domain: web development, testing, DevOps, documentation, code
  quality, design, or productivity. Trigger keywords: find skill, search skill,
  discover skill, install skill, is there a skill, how do I, skill for X.
---

# find-skills — Discover and Install Agent Skills

Helps users discover, evaluate, and install agent skills from the open
skills ecosystem. Part of the [vercel-labs/skills](https://github.com/vercel-labs/skills)
project — the CLI for the open agent skills ecosystem.

---

## Workflow

1. **Understand the need** — identify the domain, specific task, and likelihood a skill exists
2. **Check the leaderboard** — browse [skills.sh](https://skills.sh) for popular skills
3. **Search** — run `npx skills find <query>`
4. **Verify quality** — check install count (prefer 1K+), source reputation, GitHub stars
5. **Present options** — show name, description, install count, source, and install command
6. **Offer to install** — `npx skills add <owner/repo@skill> -g -y`

---

## Common skill categories

| Category | Example queries |
|----------|----------------|
| **Web Development** | "React form validation", "API documentation generator" |
| **Testing** | "unit test generator", "E2E test helper" |
| **DevOps** | "Docker compose generator", "CI pipeline helper" |
| **Documentation** | "README generator", "API docs from code" |
| **Code Quality** | "code review assistant", "linting rule generator" |
| **Design** | "UI component generator", "color palette picker" |
| **Productivity** | "task breakdown", "PR description writer" |

---

## Installation

```bash
npx skills add vercel-labs/agent-skills
```

This installs the `find-skills` skill and the `skills` CLI tool.

---

## The `npx skills` ecosystem

The `skills` CLI supports 70+ agents (Claude Code, Codex, Cursor, Windsurf,
GitHub Copilot, Cline, Roo Code, and many more). Skills are defined as
SKILL.md files with YAML frontmatter and installed via GitHub, GitLab,
or local paths.

```bash
npx skills add <source>       # Install skills
npx skills list               # List installed skills
npx skills find [query]       # Search for skills
npx skills update [skills]    # Update installed skills
npx skills remove [skills]    # Remove installed skills
```

MIT License.
