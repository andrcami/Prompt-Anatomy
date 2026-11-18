# SkillEvaluator Validation Report

**Status:** ⚠️ INCOMPLETE
**Publication status:** ⚠️ INCOMPLETE
**Profile:** default
**Policy digest:** `sha256:64a069b8853f7123049a675d6853ef8d8b424792bb9a2a5157a73ec312f38ed4`
**Quality config:** packaged, `sha256:2b34707afbb1b7b88df35e84b2b59d613943c62bfda7f2f82bc31b28b44f1af0`, min score 70
**Generated:** November 18, 2026 at 08:01 PM UTC

## Summary

| Metric | Value |
|--------|-------|
| Validator Results | 13 |
| Validators Run | 13 |
| ✅ Passed | 12 |
| ❌ Failed | 0 |
| ⚠️ Incomplete | 1 |
| Total Issues | 17 unique findings (3 medium) / 17 occurrences / 17 raw records; 1 error and 1 warning without a finding |
| Duplicate Occurrences Reconciled | 0 |

## Finding Reconciliation

| Finding ID | Severity | Finding | Occurrences | Validators |
|------------|----------|---------|-------------|------------|
| `SEF-2ab016a817c566724ba9` | MEDIUM | Missing recommended section: '&#35;&#35; Instructions' | 1 | Schema &amp; Repository Governance |
| `SEF-ae34d15e5c2826a704ff` | MEDIUM | Large skill: ~5871 estimated tokens at 4 characters per token, recommended max &lt;5000; a real tokenizer may count more | 1 | QUALITY |
| `SEF-e3f5c930756d6b8f695b` | MEDIUM | Missing recommended section: '&#35;&#35; Examples' | 1 | Schema &amp; Repository Governance |
| `SEF-378f24adfec67572e606` | LOW | No troubleshooting section documented | 1 | QUALITY |
| `SEF-4a6560f4aec006f302f9` | LOW | No prerequisites/requirements documented | 1 | QUALITY |
| `SEF-4d189b04fc5adbe42dce` | LOW | openclaw: SKILL.md reads as 23,584 characters (OpenClaw counts each CJK character as 4 or more), over the read cap for this setup: the read is refused or returns a cut prefix with a truncation notice. The cap depends on the model context (16,000 under 100K tokens, 32,000 under 200K, 64,000 above; custom providers default to 128K). Pass --context-tokens to check your setup. | 1 | Harness Compatibility |
| `SEF-9612bbfb3f32d491ac5d` | LOW | No mention of error handling or validation | 1 | QUALITY |
| `SEF-9a27cfde1ceda751f98f` | LOW | Description very long (recommend 50-150 chars): 988 chars, maximum 200 | 1 | QUALITY |
| `SEF-a6bd67456182a161d726` | LOW | Description has its trigger at characters 557-568; some harnesses show only the first ~60 characters in their skill list | 1 | Schema &amp; Repository Governance |
| `SEF-b6533ad44b39dbc6d0d2` | LOW | No '&#35;&#35; Purpose' section | 1 | QUALITY |
| ... | | *7 more unique findings* | | |

## Quality Score

| Skill | Score | Grade | Type | Correctness | Discoverability | Reliability | Efficiency |
|-------|-------|-------|------|-------------|-----------------|-------------|------------|
| prompt-anatomy | 89.0 | B | resource-based | 100.0 | 90.0 | 75.0 | 85.0 |

## Results

### ✅ Schema & Repository Governance
*Validate SKILL.md frontmatter and repository structure*

- [OK] **manifest_exists**: Found skill manifest: SKILL.md
- [OK] **frontmatter_valid**: Valid frontmatter for skill 'prompt-anatomy'
- [OK] **folder_hierarchy**: Valid general skill structure: skills/prompt-anatomy/
- [OK] **naming_convention**: Folder name 'prompt-anatomy' follows kebab-case convention
- [OK] **line_count**: SKILL.md within line limit (256/500)
- [OK] **body_heading**: Body contains a top-level heading
- [OK] **optional_files**: Found optional supporting files: agents, assets, references
- [OK] **name_consistency**: Directory name matches frontmatter: 'prompt-anatomy'

