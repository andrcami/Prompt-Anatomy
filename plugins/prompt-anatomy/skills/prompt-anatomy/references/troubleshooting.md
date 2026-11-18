# Troubleshooting

Read this when the skill's behaviour looks wrong, or when the user reports a problem with it.

| Problem | Likely cause | Fix |
|---|---|---|
| It asked about the platform inside Claude or Grok | The platform wasn't inferred | Skip the platform question when it's obvious (Step 1) |
| It answered straight away instead of asking | The request looked specific, or "skip the questions" was read as "just answer" | Re-check Gate 2. A request for a *prompt* always gets the prompt kit |
| Round 1 had more than 4 items | An "Output" item or a merged question was added | Count every numbered item, with one topic each (Step 2) |
| No "Run it on" line, or a mode with no model | The delivery format was cut short | Keep the fixed order, and name a model *and* a mode (Steps 4–5) |
| It ran the prompt before the user confirmed | The checkpoint was skipped | Stop at the checkpoint unless the user said "just run it" |
| The result didn't match the agreed table or sections | It drifted from `<output_format>` | Follow it exactly, and note any deliberate deviation (`references/running.md`) |
| It recommended a model from another platform | The platform wasn't taken into account | Recommend the best option on the user's platform first (Step 4) |
| It asked a third round of questions | The round limit was ignored | Stop after 2 rounds and 7 questions; turn the rest into listed assumptions (Step 2) |
| A subagent's answer arrived in a later message | The turn ended while the subagent was still working | Wait for it, and post the result in the same reply (`references/running.md`) |
