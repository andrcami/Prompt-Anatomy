## What and why

<!-- What does this change, and what problem does it solve? Link an issue if there is one. -->

## What it touches

- [ ] The skill (`plugins/prompt-anatomy/skills/`)
- [ ] References (anatomy, platforms/model ladder, frameworks, examples)
- [ ] Portable prompts (`portable/`)
- [ ] Evals, scripts, workflows or docs

## Checks

- [ ] Both `claude plugin validate` commands in CONTRIBUTING.md pass
- [ ] For changes to the skill or references: ran the affected evals (`claude plugin eval plugins/prompt-anatomy`), and here is the result
- [ ] Portable prompts updated to match, if behaviour changed
- [ ] No real personal or client data in examples or evals
- [ ] Bumped `version` in `plugins/prompt-anatomy/.claude-plugin/plugin.json` if installed copies need the change
