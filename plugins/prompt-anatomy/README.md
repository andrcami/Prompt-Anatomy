# Prompt Anatomy

Turns vague requests into strong prompts. Ask something broad, like *"boat purchase"* or *"find me the prices of cars in Malta"*. Prompt Anatomy asks a few targeted questions, builds a well-structured prompt for your AI platform, recommends the right model and mode, and then runs the prompt once you confirm.

## How it works

1. **Decides whether to step in.** It steps in for any task missing two or more of: goal, context, specifics (place, budget, scope), constraints, or output format. Bare topics like "boat purchase" count. It stays out of the way for quick facts ("VAT rate in Malta"), chat, follow-ups that already have context, specific requests, or when you say "just answer".
2. **Asks at most two short rounds of questions.** Round 1 has up to 4 questions. Round 2 is optional, with up to 3 follow-ups built from your answers. Every question has choices with the recommended one first, and "defaults" skips the rest.
3. **Builds the prompt** for your platform: XML-style tags for Claude, Markdown or `###` delimiters for ChatGPT, labelled sections for Grok, headings for Gemini.
4. **Recommends a model and a mode**, with a one-line reason and a cheaper or deeper alternative.
5. **Checks with you before running.** Options: Run it here · Run on [recommended model] · Compare 2 models · Adjust first · Just the prompt. The answer comes back labelled **Result (model name)**.

It also reviews and rewrites prompts you already have.

## Example

> **You:** find me the prices of cars in Malta
>
> **Prompt Anatomy:** asks about buying or selling, new or used, budget and type, and the output you want (each with choices)
>
> **You:** buying, used, under €15k, automatic hatchback
>
> **Prompt Anatomy:** returns a copy-ready prompt (context / task / requirements / output format), plus *Run it on: Claude Sonnet 5.5 + web search: a single research question, and prices change daily*. Then: *Run it here, adjust first, or just the prompt?*

More examples are in [`skills/prompt-anatomy/references/examples.md`](skills/prompt-anatomy/references/examples.md).

## Install

**Claude Code**
```
/plugin marketplace add andrcami/prompt-anatomy
/plugin install prompt-anatomy@andrcami-skills
```

**Claude (web, desktop and mobile):** upload the skill zip under Settings → Capabilities → Skills. See the [full install guide](../../INSTALL.md), which also covers ChatGPT, Grok and Gemini.

## Where the model advice comes from

On Claude, the skill uses a model ladder based on Anthropic's own guidance:

| Tier | Use for |
|------|---------|
| Haiku | Simple, single-step, easy-to-check work |
| **Sonnet (default)** | Everyday writing, comparisons, single research questions |
| Opus | Multi-step work with linked decisions and trade-offs |
| Fable | The hardest research and long-running agentic work |

Sources: the Claude Enterprise consumption guide (support.claude.com: *"when in doubt, Sonnet"*) and "Choosing a model" / "Models overview" (platform.claude.com). The API docs suggest starting with Opus for most API workloads. This skill is mostly used in chat, so it follows the consumption guide and defaults to Sonnet.

Other platforms get generic tiers (top reasoning / default / fast). **Model names change often.** The skill names the tier and the current model it knows, and you should pick the newest model in that tier in your model picker.

## What works where

| Feature | Claude | Other platforms (ChatGPT, Codex, Grok, Gemini) |
|---------|--------|-----------------------------------------------|
| Question widget | Uses the built-in question tool | Falls back to a numbered list with defaults |
| "Run on [model]" | Runs on another Claude tier through a subagent, where the session supports it | Not offered. "Run it here" or "Just the prompt" instead |
| Compare 2 models | Where more than one model is reachable | Only through a connected API tool |
| Memory-aware questions | Skips what Claude already knows about you | Depends on the platform's memory |

The skill folder also includes `agents/openai.yaml`, so it shows up with its name and icon in OpenAI's Codex app. Claude ignores that file.

Running prompts on OpenAI, Grok or Gemini models happens only through a connected API tool, never through a browser unless you ask.

## License

MIT © 2026 andrcami. See [LICENSE](LICENSE).
