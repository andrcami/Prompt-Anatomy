# Validation records

Every release is checked by [`scripts/validate.sh`](../scripts/validate.sh), and the results are kept here.

| Path | What it is |
|---|---|
| `validation/<version>/SUMMARY.md` | The report for that release: pass/fail per check, SkillEvaluator scores, eval results |
| `validation/<version>/status.json` | The same, machine-readable |
| `validation/<version>/skillevaluator/` | NVIDIA SkillEvaluator Tier 1 full report (Markdown + JSON) |
| `validation/<version>/logs/` | Raw output of every command |
| `validation/latest-status.json` | Status of the most recent release |
| `validation/evals/latest.json` | The most recent live eval run (`claude plugin eval`), summarised |

**How it's produced:** pushing a `v*` tag runs the [Release workflow](../.github/workflows/release.yml). It runs every check, publishes the GitHub Release only if they pass, and commits the report here. The [Validate workflow](../.github/workflows/validate.yml) runs the same checks on every push and pull request (see the badge in the main README).

**Checks:**
1. `claude plugin validate . --strict` (marketplace manifest)
2. `claude plugin validate plugins/prompt-anatomy --strict --profile directory` (Anthropic directory rules)
3. `./scripts/build.sh` (the installable zip builds)
4. NVIDIA SkillEvaluator 1.0.1, Tier 1: schema, PII, licence, secrets, Unicode, quality score (must be ≥ 70), harness compatibility. No high or critical findings allowed.
5. Live evals (`claude plugin eval`): run in CI when the `ANTHROPIC_API_KEY` secret exists. Otherwise the report attaches the last committed run from `validation/evals/latest.json` and shows its date.

**Known tool issue:** SkillEvaluator 1.0.1's bundled security scanner (`skillspector`) reports "incomplete" on skills that contain no code, because of an internal self-check error. The gate accepts that one case and the report always shows it. Every other scan must pass.

To run it yourself: `pip install skillevaluator==1.0.1`, then `./scripts/validate.sh validation/local`.
