# Brand Guidelines

This document outlines the brand guidelines, visual identity, and communication tone for the **AOSSIE Skills Ecosystem**, of which this repository (**Skills Core**) is the central, organization-wide module.


## Visual Identity

### Logos and Assets

All official logos are stored in the [`/public`](./public) directory of this repository.

- **Skills Ecosystem Logo:** `/public/skills-logo.svg` — The primary logo for the project. A dark folder glyph with blurred red and blue "context" blobs and an orange highlight card, capped with pixel-art `SKILLS.MD` text. Represents the ecosystem's core idea: project knowledge (skills) captured and organized as living documentation. Use this as the primary mark for the Skills Core repository, since it is the ecosystem's namesake module.
- **AOSSIE Logo:** `/public/aossie-logo.svg` — Parent organization mark. Used alongside the Skills Ecosystem logo in README headers and cross-org materials, never as a substitute for it.
- **Stability Nexus Badge:** `/public/stability.svg` — Project stability status indicator, shown in README headers.

Use `skills-logo.svg` on dark or neutral backgrounds — its base fill (`#1C1818`) is designed to sit on dark surfaces; on light backgrounds, keep it inside a dark card/container rather than placing it directly on white.

### Color Palette

The palette is drawn directly from the Skills Ecosystem logo. It favors a dark, glass-like base with warm and cool accent blobs, and is shared across every module in the ecosystem (Skills Core, PR Dashboard, Skill Bot, Skill Updater) so cross-linked docs and dashboards read as one system.

* **Folder Base (Dark Glass):** `#1C1818`
  * The logo's base fill. Use for dark surfaces, containers behind the logo, and code blocks.
* **Signal Red (Primary Accent):** `#A82020`
  * The dominant logo blob color. Use for primary emphasis, breaking-change notices, and critical governance warnings (e.g. AGENTS.md boundary violations).
* **Signal Blue (Secondary Accent):** `#0C66A6`
  * The cooler logo blob color. Use for links, informational badges, and neutral references to other ecosystem modules.
* **Skills Orange (Highlight):** `#E37A4B`
  * Used for the logo's folder outline, the accent card, and the `SKILLS.MD` pixel text. This is the "call to action" color — use it for the most important highlight on a page (e.g. "start here" onboarding links, key architectural decisions).
* **Risk / Status Indicators** (for gap-tracking and skill-freshness tooling):
  * Low / up-to-date: `#22c55e` · Medium / stale: `#f59e0b` · High / missing context: `#ef4444`
* **Accessibility Target:** All text pairings must meet or exceed WCAG 2.1 AA (4.5:1) contrast. On the dark folder base (`#1C1818`), use near-white text (`#F8FAFC` or lighter) for body copy — do not rely on the accent blob colors alone for readable text.

## Typography

Documentation in this repository (READMEs, `AGENTS.md`, skill files, `GLOSSARY.md`) is plain Markdown rendered by GitHub, so typography is governed by GitHub's default rendering rather than custom CSS. Where custom HTML/CSS is used (e.g. README badge headers, diagrams), follow these conventions for consistency with the rest of the ecosystem:

- **Primary Stack:** `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
- **Monospace (file/module names):** default system monospace — always wrap `AGENTS.md`, `context.md`, `gap_log.json`, and similar filenames in inline code formatting.
- **Weights:** Regular (400) for body copy; Bold (700–800) for module names and headings.
- **Usage:** Module names in diagrams/tables should be bold; supporting descriptions should be regular weight and muted in color, mirroring the `<b><font color='#F59E0B'>ModuleName</font></b>` pattern used in this README's Mermaid diagrams.

## Terminology & Copywriting

When writing documentation, UI copy, or community announcements, strictly adhere to the following:

- **AOSSIE Skills Ecosystem** — the overall project (not "skills ecosystem" or "Skills ecosystem" mid-sentence unless it's clearly a continuation).
- **Skills Core** — this repository specifically, as the organization-wide store of shared skills and policies.
- **PR Dashboard** — the merge-analysis module ([AOSSIE-Org/PullRequestDashboard](https://github.com/AOSSIE-Org/PullRequestDashboard)).
- **Skill Bot** (two words, capitalized) — the Discord assistant module ([AOSSIE-Org/SkillBot](https://github.com/AOSSIE-Org/SkillBot)).
- **Skill Updater** (two words, capitalized) — the knowledge-evolution/PR pipeline module.
- **`AGENTS.md`** — the per-repository agent-boundary and context file; always in inline code formatting, always capitalized exactly as shown.
- **`.agents`** — the per-repository agent configuration directory; always in inline code formatting.
- **Local-first** (hyphenated, lowercase) — describes the ecosystem's core design principle across all modules; use consistently rather than "local first" or "Local First".
- **Zero knowledge loss** — the ecosystem's governing goal; use this exact phrase when describing the purpose of the gap-logging and skill-update feedback loop.
