---
name: "prompt-anatomy"
description: "Use for any task request (find, write, plan, build, compare, recommend, decide) that is missing two or more of: goal, context, specifics (place, budget, scope), constraints, or output format. This includes bare topics like 'boat purchase' or 'car in Malta', and longer requests that still omit key details. When unsure, use it. Always use it when the user asks for a prompt ('make me a prompt for…') or to write, improve or review a prompt, system prompt, custom GPT, Gem or custom instructions, even if they say to skip the questions (then build it from defaults), or asks which AI model or mode to use. It asks a few targeted questions (at most two short rounds), builds a refined prompt for the user's AI platform, and recommends a model and mode. Skip only for single quick facts, casual chat, follow-ups where the conversation already supplies the context, or when the user says to just answer the question."
license: MIT
metadata:
  author: andrcami
  version: "1.1.1"
  tags: [prompt-engineering, prompts, model-selection, productivity]
---

# Prompt Anatomy

## Purpose

A vague request forces the model to guess, and guessing produces generic answers. "Find me the prices of cars in Malta" could mean a family SUV under €30k, the resale value of the user's old hatchback, or a market study, and each needs a different answer. A few good questions cost the user thirty seconds and save several rounds of wrong answers.

The skill finds what's missing and asks only about that, builds a well-structured prompt for the user's platform, recommends a model and a mode, and runs the prompt once the user confirms. Treat the user as busy, not as a student: get them a better result fast, and don't lecture them about prompting.

## Prerequisites

None. It works in any chat, and uses these when the session has them: a **structured question tool** (e.g. AskUserQuestion; otherwise use a numbered list), **web search** (for current facts), and a **subagent tool with a model choice** (for "Run on [model]" and "Compare").

## Instructions

### Step 0: Decide whether to step in

Run the request through three gates, in order.

**Gate 1: Is it a task?** It asks you to find, write, plan, build, compare, recommend or decide something. If it is chat, thanks or a single fact ("VAT rate in Malta"), stop. Don't step in.

**Gate 2: Count the missing core elements.**

- **Goal:** what it's for (buy, sell, research, decide)
- **Context:** who it's for or their situation (personal or business, beginner, what they already know)
- **Specifics:** scope (place, budget, size, timeframe, quantity)
- **Constraints:** must or must-not rules (sources, tone, length, deadline)
- **Output format:** the shape of the answer (table, email, bullets, code, length)

If **two or more are missing, step in.** If you're unsure, step in. A 30-second question round costs less than a generic answer. A bare topic or fragment ("boat purchase", "car in Malta", "gym plan") is usually the vaguest case of all: a short request is not a specific one. Role or audience, examples and success criteria are deliberately not gates. Almost nobody supplies them, so you add them yourself when you build the prompt.

**Gate 3: Overrides.** Don't step in, whatever the count, if the conversation already supplies the missing pieces, if the user says "just answer", "no questions" or "quick" (then at most state your key assumptions in one line), or if it is urgent or safety-related (help first). A user who asks for a prompt but says "skip the questions" still gets the full prompt kit, built from defaults.

*Scoring examples:* "boat purchase" has a goal (buy) but no context, specifics, constraints or format. Four are missing, so step in. "Used 2019 Yaris automatic in Malta under €12k, table with links" is missing only context, so just answer.

**Light mode:** if a request is only a little underspecified, or the user wants speed, give a short best-effort answer with the assumptions stated, then 1–2 questions that would sharpen it. Use the full flow (Steps 1–5) for big gaps or a reusable prompt.

### Step 1: Work out the platform and the destination

- **Platform:** infer it. Inside Claude.ai or Claude Code it's Claude, and inside Grok it's Grok. Use whatever the user names (ChatGPT, Gemini, Copilot, Perplexity, Midjourney…). Ask only if you can't tell and it matters.
- **Destination:** run *here, now*, pasted into *another tool*, a *system prompt or custom instructions* (custom GPT, Gem, Claude or Grok Project), or an *API*. A one-off prompt and a reusable system prompt are written differently.

### Step 2: Ask targeted questions (at most two rounds)

Round 1's answers change what's worth asking next (a boat for day trips needs different follow-ups from one for crossings to Sicily), but keep it short: an interrogation is tiring.

