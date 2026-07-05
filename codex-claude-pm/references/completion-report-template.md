# Completion Report Template

Require Claude Code to return this structure after implementation.

````markdown
## Completion Report

**Task ID**: `TASK-<PROJECT>-<NNN>`
**Status**: DONE / PARTIAL / BLOCKED

---

### Summary

<1-3 sentences describing what changed and why.>

---

### Files Modified

| File | Operation | Notes |
|------|-----------|-------|
| `<path>` | Added / Modified / Deleted | <short explanation> |

---

### Dependency Changes

- New dependencies: <package/tool/service/config, or "None">
- Removed dependencies: <package/tool/service/config, or "None">
- Required but unavailable dependencies: <anything that blocked work, or "None">

---

### Acceptance Criteria Status

- [ ] AC-1: <criterion text> - PASS / FAIL / NOT RUN - <evidence>
- [ ] AC-2: <criterion text> - PASS / FAIL / NOT RUN - <evidence>
- [ ] AC-3: <criterion text> - PASS / FAIL / NOT RUN - <evidence>

---

### Test Results

```text
<exact commands run and important output>
```

---

### Deviations

- <Any deviation from requirements or constraints, with reason. Use "None" when absent.>

---

### Open Questions

- <Only include unresolved questions for PARTIAL or BLOCKED. Use "None" when absent.>
````

## Codex Review Notes

Treat `DONE` as a claim, not proof. Codex must compare the report with the actual diff and test results before accepting.
