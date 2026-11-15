---
name: prompt-anatomy
description: Turns vague or underspecified requests into strong, well-structured prompts. It asks the user one short round of targeted questions (goal, context, specifics, constraints, output format, success criteria), assembles a refined prompt formatted for the user's AI platform, and recommends which model and mode to run it on (Claude, ChatGPT/OpenAI, Grok, Gemini, others). Use this skill whenever a request is broad or generic and missing details that would change the answer, such as "find me the prices of cars in Malta", "write me a marketing plan", "help with my CV" or "build me a website". Also use it whenever the user asks to write, improve, rewrite, review or "make better" a prompt, system prompt, custom GPT, Gem or custom instructions, or asks which AI model or mode they should use for a task. Skip it when the request is already specific, is a quick factual lookup, is casual chat, or the user says to just answer.
---

# Prompt Anatomy

A vague request forces the model to guess, and guessing produces generic answers. "Find me the prices of cars in Malta" could mean a new family SUV under €30k, the resale value of the user's 2015 hatchback, or a market study for an import business. Each of those needs a different answer. One short round of good questions costs the user about thirty seconds and saves several rounds of wrong answers.

This skill does three things:

1. It finds what is missing from the request and asks only about that.
2. It turns the answers into a well-structured prompt for the platform the user is on.
3. It recommends a model and mode, and offers to run the prompt.

Treat the user as a busy person, not a student. The point is to get them a better result fast. Lecturing them about prompt engineering is not the point.

## Step 0: Decide whether to step in

Compare the request with the **anatomy** below. Step in when the missing pieces would materially change the answer. These requests usually qualify:

- They are broad or generic ("prices of cars", "a marketing plan", "a workout routine").
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

## Step 2: Ask one round of targeted questions

Ask everything in **one message**. A back-and-forth interrogation is tiring.

- **Ask only about what's missing and matters.** If they already said "used cars", don't ask new or used.
- **Make questions specific to the task.** Don't ask generic ones. "What's your context?" is weak. "Are you buying for yourself, or for a business?" is strong.
- **Ask 3–6 questions.** If more seem needed, choose the ones whose answers would change the result most, and use defaults for the rest.
- **Offer choices and a default** for each question, so the user can answer fast ("1b, 2 €15k, rest default") or just say "use defaults".
- **Use a structured question tool if one exists.** Examples are a multiple-choice or ask-user widget in the client. Otherwise, use a numbered list.

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

Recommend a model and mode in 1–3 lines, matched to the task. The mode often matters as much as the model.

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

**Run it on:** [model + mode] — [one-line why]

**Assumptions I made:** [only if you filled gaps with defaults; 1–3 bullets]

Want me to run it now, or adjust anything?
~~~

Put the prompt in a fenced code block so the user gets a one-click copy button and a clean boundary. If the interface can't render Markdown, mark the start and end of the prompt with clear lines instead.

If the user is on the same platform and you have the tools the task needs (such as web search), offer to run the prompt straight away. If they say yes, answer the refined prompt fully, as if they had sent it.

## Improving an existing prompt

When the user pastes a prompt and asks to improve or review it:

1. Check it against the anatomy, and list the 2–4 most important gaps or problems in plain words. Common problems: vague goal, no format, conflicting instructions, missing context, all-caps "NEVER/ALWAYS" with no reason given, examples that are all alike.
2. Ask about the gaps only if you can't sensibly fill them yourself.
3. Give the rewritten prompt, and briefly note what changed and why.

## Worked example (short)

**User:** find me the prices of cars in Malta

**You (Step 2):**

> To get you useful prices rather than a generic overview, a few quick questions. Answer with numbers/letters, or say "defaults":
>
> 1. **Goal:** Are you a) buying, b) selling or valuing a car, c) researching the market? (default: a)
> 2. **New or used?** a) new b) used c) both (default: c)
> 3. **Budget and type:** price range, and any type or make? e.g. "under €20k, small SUV, Toyota/Kia" (default: any, grouped by type)
> 4. **Must-haves:** fuel type (petrol/diesel/hybrid/EV), max age or mileage, automatic? (default: none)
> 5. **Output:** a) table of specific listings with links, b) typical price ranges by model, c) both (default: c)
>
> Skip any you don't care about.

**User:** buying, used, under 15k, automatic hatchback, defaults for the rest

**You (Step 5):** give a Claude-formatted prompt with `<context>`, `<task>`, `<requirements>` (search current Maltese listings such as dealer sites and classifieds, prices in EUR, include year, mileage, fuel and transmission, link and date seen, note whether imported cars include registration tax) and `<output_format>` (a table, then a 3-bullet summary of typical price ranges and value tips). Recommend running it with web search on. Offer to run it now.

More before/after examples are in `references/examples.md`.
