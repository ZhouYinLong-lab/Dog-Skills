# Task Package Template

Use this template for every Claude Code implementation handoff.

````markdown
## Task Package

**Task ID**: `TASK-<PROJECT>-<NNN>`
**Title**: <one-sentence implementation outcome>
**Priority**: P0 / P1 / P2
**Estimated Scope**: Small (<50 changed lines) / Medium (50-200) / Large (>200)
**Target Working Directory**: `<absolute or repo-relative path>`
**Depends on**: `<task id or none>`
**Dependency Map**: `<none, or list runtime/tool/project/task dependencies below>`

---

### Context

<1-4 sentences explaining why this change is needed and what the current behavior is.>

Relevant files:
- `<path>` - <why Claude Code should inspect this file>
- `<path>` - <why it matters>

Current commands worth checking:
- `<command>` - <what it verifies>

Dependency notes:
- Tooling: `<claude/node/python/docker/etc. or none>`
- Runtime services: `<database/cache/local server/etc. or none>`
- Credentials/config: `<env vars/settings needed, never paste secret values>`
- Task ordering: `<previous task ids or none>`
- Risk if missing: `<fallback or expected blocked state>`

---

### Requirements

1. <Concrete action in a specific file/module/function.>
2. <Concrete action, including expected behavior.>
3. <Add or update tests/docs only when required by the task.>

---

### Constraints

- Do not change <file/module/API/scope>.
- Do not delete or skip existing tests.
- Preserve public function signatures unless explicitly listed in Requirements.
- Follow existing project style and tooling.
- Keep changes limited to the files needed for this task.
- Do not introduce new runtime dependencies without stating why and updating the relevant manifest/docs.

---

### Acceptance Criteria

- [ ] AC-1: <Mechanical, observable condition.>
- [ ] AC-2: <Mechanical, observable condition.>
- [ ] AC-3: <Test or command passes, with command named.>

---

### Test Expectations

Run these commands and include outputs in the Completion Report:

```bash
<test command>
<lint/typecheck command>
```

If a command cannot be run, explain exactly why and provide the closest verification performed.

---

### Required Completion Report

Return a report using `completion-report-template.md`. Mark each acceptance criterion PASS, FAIL, or NOT RUN with evidence.
````

## Task Package Self-Check

Before dispatching, verify:

- The task can be done without asking Codex a follow-up question.
- Every requirement starts with an action verb.
- Every acceptance criterion can be checked by reading code, running a command, or using the app.
- The constraints say what Claude Code must not touch.
- Dependencies are explicit enough that a missing tool, credential, service, or prior task becomes a clear BLOCKED report instead of guesswork.
- The test commands are realistic for the project.
- The task is small enough that Codex can review the diff after completion.
