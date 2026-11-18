# Validation report: Prompt Anatomy v1.1.0

**Result: ✅ PASSED** · commit `b1d2bb6` · 2026-11-18 20:01 UTC
Run by: GitHub Actions, run 44386331584 · Tools: 2.1.327 (Claude Code) · skillevaluator, version 1.0.1

| Check | Result |
|---|---|
| Marketplace manifest (`claude plugin validate . --strict`) | ✅ pass |
| Plugin, directory profile (`claude plugin validate plugins/prompt-anatomy --strict --profile directory`) | ✅ pass |
| Build (`./scripts/build.sh`) | ✅ pass |
| NVIDIA SkillEvaluator Tier 1: quality **89.0/100 (B)**, 0 critical, 0 high, 3 medium, 9 low (tolerated tool error: skillspector) | ✅ pass |
| Live evals (`claude plugin eval`): **7/7 cases** pass with the skill, mean lift over no skill +0.22 | ✅ pass |

## Live evals

Run 2026-11-18T19:51:18.019Z on 2.1.327, 3 runs per case with and without the skill.

| Case | With skill | Without | Runs passed (with) |
|---|---|---|---|
| boat-purchase-fires | 1.00 | 1.00 | 3/3 |
| grok-sentiment-defaults | 1.00 | 0.75 | 3/3 |
| improve-chatgpt-prompt | 1.00 | 0.67 | 3/3 |
| linkedin-prompt-delivery | 1.00 | 0.25 | 3/3 |
| specific-email-no-questions | 1.00 | 1.00 | 3/3 |
| vague-car-prices-malta | 1.00 | 0.80 | 3/3 |
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
