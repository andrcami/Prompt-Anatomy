#!/usr/bin/env bash
# Builds installable bundles into dist/:
#   prompt-anatomy.zip  - upload to Claude.ai (Settings > Capabilities > Skills) or unzip into ~/.claude/skills
#   portable/           - copy-paste versions for ChatGPT, Grok, Gemini and other assistants
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
(cd skills && zip -qr ../dist/prompt-anatomy.zip prompt-anatomy -x 'prompt-anatomy/evals/*')
cp -R portable dist/portable
echo "Built:"; ls -la dist dist/portable
