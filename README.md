# Nova Research Agent
Single-agent web researcher: **CrewAI** + **DuckDuckGo** (`ddgs`) + **Groq gpt-oss-120b** or **Gemini Flash**, UI in **Streamlit**.

## Structure
```
app.py                     # UI + chat logic
src/agent.py               # CrewAI agent, search tool, LLM factory
src/cache.py               # SQLite/Jaccard cache (no repeat research)
src/ui.py                  # theme CSS, SVG logo/icons
requirements.txt
.streamlit/config.toml
.streamlit/secrets.toml.example
```

## Deploy (no local run)
1. Push to GitHub: `git init && git add . && git commit -m "init" && git branch -M main && git remote add origin <url> && git push -u origin main`
2. share.streamlit.io → **New app** → pick repo, branch `main`, file `app.py`.
3. **Advanced settings** → Python **3.11**; paste secrets from `.streamlit/secrets.toml.example`.
4. Deploy.

## Notes
- Cache lives on the app's ephemeral disk; it resets on reboot.
- Set `GEMINI_MODEL` / `GROQ_MODEL` in secrets to change models without code edits.
