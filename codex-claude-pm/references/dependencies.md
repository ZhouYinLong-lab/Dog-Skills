# Dependencies

Use this reference when a dispatch may fail or drift because Claude Code lacks a tool, credential, service, project context, or prior task result.

## Dependency Types

- Skill dependency: The Codex skill files, templates, and dispatch scripts required to run this workflow.
- CLI dependency: Claude Code must be installed and callable as `claude` or a configured command path.
- Auth dependency: Claude Code must already be authenticated for non-interactive use.
- Shell dependency: The dispatch script requires PowerShell. On non-Windows systems, use PowerShell 7+ or manually run the equivalent `claude -p` command.
- Repository dependency: The target project must be readable, preferably under git, with a known working directory.
- Toolchain dependency: Project commands such as `npm`, `pnpm`, `python`, `pytest`, `docker`, or framework CLIs must be available if required by acceptance tests.
- Runtime dependency: Databases, queues, local servers, browsers, emulators, or external APIs required to verify behavior.
- Credential dependency: Environment variables, config files, tokens, or cloud auth required by project commands. Never include secret values in a Task Package.
- Task dependency: A Task Package may depend on an earlier task, branch, migration, generated artifact, or design decision.
- Policy dependency: Permission mode, allowed tools, branch rules, test requirements, and files that must not be touched.

## Dependency Map Format

Include this in any Task Package where dependencies matter:

```markdown
### Dependency Map

| Type | Required Item | How to Check | If Missing |
|------|---------------|--------------|------------|
| CLI | `claude` | `claude --help` | BLOCKED: ask user to install or use manual handoff |
| Auth | Claude Code login | `claude -p "ping"` | BLOCKED: user must authenticate Claude Code |
| Toolchain | `npm` | `npm --version` | PARTIAL: code only, tests not run |
| Runtime | Local database | project-specific health command | BLOCKED or skip integration tests with explanation |
| Task | `TASK-API-001` merged | `git log` or file exists | BLOCKED until prior task is present |
```

## Minimum Dependencies for Automatic Dispatch

- `claude` resolves in PATH or `-ClaudeCommand` points to the executable.
- `claude -p` works without opening an interactive login flow.
- PowerShell can execute `scripts/Invoke-ClaudeDispatch.ps1`.
- The target working directory exists and is trusted.
- Codex can inspect git status and diffs after Claude Code runs.

## Fallbacks

- If `claude` is missing, output the Task Package for manual paste into Claude Code.
- If auth is missing, stop before implementation and ask the user to finish Claude Code login.
- If project tests cannot run because tooling is missing, require Claude Code to report `NOT RUN` with the missing command and have Codex decide whether code inspection is enough.
- If runtime services are missing, split the task into implementation and integration-verification tasks.
- If task ordering is unclear, create a dependency chain of smaller Task Packages before dispatching.

## Dependency Rules

- Do not let Claude Code add new libraries casually. Require a reason, manifest update, and test coverage.
- Do not include secret values in Task Packages, reports, logs, or git.
- Treat missing dependencies as explicit `BLOCKED` or `PARTIAL`, not as silent assumptions.
- Prefer commands that verify dependencies mechanically.
- Record new dependencies in the Completion Report under `Dependency Changes`.
