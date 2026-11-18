"""Writes <out>/SUMMARY.md and status.json from scripts/validate.sh output, and exits 1 if a gate fails.

Gate rules:
- Both `claude plugin validate` runs and the build must exit 0.
- SkillEvaluator Tier 1: no validator may fail, there must be no high or critical
  finding, and the quality score must be >= 70. A scan may be "incomplete" only if it's
  a known tool-side error listed in TOLERATED_INCOMPLETE. That's reported, never hidden.
"""
import json, os, subprocess, sys, datetime, pathlib

TOLERATED_INCOMPLETE = {"skillspector"}  # its JSON self-check errors on skills with no code (SkillEvaluator 1.0.1)
out = pathlib.Path(sys.argv[1])
ex = lambda i: int((out / "logs" / f"{i}.exit").read_text().strip())
checks, ok = [], True

for cid, label in [("marketplace", "Marketplace manifest (`claude plugin validate . --strict`)"),
                   ("plugin", "Plugin, directory profile (`claude plugin validate plugins/prompt-anatomy --strict --profile directory`)"),
                   ("build", "Build (`./scripts/build.sh`)")]:
    passed = ex(cid) == 0
    ok &= passed
    checks.append((label, "✅ pass" if passed else "❌ fail"))

se_json = out / "skillevaluator" / "skillevaluator-tier1.json"
se = {}
if se_json.exists():
    d = json.loads(se_json.read_text())
    sev = d.get("severity_counts", {})
    failed = [r.get("validator") for r in d.get("results", []) if r.get("status") == "failed"]
    incomplete = set(d.get("incomplete_scans") or [])
    q = (d.get("quality_summary") or [{}])[0]
    score = q.get("overall_score", 0)
    se_pass = (not failed and sev.get("critical", 0) == 0 and sev.get("high", 0) == 0
               and score >= 70 and incomplete <= TOLERATED_INCOMPLETE)
    se = {"status": d.get("overall_status"), "quality_score": score, "grade": q.get("grade"),
          "severity_counts": sev, "failed_validators": failed, "incomplete_scans": sorted(incomplete),
          "validators": {r.get("validator"): r.get("status") for r in d.get("results", [])}}
    note = f" (tolerated tool error: {', '.join(sorted(incomplete))})" if incomplete else ""
    checks.append((f"NVIDIA SkillEvaluator Tier 1: quality **{score}/100 ({q.get('grade')})**, "
                   f"{sev.get('critical',0)} critical, {sev.get('high',0)} high, {sev.get('medium',0)} medium, {sev.get('low',0)} low{note}",
                   "✅ pass" if se_pass else "❌ fail"))
    ok &= se_pass
else:
    checks.append(("NVIDIA SkillEvaluator Tier 1 (no report produced)", "❌ fail"))
    ok = False

ev = None
if (out / "evals.json").exists():
    e = json.loads((out / "evals.json").read_text())
    agg = e.get("aggregates", {})
    rows = []
    for c in e.get("cases", []):
        arm = lambda n: [r["score"] for r in c["arms"].get(n, [])]
        w, wo = arm("with"), arm("without")
        mean = lambda xs: sum(xs) / len(xs) if xs else None
        rows.append((c["name"], mean(w), mean(wo), sum(r["passed"] for r in c["arms"].get("with", [])), len(w)))
    ev_pass = agg.get("casesPassed") == agg.get("casesTotal") and not e.get("partial")
    ok &= ev_pass
    ev = {"cases_passed": agg.get("casesPassed"), "cases_total": agg.get("casesTotal"), "mean_delta": agg.get("meanDelta"),
          "cost_usd": e.get("costUsd"), "started_at": e.get("startedAt"), "claude_version": e.get("claudeVersion")}
    checks.append((f"Live evals (`claude plugin eval`): **{agg.get('casesPassed')}/{agg.get('casesTotal')} cases** pass with the skill, "
                   f"mean lift over no skill {agg.get('meanDelta', 0):+.2f}", "✅ pass" if ev_pass else "❌ fail"))

def git(*a):
    try: return subprocess.check_output(["git", *a], text=True).strip()
    except Exception: return "unknown"
version = json.loads(pathlib.Path("plugins/prompt-anatomy/.claude-plugin/plugin.json").read_text())["version"]
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
tools = (out / "logs" / "versions.txt").read_text().strip().replace("\n", " · ") if (out / "logs" / "versions.txt").exists() else ""

lines = [f"# Validation report: Prompt Anatomy v{version}", "",
         f"**Result: {'✅ PASSED' if ok else '❌ FAILED'}** · commit `{git('rev-parse', '--short', 'HEAD')}` · {now}",
         f"Run by: {os.environ.get('VALIDATION_RUNNER', 'local')} · Tools: {tools}", "",
         "| Check | Result |", "|---|---|", *[f"| {c} | {r} |" for c, r in checks], ""]
if ev is not None:
    f = lambda x: "n/a" if x is None else f"{x:.2f}"
    lines += ["## Live evals", "", f"Run {ev['started_at']} on {ev['claude_version']}, 3 runs per case with and without the skill.", "",
              "| Case | With skill | Without | Runs passed (with) |", "|---|---|---|---|",
              *[f"| {n} | {f(w)} | {f(wo)} | {p}/{k} |" for n, w, wo, p, k in rows], ""]
if se:
    lines += ["## SkillEvaluator validators", "", "| Validator | Status |", "|---|---|",
              *[f"| {k} | {v} |" for k, v in se["validators"].items()], "",
              "The full findings are in [`skillevaluator/skillevaluator-tier1.md`](skillevaluator/skillevaluator-tier1.md). "
              "Command logs are in [`logs/`](logs/)."]
(out / "SUMMARY.md").write_text("\n".join(lines) + "\n")
(out / "status.json").write_text(json.dumps({"passed": ok, "version": version, "commit": git("rev-parse", "HEAD"),
                                             "generated_at": now, "checks": dict(checks), "skillevaluator": se, "evals": ev}, indent=2) + "\n")
print("\n".join(lines[:10 + len(checks)]))
sys.exit(0 if ok else 1)
