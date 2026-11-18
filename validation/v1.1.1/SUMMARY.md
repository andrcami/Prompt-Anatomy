# Validation report: Prompt Anatomy v1.1.1

**Result: ✅ PASSED** · commit `cbff621` · 2026-11-18 20:39 UTC
Run by: GitHub Actions, run 44393178186 · Tools: 2.1.327 (Claude Code) · skillevaluator, version 1.0.1

| Check | Result |
|---|---|
| Marketplace manifest (`claude plugin validate . --strict`) | ✅ pass |
| Plugin, directory profile (`claude plugin validate plugins/prompt-anatomy --strict --profile directory`) | ✅ pass |
| Build (`./scripts/build.sh`) | ✅ pass |
| NVIDIA SkillEvaluator Tier 1: quality **98.8/100 (A)**, 0 critical, 0 high, 0 medium, 2 low (tolerated tool error: skillspector) | ✅ pass |
| Live evals (`claude plugin eval`): **19/21 runs** pass with the skill; every case passes in at least 2 of 3 runs: yes; mean lift over no skill +0.29 | ✅ pass |

## Live evals

Run 2026-11-18T20:27:02.867Z on 2.1.327, 3 runs per case with and without the skill.

| Case | With skill | Without | Runs passed (with) |
|---|---|---|---|
| boat-purchase-fires | 0.89 | 0.78 | 2/3 |
| grok-sentiment-defaults | 1.00 | 0.75 | 3/3 |
| improve-chatgpt-prompt | 1.00 | 0.67 | 3/3 |
| linkedin-prompt-delivery | 1.00 | 0.08 | 3/3 |
| specific-email-no-questions | 1.00 | 1.00 | 3/3 |
| vague-car-prices-malta | 0.93 | 0.53 | 2/3 |
| vat-rate-no-fire | 1.00 | 1.00 | 3/3 |

## SkillEvaluator validators

| Validator | Status |
|---|---|
| Schema & Repository Governance | passed |
| Semantic Version Validation | passed |
| Security Scan | incomplete |
| PII Scan | passed |
| License Compliance | passed |
| Code Risk Analysis | passed |
| Secrets Detection | passed |
| Code Integrity & Hygiene | passed |
| Dependency Vulnerability Audit | passed |
| Unicode Smuggling Detection | passed |
| QUALITY | passed |
| SCRIPT_LINT | passed |
| Harness Compatibility | passed |

The full findings are in [`skillevaluator/skillevaluator-tier1.md`](skillevaluator/skillevaluator-tier1.md). Command logs are in [`logs/`](logs/).
