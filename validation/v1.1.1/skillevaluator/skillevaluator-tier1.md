# SkillEvaluator Validation Report

**Status:** ⚠️ INCOMPLETE
**Publication status:** ⚠️ INCOMPLETE
**Profile:** default
**Policy digest:** `sha256:64a069b8853f7123049a675d6853ef8d8b424792bb9a2a5157a73ec312f38ed4`
**Quality config:** packaged, `sha256:2b34707afbb1b7b88df35e84b2b59d613943c62bfda7f2f82bc31b28b44f1af0`, min score 70
**Generated:** November 18, 2026 at 08:39 PM UTC

## Summary

| Metric | Value |
|--------|-------|
| Validator Results | 13 |
| Validators Run | 13 |
| ✅ Passed | 12 |
| ❌ Failed | 0 |
| ⚠️ Incomplete | 1 |
| Total Issues | 6 unique findings / 6 occurrences / 6 raw records; 1 error and 1 warning without a finding |
| Duplicate Occurrences Reconciled | 0 |

## Finding Reconciliation

| Finding ID | Severity | Finding | Occurrences | Validators |
|------------|----------|---------|-------------|------------|
| `SEF-39677255abd0016bfce6` | LOW | Description very long (recommend 50-150 chars): 912 chars, maximum 200 | 1 | QUALITY |
| `SEF-e325ebce0d51ecd2e4d3` | LOW | Unexpected 'LICENSE' in skill root | 1 | Schema &amp; Repository Governance |
| `SEF-03e029934351881ba688` | INFO | opencode: Skill list and text are cached at startup; edits need a restart. | 1 | Harness Compatibility |
| `SEF-1f1bf3e8bcbcc5bec038` | INFO | Author has no email address: andrcami | 1 | Schema &amp; Repository Governance |
| `SEF-3661379ea9e5c1072875` | INFO | copilot-cli: New skills appear only after &#96;/skills reload&#96; or a restart; edits to existing skills apply at once. | 1 | Harness Compatibility |
| `SEF-477c405c4d5a50638977` | INFO | hermes: 2 files outside references/, templates/, assets/ and scripts/ (LICENSE, agents) are left out of the skill's file list; the model finds them only if SKILL.md names their paths. | 1 | Harness Compatibility |

## Quality Score

| Skill | Score | Grade | Type | Correctness | Discoverability | Reliability | Efficiency |
|-------|-------|-------|------|-------------|-----------------|-------------|------------|
| prompt-anatomy | 98.8 | A | resource-based | 100.0 | 95.0 | 100.0 | 100.0 |

## Results

### ✅ Schema & Repository Governance
*Validate SKILL.md frontmatter and repository structure*

- [OK] **manifest_exists**: Found skill manifest: SKILL.md
- [OK] **frontmatter_valid**: Valid frontmatter for skill 'prompt-anatomy'
- [OK] **folder_hierarchy**: Valid general skill structure: skills/prompt-anatomy/
- [OK] **naming_convention**: Folder name 'prompt-anatomy' follows kebab-case convention
- [OK] **line_count**: SKILL.md within line limit (166/500)
- [OK] **body_heading**: Body contains a top-level heading
- [OK] **body_recommended_section**: Found recommended section: '## Instructions' (or '## Usage')
- [OK] **body_recommended_section**: Found recommended section: '## Examples'
- [OK] **optional_files**: Found optional supporting files: agents, assets, references
- [OK] **name_consistency**: Directory name matches frontmatter: 'prompt-anatomy'

**Non-blocking findings: 2**

| Severity | Issue | Location |
|----------|-------|----------|
| [LOW] LOW | Unexpected 'LICENSE' in skill root | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/LICENSE</code> |
| [INFO] INFO | Author has no email address: andrcami | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |

<details>
<summary>View Details</summary>

