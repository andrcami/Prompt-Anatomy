# Platform Guide: Formatting and Model Recommendations

Read this when formatting the final prompt for a platform (Step 3) or recommending a model (Step 4).

> **Last reviewed: 2026-11-15.** Model line-ups change every few months. The Claude entries were checked against Anthropic's model overview on that date. The OpenAI, xAI and Google names come from general knowledge and are **examples of a tier**, not guaranteed to be current. Always recommend by tier first ("the top reasoning model"), give the example name, and tell the user to pick the newest model in that tier in their model picker. Never invent a model name.

## Contents
1. Claude (Anthropic)
2. ChatGPT / OpenAI
3. Grok (xAI)
4. Gemini (Google)
5. Other assistants (Copilot, Perplexity, Meta AI, Mistral, DeepSeek, local models)
6. Image generators
7. Task → tier cheat sheet

---

## 1. Claude (Anthropic): claude.ai, Claude apps, Claude Code, Claude API

**Formatting** (from Anthropic's prompting best practices):
- Be clear and direct. Treat Claude as a brilliant new employee who lacks context. Test: would a colleague with minimal context understand the prompt?
- Explain the reason behind instructions. Claude generalizes from the reason ("this will be read aloud by text-to-speech, so avoid ellipses").
- Use XML tags to separate parts: `<context>`, `<task>`, `<requirements>`, `<examples>`, `<output_format>`, `<document>`. Use consistent, descriptive tag names, and nest them for hierarchy.
- Give 3–5 varied examples wrapped in `<example>` tags when format or tone matters.
- Set a role in one sentence at the top, or in the system prompt or Project instructions.
- For long documents, put them first (in `<document>` tags) and the question last.
- If you want Claude to go beyond the literal request, ask for it explicitly ("include as many relevant features as possible").
- Use numbered steps when the order or completeness of steps matters.

**Where reusable prompts go:** Project instructions (claude.ai), custom Skills, `CLAUDE.md` (Claude Code), or the `system` parameter (API).

**Models: the ladder** (names verified 2026-11-15). This matches the ladder in SKILL.md Step 4. Pick the **lowest tier that does the job well**:

| Tier | Model | Use for |
|------|-------|---------|
| Simple | **Claude Haiku 5.5** | Simple, single-step, easy-to-check work: lookups, summaries, short rewrites, classification, extraction |
| **Default** | **Claude Sonnet 5.5** | Everyday work: writing, comparisons, analysis, Q&A, a single research question with web search. **When in doubt, Sonnet.** |
| Complex | **Claude Opus 5.5** | Genuinely complex, multi-step work with linked decisions and trade-offs, planning, deep analysis, non-trivial code |
| Hardest | **Claude Fable 5.2** | The hardest open-ended work: deep multi-source research, long-running agentic tasks |

*Where the default comes from:* Anthropic's API docs ("Models overview" on platform.claude.com) suggest starting with Opus 5.5 for most API workloads. The Claude Enterprise consumption guide on support.claude.com says "when in doubt, Sonnet" for chat use. This skill is mostly used in chat, so it follows the consumption guide: default to Sonnet, and step up only when you can name the extra complexity. Judge cost per finished task, not per token.

All four have adaptive thinking and a 1M-token context. On the API, the **effort** setting trades depth for speed. **Modes to mention:** web search (for current facts and prices), Research (for multi-source reports), file upload or Projects (for long documents).

---

## 2. ChatGPT / OpenAI: ChatGPT, custom GPTs, OpenAI API

**Formatting** (from OpenAI's "Best practices for prompt engineering with the OpenAI API"):
1. Use the latest, most capable model. Newer models are easier to prompt.
2. Put instructions at the **beginning**, and separate instructions from context with `###` or `"""`.
   ```
   Summarize the text below as a bullet point list of the most important points.

   Text: """
   {text}
   """
   ```
3. Be specific and detailed about context, outcome, length, format and style.
4. Show the output format with an example or skeleton (`Company names: <comma_separated_list>`). This also makes output easier to parse.
5. Start zero-shot. If that doesn't work, go few-shot (a couple of examples). Only then consider fine-tuning (API).
6. Cut fluffy descriptions. Write "Use a 3 to 5 sentence paragraph", not "fairly short, a few sentences only".
7. Say what to do instead of only what not to do. For example: "instead of asking for PII, refer the user to the help article".
8. For code, use leading words to nudge the pattern: end the prompt with `import` for Python or `SELECT` for SQL.
9. API: the "Generate Anything" feature can draft a prompt from a description.

**Parameters (API):** `temperature` near 0 for factual work, extraction and Q&A, and higher for creative work. `max_completion_tokens` is a hard cut-off, not a length control. `stop` sequences end generation.

**Reasoning vs. GPT models:** reasoning ("thinking") models do their own step-by-step reasoning. Keep their prompts direct and goal-focused, and skip "think step by step". Standard GPT models benefit from more explicit structure and steps.

**Where reusable prompts go:** custom GPT instructions (about 8,000 characters), ChatGPT Custom Instructions (short boxes, about 1,500 characters each), Projects, or the `system`/`developer` message (API).

**Model tiers** (examples as of last review; verify in the picker):

| Tier | Example | Use for |
|------|---------|---------|
| Top reasoning | GPT-5-class "Thinking" / "Pro" | Hard reasoning, maths, complex code, strategy |
| Default | GPT-5-class default / "Auto" | Everyday tasks |
| Fast / cheap | "mini" / "nano" variants (API) | High volume, simple tasks |

**Modes to mention:** Search (current facts and prices), Deep research (thorough multi-source reports), file uploads and data analysis (spreadsheets, PDFs), image generation.

---

## 3. Grok (xAI): grok.com, the X app, xAI API

**Formatting:**
- Grok follows the same general principles. Use plain, labeled sections (Role / Context / Task / Requirements / Output format) or an acronym framework from `frameworks.md` (A.P.E., R.A.C.E., C.O.A.S.T. and others). These are popular with Grok users, but they aren't Grok-specific.
- Grok has real-time access to **X (Twitter) posts** and the web. For trends, sentiment or breaking news, say so explicitly: "Search recent X posts and the web from the last 7 days and cite links."
- State the tone you want explicitly. Grok's default voice can be casual or witty, so ask for "neutral, professional" if that matters.

**Where reusable prompts go:** Custom Instructions (in settings), Projects, or the system message (API).

**Model tiers** (examples as of last review; verify in the picker):

| Tier | Example | Use for |
|------|---------|---------|
| Top reasoning | Grok 4-class (with "Think" or "Heavy") | Hard reasoning, analysis |
| Fast | Grok "Fast" variants | Quick everyday answers |
| Coding | Grok Code variants | Agentic coding |

**Modes to mention:** DeepSearch / DeeperSearch (multi-source research), Think (reasoning), X search (social trends).

---

## 4. Gemini (Google): the Gemini app, Gems, AI Studio, Vertex AI

**Formatting:**
- Use clear headings or bullet sections. Give the persona, task, context and format explicitly.
- With long context (documents, video, large files), put the instruction at the start or the end and refer to the material by name.
- Gemini integrates well with Google services (Gmail, Docs, Drive, Maps). Mention them when relevant ("use my Drive file X").

**Where reusable prompts go:** Gems (custom instructions), or system instructions (AI Studio / API).

**Model tiers** (examples as of last review; verify in the picker):

| Tier | Example | Use for |
|------|---------|---------|
| Top reasoning | Gemini "Pro" (latest version) | Hard reasoning, long documents, coding |
| Fast | Gemini "Flash" | Everyday tasks |
| Cheapest | Gemini "Flash-Lite" | High volume |

**Modes to mention:** Deep Research, Google Search grounding, file and video upload, Canvas.

---

## 5. Other assistants

- **Microsoft Copilot:** web-grounded by default. Good for Microsoft 365 documents. Use clear task and format sections.
- **Perplexity:** search-first. Ideal for current facts and prices. Ask for sources, a date range and region. Choose the model in settings, and use "Research" mode for depth.
- **Meta AI, Mistral (Le Chat), DeepSeek, local models (Llama, Qwen and others):** use the generic skeleton from `anatomy.md` with plain-text headings. Smaller or local models need **more explicit structure and examples**, and they can't browse unless a tool is connected. Tell the user they'll need to supply current data.

---

## 6. Image generators (Midjourney, DALL·E / GPT image, Imagen, Grok Imagine, Stable Diffusion, Firefly)

Write a compact descriptive prompt, not instructions:
`[subject + action], [setting], [style/medium], [mood], [lighting], [composition/camera], [colour palette], [details]` plus the aspect ratio (Midjourney: `--ar 16:9`; elsewhere, state it).
- Put the most important element first.
- Use concrete visual nouns and adjectives. Avoid abstract goals ("make it engaging").
- Use negative prompts only where supported (`--no text` in Midjourney; a "negative prompt" field in Stable Diffusion).
- For text in the image, quote it exactly and keep it short.

---

## 7. Task → tier cheat sheet

| Task | Tier | Mode | Why |
|------|------|------|-----|
| Current prices, listings, news | Default / balanced (Claude Sonnet 5.5) | **Web search on** (or Deep research for a full report) | Model memory is out of date; it needs live data |
| Market or competitor research report | Top reasoning | Deep research / Research | Many sources, synthesis |
| Hard maths, logic, strategy | Top reasoning | Thinking on | Benefits from deliberate reasoning |
| Complex coding / agentic coding | Complex or hardest tier (Claude Opus 5.5 / Fable 5.2) | Coding agent (Claude Code, Codex and others) | Long, multi-step work |
| Everyday writing, emails, summaries | Default / balanced (Claude Sonnet 5.5, GPT default, Gemini Flash, Grok Fast) | Standard | Fast and good enough |
| Long document or contract review | Top or balanced, with a large context | File upload / Projects | Needs the whole document in view |
| Bulk classification or extraction (API) | Fastest (Claude Haiku 5.5, mini/nano, Flash-Lite) | Batch | Cheap and fast at scale |
| Social trends, X sentiment | Grok | X search | Direct access to X data |
| Images | The platform's image model | Image generation | Different prompt style (see §6) |
