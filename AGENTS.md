# AGENTS.md — AOSSIE Skills Core

This repository (`AOSSIE-Org/Skills`) is the **Skills Core**: the single upstream source of
shared, organization-wide skill files consumed by every other repo in the
[AOSSIE Skills Ecosystem](https://github.com/AOSSIE-Org/Skills) (Skill Bot, PR Dashboard, and
per-project repos). Consumer repos keep a synced mirror of some of this content under their own
`org-wide-skills/` folder — **treat this repo's file layout and `SKILL.md` frontmatter schema as
a public interface**: renaming a skill folder, changing a frontmatter field, or moving a
`references/` file breaks every consuming repo's sync script and routing until they re-sync.

## Structure

- `<skill-name>/SKILL.md` — one skill per top-level folder. Required YAML frontmatter: `name`
  (kebab-case, prefixed `aossie-` for org-wide skills) and `description` (states *when* the skill
  triggers — copy the imperative, trigger-condition style used in the existing skills, e.g.
  `contributor-onboarding/SKILL.md`, `GIT-DIS-AIPolicy/SKILL.md`, `project-template/SKILL.md`).
- `<skill-name>/references/` — detail files a skill points to instead of inlining (a **context
  pointer**, per `GLOSSARY.md`) — keeps `SKILL.md` itself short so it doesn't bloat every
  consuming agent's context load.
- `<skill-name>/scripts/` — optional, for skills that ship runnable helpers alongside their
  instructions rather than pure Markdown (e.g. `resolve-coderabbit-comments/scripts/` has
  `fetch_threads.py` / `fetch_threads.sh`). Not every skill needs this.
- `GLOSSARY.md` — canonical definitions for every **bolded term** used across this repo's and
  every consumer repo's skill/`AGENTS.md` files. If a new skill introduces a new load-bearing
  term, add it here rather than defining it locally.
- `Brand.md` — visual identity, color palette, and terminology rules (exact capitalization of
  `AGENTS.md`, "PR Dashboard", "Skill Bot", "Skill Updater", "local-first", "zero knowledge
  loss", etc.). Follow it whenever writing or editing README/skill copy in this repo.
- `InteractiveSimulation/` — a static, standalone demo app (served with
  `python -m http.server`), not a skill folder; don't confuse it with the skill catalog.
- `checklist-status.json` — generated OpenSSF-badge status; don't hand-edit, it's produced by
  the checklist tooling referenced in `BestPracticesChecklist.md`.

Existing skill categories, for placing new skills or judging whether one already covers your
case: `contributor-onboarding` (entry-gate orchestrator), `GIT-DIS-AIPolicy` (AI usage /
disclosure / PR-formatting rules), `project-template` (org-level architecture standards by
stack), `mcp-integration` (MCP server setup for automated code/UI changes), and
`resolve-coderabbit-comments` (local, one-at-a-time CodeRabbit-comment fixing).

## Adding or Changing a Skill

1. Check `GLOSSARY.md` and the existing skill folders first — don't duplicate an existing skill's
   trigger scope.
2. Write `description` as a trigger condition an LLM can match against a user request, not a
   feature summary (see the existing `SKILL.md` files for the pattern).
3. Keep `SKILL.md` itself short; push detail into `references/`.
4. If the skill encodes a new organization-wide policy or architectural rule, cross-check it
   against `Brand.md` terminology and add any new bolded term to `GLOSSARY.md`.
5. Changes here don't take effect in Skill Bot / PR Dashboard until those repos re-sync their
   `org-wide-skills/` mirror — mention that in your PR description if the change is time-sensitive.

## Contributing

- **Discord-first, mandatory**: all project communication happens on the
  [Discord server](https://discord.gg/hjUhu33uAn); post PR/issue updates there, not just on
  GitHub.
- **AI disclosure required**: if you used an AI tool for code, docs, or a new skill definition,
  say so in the PR description (tool + scope) — this repo defines that policy
  (`GIT-DIS-AIPolicy/SKILL.md`) for the rest of the ecosystem, so it applies here too.
- Note: [CONTRIBUTING.md](./CONTRIBUTING.md) in this repo is still the generic, unfilled
  Template-Repo boilerplate (its "Getting Started" section describes an `npm install` /
  `npm run dev` flow that doesn't apply to this repo). Follow the Discord and AI-disclosure
  sections of it, but use the setup below instead of its npm instructions.

## Setup (for running the Interactive Simulation locally)

```bash
git clone https://github.com/AOSSIE-Org/Skills.git
cd Skills/InteractiveSimulation
python -m http.server 8000
```

Navigate to `http://localhost:8000`. Editing or adding `SKILL.md` files needs no build step —
they're plain Markdown consumed directly by the sync scripts in consumer repos.
