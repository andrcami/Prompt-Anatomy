# Contributing to Prompt Anatomy

Contributions are welcome: better questions for a task type, platform and model
updates, new before/after examples, new eval cases, and fixes to the portable
prompts.

## How it works

1. **Open an issue first** for anything larger than a small fix, so we can agree
   on the approach before you build it.
2. **Fork** the repository and work on a branch in your fork.
3. **Open a pull request** against `main`. Fill in the template.
4. **Review.** Every pull request is reviewed and approved by the maintainer
   (@andrcami) before it merges, and the **Validate** workflow must pass. Expect
   questions: the skill is a set of instructions, and a small wording change can
   change how it behaves.

## Before you open the PR

```bash
claude plugin validate . --strict
claude plugin validate plugins/prompt-anatomy --strict --profile directory
./scripts/build.sh           # builds dist/prompt-anatomy.zip and dist/portable/
```

`./scripts/validate.sh` runs all of these plus the static skill checks in one go
(it also needs `skillevaluator` on your PATH). The **Validate** workflow runs it
on every pull request.

If you changed anything in `plugins/prompt-anatomy/skills/`, also run the evals
your change affects and paste the result in the PR:

```bash
claude plugin eval plugins/prompt-anatomy
```

This uses your own Claude Code session, which counts against your plan's usage.

## Ground rules

- **Keep the three copies in step.** A change to the skill's behaviour in
  `SKILL.md` usually needs the same change in `portable/system-prompt.md` and,
  if it fits, `portable/custom-instructions-short.txt`.
- **Model names go in one place.** Model ladders and names live in
  `references/platforms.md`. Update its "Last reviewed" date when you change them.
  Never add a model name you can't link to a provider's own page.
- **No personal data.** Examples and eval cases use invented requests, never a
  real person's or client's details.
- **Don't rename the plugin.** `prompt-anatomy` is its published name. Change
  `displayName` instead.
- **Bump the version** in `plugins/prompt-anatomy/.claude-plugin/plugin.json`
  when installed copies need your change, and add release notes under
  `.github/release-notes/`.
- **Keep PRs focused.** One concern per pull request.

## Conduct

Everyone taking part is expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Licence

By contributing, you agree that your contribution is licensed under the MIT
licence in [LICENSE](LICENSE).
