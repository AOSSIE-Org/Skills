# AOSSIE Skills Ecosystem - Interactive Simulation

This folder is a **grounded, code-accurate walkthrough** of how the AOSSIE Skills Ecosystem actually runs today — built for external contributors who need to understand the real internals before opening a PR, not a marketing mockup.

Every technical claim shown (file paths, thresholds, model names, gap-log reasons, sample queries) was sourced by reading the actual source of:
- **[SkillBot](https://github.com/AOSSIE-Org/SkillBot)** — `bot.py`, `repo_router.py`, `repo_metadata.py`, `gap_log.json`, `.env.example`
- **[PullRequestDashboard](https://github.com/AOSSIE-Org/PullRequestDashboard)** — `main.py`, `github.py`, `context.py`, `grouping.py`, `ollama.py`, `render.py`
- **This repo (`AOSSIE-Org/Skills`)** — `AGENTS.md`, every `SKILL.md`, `GLOSSARY.md`
- **[SocialShareButton](https://github.com/AOSSIE-Org/SocialShareButton)** — used as the real, working example of a per-repo `AGENTS.md` + `.agent/` layout

It covers:
1. **Per-Repository Context** — `AGENTS.md` as a task-intent router, plus `.agent/core|instructions|info/*.md` (real example content, not invented).
2. **Skills Core** — the org-wide `SKILL.md` files in this repo, and how `SkillBot/scripts/sync_org_skills.py` actually distributes them (no git subtree, despite older docs).
3. **Skill Bot** — the real keyword-routing + fixed-priority context concatenation + unconditional-Ollama-call flow, with **no vector search and no confidence threshold anywhere in the codebase**.
4. **PR Dashboard** — the real CLI pipeline: `gh` fetch → sentence-transformer clustering → post-hoc Ollama explanation → static SVG/HTML output. Not a running web app.
5. **Skill Updater** — clearly marked **ROADMAP**. `gap_log.json` is a real, growing sink; nothing in this org's active code reads it back yet.

A **"Docs vs Code"** panel (top-right button) lists concrete, verified gaps between what the docs claim and what the code does — several are good first contributions.

---

## How to Run

This folder has no build step and no `package.json` — it's static HTML/CSS/JS. Two ways to view it:

### 1. Local Server (recommended)
Run Python's built-in HTTP server from this directory:
```bash
python -m http.server 8000
```
Then open [http://localhost:8000/index.html](http://localhost:8000/index.html).

### 2. Direct File Opening
Double-click `index.html` to open it in your browser.
*(FontAwesome and Google Fonts require internet access to load icons/typography — a local server avoids any `file://` CORS quirks but isn't strictly required.)*