**1. Unexpected 'LICENSE' in skill root**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/LICENSE`
- Check: `unexpected_file`
- Finding ID: `SEF-e325ebce0d51ecd2e4d3`
- Occurrence ID: `SEO-ee98ff3ad4ee60744543`
- Fix: Consider moving to one of: agents/, assets/, config/, evals/, references/, scripts/, tests/, tools/. To allow additional directories, set $SKILLEVALUATOR_SCHEMA_ALLOWED_DIRS.

**2. Author has no email address: andrcami**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `author_without_email`
- Finding ID: `SEF-1f1bf3e8bcbcc5bec038`
- Occurrence ID: `SEO-9a451cea630270520ed8`
- Content: `author: andrcami`
- Fix: A name is accepted as attribution unless the profile requires a contact address (such as 'registry'); then use 'Name <email@example.com>'

</details>


### ✅ Semantic Version Validation
*Validate optional metadata.version labels and require strict bumps*

- [OK] **version_semver**: Valid semantic version: 1.1.1

### ⚠️ INCOMPLETE Security Scan
*Detect security vulnerabilities and PII/secrets*

**Incomplete scanners:** skillspector

**1 errors, 0 warnings**

**Execution errors:**

- ❌ skillspector JSON component inventory contradicts analysis completeness; security scan did not complete


### ✅ PII Scan
*Detect PII and local identifiers*

- [OK] **pii_scan_start**: Scanning 8 files for PII
- [OK] **pii_detection**: No PII detected in 8 files (emails, SSNs, phone numbers, paths)

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

- [OK] **dead_links_scan**: Checking 7 markdown files for dead links
- [OK] **dead_links**: All relative links valid in 7 markdown file(s)
- [OK] **dependencies**: No dependency files found (requirements.txt, pyproject.toml)
- [OK] **test_discovery**: No standard Python test-file candidates found; target tests were not executed and coverage was not measured. Consider adding tests.

### ✅ Dependency Vulnerability Audit
*Scan dependencies for CVE vulnerabilities using pip-audit and Safety*

- [OK] **dependency_file_discovery**: No dependency files found - vulnerability audit is not applicable

### ✅ Unicode Smuggling Detection
*Detect invisible Unicode characters and ASCII smuggling*

- [OK] **unicode_scan**: No invisible Unicode characters detected in 8 file(s)

### ✅ A QUALITY
*Skill quality scoring across Correctness (35%), Discoverability (25%), Reliability (25%), and Efficiency (15%)*

**Overall: 98.8/100 (Grade: A)** | Skill Type: resource-based

| Dimension | Score | Weight |
|-----------|-------|--------|
| Correctness | 100.0 | 35% |
| Discoverability | 95.0 | 25% |
| Reliability | 100.0 | 25% |
| Efficiency | 100.0 | 15% |

- [OK] **quality_score**: Score: 98.8/100 (Grade: A)

**Non-blocking findings: 1**

| Severity | Issue | Location |
|----------|-------|----------|
| [LOW] LOW | Description very long (recommend 50-150 chars): 912 chars, maximum 200 | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |

<details>
<summary>View Details</summary>

**1. Description very long (recommend 50-150 chars): 912 chars, maximum 200**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `quality_discoverability`
- Finding ID: `SEF-39677255abd0016bfce6`
- Occurrence ID: `SEO-d30270bc1fe7ecf986a9`
- Fix: Keep descriptions concise for progressive disclosure

</details>


### ✅ SCRIPT_LINT
*AST-based code quality checks for skill scripts*

- [OK] **lint**: No scripts/ or tools/ directory found

### ✅ Harness Compatibility
*Advisory: whether each agent harness loads, degrades or drops the skill*

- All checks passed

**Non-blocking findings: 3**

| Severity | Issue | Location |
|----------|-------|----------|
| [INFO] INFO | copilot-cli: New skills appear only after &#96;/skills reload&#96; or a restart; edits to existing skills apply at once. | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [INFO] INFO | hermes: 2 files outside references/, templates/, assets/ and scripts/ (LICENSE, agents) are left out of the skill's file list; the model finds them only if SKILL.md names their paths. | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |
| [INFO] INFO | opencode: Skill list and text are cached at startup; edits need a restart. | <code>/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md</code> |

<details>
<summary>View Details</summary>

**1. copilot-cli: New skills appear only after `/skills reload` or a restart; edits to existing skills apply at once.**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `CP-RELOAD`
- Finding ID: `SEF-3661379ea9e5c1072875`
- Occurrence ID: `SEO-c8cf615750a5322b23b0`

**2. hermes: 2 files outside references/, templates/, assets/ and scripts/ (LICENSE, agents) are left out of the skill's file list; the model finds them only if SKILL.md names their paths.**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `HM-LINKED-LAYOUT`
- Finding ID: `SEF-477c405c4d5a50638977`
- Occurrence ID: `SEO-700b97ea9452fb5f98a9`
- Fix: Move supporting files under references/, templates/, assets/ or scripts/.

**3. opencode: Skill list and text are cached at startup; edits need a restart.**
- File: `/home/runner/work/Prompt-Anatomy/Prompt-Anatomy/plugins/prompt-anatomy/skills/prompt-anatomy/SKILL.md`
- Check: `OC-RELOAD`
- Finding ID: `SEF-03e029934351881ba688`
- Occurrence ID: `SEO-3a644a6cbd43de8704ab`

</details>


---
*Generated by SkillEvaluator*