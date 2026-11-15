# Worked Examples

Before/after examples showing the full flow. Use them to calibrate how many questions to ask, how specific they should be, and what the delivered prompt looks like on each platform. They follow SKILL.md: at most two rounds of questions, a model plus a mode, a checkpoint before running, and a labelled **Result (model)**.

---

## Example 1: Shopping research (Claude)

**User:** find me the prices of cars in Malta

**Round 1 questions** (asked with the question widget, 4 at most, recommended choice first):
> 1. **Goal:** Buying (Recommended) · Selling or valuing · Market research
> 2. **New or used?** Used (Recommended) · New · Both
> 3. **Budget and type:** Under €15k, any type (Recommended) · €15–30k · Over €30k · *(or type your own, e.g. "under €20k, small SUV")*
> 4. **Output:** Listings with links + typical price ranges (Recommended) · Listings only · Price ranges only
>
> Without a question widget, ask the same questions as a numbered list with a default for each, and say the user can reply "defaults".

Re-check: transmission and body type would still change the answer, so a short round 2 is worth it (each follow-up includes "Use defaults"). If the user had answered "defaults", skip straight to delivery.

**User (after both rounds):** buying, used, under €15k, automatic hatchback, defaults for the rest

**Delivered:**

````
**Your refined prompt:**
```text
You are a car-buying advisor who knows the Maltese used-car market.

<context>
I live in Malta and want to buy a used automatic hatchback for personal use. My budget is up to €15,000 all-in.
</context>

<task>
Find current listings and typical prices for used automatic hatchbacks in Malta within my budget, so I can shortlist cars to view.
</task>

<requirements>
- Search the web for current listings on Maltese dealer websites and classified sites. Prices in EUR.
- For each car: make/model, year, mileage, fuel type, transmission, price, seller type (dealer/private), link, and the date you saw it.
- Note whether imported cars include registration tax, because that significantly changes the real cost in Malta.
- Only include listings you actually found. If you can't verify a price, say so instead of estimating.
</requirements>

<output_format>
1. A table of 8–12 listings, sorted by price.
2. A short "typical price ranges" summary by popular model (3–5 bullets).
3. Three practical tips for getting good value when buying used in Malta.
</output_format>
```

**Run it on:** Claude Sonnet 5.5 + **web search** — a single research question, so Sonnet is the right tier on the ladder; prices change daily, so search must be on.
**Go deeper:** Research mode for a dealer-by-dealer comparison. Don't use a model without search, because the prices would be stale.

**Assumptions I made:** personal use, any fuel type, no maximum mileage.

How do you want to continue? Run it here (Recommended) · Adjust first · Just the prompt
````

**User:** Run it here

**Result** (the answer always opens with a rule and a labelled heading, and follows the prompt's `<output_format>` exactly):

```
---
**Result (Claude Sonnet 5.5)**

| # | Make/model | Year | Mileage | ... |
```

---

## Example 2: Writing (ChatGPT)

**User:** write a linkedin post about my new job, I use chatgpt

**Questions (4, because the platform is known):**
> 1. **Role and company:** what's the new role and company? (needed)
> 2. **Tone:** a) professional and grateful b) excited and personal c) understated (default: a)
> 3. **Must mention:** thanks to anyone, what you'll work on, what you're leaving? (default: a brief thank-you to the previous team)
> 4. **Length:** a) short (≈50 words) b) medium (≈120 words) c) story-style (≈250 words) (default: b)

**Delivered prompt (OpenAI style, instructions first, `"""` delimiters):**
```text
Write a LinkedIn post announcing my new job. Use a professional, grateful tone and about 120 words. Write in the first person, with 1–2 short paragraphs and no more than 3 relevant hashtags at the end. Avoid clichés like "I'm thrilled to announce"; open with a specific detail instead.

Details:
"""
New role: Senior Data Analyst at Acme Logistics
Previous company: Beta Retail (3 years)
Mention: thanks to my Beta Retail team; I'll be working on supply-chain forecasting
"""

Give me 2 variations so I can choose.
```
**Run it on:** ChatGPT's default model + default chat. Writing doesn't need a reasoning model or search.

Then the checkpoint: Run it here (here = this conversation, if it's ChatGPT) · Adjust first · Just the prompt. When the prompt is meant for another platform, "Just the prompt" is the natural choice. Offer to run it here only if the current assistant can do the task as well.

---

## Example 3: Reviewing an existing prompt

**User:** improve this prompt: "You are an expert. NEVER be wrong. Write about marketing."

**Delivered:**
> **Main issues:**
> 1. No real goal: marketing for what, for whom, to achieve what?
> 2. "NEVER be wrong" can't be followed and gives no guidance. It's better to ask the model to flag uncertainty.
> 3. No format or length.
> 4. "Expert" is vague. Name the expertise.
>
> Two quick questions, or I'll use defaults: what's the business, and what's the output for (blog, plan, social posts)?

Then give the rewritten prompt, plus a one-line note on each change.

---

## Example 4: When NOT to step in

**User:** what's the boiling point of water at sea level in fahrenheit
→ Just answer: 212°F. No questions.

**User:** Write a 150-word formal email to my landlord, Mr. Borg, asking to fix the boiler in flat 3 by Friday; it's been broken since Monday.
→ Already specific. Just write it.

**User:** quick, no questions: ideas for a 10-year-old's birthday party
→ Answer directly, with one line stating the assumptions ("assuming indoors, ~10 kids, a moderate budget"), and end with "Want a tailored plan? Tell me the budget and interests."
