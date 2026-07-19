# Research Project Evaluation Rubrics

## Contents

1. Evidence standard
2. Completion dimensions
3. Course-project score
4. Paper-submission score
5. Open-source maturity score
6. Default caps
7. Output calibration

## 1. Evidence standard

Use four evidence classes:

| Class | Meaning | Examples |
| --- | --- | --- |
| Verified execution | Directly run in this audit | test logs, regenerated metrics, entry-point failure |
| Repository observation | Directly inspected | code line, committed file, Git status |
| External primary source | Official/current evidence | course page, venue policy, paper, API docs |
| Inference | Reasoned but not directly observed | expected grade, acceptance probability |

For every decisive positive or negative finding, provide at least one verifiable source. Label inference and confidence explicitly.

## 2. Completion dimensions

Report completion in three separate percentages:

- **Deliverable completion:** mandatory requested artifacts exist and are internally consistent.
- **Scientific completion:** protocol, baselines, ablations, statistical validity, and generalization support the claims.
- **Engineering completion:** clean install, tests, CI, packaging, release, and external reproducibility.

Do not average them unless the user asks for a single project-management completion number.

## 3. Course-project score

Default 100-point rubric when no official rubric exists:

| Dimension | Weight | Full-credit standard |
| --- | ---: | --- |
| Problem definition and requirement fit | 10 | Clear task, correct benchmark, explicit objective |
| Algorithm implementation | 20 | Substantive implementation, not a thin wrapper; correct and readable |
| Experimental completeness | 20 | Relevant baselines, metrics, sufficient cases, reproducible results |
| Analysis and rigor | 15 | Failure analysis, uncertainty, limitations, claims match evidence |
| Technical report | 15 | Required language/template, coherent method/results, adequate citations |
| Reproducibility | 10 | Setup and primary pipeline verified from a clean or isolated revision |
| Code quality | 5 | Modular code, tests or checks, reasonable dependency management |
| Submission/demo risk | 5 | Required files, stable entry point, identity/template/deadline compliance |

Score bands:

- 95–100: exceptional course research artifact
- 90–94: excellent / A range
- 85–89: strong / A- or high B+ range
- 80–84: solid but incomplete research execution
- 70–79: meets basics with major gaps
- below 70: incomplete or unreliable

Use the institution's actual grade mapping when known. If peer review or presentation is unknown, widen the interval by at least 3 points.

## 4. Paper-submission score

Score each dimension from 0–10:

| Dimension | Weight |
| --- | ---: |
| Novelty and literature positioning | 20% |
| Technical soundness/depth | 20% |
| Experimental validity | 25% |
| Significance and likely impact | 15% |
| Writing and presentation | 10% |
| Reproducibility and artifact quality | 10% |

Decision calibration:

- 8.0–10: strong accept territory
- 7.0–7.9: accept territory
- 6.0–6.9: weak accept / competitive borderline
- 5.0–5.9: borderline
- 4.0–4.9: weak reject
- below 4.0: reject / strong reject

If the user explicitly asks for an acceptance probability, first name the assumed venue tier and then use these deliberately broad judgment ranges as a starting point:

| Review territory | Conditional probability heuristic |
| --- | ---: |
| Strong accept | 40–70% |
| Accept | 25–50% |
| Weak accept | 10–30% |
| Borderline | 5–20% |
| Weak reject | 1–10% |
| Reject / strong reject | <1–5% |

These are not venue base rates or statistically fitted forecasts. Move the range downward for desk-reject risks, incomplete anonymity, out-of-scope contributions, or evidence that was not independently reproduced. If no venue tier is specified, prefer a venue-level judgment over a numeric probability.

Venue calibration must consider contribution type:

- **Main conference:** substantial novelty plus broad, strong empirical support.
- **Workshop paper:** focused insight can suffice, but protocol and comparisons must still be credible.
- **Student forum/demo:** implementation and analysis may be the primary contribution.
- **Preprint:** uploadability is not peer-review quality.

## 5. Open-source maturity score

Use six equal dimensions; score each 0–100 and report the arithmetic mean:

| Dimension | What to inspect |
| --- | --- |
| Community health | contributors, bus factor, issues/PRs, templates, conduct, external participation |
| Maintainability | activity period, release cadence, issue response, roadmap, versioning |
| Security | policy, private reporting, dependency scanning, code/secret scanning, protection rules |
| Documentation | README, setup, API/user docs, troubleshooting, examples, changelog |
| Adoption | visibility, stars/forks/watchers, downloads, releases, downstream users/citations |
| Code quality | tests, CI, coverage, typing, linting, packaging, dependency locking, architecture |

Maturity bands:

- 85–100: mature, broadly trusted OSS
- 75–84: strong maintained OSS
- 60–74: credible research OSS / usable early project
- 45–59: promising prototype with release gaps
- 30–44: early research artifact
- below 30: private/internal or incomplete artifact

## 6. Default caps

Apply these caps unless strong contrary evidence is documented:

- Course reproducibility ≤ 5/10 when the documented main path fails.
- Paper experimental validity ≤ 4/10 when a non-random subset below 5% of the benchmark supports broad claims without external validation.
- Paper novelty ≤ 4/10 when no targeted related-work search or direct comparison exists.
- Paper reproducibility ≤ 5/10 when the evaluated revision cannot be identified or rerun.
- OSS adoption ≤ 10/100 when the repository is private or inaccessible to intended users.
- OSS code quality ≤ 40/100 when both automated tests and CI are absent.
- OSS maturity cannot exceed 59 when third-party data redistribution or licensing is unresolved.

Caps are safeguards, not substitutes for reasoning. Explain every applied or overridden cap.

## 7. Output calibration

Always state:

- exact date and repository revision
- working-tree cleanliness
- which commands were actually executed
- which GPU/network/full-dataset paths were not executed
- central score, plausible interval, and confidence
- the one next objective with the greatest expected score/risk improvement

Do not present estimated acceptance probabilities with more than one significant digit unless a venue-specific model is available.
