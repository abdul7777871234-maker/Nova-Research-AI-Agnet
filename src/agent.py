"""Single CrewAI research agent: DuckDuckGo search + Groq / Gemini LLM."""
import os
import streamlit as st

os.environ.setdefault("CREWAI_DISABLE_TELEMETRY", "true")
os.environ.setdefault("OTEL_SDK_DISABLED", "true")

from crewai import Agent, Crew, LLM, Process, Task
from crewai.tools import tool
from ddgs import DDGS

PROVIDERS = {
    "Groq · gpt-oss-120b": "groq",
    "Google · Gemini Flash": "gemini",
}


def _secret(name: str, default: str = "") -> str:
    try:
        return st.secrets[name]
    except Exception:
        return os.environ.get(name, default)


def build_llm(provider: str) -> LLM:
    if provider == "groq":
        key = _secret("GROQ_API_KEY")
        if not key:
            raise RuntimeError("GROQ_API_KEY missing in Streamlit secrets.")
        return LLM(model=f"groq/{_secret('GROQ_MODEL', 'openai/gpt-oss-120b')}", api_key=key, temperature=0.2)
    key = _secret("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY missing in Streamlit secrets.")
    return LLM(model=f"gemini/{_secret('GEMINI_MODEL', 'gemini-3.8-flash')}", api_key=key, temperature=0.2)


def _make_search_tool(max_results: int, region: str, timelimit: str | None):
    seen: dict[str, str] = {}  # per-run memo: identical searches cost nothing

    @tool("duckduckgo_search")
    def duckduckgo_search(query: str) -> str:
        """Search the web with DuckDuckGo. Input: a concise search query."""
        k = query.strip().lower()
        if k in seen:
            return "(Already searched this query; reuse earlier results.)\n" + seen[k]
        try:
            hits = DDGS().text(query, region=region, timelimit=timelimit, max_results=max_results)
        except Exception as e:  # rate limits etc.
            return f"Search failed: {e}"
        out = "\n\n".join(f"[{i}] {h['title']}\n{h['href']}\n{h['body']}" for i, h in enumerate(hits, 1)) or "No results."
        seen[k] = out
        return out

    return duckduckgo_search


def research(query: str, provider: str, depth: int, style: str, region: str, timelimit: str | None) -> str:
    llm = build_llm(provider)
    search = _make_search_tool(max_results=depth + 2, region=region, timelimit=timelimit)
    agent = Agent(
        role="Senior Research Analyst",
        goal="Research topics thoroughly using web search and deliver accurate, well-sourced answers.",
        backstory="You verify claims across sources, avoid redundant searches, and always cite URLs.",
        tools=[search], llm=llm, allow_delegation=False, verbose=False,
        max_iter=depth + 2,
    )
    task = Task(
        description=(f"Research: {query}\nUse at most {depth} distinct searches; never repeat a query. "
                     f"Answer style: {style}. Cite sources as markdown links."),
        expected_output="A markdown answer with a short summary, key findings, and a Sources section.",
        agent=agent,
    )
    result = Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=False).kickoff()
    return str(result.raw if hasattr(result, "raw") else result)
