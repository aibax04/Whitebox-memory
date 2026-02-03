# White Box Multi-Agent Memory

## 🚀 Projects
- **Simpliautomate (SimpliiV2):**
    - High-performance, AI-powered social media automation platform.
    - Successfully cloned and initialized.
    - Set up a modern development workflow with `venv` and required dependencies.
    - **Resolved Blockers:**
        - Fixed `SyntaxError` in `visual_planning_agent.py` caused by nested quotes in an f-string.
        - Migrated database from PostgreSQL to **SQLite (`simplii.db`)** for local development, updating `backend/db/database.py` and `backend/db/models.py` (handling `JSONB` to `JSON` fallback).
        - Initialized the database schema via `init_sqlite.py`.
        - Installed missing dependencies: `feedparser`, `python-dateutil`, and `aiosqlite`.
    - **Current Status:** Backend server is operational on `localhost:35000`.

- **Static-Website-Example:**
    - Cloned and modernized a legacy static template.
    - Integrated **Vite** and **Sass** for a modern frontend workflow.
    - Optimized SEO metadata and decoupled layout from legacy `skel.js`.

## 🧠 Decisions
- **Database Strategy:** Switched to SQLite locally to eliminate the need for a managed PostgreSQL instance during development/testing.
- **Workflow:** Using `Vite` for static assets and `FastAPI` for backend intelligence.
- **Agent Architecture:** Implemented a specialized 4-agent system (Correspondent, Pilot, Enhancer, Auditor) coordinated by White Box.
- **Correspondent Setup:** Registered Google OAuth credentials and initiated authentication for `whiteboxpsi@gmail.com`.

## ⚠️ Notes for Future Sessions
- `simpliautomate` requires `GOOGLE_API_KEY` for Gemini-powered news fetching and content generation.
- Ensure `venv` is activated when running the backend: `source venv/bin/activate`.
- Gmail access via `gog` requires manual user authorization for each account.
