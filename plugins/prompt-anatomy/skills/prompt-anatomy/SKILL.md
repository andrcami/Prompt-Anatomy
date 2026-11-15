---
name: "prompt-anatomy"
description: "Turns underspecified requests into strong prompts: asks a few targeted questions (at most two short rounds), builds a refined prompt for the user's AI platform, and recommends a model and mode. Default to using it for any task request (asking to find, write, plan, build, compare, recommend or decide) that is missing two or more of: goal, context, specifics (place, budget, scope), constraints, or output format. This includes bare topics like \"boat purchase\" or \"car in Malta\", and longer requests that still omit key details. When unsure, use it. Also use when the user asks to write, improve or review a prompt, system prompt, custom GPT, Gem or custom instructions, or asks which AI model or mode to use. Skip only for single quick facts, casual chat, follow-ups where the conversation already supplies the context, or when the user says to just answer."
license: MIT
---

# Prompt Anatomy

A vague request forces the model to guess, and guessing produces generic answers. "Find me the prices of cars in Malta" could mean a new family SUV under €30k, the resale value of the user's 2015 hatchback, or a market study for an import business. Each of those needs a different answer. A few good questions cost the user about thirty seconds and saves several rounds of wrong answers.

This skill does three things:

1. It finds what is missing from the request and asks only about that.
2. It turns the answers into a well-structured prompt for the platform the user is on.
3. It recommends a model and mode, and offers to run the prompt.

Treat the user as a busy person, not a student. The point is to get them a better result fast. Lecturing them about prompt engineering is not the point.

## Step 0: Decide whether to step in

Run the request through three gates, in order.

**Gate 1: Is it a task?** It asks you to find, write, plan, build, compare, recommend or decide something. If it is chat, thanks or a single fact ("VAT rate in Malta"), stop. Don't step in.

**Gate 2: Count the missing core elements.** Check these five:

| Element | Present if the message says… |
|---|---|
| **Goal** | what it's for: buy, sell, research, decide |
| **Context** | who it's for or their situation: personal or business, beginner, what they already know |
| **Specifics** | scope: place, budget, size, timeframe, quantity |
| **Constraints** | must or must-not rules: sources, tone, length, deadline |
| **Output format** | the shape of the answer: table, email, bullets, code, length |

If **two or more are missing, step in.** If you're unsure, step in. A 30-second question round costs less than a generic answer. Role or audience, examples and success criteria are deliberately not gates. Almost nobody supplies them, so you add them yourself when you build the prompt.

**Gate 3: Overrides.** Don't step in, whatever the count, if the conversation already supplies the missing pieces, if the user says "just answer" or "no questions", or if it is urgent or safety-related.

*Scoring examples:* "boat purchase" has a goal (buy) but no context, specifics, constraints or format. Four are missing, so step in. "Used 2019 Yaris automatic in Malta under €12k, table with links" is missing only context, so just answer.

These requests usually qualify:

- They are broad or generic ("prices of cars", "a marketing plan", "a workout routine").
- They are a bare topic or fragment with no question at all ("boat purchase", "car in Malta", "gym plan"). A short request is not a specific request. A 2-word topic is usually the vaguest case of all, so step in.
- They are missing the who, what, where, when, how much, or what format.
- The user explicitly asks for help writing or improving a prompt, or asks which model to use.

Don't step in in these cases, because there the questions cost more than they save:

- The request is already specific. A user who gave budget, location, type and format has done the work, so just answer.
- It is a quick fact, a definition, casual chat, or a follow-up in a conversation that already has context.
- The user says "just answer", "no questions", "quick" or similar. Respect that. At most, state your key assumptions in one line at the top of the answer.
- It is urgent or safety-related. Help first.

**Light mode.** Sometimes a request is only a little underspecified, or the user seems to want speed. Then give a short best-effort answer with your assumptions stated, and end with 1–2 questions that would sharpen it. Use full mode (Steps 1–5) when the gaps are big, or when the user wants a reusable prompt.

## The anatomy of a good prompt

These are the stages to check. Not every prompt needs all of them. A one-off question may need four, and a system prompt for a custom GPT needs nearly all of them.

| # | Element | What it pins down | Example question |
|---|---------|-------------------|------------------|
| 1 | **Goal** | What they want and what decision or action it serves | "Are you buying, selling, or researching the market?" |
| 2 | **Context** | Who they are, background, what they already know or tried | "Is this for you personally or for a business?" |
| 3 | **Specifics / inputs** | Scope: place, time, budget, quantities, data they have | "New or used? Rough budget?" |
| 4 | **Role / audience** | Expert lens for the model; who will read the output | "Should this read like advice from a car dealer or a consumer advocate?" |
| 5 | **Constraints** | Must and must-not rules, sources, tone, length, deadline | "Only trusted sources, or include private classifieds?" |
| 6 | **Output format** | Table, bullets, email, JSON, code; length | "A comparison table with price, year, mileage and link?" |
| 7 | **Examples** | A sample of what good looks like (optional, but powerful) | "Have an example you liked?" |
| 8 | **Success criteria** | How they'll judge the result; what "done" means | "What would make this answer genuinely useful to you?" |

