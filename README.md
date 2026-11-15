# Prompt Anatomy

A skill that turns vague requests into strong prompts.

Suppose you ask an AI something broad like *"find me the prices of cars in Malta"*. Prompt Anatomy steps in with **one short round of targeted questions**: buying or selling? new or used? budget? what format? Each question comes with choices and a default, so you can answer in seconds. It then gives you:

1. **A refined, well-structured prompt** formatted for the AI you're using (Claude, ChatGPT, Grok, Gemini and others)
2. **A model and mode recommendation** (for example, "turn web search on, because prices change daily")
3. **The assumptions it made**, plus an offer to run the prompt straight away

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
skills/prompt-anatomy/         # The skill (Agent Skills format: SKILL.md + references)
  SKILL.md                     # Core workflow
  references/anatomy.md        # Deep guide + question banks by task type
  references/platforms.md      # Formatting + model tiers per platform
  references/frameworks.md     # APE, RACE, CO-STAR, RISEN, CRISPE, ...
  references/examples.md       # Before/after examples
  evals/                       # Test cases
portable/
  system-prompt.md             # Paste-in version for custom GPTs, Gems, Grok/Claude Projects (~4.7k chars)
  custom-instructions-short.txt# Under 1,500 chars, for ChatGPT/Grok custom-instruction boxes
.claude-plugin/                # Makes this repo a Claude Code plugin marketplace
INSTALL.md / PUBLISHING.md     # Install + store submission guides
scripts/build.sh               # Builds dist/prompt-anatomy.zip + dist/portable/
```

## Installation

**Full step-by-step guide: [INSTALL.md](INSTALL.md)**

- **Claude (web, desktop, mobile):** Settings → Capabilities → Skills → upload `prompt-anatomy.zip`
- **Claude Code:** `/plugin install prompt-anatomy --marketplace andrcami/prompt-anatomy`
- **ChatGPT, Grok, Gemini:** paste [`portable/system-prompt.md`](portable/system-prompt.md) into a custom GPT, Project or Gem, or paste [`portable/custom-instructions-short.txt`](portable/custom-instructions-short.txt) into your custom instructions

Publishing to the stores and directories: see [PUBLISHING.md](PUBLISHING.md).

## Keeping model recommendations fresh

Model line-ups change every few months. `references/platforms.md` recommends by **tier** (top reasoning / default / fast) and carries a "last reviewed" date. When a provider ships new models, update the tables there and the date.

## Testing

Test cases live in `skills/prompt-anatomy/evals/`. With Claude Code you can run them:

```
cd skills/prompt-anatomy && claude plugin eval .
```

## License

[MIT](LICENSE) © 2026 andrcami. You're free to use, modify and share this skill, including commercially, as long as the copyright and licence notice stays with every copy or modified version.
