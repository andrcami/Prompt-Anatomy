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
scripts/build.sh               # Builds dist/prompt-anatomy.zip + dist/portable/
```

## Installation

Run `./scripts/build.sh` first to create `dist/prompt-anatomy.zip`.

### Claude (claude.ai, desktop and mobile apps)
1. Make sure skills are enabled: **Settings → Capabilities** (the exact menu names can vary by plan and version).
2. Upload `dist/prompt-anatomy.zip` under **Skills**.
3. Optional but recommended: to make it kick in on *every* vague request, add this to your profile preferences or to a Project's instructions:
   > Before answering broad or underspecified requests, use the prompt-anatomy skill to ask me clarifying questions first, unless I say "just answer".

   Skills are triggered by the model's judgment. Simple-looking questions ("car prices in Malta") sometimes get answered directly without the skill, and this line makes the behavior consistent.

### Claude Code
Pick one of these:
- **As a plugin:**
  ```
  /plugin marketplace add andrcami/prompt-anatomy
  /plugin install prompt-anatomy@prompt-anatomy
  ```
- **As a personal skill:** `cp -r skills/prompt-anatomy ~/.claude/skills/`
- **For one project:** `cp -r skills/prompt-anatomy .claude/skills/`

Invoke it explicitly with `/prompt-anatomy`, or let it trigger automatically. For always-on behavior, add the line from step 3 above to your `CLAUDE.md`.

### Other tools that support Agent Skills (`SKILL.md`)
A growing number of coding agents read the same `SKILL.md` format (for example, OpenAI Codex reads `~/.codex/skills/`). Copy `skills/prompt-anatomy/` into that tool's skills folder. Check its docs for the exact path.

### ChatGPT (OpenAI)
- **Custom GPT (best):** Explore GPTs → Create → Configure → paste `portable/system-prompt.md` into **Instructions**. Turn on Web Search. You can also upload the `references/*.md` files as Knowledge.
- **Project:** paste `portable/system-prompt.md` into the project instructions.
- **Everywhere:** Settings → Personalization → Custom instructions → paste `portable/custom-instructions-short.txt`.

### Grok (xAI)
- **Project:** create a Project and paste `portable/system-prompt.md` as its instructions.
- **Everywhere:** Settings → Customize / Custom Instructions → paste `portable/custom-instructions-short.txt`.

### Gemini (Google)
- **Gem:** Gems → New Gem → paste `portable/system-prompt.md` into the instructions. You can upload the reference files as knowledge.

### Anything else (API system prompts, Copilot, Perplexity, local models)
Use `portable/system-prompt.md` as the system prompt or custom instructions.

## Keeping model recommendations fresh

Model line-ups change every few months. `references/platforms.md` recommends by **tier** (top reasoning / default / fast) and carries a "last reviewed" date. When a provider ships new models, update the tables there and the date.

## Testing

Test cases live in `skills/prompt-anatomy/evals/`. With Claude Code you can run them:

```
cd skills/prompt-anatomy && claude plugin eval .
```

## License

[MIT](LICENSE) © 2026 andrcami. You're free to use, modify and share this skill, including commercially, as long as the copyright and licence notice stays with every copy or modified version.
