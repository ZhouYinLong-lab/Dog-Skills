# Evaluation

Use this reference to judge whether `codex-claude-pm` is useful on real work. Evaluate the workflow, not just whether code changed.

## Good Run Definition

A run is good when:

- Codex produced a self-contained Task Package.
- Claude Code completed the task without needing clarification.
- The diff stayed inside the intended scope.
- Acceptance criteria were specific enough to verify mechanically.
- Tests or equivalent checks were run and reported.
- Codex independently inspected the report, diff, and important test evidence.
- The final decision was unambiguous: ACCEPT, CHANGE REQUEST, PARTIAL, or BLOCKED.
- Long-running work can be tracked through status/result files without losing stdout, stderr, or metadata.

## Scorecard

Score each category 0-2 after a real task.

| Category | 0 | 1 | 2 |
|----------|---|---|---|
| Task clarity | Vague, required guessing | Mostly clear with some ambiguity | Specific files, actions, constraints, and AC |
| Dependency handling | Missing dependencies discovered late | Some dependencies named | Tool/auth/runtime/task dependencies mapped before dispatch |
| Scope control | Diff touched unrelated areas | Minor extra changes | Diff stayed inside stated scope |
| Claude autonomy | Claude needed follow-up | Completed with small assumptions | Completed from one Task Package |
| Report quality | No usable report | Partial report | Structured report with AC evidence and tests |
| Verification | Codex trusted report only | Some diff/test review | Independent diff and test verification |
| Accuracy | Buggy or unreviewable result | Mostly correct with fixes | Correct or precise Change Request |
| Token efficiency | More work than direct Codex edit | Similar cost | Codex saved implementation tokens while preserving review quality |
| Run management | Output lost or hard to find | Logs exist but status unclear | Job ID, status, stdout, stderr, metadata, and cancellation path are clear |

Interpretation:

- 16-18: Excellent. Keep using this workflow.
- 12-15: Useful. Tighten weak categories.
- 7-11: Marginal. Split tasks smaller or improve templates.
- 0-5: Poor fit. Codex should handle this type of task directly or redesign the workflow.

## Smoke Tests

Run these before trusting a new installation:

1. Validate skill structure:

```powershell
python "C:\Users\26585\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\codex-claude-pm"
```

2. Check dispatch prerequisites:

```powershell
powershell -ExecutionPolicy Bypass -File ".\codex-claude-pm\scripts\Test-ClaudeDispatchPrereqs.ps1" -WorkingDirectory .
```

3. Dry-run dispatch:

```powershell
powershell -ExecutionPolicy Bypass -File ".\codex-claude-pm\scripts\Invoke-ClaudeDispatch.ps1" `
  -TaskPackage "## Task Package`n`nSmoke test only. Do not edit files." `
  -WorkingDirectory . `
  -DryRun
```

4. Background plumbing dry-run:

```powershell
powershell -ExecutionPolicy Bypass -File ".\codex-claude-pm\scripts\Invoke-ClaudeDispatch.ps1" `
  -TaskPackage "## Task Package`n`nDry run only." `
  -WorkingDirectory . `
  -DryRun `
  -JobId cc-smoke-test

powershell -ExecutionPolicy Bypass -File ".\codex-claude-pm\scripts\Get-ClaudeDispatchRun.ps1" `
  -WorkingDirectory . `
  -JobId cc-smoke-test
```

## Forward Tests

Use at least three realistic tasks:

- Small surgical edit: one file, one test.
- Medium feature change: multiple files in one module.
- Failure-path task: missing dependency or impossible test command should produce BLOCKED or PARTIAL cleanly.

For each test, collect:

- Original user request.
- Generated Task Package.
- Claude Code Completion Report.
- `git diff --stat`.
- Commands Codex ran for verification.
- Scorecard result.

## Failure Signals

The skill needs revision when:

- Claude Code often asks follow-up questions.
- Completion Reports omit acceptance criteria or test evidence.
- Diffs regularly include unrelated files.
- Codex cannot verify the result without rereading the whole repository.
- Dependencies are discovered only after implementation.
- Change Requests are broad rewrites rather than focused corrections.
- The workflow costs more time and tokens than direct Codex implementation for the same task class.
