"""Tiny SQLite cache so the agent never re-researches the same topic."""
import json, re, sqlite3, time
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data" / "cache.db"
_STOP = {"the", "a", "an", "of", "to", "in", "on", "for", "and", "is", "are", "what", "how", "why", "about", "tell", "me"}


def _conn():
    DB.parent.mkdir(exist_ok=True)
    c = sqlite3.connect(DB)
    c.execute("CREATE TABLE IF NOT EXISTS r (key TEXT PRIMARY KEY, query TEXT, tokens TEXT, answer TEXT, ts REAL)")
    return c


def _tokens(q: str) -> list[str]:
    return sorted({t for t in re.findall(r"[a-z0-9]+", q.lower()) if t not in _STOP})


def get(query: str, threshold: float = 0.8):
    """Exact or near-duplicate (Jaccard) match. Returns answer or None."""
    toks = set(_tokens(query))
    if not toks:
        return None
    with _conn() as c:
        for q, t, a in c.execute("SELECT query, tokens, answer FROM r"):
            other = set(json.loads(t))
            if other and len(toks & other) / len(toks | other) >= threshold:
                return a
    return None


def put(query: str, answer: str):
    toks = _tokens(query)
    with _conn() as c:
        c.execute("INSERT OR REPLACE INTO r VALUES (?,?,?,?,?)",
                  (" ".join(toks), query, json.dumps(toks), answer, time.time()))
