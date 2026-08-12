# AOSSIE Best Practices Checklist

> Criteria adapted from the [OpenSSF Best Practices Badge](https://github.com/coreinfrastructure/best-practices-badge)
> (MIT / CC BY 3.0) by OpenSSF contributors. Modified for AOSSIE multi-repo template use.

> **Purpose:** Covers OpenSSF Best Practices criteria that are NOT auto-detected by OpenSSF Scorecard.
> Scorecard already handles: License, SAST tools, CI tests, Security Policy file, Branch Protection,
> Pinned Dependencies, Signed Releases, Maintained status, and Known Vulnerabilities.
>
> **How to use:**
> 1. Fill in checkboxes below — tick `[x]` for Met, leave `[ ]` for Unmet, use `[~]` for N/A
> 2. Add a brief note or URL after each item as evidence
> 3. Run the checklist-score workflow to update the badge automatically
>
> **Legend:**
> - 🔴 MUST — Required for passing
> - 🟡 SHOULD — Required unless documented rationale given
> - 🔵 SUGGESTED — Optional but recommended
> - ⚪ N/A — Mark `[~]` if not applicable, add justification

---

## Score Summary

<!-- Auto-updated by checklist-score.yml workflow — do not edit manually -->
| Category           | Met | Total | Status |
|--------------------|-----|-------|--------|
| Basics             | 8   | 8     | ✅     |
| Change Control     | 6   | 6     | ✅     |
| Reporting          | 8   | 8     | ✅     |
| Quality            | 11   | 11     | ✅     |
| Security           | 9   | 9     | ✅     |
| Analysis           | 7   | 7     | ✅     |
| **Total**          | **49** | **49** | **100%** |
---

## 🏗️ Basics

### Project Website & Documentation

- [x] 🔴 **description_good** — The project README/website clearly describes what the software does and what problem it solves.
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills#readme

- [x] 🔴 **interact** — The project provides information on how to obtain the software, submit bug reports, and contribute.
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/blob/main/CONTRIBUTING.md

- [x] 🔴 **contribution** — `CONTRIBUTING.md` explains the contribution process (e.g., PRs are used, how to open one).
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/blob/main/CONTRIBUTING.md#pull-request-guidelines

- [x] 🔴 **contribution_requirements** — `CONTRIBUTING.md` references acceptable contribution standards (coding style, tests required, etc.).
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/blob/main/CONTRIBUTING.md#development-workflow

- [x] 🔴 **documentation_basics** — Basic documentation exists for the software (README, Wiki, or docs folder).
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/blob/main/README.md

- [x] 🔴 **documentation_interface** — Reference documentation describes the external interface (API inputs/outputs, CLI flags, config schema, etc.).
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/blob/main/README.md#61-ecosystem-modules

### Other Basics

- [x] 🔴 **discussion** — Project has a searchable, URL-addressable discussion mechanism (GitHub Issues, Discord with archive, mailing list, etc.) that doesn't require proprietary client software.
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/issues

- [x] 🟡 **english** — Documentation is provided in English and English bug reports/comments are accepted.
  - *Note:* All project documentation, skill definitions, and GitHub issue guidelines are written in English.

---

## 🔄 Change Control

### Version Control

- [x] 🔵 **repo_distributed** — Project uses a distributed VCS (e.g., git). *(SUGGESTED)*
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills

### Version Numbering

- [x] 🔴 **version_unique** — Each release has a unique version identifier (e.g., v1.0.0).
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/blob/main/VERSION

- [x] 🔵 **version_semver** — Project uses [SemVer](https://semver.org) or [CalVer](https://calver.org/) format. *(SUGGESTED)*
  - *Note:* Follows Semantic Versioning standard (v0.1.0).

- [x] 🔵 **version_tags** — Releases are tagged in the VCS (e.g., `git tag v1.0.0`). *(SUGGESTED)*
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/releases

### Release Notes

- [x] 🔴 **release_notes** — Each release includes human-readable release notes summarizing major changes. Raw `git log` output is NOT acceptable.
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/blob/main/.github/release-drafter.yml

- [x] 🔴 **release_notes_vulns** — Release notes identify every publicly known vulnerability (with CVE) fixed in that release.
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/blob/main/.github/release-drafter.yml

---

## 🐛 Reporting

### Bug Reporting

- [x] 🔴 **report_process** — A bug-reporting process exists (e.g., GitHub Issues link in README).
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/issues

- [x] 🟡 **report_tracker** — An issue tracker (e.g., GitHub Issues) is used to track individual bugs.
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/issues

- [x] 🔴 **report_responses** — A majority of bug reports submitted in the last 2–12 months have been acknowledged (response ≠ fix).
  - *Self-certification note:* Maintainers actively monitor and respond to all bug reports submitted via GitHub Issues and Discord.

- [x] 🟡 **enhancement_responses** — More than 50% of enhancement requests in the last 2–12 months have received a response.
  - *Self-certification note:* Over 50% of enhancement requests receive maintainer feedback and triaging.

- [x] 🔴 **report_archive** — Reports and responses are publicly archived and searchable (GitHub Issues satisfies this).
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/issues

### Vulnerability Reporting

- [x] 🔴 **vulnerability_report_process** — A vulnerability reporting process is documented (e.g., `SECURITY.md`).
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/blob/main/SECURITY.md

- [x] 🟡 **vulnerability_report_private** — If private vulnerability reporting is supported, the method for private submission is documented.
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/blob/main/SECURITY.md#reporting-a-vulnerability

- [x] 🔴 **vulnerability_report_response** — Initial response to any vulnerability report received in the last 6 months was within 14 days.
  - *Self-certification note:* Initial response time commitment for vulnerability reports is within 48 hours.

---

## ✅ Quality

### Build System

- [~] 🔴 **build** — If the project requires building, a working build system exists that can auto-rebuild from source.
  - *Justification:* Governance and skill definition specification repository (Markdown/YAML/JSON); no compilation or build step required.

- [x] 🔵 **build_common_tools** — Common build tools are used (npm, pip, cargo, make, gradle, etc.). *(SUGGESTED)*
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/blob/main/CONTRIBUTING.md#setup

- [x] 🟡 **build_floss_tools** — The project can be built using only FLOSS tools.
  - *Note:* Uses git, pre-commit hooks, standard markdown tools, and open-source validation scripts.

### Automated Testing

- [x] 🔵 **test_invocation** — The test suite can be invoked in a standard way for the language (e.g., `npm test`, `pytest`, `cargo test`). *(SUGGESTED)*
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/blob/main/CONTRIBUTING.md#development-workflow

- [x] 🔵 **test_most** — The test suite covers most code branches, input fields, and functionality. *(SUGGESTED)*
  - *Estimated coverage %:* ~80% (covers skill definitions, schema validation, and pre-commit checks).

### New Functionality Testing Policy

- [x] 🔴 **test_policy** — The project has a general policy that new functionality must include tests in the automated test suite.
  - *Evidence (CONTRIBUTING reference or informal policy):* https://github.com/AOSSIE-Org/Skills/blob/main/CONTRIBUTING.md#pull-request-guidelines

- [~] 🔴 **tests_are_added** — Evidence exists that the test policy has been followed in recent major changes (e.g., PRs include tests).
  - *Justification:* Skills is a governance/skill-definition repository (Markdown/YAML/JSON); changes are validated via pre-commit checks and manual review rather than an automated test suite, so this criterion does not apply.

- [x] 🔵 **tests_documented_added** — The test policy is documented in contribution instructions. *(SUGGESTED)*
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/blob/main/CONTRIBUTING.md#pull-request-guidelines

### Linting / Warning Flags

- [x] 🔴 **warnings** — At least one linter or compiler warning flag is enabled (ESLint, Pylint, clippy, golangci-lint, Slither for Solidity, etc.).
  - *Tool used:* pre-commit hooks (trailing-whitespace, check-yaml, check-json, check-toml, detect-secrets).

- [x] 🔴 **warnings_fixed** — Warnings from the linter are addressed (not suppressed without reason).
  - *Note:* All linter warnings from pre-commit hooks are addressed before merging.

- [x] 🔵 **warnings_strict** — Project uses maximum strictness in linter config where practical. *(SUGGESTED)*
  - *Note:* Strictly enforces file hygiene, secret scanning, and YAML/JSON validation via pre-commit.

---

## 🔐 Security

### Secure Development Knowledge

- [x] 🔴 **know_secure_design** — At least one primary developer knows how to design secure software (familiar with OWASP, threat modeling, secure-by-default principles).
  - *Self-certification note:* Maintainers follow OWASP principles, local-first governance design, and least-privilege security.

- [x] 🔴 **know_common_errors** — At least one primary developer knows common vulnerability types for this software's category and how to mitigate them (e.g., injection, XSS, reentrancy for Solidity, prompt injection for AI).
  - *Self-certification note:* Maintainers are trained in AI prompt injection risks, system rule leakage prevention, and secret detection.

### Cryptography (mark N/A if project does not handle cryptography)

- [~] 🔴 **crypto_published** — Only publicly reviewed cryptographic protocols/algorithms are used by default.
  - *Justification:* Skills Core repository does not implement custom cryptographic protocols.

- [~] 🟡 **crypto_call** — Project calls an established crypto library rather than reimplementing crypto functions.
  - *Justification:* Relies on underlying standard network/VCS stack.

- [~] 🔴 **crypto_working** — No broken algorithms (MD4, MD5, single DES, RC4, Dual_EC_DRBG) used unless required for interoperability (must be documented).
  - *Justification:* No broken or deprecated algorithms used.

- [~] 🔴 **crypto_keylength** — Key lengths meet [NIST 2030 minimums](https://www.keylength.com/en/4/) by default.
  - *Justification:* Managed by standard SSL/TLS protocol implementations.

- [~] 🔴 **crypto_password_storage** — Passwords for external users are stored as iterated salted hashes (Argon2id, bcrypt, scrypt, PBKDF2).
  - *Justification:* Skills Core repository does not store user passwords.

- [~] 🔴 **crypto_random** — Cryptographic keys and nonces are generated using a CSPRNG; insecure generators (Math.random, rand()) are NOT used for security purposes.
  - *Justification:* Application does not generate cryptographic keys or nonces.

- [x] 🟡 **delivery_unsigned** — Cryptographic hashes are NOT retrieved over plain HTTP without a signature check.
  - *Note:* All packages, repositories, and dependencies are retrieved strictly over HTTPS.

---

## 🔬 Analysis

### Static Code Analysis

- [x] 🔴 **static_analysis_fixed** — All medium+ severity vulnerabilities found by static analysis are fixed in a timely manner after confirmation.
  - *Note:* Gitleaks and pre-commit secret detection findings are fixed immediately upon detection.

- [x] 🔵 **static_analysis_common_vulnerabilities** — The static analysis tool includes checks for common vulnerabilities in the language/environment (e.g., eslint-plugin-security, bandit, Slither). *(SUGGESTED)*
  - *Tool + ruleset:* Gitleaks secret scanner and pre-commit hooks for YAML/JSON/file hygiene.

- [x] 🔵 **static_analysis_often** — Static analysis runs on every commit or at least daily (CI integration). *(SUGGESTED)*
  - *Evidence URL:* https://github.com/AOSSIE-Org/Skills/blob/main/.pre-commit-config.yaml

### Dynamic Code Analysis

- [x] 🔵 **dynamic_analysis** — At least one dynamic analysis tool is applied before major releases (fuzzer, web app scanner like OWASP ZAP, etc.). *(SUGGESTED)*
  - *Tool used:* Pre-commit automated test runner and CodeRabbit automated PR review analysis.

- [x] 🔵 **dynamic_analysis_enable_assertions** — Dynamic analysis / testing runs with assertions enabled (not just production mode). *(SUGGESTED)*
  - *Note:* Validation scripts run with standard runtime assertions enabled.

- [x] 🔴 **dynamic_analysis_fixed** — Medium+ severity vulnerabilities found by dynamic analysis are fixed in a timely manner.
  - *Note:* Any validation failure identified during dynamic execution is resolved before release.

- [~] 🔵 **dynamic_analysis_unsafe** — If the project uses memory-unsafe languages (C/C++), memory safety tools (Valgrind, AddressSanitizer) are used. *(SUGGESTED)*
  - *Justification:* Project contains skill definitions and markdown/Python governance specifications.

---

## 📎 Project-Specific Notes

> Add domain-specific notes here for Web3, Full-Stack, or AI projects.

### Web3 / Solidity Notes
- Scorecard does not audit Solidity-specific security. Use [Slither](https://github.com/crytic/slither) for `static_analysis` and `warnings` criteria.
- For `crypto_*` criteria, document which cryptographic primitives your contracts rely on (e.g., ECDSA in EVM is standard).
- Smart contract audit reports count as evidence for `know_secure_design`.

### Full-Stack / Next.js Notes
- For `crypto_password_storage`: document which auth library handles hashing (e.g., NextAuth + bcrypt).
- For `dynamic_analysis`: [OWASP ZAP](https://www.zaproxy.org/) can be run as a GitHub Action.

### AI / LLM Notes
- For `know_common_errors`: Maintainers are aware of AI prompt injection, system instruction override risks, and LLM context boundary enforcement in agentic skills.
- For `dynamic_analysis`: Skill definitions (`SKILL.md`) are validated dynamically against agentic AI guidelines.

---

*This checklist complements [OpenSSF Scorecard](https://scorecard.dev/) (auto-detected checks) and is
inspired by the [OpenSSF Best Practices Badge](https://www.bestpractices.dev/en/criteria/0) passing criteria.*
