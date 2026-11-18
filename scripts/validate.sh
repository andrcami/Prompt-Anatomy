#!/usr/bin/env bash
# Runs every release check and writes a report to the folder given (default: validation/latest).
#   1. claude plugin validate (marketplace, strict)
#   2. claude plugin validate (plugin, strict, Anthropic directory profile)
#   3. ./scripts/build.sh
#   4. NVIDIA SkillEvaluator Tier 1 (static checks, no LLM)
#   5. Optional: claude plugin eval (RUN_EVALS=1), or attach an existing run (EVALS_JSON=path)
# Exits non-zero if a check fails. See scripts/validation_summary.py for the gate rules.
# Needs: claude (Claude Code CLI) and skillevaluator on PATH, or set CLAUDE_BIN / SKILLEVALUATOR_BIN.
set -uo pipefail
cd "$(dirname "$0")/.."
OUT="${1:-validation/latest}"
CLAUDE_BIN="${CLAUDE_BIN:-claude}"
SE_BIN="${SKILLEVALUATOR_BIN:-skillevaluator}"
SKILL=plugins/prompt-anatomy/skills/prompt-anatomy
rm -rf "$OUT" && mkdir -p "$OUT/logs"

run() {  # run <id> <command...>: log output, record exit code
  local id=$1; shift
  "$@" >"$OUT/logs/$id.log" 2>&1; echo $? >"$OUT/logs/$id.exit"
  echo "$id: exit $(cat "$OUT/logs/$id.exit")"
}
run marketplace "$CLAUDE_BIN" plugin validate . --strict
run plugin      "$CLAUDE_BIN" plugin validate plugins/prompt-anatomy --strict --profile directory
run build       ./scripts/build.sh
run skillevaluator "$SE_BIN" tier1 "$SKILL" --no-llm -r json,markdown -o "$OUT/skillevaluator"

# Optional: live evals (real model runs, billed). Set RUN_EVALS=1; needs Claude credentials.
if [ "${RUN_EVALS:-0}" = "1" ]; then
  run evals "$CLAUDE_BIN" plugin eval plugins/prompt-anatomy --trust-plugin -j "${EVAL_CONCURRENCY:-4}" --json "$OUT/evals.json"
elif [ -n "${EVALS_JSON:-}" ] && [ -f "$EVALS_JSON" ]; then
  cp "$EVALS_JSON" "$OUT/evals.json"   # reuse a recent local eval run
fi

{ "$CLAUDE_BIN" --version 2>/dev/null | head -1; "$SE_BIN" --version 2>/dev/null | head -1; } >"$OUT/logs/versions.txt"
python3 scripts/validation_summary.py "$OUT"