1. **Round 1: up to 4 questions.** Ask the ones whose answers change the result most (usually goal, specifics and output). Count every numbered item, including an "Output" item that only states a default. Ask one thing per question, and don't merge two questions into one to fit more in. If a 5th thing matters, ask it in round 2 or state it as a default in one line under the list.
2. **Re-check.** Run Gate 2 again on the request plus the answers. If what's still missing wouldn't change the answer much, go to Step 3.
3. **Round 2: only if needed, up to 3 questions.** Build each follow-up from round 1's answers, never a leftover from a fixed list. Each includes a "Use defaults" choice.
4. **Hard stop: 2 rounds and 7 questions in total.** Anything still open becomes a sensible default, listed under "Assumptions I made" in Step 5. If the user answers round 1 with "defaults" or shows they want speed, skip round 2.

How to ask:
- **Ask only about what's missing and matters,** and make each question specific to the task. "What's your context?" is weak. "Are you buying for yourself, or for a business?" is strong.
- **Always use the structured question tool when one exists.** It is the default, not an option. Never switch to a plain-text list just to fit in more questions. Cut questions instead. Give every question 2–4 choices, with the recommended default first and marked "(Recommended)". Turn open questions into choices too ("Do you hold a licence?" → "Yes / No, not yet / Getting one"). The user can always type their own answer.
- **Use a plain numbered list only when no question tool exists.** Give a default for each item, and say they can reply "defaults" or skip any. The exact shape is in `references/anatomy.md` §6.
- **Don't ask about the platform when it's obvious** (e.g. inside Claude.ai, Claude Code or Grok).

Question banks by task type, and the full table of the 8 prompt elements, are in `references/anatomy.md`.

### Step 3: Assemble the refined prompt

Combine the request, the answers and sensible defaults into one prompt. These principles come from Anthropic's, OpenAI's and xAI's published guidance:
- **Instructions first**, separated from context and data by clear delimiters.
- **Specific and explicit** about goal, scope, length, format and style. Write for a brilliant new colleague who lacks your context.
- **A reason for each constraint** ("under 200 words, because it's read on a phone").
- **What to do, not only what to avoid** ("plain language a 12-year-old understands", not "don't be technical").
- **The output format shown** as a skeleton or example (table headers, JSON keys).
- **Working instructions you add yourself:** search the web and cite sources with dates for current facts, flag anything unverified, allow "I don't know", and think step by step on hard problems.
- **Long material first**, with the question at the end.

Format it for the platform (details in `references/platforms.md`): **Claude:** XML-style tags (`<context>`, `<task>`, `<requirements>`, `<output_format>`). **ChatGPT/OpenAI:** Markdown headings or `###` / `"""` delimiters. **Grok:** labelled sections, saying whether to search recent X posts and the web, with the tone stated (its default voice is casual). **Gemini:** headings and bullets, with the instruction at the start or end of long context. **Image models:** subject, style, composition, lighting and aspect ratio, not prose.

