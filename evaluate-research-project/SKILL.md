---
name: evaluate-research-project
description: Evidence-based evaluation of research repositories across course-project completion, real paper-submission readiness, and open-source maturity. Use when asked to assess a course assignment, capstone, research prototype, GitHub repository, OpenReview submission, expected grade, venue level, publication probability, reproducibility, novelty, engineering quality, or OSS readiness; also trigger for Chinese requests such as 评估项目、完成度、大作业评分、论文投稿水平、开源成熟度、仓库水平、能投什么会议。
metadata:
  category: thinking
---

# Evaluate Research Project

Produce three independent verdicts: course quality, research-paper readiness, and open-source maturity. Do not infer one from another.

## Required resources

Read `references/rubrics.md` completely before assigning scores. Run `scripts/collect_evidence.py` when the target is a local Git repository.

## Workflow

### 1. Establish the evaluation target

- Resolve the repository root, current branch, commit, remote, date, and requested evaluation lanes.
- Locate any course specification, grading rubric, target venue, paper template, or release goal supplied by the user or linked from the repository.
- Browse current official sources when rules, venue policy, repository metrics, or related work may have changed.
- If no rubric or venue is specified, use the default rubrics and label the resulting grade/probability as an estimate.
- If the official course rubric cannot be obtained, score general project quality only. Mark requirement compliance as **not evaluated** and do not imply an exact official grade.
- Treat evaluation as read-only. Do not fix, publish, change visibility, rewrite history, or regenerate committed artifacts unless separately asked.

### 2. Separate the three repository states

Never collapse these states:

1. **Working tree** — includes uncommitted files and is relevant to the developer's current build.
2. **Committed HEAD** — the reproducible local revision.
3. **Remote/public artifact** — what reviewers or users can actually access.

Report material differences. Do not credit the remote artifact for uncommitted improvements. If the repository is private, do not call it an active open-source project merely because it has an OSI license.

### 3. Collect evidence

Run:

```bash
python <skill-dir>/scripts/collect_evidence.py <repo-root> --pretty
```

Then inspect only the files needed to verify the findings:

- README, license, contributing/security documents, changelog, release metadata
- course specification and report source/PDF
- data selection and preprocessing code
- core algorithms and their configuration
- experiment, evaluation, statistics, and visualization scripts
- committed metrics, logs, tables, and figures
- dependency files, package metadata, tests, CI, lint/type-check configuration

The collector reports local Git evidence only; it does not prove public visibility, adoption, branch protection, security configuration, or CI health. For remote GitHub evidence, prefer `gh repo view`, `gh run list`, `gh release list`, and direct repository pages. Verify at least visibility, stars/forks, releases, recent workflow status, and accessible community/security surfaces when scoring the OSS lane. Record URLs and the observation date. If remote access fails, mark these fields unknown rather than zero.

### 4. Validate execution claims

- Run syntax/import checks, existing tests, and the smallest meaningful smoke experiment. By default, time-box the smoke path to five minutes and one minimal input; stop cleanly and report partial validation if a longer benchmark is required.
- When safe and proportionate, rerun the primary CPU experiment and compare regenerated summaries to committed outputs.
- If the working tree is dirty, test committed HEAD in a verified temporary Git worktree rather than modifying user files.
- Verify temporary paths are inside an intended temp directory before removal.
- Do not claim GPU, external-service, or full-dataset reproducibility when those paths were not executed.
- Record commands, exit status, runtime failures, and metric differences.
- A syntax pass is not proof of runtime correctness; execute documented entry points that contain top-level setup. Do not treat an arbitrary package-level symbol probe as a failure unless that symbol is part of the documented public API.

### 5. Run independent review lanes

When subagents are available and the task warrants a full audit, run up to three independent lanes:

- **Course reviewer:** compliance, implementation, experiments, report, demonstration risk, predicted grade.
- **Adversarial paper reviewer:** novelty, protocol validity, leakage, baselines, ablations, statistics, related work, anonymity, venue decision.
- **OSS evaluator:** community, maintenance, security, documentation, adoption, code quality, data/license/release risk.

Give each lane raw repository context and its scope, not the expected conclusion. The main agent must independently verify decisive findings before synthesis.

### 6. Apply adversarial checks

Actively test for:

- convenience sampling, class/size bias, benchmark leakage, GT-derived inputs, and tuning on the evaluation set
- unequal perturbation severity, incompatible conditions, inadequate trials, and unreported failure cases
- weak or missing baselines, component ablations, efficiency measurements, and cross-dataset/model validation
- multiple testing without correction, pseudo-replication, post-hoc hypotheses, and tautological oracle comparisons
- novelty claims that overlap existing literature; search primary papers and official proceedings
- README/report claims that disagree with executable code, dependencies, committed outputs, or remote state
- anonymous-review leaks in author fields, URLs, Git history, PDF metadata, filenames, and searchable exact results
- third-party dataset/model redistribution that the repository license cannot grant
- tests that pass only in the current environment because dependency ranges contradict used APIs

### 7. Score and calibrate

- Use `references/rubrics.md`; show subscores and evidence.
- Give a central estimate, a reasonable interval, confidence, and the assumptions that drive the interval.
- Distinguish mandatory deliverable completion, scientific completeness, and engineering/release completeness.
- Publication probabilities are judgment calls, not venue base rates. Give them only when requested, name the assumed venue tier, and use the broad calibration in the rubric.
- Apply rubric caps unless strong contrary evidence is documented.

### 8. Report the result

Lead with a compact verdict table:

| Target | Current level | Score or range |
| --- | --- | ---: |
| Course project | ... | ... |
| Real paper submission | ... | ... |
| Open-source project | ... | ... |

Then include:

1. evaluation scope and exact revision/state
2. verified strengths
3. decisive blockers, ordered by impact
4. course score breakdown
5. paper decision and realistic venue tier
6. OSS six-dimension score
7. concrete runtime/reproducibility findings
8. the smallest next goal that removes the highest-risk blocker

Use clickable local file links with exact line numbers and web links for external evidence. Clearly distinguish observed facts from inferences.

## Guardrails

- Never equate a strong course project with a publishable paper.
- Never equate a polished README with mature software.
- Never equate statistical significance with an unbiased protocol.
- Never describe a private repository as publicly adopted open source.
- Never call a composition literature-first without a related-work search.
- Never hide a failed command behind successful committed output.
- Do not average the three headline scores into one meaningless total.