The model also benefits from **working instructions**. You add these yourself when you build the prompt, so don't ask the user about them: think step by step for hard problems, search the web for current facts, cite sources with dates, say when unsure, and ask before assuming.

For a deeper guide to each element, and for question banks by task type (research and shopping, writing, coding, data, images, business, learning, system prompts), read `references/anatomy.md`.

## Step 1: Work out the platform and the destination

Two things shape the final prompt:

- **The platform.** Infer it when you can. Inside Claude.ai or Claude Code, it's Claude. If the user mentions ChatGPT, Grok, Gemini, Copilot, Perplexity, Midjourney or similar, use that. If you can't tell and it matters (for example, they want a prompt to paste elsewhere), add it as one of the questions.
- **The destination.** Is the prompt to be run *right here, now*, pasted into *another tool*, used as a *system prompt or custom instructions* (custom GPT, Gem, Claude Project, Grok project), or sent through an *API*? A one-off chat prompt and a reusable system prompt are written differently.

## Step 2: Ask targeted questions (at most two rounds)

Ask in rounds, not all at once. Round 1's answers often change what's worth asking next. A boat for day trips needs different follow-ups from one for crossings to Sicily. But keep it short, because an interrogation is tiring.

1. **Round 1: up to 4 questions.** Ask the ones whose answers change the result most (usually goal, specifics and output).
2. **Re-check.** Run Gate 2 again on the original request plus the answers. If what's still missing wouldn't change the answer much, go to Step 3.
3. **Round 2: only if needed, up to 3 questions.** Build each follow-up from round 1's answers, never a leftover from a fixed list. Each question includes a "Use defaults" choice so the user can skip it.
4. **Hard stop: 2 rounds and 7 questions in total.** Never start a third round. Anything still open becomes a sensible default, listed under "Assumptions I made" in Step 5.

If the user answers round 1 with "defaults" or shows they want speed, skip round 2.

- **Ask only about what's missing and matters.** If they already said "used cars", don't ask new or used.
- **Make questions specific to the task.** Don't ask generic ones. "What's your context?" is weak. "Are you buying for yourself, or for a business?" is strong.
- **Stay within the round limits above.** If more questions seem needed, choose the ones whose answers would change the result most, and use defaults for the rest. List those defaults under "Assumptions I made" in Step 5, so the user can still correct them.
- **Offer choices and a default** for each question, so the user can answer fast ("1b, 2 €15k, rest default") or just say "use defaults".
- **Always use the structured question tool when one exists** (for example AskUserQuestion, or a multiple-choice widget). It is the default, not an option. Never switch to a plain-text list just to fit in more questions. Cut questions instead. Every question needs 2–4 answer choices. Put the recommended default first and mark it "(Recommended)". Open-ended questions ("do you hold a licence?") must also be turned into choices ("Yes / No, not yet / Getting one"). The user can always type their own answer.
- **Use the plain-text numbered list only when no question tool exists** in the session.
- **Don't ask about the platform when it's obvious.** Inside Claude.ai or Claude Code, assume Claude and skip the platform question.

Use this shape for a plain-text question message:

```
To get you a genuinely useful answer, a few quick questions. Reply with numbers/letters, or just say "defaults":

1. **[Element]: [Specific question]?**
   a) … b) … c) … (default: b)
2. **[Element]: [Specific question]?** (default: …)
…
[Optional] Where will you use this prompt: here, ChatGPT, Grok, Gemini, other? (default: here)
```

Add one line saying they can skip any question. Don't explain the anatomy unless they ask.

## Step 3: Assemble the refined prompt

Combine the request, the answers and sensible defaults into one prompt. These principles come from the published guidance of Anthropic, OpenAI and xAI, and they hold across platforms:

- **Put the instructions first.** Begin with a clear task statement, and separate instructions from context and data with clear delimiters.
- **Be specific and explicit** about goal, scope, length, format and style. Assume the model is a brilliant new colleague who lacks your context.
- **Give the reason behind constraints.** "Keep it under 200 words because it goes on a phone screen" works better than "under 200 words".
- **Say what to do, not only what to avoid.** Write "use plain language a 12-year-old understands", not "don't be technical".
- **Show the output format.** Give an example of it, or a skeleton (table headers, JSON keys) when the format matters.
- **For current facts** (prices, news, availability), tell the model to search the web and to give sources and dates. Also tell it to flag anything it couldn't verify.
- **Invite honesty.** Allow "I don't know", and ask for uncertainty to be flagged instead of filled with guesses.
- **Put long material first.** With long documents or data, place them at the top and the question at the end.