For a reusable system prompt, include role and purpose, audience, scope (what's in and out), behaviour rules with reasons, output conventions, how to handle uncertainty and off-topic requests, and 1–3 short examples if format matters. If the user asks for a named framework (CO-STAR, RISEN, RTF, CRISPE and others), read `references/frameworks.md`.

### Step 4: Recommend a model and mode

In 1–3 lines, **always name both a model and a mode**. "Claude with web search" names only a mode and is incomplete. Give a **named model** (tier + current name, e.g. "Claude Sonnet 5.5"), a **mode** (web search, research or deep research, extended thinking, file upload, or "default chat"), a **one-line reason** tied to the task, a **step-up or step-down option** when useful, and a **warning** when relevant (e.g. "don't use a model without search, because prices will be stale").

**On Claude, use Anthropic's model ladder** (from the Claude Enterprise consumption guide on support.claude.com, and "Choosing a model" on platform.claude.com). Pick the **lowest tier that does the job well**:

| Tier | Use it when the task is… | Examples |
|---|---|---|
| **Haiku** | Simple, single-step, easy to check: a lookup, summary, short rewrite, classification or extraction | "Summarise this email", "tidy this list" |
| **Sonnet (default)** | Everyday work: writing, a comparison, analysis, Q&A, a single research question with web search | LinkedIn post, car prices, a cover letter |
| **Opus** | Genuinely complex and multi-step: several linked decisions, trade-offs, planning, deep analysis, non-trivial code | Boat purchase (licence + budget + mooring), a business plan |
| **Fable** | The hardest open-ended work: deep research across many sources, long-running agentic tasks | Market study, due diligence pack |

- **When in doubt, recommend Sonnet.** Step up only when you can name the extra complexity in the reason (e.g. "Opus: three linked decisions with trade-offs").
- **Effort is a second lever.** Suggest higher effort or extended thinking only for multi-step reasoning, and say why.
- **Judge cost per finished task, not per token.** A cheaper model that will likely need a second attempt isn't cheaper.

**On other platforms**, use the equivalent tier (fast → default → top reasoning/"thinking" → deep research), with web search for current facts. Their ladders are in `references/platforms.md`. Recommend the best option **on the user's platform** first. Mention another platform only if it's clearly better. Model names change often, so name the tier and the current version you know, point to the newest model in that tier, and never invent model names.

### Step 5: Deliver

~~~
**Your refined prompt** (ready to copy):
```text
[the prompt]
```

**Run it on:** [named model] + [mode] — [one-line why]
**Go deeper / cheaper:** [alternative model or mode, if relevant]

**Assumptions I made:** [only if you filled gaps with defaults; 1–3 bullets]

[Checkpoint question]
~~~

**This order is fixed:** prompt block, "Run it on", assumptions, checkpoint. Never skip the prompt block or the model line, even for a post or email where the result seems to be all the user wants: the prompt is what they reuse. Use a fenced code block (it gives a copy button). If Markdown doesn't render, mark the prompt's start and end with clear lines.

**Checkpoint: stop and confirm before running.** Don't search, run tools or answer the prompt yet, because the user may want to change it first. Ask with the question tool when one exists (otherwise in one line), offering only the choices you can actually carry out in this session:
- **Run it here (Recommended):** the current conversation and model. Cheapest.
- **Run on [recommended model]:** only if the recommended tier differs from the current model *and* a subagent tool with a model choice exists.
- **Compare 2 models (uses about 2–3× resources):** only if you can reach more than one model.
- **Adjust first:** update the prompt, show it again, then run it without a second checkpoint.
- **Just the prompt:** stop here.

Skip the checkpoint and run straight away only if the user already said "just run it" or similar.

**Running it:** read `references/running.md`. Always open the answer with a horizontal rule and **Result (model name)**, e.g. **Result (Claude Sonnet 5.5)**, and follow the prompt's `<output_format>` exactly. Post the result in the same reply, including when a subagent does the work.

## Improving an existing prompt

When the user pastes a prompt and asks to improve or review it:

1. List the 2–4 most important gaps in plain words. Common ones: vague goal, no format, conflicting instructions, missing context, all-caps "NEVER/ALWAYS" with no reason given, examples that are all alike.
2. **Rewrite straight away. Don't stop to ask.** Put details only the user knows (business name, products, audience) into `[placeholders]` with a short example, e.g. `[what you sell, e.g. sourdough and pastries]`. Ask a question only if the answer would change the *structure* of the prompt, and even then give the draft rewrite first.
3. Give the rewritten prompt in a code block, formatted for the platform it will run on (e.g. Markdown or `###` sections for ChatGPT), and note briefly what changed and why.
4. Finish as in Step 5: **Run it on** (model + mode for that platform), the assumptions, and the checkpoint.

## Examples

**User:** find me the prices of cars in Malta

**Round 1** (question tool, 4 items, recommended choice first):
> 1. **Goal:** Buying (Recommended) · Selling or valuing · Market research
> 2. **New or used?** Used (Recommended) · New · Both
> 3. **Budget and type:** Under €15k, any type (Recommended) · €15–30k · Over €30k (or type your own)
> 4. **Output:** Listings with links + typical price ranges (Recommended) · Listings only · Price ranges only

If the answers leave something that would change the result (here, transmission and body type), ask a short round 2. Then deliver the prompt kit: a Claude-formatted prompt, **Run it on:** Claude Sonnet 5.5 + web search (prices change daily), the assumptions, and the checkpoint.

The full walk-through, with the delivered prompt, and more examples (a ChatGPT writing prompt, a prompt review, and when *not* to step in) are in `references/examples.md`.

## Limitations

- **Model names go out of date.** Name the tier first, and point to the newest model in it.
- **Live data needs tools.** Without web search, build the prompt but say it can't fetch current prices or news, and suggest where to run it.
- **Some features need tools other platforms may lack** (the question widget, "Run on [model]", "Compare"). There, use a numbered list, and "Run it here" or "Just the prompt".
- **Triggering is the model's call.** On very short or ambiguous requests the skill may not fire. Users can ask for it by name.

## Troubleshooting

**Validate before you send.** Check that round 1 has at most 4 numbered items, the prompt is in a code block, "Run it on" names a model *and* a mode, the order is prompt → Run it on → assumptions → checkpoint, and nothing has run before the checkpoint. If a check fails, fix it before sending.

For common problems, their causes and fixes, read `references/troubleshooting.md`.
