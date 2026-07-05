---
name: codex-claude-pm
description: Codex as product manager and reviewer for delegating coding implementation to Claude Code. Use when the user wants Codex to split software work into precise Task Packages, call or hand off to Claude Code for implementation, review Completion Reports, inspect diffs, run verification, and issue acceptance or change requests. Trigger for requests mentioning Claude Code delegation, saving Codex quota, cc-dispatch, task packages, implementation handoff, PM/reviewer workflow, or Codex supervising another coding agent.
---

# Codex Claude PM

Use this skill to make Codex the planner, reviewer, and final owner while Claude Code performs the implementation work. Treat the workflow as an engineering ticket system, not an open-ended chat.

## Core Rule

Codex owns correctness. Claude Code may write code, but Codex must still inspect scope, compare against acceptance criteria, and independently verify the result before accepting it.

## Workflow

1. Orient in the repository.
   - Check the current working directory, git status, relevant files, package scripts, and existing tests.
   - Prefer `rg` and targeted file reads. Avoid broad rewrites before understanding local patterns.
   - If the worktree is dirty, note user changes and avoid overwriting unrelated edits.

2. Decide whether to dispatch.
   - Dispatch to Claude Code when the request is mostly implementation and can be specified with concrete files, constraints, and acceptance criteria.
   - Keep Codex-local work when the task is mainly product judgment, architecture choice, security review, small surgical edit, or high-risk secret/credential handling.
   - Split work before dispatch if it touches more than 3 unrelated modules, exceeds about 300 expected changed lines, or has separable dependencies.

3. Write a Task Package.
   - Use `references/task-package-template.md`.
   - List precise files and boundaries.
   - Convert vague intent into numbered executable requirements.
   - Define mechanical acceptance criteria and exact test commands.
   - Include a required Completion Report format from `references/completion-report-template.md`.

4. Quality-check the Task Package before sending.
   - Read `references/review-checklist.md` when the task has meaningful risk.
   - Ensure Claude Code can act without follow-up questions.
   - Prefer smaller, verifiable tasks over one broad prompt.

5. Dispatch to Claude Code.
   - If the local CLI is available, use `scripts/Invoke-ClaudeDispatch.ps1`.
   - If the CLI is unavailable or blocked by login, output the Task Package for manual paste into Claude Code.
   - Prefer non-interactive Claude Code mode: `claude -p`.

6. Verify the result.
   - Read Claude Code's Completion Report.
   - Inspect `git diff --stat` and targeted `git diff` for modified files.
   - Run the requested tests yourself when feasible.
   - Check that all acceptance criteria are actually satisfied; do not trust PASS labels alone.

7. Decide.
   - ACCEPT only when requirements, constraints, and tests are satisfied or deviations are explicitly acceptable.
   - Issue a Change Request when a fix is needed. Use `references/change-request-template.md`.
   - If Claude Code exposes unrelated failures, record them separately instead of silently expanding scope.

## CLI Dispatch

Use the bundled script from the repository root or target project root:

```powershell
powershell -ExecutionPolicy Bypass -File .\codex-claude-pm\scripts\Invoke-ClaudeDispatch.ps1 `
  -TaskPackagePath .\.codex-claude-pm\tasks\TASK-APP-001.md `
  -WorkingDirectory . `
  -PermissionMode acceptEdits `
  -OutputFormat text
```

Useful modes:

```powershell
# Preview command and write logs without calling Claude Code
powershell -ExecutionPolicy Bypass -File .\codex-claude-pm\scripts\Invoke-ClaudeDispatch.ps1 `
  -TaskPackagePath .\.codex-claude-pm\tasks\TASK-APP-001.md `
  -DryRun

# More autonomous local execution in a trusted sandbox or disposable worktree
powershell -ExecutionPolicy Bypass -File .\codex-claude-pm\scripts\Invoke-ClaudeDispatch.ps1 `
  -TaskPackagePath .\.codex-claude-pm\tasks\TASK-APP-001.md `
  -PermissionMode auto

# Constrain Claude Code to specific tools
powershell -ExecutionPolicy Bypass -File .\codex-claude-pm\scripts\Invoke-ClaudeDispatch.ps1 `
  -TaskPackagePath .\.codex-claude-pm\tasks\TASK-APP-001.md `
  -AllowedTools "Read","Edit","Bash(npm test*)","Bash(git diff*)"
```

The script writes each run under `.codex-claude-pm/runs/<timestamp>/` with the task package, command metadata, stdout, and stderr.

## Accuracy Practices

- Make every requirement observable: name the file, function, UI state, API response, or test behavior.
- Put "do not change" constraints in the Task Package, especially public APIs, unrelated files, migrations, lockfiles, generated files, and user data.
- Include negative cases and boundary cases in acceptance criteria.
- Require Claude Code to report exact files changed and test outputs.
- Run independent verification from Codex after Claude Code returns.
- Prefer `acceptEdits` or `auto` over `bypassPermissions` unless the project is isolated and trusted.
- Use a fresh branch or worktree for large tasks.
- If a completion report says tests failed because of pre-existing issues, verify that claim with targeted commands before accepting.

## Manual Handoff Format

When automatic CLI dispatch is not appropriate, respond with:

1. The Task Package to paste into Claude Code.
2. The exact target working directory.
3. The expected Completion Report format.
4. The verification commands Codex will run after the report returns.

## References

- `references/task-package-template.md` - canonical Task Package format.
- `references/completion-report-template.md` - required Claude Code response format.
- `references/change-request-template.md` - format for follow-up fixes.
- `references/review-checklist.md` - pre-dispatch and post-dispatch quality gates.
