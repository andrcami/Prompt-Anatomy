# Installing Prompt Anatomy

Prompt Anatomy is a **skill**, not a connector. Connectors link an AI to outside services such as Gmail or Drive. Skills are instructions the AI loads when they're relevant. Find your platform below.

| Platform | How | Time |
|----------|-----|------|
| [Claude (web, desktop, mobile)](#claude-web-desktop-and-mobile) | Upload the skill (or add it from the Directory once listed) | 1 min |
| [Claude Code](#claude-code) | One command | 1 min |
| [ChatGPT](#chatgpt) | Custom GPT or Custom Instructions | 3 min |
| [Grok](#grok) | Project or Custom Instructions | 2 min |
| [Gemini](#gemini) | A Gem | 2 min |
| [Other tools](#other-tools) | System prompt / skills folder | 2 min |

---

## Claude (web, desktop and mobile)

**Option A: upload the skill**
1. Download `prompt-anatomy.zip` from the [latest release](https://github.com/andrcami/prompt-anatomy/releases), or build it yourself with `./scripts/build.sh` (it lands in `dist/`).
2. In Claude, open **Settings → Capabilities** and make sure **Skills** is turned on. On Team or Enterprise plans, an admin may need to allow skills first.
3. Click **Upload skill** and choose `prompt-anatomy.zip`.
4. It now appears in your skills list, where you can switch it on and off.

Menu names change between app versions. If it isn't under Capabilities, look for a **Skills** or **Customize** section in Settings.

**Option B: from the Directory** (once it's listed)
Open **[claude.ai/directory](https://claude.ai/directory)**, search "Prompt Anatomy", and click **Add**. The skill then also syncs to your Claude Code sessions.

**Make it trigger every time (recommended)**
Claude decides when to use a skill, and it sometimes answers simple-looking questions directly. For consistent behavior, add this line to **Settings → Profile** (your preferences) or to a Project's instructions:

> Before answering broad or underspecified requests, use the prompt-anatomy skill to ask me clarifying questions first, unless I say "just answer".

---

## Claude Code

Inside a session:
```
/plugin install prompt-anatomy --marketplace andrcami/prompt-anatomy
```
Or in two steps (works in older versions):
```
/plugin marketplace add andrcami/prompt-anatomy
/plugin install prompt-anatomy@prompt-anatomy
```
To get new versions, run `claude plugin update prompt-anatomy@prompt-anatomy`, or turn on auto-update for the marketplace in `/plugin`.

**Without the plugin system:** copy the folder into your skills directory.
```bash
git clone https://github.com/andrcami/prompt-anatomy
cp -r prompt-anatomy/skills/prompt-anatomy ~/.claude/skills/        # all projects
# or: cp -r prompt-anatomy/skills/prompt-anatomy .claude/skills/   # one project
```

**Use it:** type `/prompt-anatomy` (or `/prompt-anatomy:prompt-anatomy` when installed as a plugin), or just ask something vague and let it trigger. For always-on behavior, add the line from the Claude section above to your `CLAUDE.md`.

---

## ChatGPT

**Option A: a custom GPT (best)**
1. Go to **Explore GPTs → Create → Configure**.
2. Name: *Prompt Anatomy*. Paste the contents of [`portable/system-prompt.md`](portable/system-prompt.md) into **Instructions**.
3. Under **Capabilities**, turn on **Web Search**.
4. Optional: upload the files in `skills/prompt-anatomy/references/` as **Knowledge**.
5. Click **Create**, then choose who can see it: only you, anyone with the link, or the GPT Store.

**Option B: in every chat**
**Settings → Personalization → Custom instructions** → paste [`portable/custom-instructions-short.txt`](portable/custom-instructions-short.txt). It's under 1,500 characters, so it fits.

**Option C: a Project**
Create a Project and paste `portable/system-prompt.md` into its instructions.

---

## Grok

- **A Project:** create a Project and paste [`portable/system-prompt.md`](portable/system-prompt.md) into its instructions.
- **Every chat:** **Settings → Customize / Custom Instructions** → paste [`portable/custom-instructions-short.txt`](portable/custom-instructions-short.txt).

---

## Gemini

1. Open **Gems → New Gem**.
2. Name: *Prompt Anatomy*. Paste [`portable/system-prompt.md`](portable/system-prompt.md) into the instructions.
3. Optional: add the `references/*.md` files as knowledge.
4. Save. You can share the Gem by link.

---

## Other tools

- **Tools that read `SKILL.md` skills** (for example, OpenAI Codex, which reads `~/.codex/skills/`, and other agents that support the Agent Skills format): copy `skills/prompt-anatomy/` into that tool's skills folder.
- **Anything with a system prompt or custom instructions** (APIs, Copilot, Perplexity Spaces, local models): use `portable/system-prompt.md`.

---

## Uninstall

- **Claude:** Settings → Capabilities → Skills → remove it.
- **Claude Code:** `claude plugin uninstall prompt-anatomy@prompt-anatomy`, or delete `~/.claude/skills/prompt-anatomy`.
- **ChatGPT, Grok and Gemini:** delete the GPT, Project or Gem, or clear the custom instructions.
