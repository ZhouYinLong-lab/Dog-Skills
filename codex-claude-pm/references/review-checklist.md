# Review Checklist

Use this checklist before dispatching and before accepting Claude Code output.

## Pre-Dispatch

- Scope is small enough to review.
- The repository state is understood with `git status`.
- Relevant files and commands are listed.
- Requirements are actions, not aspirations.
- Acceptance criteria include boundaries, normal cases, and likely edge cases.
- Constraints protect public APIs, unrelated modules, generated artifacts, lockfiles, migrations, secrets, and user data.
- Test expectations name exact commands.
- The prompt asks for a structured Completion Report.

## Dispatch Safety

- Use `acceptEdits` when you want Claude Code to propose edits with safer permission handling.
- Use `auto` only in trusted local projects or disposable worktrees.
- Use `bypassPermissions` only when the user explicitly accepts the risk or the environment is isolated.
- Prefer a fresh branch/worktree for large or risky changes.
- Avoid dispatching secrets, private tokens, production credentials, or irreversible operations.

## Post-Dispatch

- Read the Completion Report and note every FAIL, NOT RUN, and deviation.
- Inspect `git diff --stat`.
- Inspect targeted diffs for changed files.
- Check that no unrelated files were modified.
- Run requested tests independently when feasible.
- Verify behavior, not just existence of code.
- If tests were not run, decide whether the gap is acceptable before accepting.
- If scope expanded unexpectedly, issue a Change Request or revert only the agent's unrelated changes with user awareness.

## Acceptance Decision

Accept only when:

- Requirements are implemented.
- Constraints are respected.
- Acceptance criteria pass or explicitly accepted deviations are documented.
- Codex has independently checked the important evidence.

Request changes when:

- Any core acceptance criterion fails.
- The implementation changes unrelated behavior.
- Tests are missing for risky logic.
- The report and diff disagree.
- The result is too broad to confidently review.
