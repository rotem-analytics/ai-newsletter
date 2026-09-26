# AI Newsletter

## Goal
A personal weekly newsletter on data & AI, delivered by email.
Bilingual (Hebrew/English), with links to original sources,
clear summaries, and simplification of complex topics without losing depth.

## Constraints
- Zero cost: no paid APIs. Summaries via Google Gemini API free tier.
- Sources are RSS feeds.
- Weekly run via GitHub Actions (free tier).
- Output: a designed, bilingual web page (Hebrew/English toggle) hosted on GitHub Pages. The weekly email contains a short teaser with a link to the full page.
- Environment: Windows, PowerShell, Python.

## Decisions
- Gemini library: `google-genai`. Secrets loaded with `python-dotenv`.
- Model: use the alias `gemini-flash-latest` (`gemini-2.5-flash` returned 404; versioned names get deprecated).
- The API key is stored in `.env` as `GEMINI_API_KEY`. Never print it or commit it.
- The free tier sometimes returns 503 (temporary overload). Real API calls will need retry logic.

## How to work with me
- I'm learning. This project is also coding practice.
- Work in small steps. One step at a time, and wait for me before moving on.
- Before writing code, explain the plan briefly. After writing, explain what the code does.
- Explain in Hebrew; code, comments, and file names in English.
- Prefer simple, readable code over clever code.
