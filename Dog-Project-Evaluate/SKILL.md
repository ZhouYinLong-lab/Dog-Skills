---
name: Dog-Project-Evaluate
description: >
  三通道独立评估研究项目：课程作业完成度评分、论文投稿水平判定、开源项目成熟度审计。
  输出含结论总表、分项评分、证据引用、决定性阻断项和升级路线图。
  Trigger: 评估项目, 完成度, 大作业评分, 论文投稿, 开源成熟度, 能投什么会议,
  仓库水平, 这个项目什么水平, evaluate project, course assignment, capstone,
  paper readiness, OSS maturity, repository audit, venue recommendation,
  acceptance probability, 毕业论文评估, 研究原型评估.
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

Lead with a one-line overall verdict, then a compact verdict table, followed by detailed sections.

#### 8.1 Opening verdict (one line)

> 这是一份[强度等级]的[类型]课程研究项目，但还不是可以投[领域]会议的研究论文，也还不能算成熟开源项目。

#### 8.2 Verdict table

| 评价对象 | 当前水平 | 评分/概率 |
| --- | --- | ---: |
| 课程硬性要求完成度 | [完成状态] | [百分比] |
| 课程大作业综合质量 | [等级] / [档位] | [分数]/100，合理区间 [low]–[high] |
| 外部论文投稿 | [当前定位] | [分数]/10，[Decision] |
| 顶会主会 | [竞争力判断] | [概率] |
| 相关正式 Workshop | [竞争力判断] | [概率] |
| 开源成熟度 | [状态描述] | [分数]/100 |
| 原样公开后的水平 | [公开后定位] | 约 [分数]/100 |

#### 8.3 Tools used

List any skills or external sources consulted during this evaluation (e.g., find-skills, superpowers, repo-evaluator, adversarial-review), with version/stars context where relevant.

#### 8.4 Completion status and overall level

- Summarize what the official requirements demand and whether each was met (with evidence of over-delivery where applicable).
- Report the smoke-test result: exact commit, environment, commands run, metrics reproduced, and whether outputs matched.
- Give the overall positioning statement.

#### 8.5 Course score breakdown

Table with per-dimension scores matching the rubric, followed by rationale for each deduction. Distinguish "content is insufficient" from "content is solid but missing specific dimensions."

If the official rubric differs, map its dimensions explicitly.

#### 8.6 Real submission level

State the bottom line directly (e.g., "直接投 CVPR/ICCV/ECCV/NeurIPS/ICML/ICLR 会是 Strong Reject").

Venue-tier probability table:

| 投稿层级 | 当前接收概率 |
| --- | ---: |
| 顶会主会 (list specific venues) | <1% |
| 二线会议主会 (list specific venues) | 1–5% |
| 相关 Workshop 正式短文 | 5–15% |
| 学生论坛 / 课程 Workshop / 非正式 Poster | 40–70% |
| arXiv / OpenReview Preprint | 可发布，不代表同行评审认可 |

Decisive rejection points — each with:
- Concrete evidence (file links with line numbers, web links)
- Why this alone could cause rejection
- What would be needed to address it

Include at minimum: sample representativeness, noise protocol fairness, novelty overlap, baseline/ablation gaps, parameter tuning on test set, statistical over-interpretation, and double-blind risks.

Identify the single most promising paper direction if developed further.

#### 8.7 Open-source maturity

Six-dimension score table:

| 维度 | 分数 |
| --- | ---: |
| 社区健康 | xx/100 |
| 维护性 | xx/100 |
| 安全性 | xx/100 |
| 文档质量 | xx/100 |
| 采纳度 | xx/100 |
| 代码质量 | xx/100 |
| **综合** | **xx/100** |

Current status summary (visibility, stars/forks/issues/PRs, releases, Bus Factor, CI, packaging).
Public-release readiness: score if the repo were made public today, with specific risks flagged (e.g., tracked dataset files with incompatible licenses).

#### 8.8 Concrete runtime errors found

If any execution errors were discovered during validation, list each with:
- Exact file and line number (clickable local links)
- The error type and root cause
- The fix needed

#### 8.9 Upgrade roadmap

Three-tier prioritization:

1. **课程提交前 (before submission):** smallest fixes that remove immediate blockers.
2. **外部投稿前 (before paper submission):** what a credible paper requires.
3. **真正开源前 (before OSS release):** what mature open-source software requires.

#### 8.10 Output conventions

- Use clickable local file links with exact line numbers and web links for external evidence.
- Clearly distinguish observed facts from inferences.
- State exact date, repository revision, working-tree cleanliness, which commands were actually executed, and which paths were not executed (GPU/network/full-dataset).
- Do not present estimated acceptance probabilities with more than one significant digit unless a venue-specific model is available.
- Central score, plausible interval, and confidence on every headline number.
- The one next objective with the greatest expected score/risk improvement.

## Guardrails

- Never equate a strong course project with a publishable paper.
- Never equate a polished README with mature software.
- Never equate statistical significance with an unbiased protocol.
- Never describe a private repository as publicly adopted open source.
- Never call a comparison literature-first without a related-work search.
- Never hide a failed command behind successful committed output.
- Do not average the three headline scores into one meaningless total.
