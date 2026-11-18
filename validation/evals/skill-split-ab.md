# A/B check: splitting SKILL.md into reference files (2026-11-18)

**Why:** NVIDIA SkillEvaluator flagged SKILL.md as too long (about 22,600 characters, against a recommended limit of about 15,000) and missing some standard sections. SKILL.md was cut to about 15,500 characters. Reference material moved to `references/running.md`, `references/troubleshooting.md` and `references/anatomy.md` §1 and §6. Every rule the skill applies on every request stayed in SKILL.md.

**Quality score (SkillEvaluator Tier 1):** 89.0 (B) → **98.8 (A)**.

**Did behaviour change?** The two most format-sensitive cases were run 9 times each, on the released v1.1.0 SKILL.md and on the split version (Claude Code 2.1.327, eval model Sonnet 5.5):

| Case | v1.1.0 (released) | Split version |
|---|---|---|
| boat-purchase-fires (≤4 boat-specific questions) | 8/9 runs fully pass (mean 0.96) | **9/9** (mean 1.00) |
| vague-car-prices-malta (asks first, ≤4 specific questions with defaults, no platform question) | 9/9 (1.00) | **9/9** (1.00) |

**Full suite on the split version** (`latest.json`): 19/21 runs pass. Every case passes in at least 2 of its 3 runs, and the mean lift over no skill is +0.29 (v1.1.0's run: +0.22). The two single-run misses (one 5-item question list, one early answer) didn't recur in the 18 extra runs above.

**Triggering** (`claude -p`, the plugin installed next to many other skills): fired on "boat purchase", "car in Malta purchase", "plan a trip to Sicily", "gift ideas…", "make me a prompt…, skip the questions" and "which AI model should I use…". Didn't fire on the VAT rate, "thanks" or a fully specified Yaris request. On "write a LinkedIn post", a dedicated LinkedIn skill in the same environment competes: the split version won 2 of 4 runs, against 0 of 4 for v1.1.0. The description now puts *when to use* first.