**Non-blocking findings: 5**

| Severity | Issue | Location |
|----------|-------|----------|
| [MED] MEDIUM | Missing recommended section: '## Instructions' | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [MED] MEDIUM | Missing recommended section: '## Examples' | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [LOW] LOW | Unexpected 'LICENSE' in skill root | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/LICENSE</code> |
| [INFO] INFO | Author has no email address: andrcami | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [LOW] LOW | Description has its trigger at characters 557-568; some harnesses show only the first ~60 characters in their skill list | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |

<details>
<summary>View Details</summary>

**1. Missing recommended section: '## Instructions'**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `body_recommended_section`
- Finding ID: `SEF-2ab016a817c566724ba9`
- Occurrence ID: `SEO-bececce9c87a52c03138`
- Fix: Consider adding a '## Instructions' or '## Usage' section. Per agentskills.io the body format is unrestricted, so this is a convention nudge — it also gives the quality scorer a stable anchor for instruction-quality heuristics.

**2. Missing recommended section: '## Examples'**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `body_recommended_section`
- Finding ID: `SEF-e3f5c930756d6b8f695b`
- Occurrence ID: `SEO-b58c8d0148739e2f99d5`
- Fix: Consider adding a '## Examples' section. If examples are already inline under instructions, this can be skipped.

