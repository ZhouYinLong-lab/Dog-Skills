---
name: dbskill
description: >
  Business diagnostic toolbox with 21 Claude Code skills extracted from 12,307
  tweets and refined into 4,176 knowledge atoms. Covers business model diagnosis
  (6 axioms), benchmark analysis, content creation diagnosis, short-video hook
  optimization, Xiaohongshu title formulas, AI writing detection, execution
  diagnosis (Adlerian psychology), concept deconstruction (Wittgenstein-style),
  goal clarification, good question generation, personal decision systems,
  interactive learning, state management (save/restore/report), and multi-role
  chatrooms. Use when the user needs business diagnostics, content strategy,
  decision-making frameworks, or self-improvement methodology. Trigger keywords:
  问诊, 诊断, 对标, benchmark, 内容诊断, 钩子, hook, 小红书标题, AI检测,
  AI writing check, 慢就是快, slow is fast, 行动诊断, 解构, deconstruct,
  目标, goal, 好问题, good question, 决策系统, decision, 学习, learning.
metadata:
  category: business
---

# dbskill — 别声张商业诊断工具箱

Business diagnostic toolbox by dontbesilent. 21 Claude Code skills extracted
from 12,307 tweets and refined into a structured knowledge system.

Version 2.14.2. CC BY-NC 4.0 License.

---

## Installation

```bash
# Claude Code Plugin Marketplace
claude plugin marketplace add dontbesilent2025/dbskill
claude plugin install dbs@dontbesilent-skills

# npx skills
npx -y skills add dontbesilent2025/dbskill -g --all
```

---

## Skills Overview

### Diagnostic Tools (核心诊断)

| Skill | Trigger | Purpose |
|-------|---------|---------|
| `dbs` | `/dbs` | **Main router** — listens and routes to the correct diagnostic skill |
| `dbs-diagnosis` | `/dbs-diagnosis`, `/问诊` | **Business model diagnosis** — consultation (dissolve questions) and checkup (analyze business model) modes |
| `dbs-benchmark` | `/dbs-benchmark` | **Benchmark analysis** — five-layer filtering to find the right entity to imitate |
| `dbs-content` | `/dbs-content` | **Content creation diagnosis** — five-dimensional testing for content quality |
| `dbs-content-system` | `/dbs-content-system` | **Content structuring** — turn local content assets into a sustainable engineering project |
| `dbs-hook` | `/dbs-hook` | **Short-video hook optimization** — diagnose and generate improved opening hooks |
| `dbs-xhs-title` | `/dbs-xhs-title` | **Xiaohongshu title formulas** — match against 75 proven viral title patterns |
| `dbs-ai-check` | `/dbs-ai-check` | **AI writing detection** — 22-feature scan (diagnosis only, no rewriting) |
| `dbs-slowisfast` | `/dbs-slowisfast` | **"Slow is fast"** — find friction-building assets, identify what's worth doing slowly |
| `dbs-action` | `/dbs-action` | **Execution diagnosis** — Adlerian psychology framework for knowing what to do but not doing it |
| `dbs-deconstruct` | `/dbs-deconstruct` | **Concept deconstruction** — Wittgenstein-style examination of vague business concepts |
| `dbs-goal` | `/dbs-goal` | **Goal clarification** — audit vague goals into inspectable deliverables |
| `dbs-good-question` | `/dbs-good-question`, `/好问题` | **Good question generator** — rewrite fuzzy questions into agent-reasoning-capable specs |
| `dbs-decision` | `/dbs-decision`, `/决策系统` | **Personal decision system** — four-layer local knowledge project with privacy mode |

### Learning Tools

| Skill | Trigger | Purpose |
|-------|---------|---------|
| `dbs-learning` | `/dbs-learning`, `/dbs-learn` | **Interactive learning** — split topics into sequenced articles with feedback-based adaptation |

### State Management

| Skill | Trigger | Purpose |
|-------|---------|---------|
| `dbs-save` | `/dbs-save` | Save current diagnostic state to `~/.dbs/sessions/` (append-only) |
| `dbs-restore` | `/dbs-restore` | Restore last saved state to continue where you left off |
| `dbs-report` | `/dbs-report` | Merge multiple saved states into a timestamped Markdown report |

### Chatroom Series

| Skill | Trigger | Purpose |
|-------|---------|---------|
| `dbs-chatroom-austrian` | `/dbs-chatroom-austrian`, `/奥派` | Austrian Economics chatroom — Hayek × Mises × Claude dialogue |
| `dbs-chatroom` | `/dbs-chatroom`, `/定向聊天室` | Directed chatroom — multi-role dialogue with judge summary |

### Agent Infrastructure

| Skill | Trigger | Purpose |
|-------|---------|---------|
| `dbs-agent-migration` | `/dbs-agent-migration` | **Agent workspace migration** — standardize any project across Claude Code/Codex/Grok |

---

## Knowledge Base

The `知识库/` directory contains:
- **高频概念词典.md** — 46 high-frequency terms from 4,176 knowledge atoms
- **原子库/** — 4,176 structured knowledge atoms (JSONL format)
- **Skill知识包/** — Detailed methodology documents for diagnosis, benchmark, content, action, deconstruct, and decision systems

---

## Key Design Principles

- **6 Business Axioms** — business model is objective, business determines morality, pricing IS the product, etc.
- **Wittgenstein-style language analysis** — dissolve vague concepts through precise inquiry
- **Adlerian psychology** — execution barriers as psychological patterns
- **"Slow is fast"** — friction-building as a competitive advantage

---

## License

CC BY-NC 4.0