Then format the prompt for the platform. Read `references/platforms.md` for each platform's conventions. In short:

- **Claude:** XML-style tags (`<context>`, `<task>`, `<output_format>`) work very well.
- **OpenAI / ChatGPT:** Markdown headings or `###` / `"""` delimiters.
- **Grok:** plain labeled sections or an acronym framework; say explicitly whether to search recent X posts and the web, and state the tone (its default voice can be casual).
- **Gemini:** headings and bullet lists; put the instruction at the start or end of long context.
- **Image models:** subject, style, composition, lighting and aspect ratio, not long prose.

For a reusable system prompt, include: role and purpose, audience, scope (what's in and out), behavior rules with reasons, output conventions, how to handle uncertainty and off-topic requests, and 1–3 short examples if format matters.

If the user asks for a named framework (CO-STAR, RISEN, RTF, CRISPE and others), or the task fits one, read `references/frameworks.md`.

## Step 4: Recommend a model and mode

Recommend a model and mode in 1–3 lines, matched to the task. The mode often matters as much as the model, but **always name both**. "Claude with web search" names only a mode and is incomplete. Every recommendation must include:

- **A named model:** the platform's tier plus the current model name you know (e.g. "Claude Sonnet, the balanced tier").
- **A mode:** web search, research or deep research, extended thinking or reasoning, or file upload. Say "default chat" if none is needed.
- **A one-line reason** tied to the task.
- **A step-up or step-down option** when one makes sense (e.g. "for a deeper multi-source report, use Research mode").
- **When it applies, a warning about what to avoid** (e.g. "don't use a model without search, because prices will be stale").

**On Claude (Claude.ai, Claude Code, Cowork or the API), use Anthropic's own model ladder.** It follows Anthropic's published guidance: the Claude Enterprise consumption guide on support.claude.com and "Choosing a model" on platform.claude.com. Score the task from what you already know from the request and the answers, then pick the **lowest tier that does the job well**:

| Tier | Use it when the task is… | Examples | Token use |
|---|---|---|---|
| **Haiku** | Simple, single-step, easy to check: a lookup, summary, short rewrite, classification or extraction | "Summarise this email", "tidy this list" | Low |
| **Sonnet (default)** | Everyday work: writing, a comparison, analysis, Q&A, a single research question with web search | LinkedIn post, car prices, a cover letter | Moderate |
| **Opus** | Genuinely complex and multi-step: several linked decisions, trade-offs, planning, deep analysis, non-trivial code, or when quality matters more than speed | Boat purchase (licence + budget + mooring), a business plan, an architecture review | High |
| **Fable** | The hardest open-ended work: deep research across many sources, complex analysis, long-running agentic tasks | Market study, due diligence pack | Very high |

Rules for applying the ladder:

- **When in doubt, recommend Sonnet.** Step up only when you can name the extra complexity in the one-line reason (e.g. "Opus: three linked decisions with trade-offs").
- **Effort is a second lever.** Leave it at the default for routine work. Suggest higher effort or extended thinking only for multi-step reasoning, and say why.
- **The mode is chosen separately:** web search for current facts, Research mode for thorough multi-source reports, file upload for long documents.
- **Judge cost per finished task, not per token.** A cheaper model that will likely need a second attempt isn't cheaper.
- Model names change. Name the tier and the current version you know (e.g. "Claude Sonnet 5.5"), and tell the user to pick the newest model in that tier if the name has moved on.

**On other platforms, match the task to their equivalent tier:**

- **Current facts, prices or news:** a model with **web search** turned on, or a deep research mode for thorough multi-source reports.
- **Hard reasoning, maths, strategy or complex code:** the platform's top reasoning or "thinking" model.
- **Everyday writing and summarizing:** the platform's balanced default model.
- **High-volume, simple or speed-critical work:** the fast, cheap tier.
- **Long documents:** a model with a large context window, plus file upload.

Read `references/platforms.md` for model tiers per platform. Model line-ups change often. Name the tier and the current example you know, and tell the user to choose the newest model in that tier in their model picker if the name has changed. Don't invent model names. If you're unsure what a platform currently offers, describe the tier.

If the user is on a different platform from the one you'd ideally choose, recommend the best option **on their platform** first. Mention an alternative only if it's clearly better for the task (for example, "for live prices, any assistant with web search beats one without").

## Step 5: Deliver

Keep the delivery short. Use this structure:

~~~
**Your refined prompt** (ready to copy):
```text
[the prompt]
```

**Run it on:** [named model] + [mode] — [one-line why]
**Go deeper / cheaper:** [alternative model or mode, if relevant]

**Assumptions I made:** [only if you filled gaps with defaults; 1–3 bullets]

[Checkpoint question, see below]
~~~

**This order is fixed.** Every delivery shows the prompt block, then the "Run it on" line, then the assumptions, then the checkpoint. Never skip the prompt block or the model line, even for writing tasks like a post or email where the result seems to be all the user wants. The prompt is what they reuse, and the model line is part of the deliverable.

**Checkpoint: stop and confirm before running.** Don't search, run tools or answer the prompt yet. The user may want to change the prompt first, and anything run on a wrong premise is wasted. Ask with the structured question tool when one exists (otherwise ask in one line), with these choices:

- **Run it here (Recommended):** run the prompt in the current conversation and model. This is the cheapest option.
- **Run on [recommended model]:** offer this only when the recommended tier differs from the current model *and* a subagent tool that accepts a model choice exists (see "Running it").
- **Compare 2 models (uses about 2–3× resources):** run the same prompt on two models and show the answers side by side. Offer this only when you can reach more than one model. Use 3 models only if the user asks.
- **Adjust first:** the user says what to change. Update the prompt, show it again, then run it straight away without a second checkpoint.
- **Just the prompt:** stop here. They'll use it elsewhere.

Offer only the choices you can actually carry out in this session. Check your tools before asking.

**Skip the checkpoint and run immediately** only if the user has already said to ("just run it", "go ahead and do it") in the original request or in their answers to the questions.

Put the prompt in a fenced code block so the user gets a one-click copy button and a clean boundary. If the interface can't render Markdown, mark the start and end of the prompt with clear lines instead.

**Running it.** Once the user confirms, carry out the choice they picked:

- **Run it here:** answer the refined prompt yourself, fully, as if they had sent it. If a tool the task needs is missing (such as web search), say so and say where to paste the prompt instead.
- **Run on [model]:** start a subagent on that tier (e.g. the Agent tool's `model` parameter: haiku, sonnet, opus, fable). Pass it the full refined prompt plus one line: "Answer this fully; use web search if the prompt asks for current facts; end with sources." The subagent starts cold, so the prompt must be self-contained. The user never sees the subagent's report, so relay its full answer yourself.
- **Other platforms (OpenAI, Grok, Gemini):** run there only through a connected tool that can call that provider's model (directly or through a router such as OpenRouter). Use a browser only if the user explicitly asks.
- **Compare:** to avoid repeating work, do any web research **once** first, then give each model the same prompt plus the same findings, in parallel. Show one section per model, labelled with the model name, and end with a 2–3 line verdict on which answer was strongest and why. Say that this compares how the models reason and write, not how they search.

Always open the answer with a horizontal rule and a **Result** heading that names the model it ran on, e.g. **Result (Claude Sonnet 5.5)**. That keeps the prompt kit and the answer clearly separate.

- **Follow the prompt's `<output_format>` exactly** (the same table columns, sections and order). The user agreed to that format at the checkpoint. If you deliberately deviate, for example because a column has no data, say so in one line.
- **When you use a subagent, wait for it and post the result in the same reply.** Don't say "I'll post it when it finishes" and end your turn, because the user would have to prompt you again to see the answer.

## Improving an existing prompt

When the user pastes a prompt and asks to improve or review it:

1. Check it against the anatomy, and list the 2–4 most important gaps or problems in plain words. Common problems: vague goal, no format, conflicting instructions, missing context, all-caps "NEVER/ALWAYS" with no reason given, examples that are all alike.
2. Ask about the gaps only if you can't sensibly fill them yourself.
3. Give the rewritten prompt, and briefly note what changed and why.

## Worked example (short)

**User:** find me the prices of cars in Malta

**You (Step 2, round 1, using the question widget):**

> 1. **Goal:** Buying (Recommended) · Selling or valuing · Market research
> 2. **New or used?** Used (Recommended) · New · Both
> 3. **Budget and type:** Under €15k, any type (Recommended) · €15–30k · Over €30k (or type your own)
> 4. **Output:** Listings with links + typical price ranges (Recommended) · Listings only · Price ranges only

Without a question widget, ask the same four questions as a numbered list with a default for each, and add that they can reply "defaults" or skip any. If the answers leave something that would change the result (here, transmission and body type), ask a short round 2.

**User (after round 2):** buying, used, under €15k, automatic hatchback, defaults for the rest

**You (Step 5):** give a Claude-formatted prompt with `<context>`, `<task>`, `<requirements>` (search current Maltese listings such as dealer sites and classifieds, prices in EUR, include year, mileage, fuel and transmission, link and date seen, note whether imported cars include registration tax) and `<output_format>` (a table, then a 3-bullet summary of typical price ranges and value tips). Recommend Claude Sonnet with web search on (a single research question, so Sonnet is the right tier on the ladder), and Research mode for a deeper dealer-by-dealer comparison. Then ask the checkpoint question: run it here, adjust first, or just the prompt.

More before/after examples are in `references/examples.md`.