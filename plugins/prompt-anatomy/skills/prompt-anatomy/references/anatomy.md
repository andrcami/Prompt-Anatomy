# The Anatomy of a Prompt: Deep Guide and Question Banks

Read this file when you need more than the summary table in SKILL.md: when the task type is unfamiliar, when you're building a reusable or system prompt, or when the user wants to learn *why* each element matters.

## Contents
1. The elements in depth
2. Working instructions (added by you, not asked about)
3. Question banks by task type
4. Choosing which questions to ask
5. Prompt skeletons

---

## 1. The elements in depth

### Goal
What the user wants and **what they'll do with it**. The second half matters most. "Car prices" for a buyer needs listings and negotiation tips. For a seller it needs valuations. For an analyst it needs averages and trends. Ask about the decision or action the answer will support.

### Context
Who the user is and what surrounds the task: their expertise level, what they already know or tried, and why now. Context lets the model skip what the user already knows and pitch the answer at the right level. Rule of thumb: if a smart colleague would ask "wait, why do you need this?", the answer belongs in the prompt.

### Specifics and inputs
The concrete parameters: location, dates or time range, budget, quantities, names, versions, and the data or files the user has. This is usually where vague prompts fail hardest. Also ask whether the user has material to attach (a document, a spreadsheet, a draft, a screenshot).

### Role and audience
- **Role:** the expert lens the model should take ("act as a Malta-based car-buying advisor"). Even one sentence focuses tone and depth.
- **Audience:** who reads the output (the user, their boss, customers, children, developers). This sets vocabulary, depth and tone.

### Constraints
Hard rules: length limits, sources to use or avoid, tone, things to exclude, deadlines, legal or brand requirements. Write each one with its *reason* where possible. Models follow constraints better when they understand them, and can apply the spirit to cases the rule didn't foresee.

### Output format
The shape of the answer: a table (with which columns?), a bulleted summary, an email, a slide outline, JSON with given keys, code in a given language, a word count. Showing a skeleton beats describing one.

### Examples
One to five samples of good output, or of the input→output pattern. Examples are among the strongest ways to steer format and tone. Make them varied, so the model doesn't copy surface details, and label them clearly as examples. Optional for one-off questions; very valuable for reusable prompts.

### Success criteria
How the user will judge the result. "Done" might mean "I can compare five specific cars and know which to view this weekend". Stating this helps the model prioritize, and it helps the user see if the answer delivered.

---

## 2. Working instructions (you add these; don't ask the user)

Add whichever apply when you build the prompt:

- **Current information:** "Search the web for current [prices/listings/news]. Include the source and the date for each data point. Flag anything you couldn't verify."
- **Reasoning:** "Think through this step by step before answering." Or, on platforms with a thinking or reasoning mode, recommend turning it on.
- **Honesty:** "If you're unsure or the data isn't available, say so rather than estimating without saying so."
- **Clarification:** "If something important is ambiguous, ask me before proceeding." Useful for reusable or agent prompts.
- **Verification:** "Double-check calculations and make sure every listing link is real."
- **Structure for long inputs:** put documents first, wrapped in tags or delimiters, and the question last.

---

## 3. Question banks by task type

Pick the most relevant questions: up to 4 in round 1, and up to 3 follow-ups in an optional round 2 (see SKILL.md Step 2). Always offer 2–4 choices, with the recommended default first.

### Research, shopping and price comparison
- Buying, selling, or researching?
- Location or market (country, city, online-only?)
- New, used, or both? Budget range?
- Must-have features or specs; deal-breakers
- Preferred sources (official retailers, marketplaces, reviews) or ones to avoid
- Output: specific listings with links, typical price ranges, or a recommendation?
- How recent must the data be?

### Writing (emails, posts, articles, CVs, essays)
- Purpose: inform, persuade, apply, apologize, announce?
- Audience and their relationship to the user
- Tone: formal, friendly, bold, empathetic? Any brand voice?
- Length and channel (LinkedIn, email, print, website)
- Key points that must be included; things to avoid
- An existing draft or an example they like?

### Coding and technical
- Language, framework, versions, environment
- New code, a fix, a refactor, or an explanation?
- Existing code, error messages, or logs to share?
- Constraints: performance, dependencies allowed, style guide, tests required?
- Output: full file, diff, or snippet plus explanation?
- The user's experience level (affects how much explanation to give)

### Data analysis and spreadsheets
- What data (attach it?), and its size and columns
- The question to answer, or the decision it supports
- Tool: Excel, Google Sheets, Python, SQL?
- Output: a chart, a summary, a formula, a cleaned file?

### Image and video generation
- Subject and action; setting
- Style (photo, illustration, 3D, a named art movement), mood, colour palette
- Composition and camera (close-up, wide, angle), lighting
- Aspect ratio and resolution; text in the image?
- Things to exclude (negative prompt, where supported)

### Business and strategy (plans, pitches, marketing)
- Business type, stage, size, market and location
- Goal and time horizon; budget
- Target customer
- Existing assets or constraints (team, channels, brand)
- Output: a one-page plan, a detailed document, a slide outline, an action checklist?

### Learning and explanations
- Current level of knowledge
- Why they're learning it (exam, job, curiosity, a project)
- Preferred style: analogies, worked examples, quizzes, step-by-step
- Depth and time available

### Planning (travel, events, fitness, meals)
- Dates, duration, location, group size
- Budget
- Preferences and restrictions (diet, mobility, fitness level, interests)
- Output: a day-by-day itinerary, a checklist, a schedule table?

### System prompts, custom GPTs, Gems, Claude Projects and agents
- What the assistant is for, and who uses it
- Its scope: what it should and shouldn't handle
- Personality and tone
- Knowledge or files it relies on
- Tools it can use (web, code, files) and when to use them
- Output conventions
- How to handle uncertainty, off-topic requests and sensitive topics
- Example conversations showing ideal behaviour

---

## 4. Choosing which questions to ask

Rank the missing elements by **how much the answer would change** depending on the reply. Ask the top 4 in round 1, and use defaults for the rest. Good tie-breakers:

1. Goal and decision (changes everything)
2. Hard scope parameters (location, budget, dates, versions)
3. Output format (changes how usable the answer is)
4. Constraints and sources
5. Tone, audience and examples (often fine on a sensible default)

After round 1, re-check the gaps. Ask a second round (up to 3 follow-ups, built from round 1's answers, each with a "Use defaults" choice) only if what's still missing would change the answer. Never go beyond 2 rounds or 7 questions in total. Anything still open becomes a default, listed as an assumption. If the user answered round 1 with "defaults", skip round 2.

---

## 5. Prompt skeletons

### Generic (any platform; adapt the delimiters)
```
[Role: one sentence.]

Context:
[Who I am, why I need this, what I already know.]

Task:
[Clear statement of what to do.]

Requirements:
- [Specifics and scope]
- [Constraints, each with its reason]
- [Sources / search instructions if current info is needed]

Output format:
[Skeleton or description: table columns, sections, length]

Success looks like: [one line]
If anything important is unclear or unavailable, say so.
```

### Reusable system prompt
```
# Role and purpose
# Audience
# Scope (in / out)
# How to behave (rules with reasons)
# Tools and when to use them
# Output conventions
# Handling uncertainty, off-topic and sensitive requests
# Examples
```