**3. Unexpected 'LICENSE' in skill root**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/LICENSE`
- Check: `unexpected_file`
- Finding ID: `SEF-e325ebce0d51ecd2e4d3`
- Occurrence ID: `SEO-ee98ff3ad4ee60744543`
- Fix: Consider moving to one of: agents/, assets/, config/, evals/, references/, scripts/, tests/, tools/. To allow additional directories, set $SKILLEVALUATOR_SCHEMA_ALLOWED_DIRS.

**4. Author has no email address: andrcami**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `author_without_email`
- Finding ID: `SEF-1f1bf3e8bcbcc5bec038`
- Occurrence ID: `SEO-9a451cea630270520ed8`
- Content: `author: andrcami`
- Fix: A name is accepted as attribution unless the profile requires a contact address (such as 'registry'); then use 'Name <email@example.com>'

**5. Description has its trigger at characters 557-568; some harnesses show only the first ~60 characters in their skill list**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `description_trigger`
- Finding ID: `SEF-a6bd67456182a161d726`
- Occurrence ID: `SEO-083fad1db4d3c3e5bcd1`
- Fix: State when to use the skill within the first 60 characters

</details>


### ✅ Semantic Version Validation
*Validate optional metadata.version labels and require strict bumps*

- [OK] **version_semver**: Valid semantic version: 1.1.0

### ⚠️ INCOMPLETE Security Scan
*Detect security vulnerabilities and PII/secrets*

**Incomplete scanners:** skillspector

**1 errors, 0 warnings**

**Execution errors:**

- ❌ skillspector JSON component inventory contradicts analysis completeness; security scan did not complete


### ✅ PII Scan
*Detect PII and local identifiers*

- [OK] **pii_scan_start**: Scanning 6 files for PII
- [OK] **pii_detection**: No PII detected in 6 files (emails, SSNs, phone numbers, paths)

### ✅ License Compliance
*Validate license compliance for Skills, Rules, and Workflows*

- [OK] **license_compliance**: License compliance scan completed (allowed)

### ✅ Code Risk Analysis
*Static code analysis using Bandit and packaged Semgrep rules*

- [OK] **code_file_discovery**: No code files found - code risk analysis is not applicable

### ✅ Secrets Detection
*Detect hardcoded secrets, API keys, and credentials using Gitleaks*

- [OK] **gitleaks**: No secrets detected by Gitleaks

### ✅ Code Integrity & Hygiene
*Validate dead links, dependencies, and static Python test-file discovery*

- [OK] **dead_links_scan**: Checking 5 markdown files for dead links
- [OK] **dead_links**: All relative links valid in 5 markdown file(s)
- [OK] **dependencies**: No dependency files found (requirements.txt, pyproject.toml)
- [OK] **test_discovery**: No standard Python test-file candidates found; target tests were not executed and coverage was not measured. Consider adding tests.

### ✅ Dependency Vulnerability Audit
*Scan dependencies for CVE vulnerabilities using pip-audit and Safety*

- [OK] **dependency_file_discovery**: No dependency files found - vulnerability audit is not applicable

### ✅ Unicode Smuggling Detection
*Detect invisible Unicode characters and ASCII smuggling*

- [OK] **unicode_scan**: No invisible Unicode characters detected in 6 file(s)

### ✅ B QUALITY
*Skill quality scoring across Correctness (35%), Discoverability (25%), Reliability (25%), and Efficiency (15%)*

**Overall: 89.0/100 (Grade: B)** | Skill Type: resource-based

| Dimension | Score | Weight |
|-----------|-------|--------|
| Correctness | 100.0 | 35% |
| Discoverability | 90.0 | 25% |
| Reliability | 75.0 | 25% |
| Efficiency | 85.0 | 15% |

- [OK] **quality_score**: Score: 89.0/100 (Grade: B)

**Non-blocking findings: 7**

| Severity | Issue | Location |
|----------|-------|----------|
| [LOW] LOW | Description very long (recommend 50-150 chars): 988 chars, maximum 200 | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [LOW] LOW | No '## Purpose' section | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [LOW] LOW | No mention of error handling or validation | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [LOW] LOW | No prerequisites/requirements documented | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [LOW] LOW | No limitations documented | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [LOW] LOW | No troubleshooting section documented | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [MED] MEDIUM | Large skill: ~5871 estimated tokens at 4 characters per token, recommended max &lt;5000; a real tokenizer may count more | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |

<details>
<summary>View Details</summary>

**1. Description very long (recommend 50-150 chars): 988 chars, maximum 200**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `quality_discoverability`
- Finding ID: `SEF-9a27cfde1ceda751f98f`
- Occurrence ID: `SEO-c8c17679c18dd7997ded`
- Fix: Keep descriptions concise for progressive disclosure

**2. No '## Purpose' section**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `quality_discoverability`
- Finding ID: `SEF-b6533ad44b39dbc6d0d2`
- Occurrence ID: `SEO-5ddc593a53bd5739caa0`
- Fix: Add purpose section to clarify use cases

**3. No mention of error handling or validation**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `quality_reliability`
- Finding ID: `SEF-9612bbfb3f32d491ac5d`
- Occurrence ID: `SEO-db6facf0bb0ff35d0a7c`
- Fix: Document expected errors and how to handle them

**4. No prerequisites/requirements documented**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `quality_reliability`
- Finding ID: `SEF-4a6560f4aec006f302f9`
- Occurrence ID: `SEO-4aba1fb37f24f184c5ce`
- Fix: Document dependencies, API keys, or setup needed

**5. No limitations documented**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `quality_reliability`
- Finding ID: `SEF-fc6fe3747c071963a76e`
- Occurrence ID: `SEO-8562d017d138ba3a8dc9`
- Fix: Add '## Limitations' section with known issues/constraints

**6. No troubleshooting section documented**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `quality_reliability`
- Finding ID: `SEF-378f24adfec67572e606`
- Occurrence ID: `SEO-a47d52bbcc7eeda27a60`
- Fix: Add '## Troubleshooting' with Error/Cause/Solution patterns

**7. Large skill: ~5871 estimated tokens at 4 characters per token, recommended max <5000; a real tokenizer may count more**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `quality_efficiency`
- Finding ID: `SEF-ae34d15e5c2826a704ff`
- Occurrence ID: `SEO-7d9fc2dd0db737bde6f9`
- Fix: Per agentskills.io, SKILL.md should be concise (~500 lines) — large skill bodies increase token cost after invocation; long or unfocused top-level descriptions can degrade agent routing accuracy. Keep required sections concise; move detailed examples, reference material, and supporting docs to the references/ directory

</details>


### ✅ SCRIPT_LINT
*AST-based code quality checks for skill scripts*

- [OK] **lint**: No scripts/ or tools/ directory found

### ✅ Harness Compatibility
*Advisory: whether each agent harness loads, degrades or drops the skill*

- All checks passed

**Non-blocking findings: 5**

| Severity | Issue | Location |
|----------|-------|----------|
| [INFO] INFO | copilot-cli: New skills appear only after &#96;/skills reload&#96; or a restart; edits to existing skills apply at once. | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [INFO] INFO | hermes: The skill list shows only the first ~60 chars of the description (57 + '...' in 0.16, a word boundary near 59 on main), and the trigger isn't in them. | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [INFO] INFO | hermes: 2 files outside references/, templates/, assets/ and scripts/ (LICENSE, agents) are left out of the skill's file list; the model finds them only if SKILL.md names their paths. | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [LOW] LOW | openclaw: SKILL.md reads as 23,584 characters (OpenClaw counts each CJK character as 4 or more), over the read cap for this setup: the read is refused or returns a cut prefix with a truncation notice. The cap depends on the model context (16,000 under 100K tokens, 32,000 under 200K, 64,000 above; custom providers default to 128K). Pass --context-tokens to check your setup. | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [INFO] INFO | opencode: Skill list and text are cached at startup; edits need a restart. | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |

<details>
<summary>View Details</summary>

**1. copilot-cli: New skills appear only after `/skills reload` or a restart; edits to existing skills apply at once.**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `CP-RELOAD`
- Finding ID: `SEF-3661379ea9e5c1072875`
- Occurrence ID: `SEO-c8cf615750a5322b23b0`

**2. hermes: The skill list shows only the first ~60 chars of the description (57 + '...' in 0.16, a word boundary near 59 on main), and the trigger isn't in them.**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `HM-DESC-60`
- Finding ID: `SEF-e0623bdfb91d6bbb829f`
- Occurrence ID: `SEO-de024a9f9f389aab924a`
- Fix: Put the trigger ("Use when …") in the first 57 characters.

**3. hermes: 2 files outside references/, templates/, assets/ and scripts/ (LICENSE, agents) are left out of the skill's file list; the model finds them only if SKILL.md names their paths.**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `HM-LINKED-LAYOUT`
- Finding ID: `SEF-477c405c4d5a50638977`
- Occurrence ID: `SEO-700b97ea9452fb5f98a9`
- Fix: Move supporting files under references/, templates/, assets/ or scripts/.

**4. openclaw: SKILL.md reads as 23,584 characters (OpenClaw counts each CJK character as 4 or more), over the read cap for this setup: the read is refused or returns a cut prefix with a truncation notice. The cap depends on the model context (16,000 under 100K tokens, 32,000 under 200K, 64,000 above; custom providers default to 128K). Pass --context-tokens to check your setup.**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `OW-READ-BUDGET`
- Finding ID: `SEF-4d189b04fc5adbe42dce`
- Occurrence ID: `SEO-c36ad0e87d946bf0d49a`
- Fix: Keep SKILL.md under about 15,000 characters (about 3,700 CJK characters); move detail into references/ files.

**5. opencode: Skill list and text are cached at startup; edits need a restart.**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `OC-RELOAD`
- Finding ID: `SEF-03e029934351881ba688`
- Occurrence ID: `SEO-3a644a6cbd43de8704ab`

</details>


---
*Generated by SkillEvaluator*