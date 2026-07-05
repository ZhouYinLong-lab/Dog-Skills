# Change Request Template

Use a Change Request when Claude Code's result is close but fails acceptance criteria, violates constraints, or needs a focused correction.

````markdown
## Task Package

**Task ID**: `TASK-<PROJECT>-<NNN>-CR<NUMBER>`
**Title**: <specific correction>
**Priority**: P0 / P1 / P2
**Estimated Scope**: Small / Medium / Large
**Depends on**: `TASK-<PROJECT>-<NNN>`

---

### Context

This is a change request for `TASK-<PROJECT>-<NNN>`.

Observed issue:
- <What Codex found in the diff, tests, or behavior. Include file paths and line numbers when possible.>

---

### Requirements

1. <Only the incremental correction.>
2. <Update or add tests if needed to prevent recurrence.>

---

### Constraints

- Do not rewrite unrelated completed work from the parent task.
- Keep changes limited to the failing acceptance criteria unless explicitly stated.

---

### Acceptance Criteria

- [ ] AC-1: <The specific failure is fixed.>
- [ ] AC-2: <Relevant tests pass.>

---

### Test Expectations

```bash
<targeted command>
```
````
