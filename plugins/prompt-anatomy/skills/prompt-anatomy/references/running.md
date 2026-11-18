# Running the refined prompt

Read this once the user has answered the checkpoint (SKILL.md Step 5) and picked how to run the prompt.

## Contents
1. Rules for every run
2. Run it here
3. Run on [recommended model]
4. Compare 2 models
5. Other platforms (OpenAI, Grok, Gemini)
6. Adjust first

---

## 1. Rules for every run

- **Label the result.** Open the answer with a horizontal rule and a **Result** heading that names the model it ran on, e.g. **Result (Claude Sonnet 5.5)**. That keeps the prompt kit and the answer clearly separate.
- **Follow the prompt's `<output_format>` exactly**: the same table columns, sections and order. The user agreed to that format at the checkpoint. If you deliberately deviate, for example because a column has no data, say so in one line.
- **Answer in the same reply.** When a subagent or another tool does the work, wait for it and post the result in the same reply. Don't say "I'll post it when it finishes" and end your turn, because the user would have to prompt you again to see the answer.
- **Missing tools.** If the task needs a tool you don't have (for example web search for current prices), say so plainly, and say where to paste the prompt instead (an assistant with web search). Don't present guesses as current facts.

## 2. Run it here (the default; cheapest)

Answer the refined prompt yourself, fully, as if the user had sent it. Use the tools it asks for (web search for current facts) and end with sources where the prompt asks for them.

## 3. Run on [recommended model]

Offer this only when the recommended tier differs from the current model **and** a subagent tool that accepts a model choice exists (e.g. the Agent tool's `model` parameter: `haiku`, `sonnet`, `opus`, `fable`).

1. Start the subagent on that tier.
2. Pass it the **full refined prompt** plus one line: "Answer this fully; use web search if the prompt asks for current facts; end with sources." The subagent starts cold, so the prompt must be self-contained.
3. The user never sees the subagent's report, so relay its full answer yourself, under **Result (model name)**.

## 4. Compare 2 models (uses about 2–3× resources)

Offer this only when you can reach more than one model. Use 3 models only if the user asks.

1. To avoid repeating work, do any web research **once**, first.
2. Give each model the same prompt plus the same findings, in parallel.
3. Show one section per model, each labelled **Result (model name)**.
4. End with a 2–3 line verdict on which answer was strongest and why. Say that this compares how the models reason and write, not how they search.

## 5. Other platforms (OpenAI, Grok, Gemini)

Run a prompt on another provider's model only through a connected tool that can call that model (directly or through a router such as OpenRouter). Use a browser only if the user explicitly asks, because it's slow and breaks easily. Otherwise, the right choice is "Just the prompt", and the user pastes it there.

## 6. Adjust first

The user says what to change. Update the prompt, show it again in a code block, then run it straight away with the option they chose before, without a second checkpoint.
