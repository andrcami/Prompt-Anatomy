# Prompt Anatomy

[![Validate](https://github.com/andrcami/prompt-anatomy/actions/workflows/validate.yml/badge.svg)](https://github.com/andrcami/prompt-anatomy/actions/workflows/validate.yml) [![Latest release](https://img.shields.io/github/v/release/andrcami/prompt-anatomy)](https://github.com/andrcami/prompt-anatomy/releases/latest) [![Validation report](https://img.shields.io/badge/validation-report-blue)](validation/) [![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A skill that turns vague requests into strong prompts.

Suppose you ask an AI something broad like *"find me the prices of cars in Malta"*. Prompt Anatomy steps in with **a few targeted questions** (at most two short rounds): buying or selling? new or used? budget? what format? Each question comes with choices and a recommended default, so you can answer in seconds. It then gives you:

1. **A refined, well-structured prompt** formatted for the AI you're using (Claude, ChatGPT, Grok, Gemini and others)
2. **A named model and mode** (for example, "Claude Sonnet 5.5 + web search, because prices change daily")
3. **The assumptions it made**, then a checkpoint: run it here, run it on the recommended model, compare two models, adjust first, or just take the prompt

It also reviews and rewrites prompts you already have, and it stays out of the way when your request is already specific or you say "just answer".

It's built on the published guidance from [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) and [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api), and on the acronym frameworks popularised for Grok ([Sarah Morino, Medium](https://medium.com/@SarahMorino/how-to-master-the-grok-prompt-framework-12-proven-structures-for-better-ai-results-62400ace9fd0)).

## The anatomy

| # | Element | Pins down |
|---|---------|-----------|
| 1 | Goal | What you want, and what decision it serves |
| 2 | Context | Who you are, background, what you tried |
| 3 | Specifics | Location, dates, budget, data |
| 4 | Role / audience | The expert lens, and who reads the result |
| 5 | Constraints | Rules, sources, tone, length |
| 6 | Output format | Table, bullets, email, code |
| 7 | Examples | What good looks like |
| 8 | Success criteria | How you'll judge the result |

## Repository layout

```
.claude-plugin/marketplace.json      # The "andrcami-skills" marketplace (lists the plugins below)
plugins/prompt-anatomy/              # The Claude Code / Claude plugin
  .claude-plugin/plugin.json         # Plugin manifest (+ icon.png)
  README.md                          # What it does, model-ladder sources, what's Claude-only
  skills/prompt-anatomy/             # The skill itself (Agent Skills format)
    SKILL.md                         # Core workflow
    references/anatomy.md            # Deep guide + question banks by task type
    references/platforms.md          # Formatting + model ladder/tiers per platform
    references/frameworks.md         # APE, RACE, CO-STAR, RISEN, CRISPE, ...
    references/examples.md           # Before/after examples
  evals/                             # Test cases (claude plugin eval)
portable/
  system-prompt.md                   # Paste-in version for custom GPTs, Gems, Grok/Claude Projects
  custom-instructions-short.txt      # Under 1,500 chars, for custom-instruction boxes
INSTALL.md / PUBLISHING.md           # Install + store submission guides
scripts/build.sh                     # Builds dist/prompt-anatomy.zip + dist/portable/
scripts/validate.sh                  # Runs every release check and writes a report
validation/                          # Validation reports for each release
.github/workflows/                   # Validate on every push; Release on v* tags
```

## Installation

**Full step-by-step guide: [INSTALL.md](INSTALL.md)**

- **Claude (web, desktop, mobile):** Settings → Capabilities → Skills → upload `prompt-anatomy.zip`
- **Claude Code:** `/plugin marketplace add andrcami/prompt-anatomy`, then `/plugin install prompt-anatomy@andrcami-skills`
- **Grok:** Settings → Skills → New Skill → upload `prompt-anatomy.zip` (same skill as Claude)
- **ChatGPT, Gemini:** paste [`portable/system-prompt.md`](portable/system-prompt.md) into a custom GPT, Project or Gem, or paste [`portable/custom-instructions-short.txt`](portable/custom-instructions-short.txt) into your custom instructions

Publishing to the stores and directories: see [PUBLISHING.md](PUBLISHING.md).

## Keeping model recommendations fresh

On Claude, the skill follows a model ladder based on Anthropic's own guidance (the Claude Enterprise consumption guide on support.claude.com, and "Choosing a model" on platform.claude.com): Haiku for simple work, **Sonnet by default**, Opus for multi-step work with linked decisions, Fable for the hardest. On other platforms it recommends by tier (top reasoning / default / fast).

Model names change every few months, so pick the newest model in each tier. `references/platforms.md` carries a "last reviewed" date. When a provider ships new models, update the tables there and the date.

## Testing

Test cases live in `plugins/prompt-anatomy/evals/`. With Claude Code you can run them:

```
claude plugin eval plugins/prompt-anatomy
```

## License

[MIT](LICENSE) © 2026 andrcami. You're free to use, modify and share this skill, including commercially, as long as the copyright and licence notice stays with every copy or modified version.
