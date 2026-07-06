# codex-plugin-cc Study Notes

Source studied: `openai/codex-plugin-cc`.

## What Transfers Well

- Split user-facing commands from execution helpers.
- Keep setup, dispatch, status, result, and cancel as separate operations.
- Store each run as a durable job with metadata, stdout, stderr, and status.
- Support foreground for small bounded work and background for long work.
- Preserve delegate output; do not rewrite or silently summarize it in the transport layer.
- Keep review-only flows separate from write-capable implementation flows.
- Provide resume/result pointers so a human or the supervising agent can continue from the right run.
- Treat setup/auth failures as explicit blockers instead of improvising.

## What Does Not Transfer Directly

- `codex-plugin-cc` uses Claude Code plugin slash commands and the Codex app-server. This skill runs inside Codex and calls the local `claude` CLI, so there is no Claude plugin command router or Codex app-server equivalent.
- Claude Code background execution in the plugin uses Claude's own tool runtime. This skill uses PowerShell `Start-Process`, so cancellation can stop the wrapper process but may not interrupt every child process on every platform.
- `codex-plugin-cc` can import Claude sessions into Codex threads. The reverse direction is not exposed by `claude -p`; this skill records task packages and outputs instead.

## Adopted Changes

- Add `-Background` and `-JobId` to `Invoke-ClaudeDispatch.ps1`.
- Write `metadata.json`, `status.json`, `stdout.txt`, `stderr.txt`, and `task-package.md` for every run.
- Add `Get-ClaudeDispatchRun.ps1` for `/status` and `/result`-style inspection.
- Add `Stop-ClaudeDispatchRun.ps1` for best-effort cancellation.
- Document foreground/background selection and result-preservation rules in `SKILL.md`.
