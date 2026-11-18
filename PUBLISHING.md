# Publishing Prompt Anatomy

How to list this skill in each platform's store or directory. Checked 2026-11-15. Store rules change, so confirm on each platform before you submit.

## Before every release

- [ ] Bump `version` in `plugins/prompt-anatomy/.claude-plugin/plugin.json`. Users who already installed it only get the update if the version changes.
- [ ] `claude plugin validate . --strict` (marketplace) and `claude plugin validate plugins/prompt-anatomy --strict --profile directory` (plugin) both pass.
- [ ] `./scripts/build.sh` passes, and you've attached `dist/prompt-anatomy.zip` to a GitHub Release.
- [ ] Optional: `claude plugin eval plugins/prompt-anatomy` to re-run the test cases.

## 1. Claude: Anthropic's Directory (claude.ai, Cowork and Claude Code)

One listing reaches people on claude.ai, in Cowork and in Claude Code (where it syncs as `prompt-anatomy@synced`).

1. **Requirements:** a paid claude.ai plan (Pro, Max or Ultra; on Team or Enterprise, an Owner submits). The repo must be on GitHub, and should be **public** with this content on **`main`**.
2. Validate locally: `claude plugin validate plugins/prompt-anatomy --strict --profile directory`. When the portal asks for the plugin's location in the repo, give `plugins/prompt-anatomy`. It already passes, icon included. The portal also runs a safety scan and a policy review, which the CLI doesn't.
3. Read the [pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist) and the [component support table](https://claude.com/docs/plugins/platform-support). This plugin contains only a skill, which loads everywhere.
4. Submit at the developer portal: **[claude.ai/directory/manage](https://claude.ai/directory/manage)**. See [Submit a plugin](https://claude.com/docs/plugins/submit#submit-a-plugin).
5. Each version is reviewed before it's published. For later versions, see [Update a published plugin](https://claude.com/docs/plugins/submit#update-a-published-plugin).

Notes:
- The icon (`plugins/prompt-anatomy/.claude-plugin/icon.png`) becomes the listing icon **only the first time** you save or submit in the portal, so finalize it before then.
- Don't rename the plugin (`prompt-anatomy`) after it's published. Change `displayName` instead.
- Anthropic's own `claude-plugins-official` marketplace doesn't take open submissions.

**Already live, no review needed:** anyone can install from this repo as a self-hosted marketplace. See [INSTALL.md](INSTALL.md#claude-code).

## 2. ChatGPT: the GPT Store

ChatGPT doesn't install Claude-style skills, so publish the skill as a **custom GPT**:

1. Create the GPT as described in [INSTALL.md](INSTALL.md#chatgpt), using `portable/system-prompt.md`, with Web Search on.
2. Verify your **Builder Profile**: Settings → Builder profile. Verify a name (from billing) or a domain you own. Add links (GitHub) if you like.
3. Add conversation starters such as "Find me car prices in Malta", "Improve this prompt: …" and "Which model should I use for …?". Upload a profile picture (you can reuse `plugins/prompt-anatomy/.claude-plugin/icon.png`).
4. **Share → GPT Store**, choose a category (Productivity), and publish. Store listings require a paid plan and are subject to OpenAI's usage policies and review.

For coding agents, OpenAI Codex reads the same `SKILL.md` format, so people can copy `plugins/prompt-anatomy/skills/prompt-anatomy/` into `.agents/skills/` or `~/.codex/skills/`. The skill includes `agents/openai.yaml` (display name, short description, icon and default prompt for the Codex app). OpenAI also keeps a public skills catalog on GitHub ([openai/skills](https://github.com/openai/skills)). Check its contribution guidelines to see whether it accepts community submissions.

## 3. Grok

Grok now supports **Skills** (Settings → Skills → New Skill), and this skill works there unchanged, as tested on 2026-11-18. As of this writing there's **no public skills store** for Grok. Your options:
- Point people to `prompt-anatomy.zip` (attach it to a GitHub Release) and [INSTALL.md](INSTALL.md#grok).
- Share a Grok **Project** by link, if your plan allows it.
- Point people to `portable/` in this repo and [INSTALL.md](INSTALL.md#grok).
Check xAI's announcements, because a store may appear.

## 4. Gemini

Google has **no public store for Gems** as of this writing. You can **share a Gem by link** from the Gem manager, and people with the link can use or copy it.

## 5. Cross-platform skill directories

The `SKILL.md` format is an open standard (Agent Skills) used by several tools. Community-run skill directories and "awesome" lists on GitHub accept submissions, usually by pull request. Listing the repo there helps discovery across tools. Choose actively maintained lists, and follow each one's contribution rules.

## Promote it

- Use a clear README hero line and a before/after GIF of the Malta example.
- Add GitHub topics: `claude-skill`, `agent-skills`, `prompt-engineering`, `chatgpt`, `grok`, `gemini`.
- Share it with the Claude Code, ChatGPT and prompt-engineering communities.
