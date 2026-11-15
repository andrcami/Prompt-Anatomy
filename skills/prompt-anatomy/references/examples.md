# Worked Examples

Before/after examples showing the full flow. Use them to calibrate how many questions to ask, how specific they should be, and what the delivered prompt looks like on each platform.

---

## Example 1: Shopping research (Claude)

**User:** find me the prices of cars in Malta

**Questions:**
> To get you useful prices rather than a generic overview, a few quick questions. Answer with numbers/letters, or say "defaults":
>
> 1. **Goal:** a) buying b) selling or valuing c) market research (default: a)
> 2. **New or used?** a) new b) used c) both (default: c)
> 3. **Budget and type:** e.g. "under €20k, small SUV" (default: any, grouped by type)
> 4. **Must-haves:** fuel (petrol/diesel/hybrid/EV), automatic, max age or mileage? (default: none)
> 5. **Output:** a) specific listings with links b) typical price ranges by model c) both (default: c)

**User:** buying, used, under 15k, automatic hatchback, defaults for the rest

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

**Run it on:** Claude Opus 5.5 (or Sonnet 5.5 for speed) with **web search on**, because prices change daily and model memory is out of date.

**Assumptions:** personal use, any fuel type, no maximum mileage.

Want me to run it now?
````

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
**Run it on:** ChatGPT's default model. Writing doesn't need a reasoning model.

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
