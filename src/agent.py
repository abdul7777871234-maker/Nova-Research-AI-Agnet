"""Single CrewAI research agent: DuckDuckGo search + Groq / Gemini (with fallback)."""
import os
from typing import Optional, Type

import streamlit as st

os.environ.setdefault("CREWAI_DISABLE_TELEMETRY", "true")
os.environ.setdefault("OTEL_SDK_DISABLED", "true")

import litellm
from crewai import Agent, Crew, LLM, Process, Task
from crewai.tools import BaseTool
from ddgs import DDGS
from pydantic import BaseModel, Field

PROVIDERS = {
    "Groq · gpt-oss-120b": "groq",
    "Google · Gemini Flash": "gemini",
}

DEFAULT_GEMINI = ("gemini-3.8-flash,gemini-3.7-flash,gemini-3.6-flash,gemini-3.5-flash,"
                  "gemini-3.2-flash,gemini-3.1-flash,gemini-3-flash")


# ---- Patch: CrewAI adds an internal "cache_breakpoint" key that Groq rejects ----
def _strip(messages):
    if isinstance(messages, list):
        return [{k: v for k, v in m.items() if k != "cache_breakpoint"} if isinstance(m, dict) else m
                for m in messages]
    return messages


def _wrap(fn):
    def inner(*args, **kwargs):
        if "messages" in kwargs:
            kwargs["messages"] = _strip(kwargs["messages"])
        kwargs.pop("is_litellm", None)
        return fn(*args, **kwargs)
    inner._patched = True
    return inner


if not getattr(litellm.completion, "_patched", False):
    litellm.completion = _wrap(litellm.completion)


def _secret(name: str, default: str = "") -> str:
    try:
        return st.secrets[name]
    except Exception:
        return os.environ.get(name, default)


def build_llm(provider: str, model: str | None = None) -> LLM:
    if provider == "groq":
        key = _secret("GROQ_API_KEY")
        if not key:
            raise RuntimeError("GROQ_API_KEY missing in Streamlit secrets.")
        return LLM(model=f"groq/{_secret('GROQ_MODEL', 'openai/gpt-oss-120b')}", api_key=key, temperature=0.2)
    key = _secret("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY missing in Streamlit secrets.")
    return LLM(model=f"gemini/{model}", api_key=key, temperature=0.2)


class SearchInput(BaseModel):
    query: str = Field(..., description="The web search text, e.g. 'impact of AI on university students'.")


class WebLookup(BaseTool):
    name: str = "web_lookup"
    description: str = ("Look up information on the internet. Call with exactly one argument: "
                        "'query' (a short search phrase).")
    args_schema: Type[BaseModel] = SearchInput
    max_results: int = 4
    region: str = "wt-wt"
    timelimit: Optional[str] = None
    seen: dict = {}

    def _run(self, query: str) -> str:
        k = query.strip().lower()
        if k in self.seen:
            return "(Already searched this query; reuse earlier results.)\n" + self.seen[k]
        try:
            hits = DDGS().text(query, region=self.region, timelimit=self.timelimit, max_results=self.max_results)
        except Exception as e:
            return f"Search failed: {e}"
        out = "\n\n".join(f"[{i}] {h['title']}\n{h['href']}\n{h['body']}" for i, h in enumerate(hits, 1)) or "No results."
        self.seen[k] = out
        return out


def _run(llm, query, depth, style, region, timelimit) -> str:
    search = WebLookup(max_results=depth + 2, region=region, timelimit=timelimit, seen={})
    agent = Agent(
        role="Senior Research Analyst",
        goal="Research topics thoroughly using web search and deliver accurate, well-sourced answers.",
        backstory="You verify claims across sources, avoid redundant searches, and always cite URLs.",
        tools=[search], llm=llm, allow_delegation=False, verbose=False, max_iter=depth + 2,
    )
    task = Task(
        description=(f"Research: {query}\nUse the web_lookup tool with ONLY the 'query' argument. "
                     f"Use at most {depth} distinct searches; never repeat a query. "
                     f"Answer style: {style}. Cite sources as markdown links."),
        expected_output="A markdown answer with a short summary, key findings, and a Sources section.",
        agent=agent,
    )
    result = Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=False).kickoff()
    return str(result.raw if hasattr(result, "raw") else result)


def _is_tool_glitch(err: Exception) -> bool:
    s = str(err).lower()
    return "tool_use_failed" in s or "tool call validation failed" in s


def _should_fallback(err: Exception) -> bool:
    s = str(err).lower()
    return any(w in s for w in ("503", "unavailable", "overloaded", "high demand", "429", "rate limit",
                                "quota", "resource_exhausted", "404", "not found", "not_found",
                                "500", "internal", "timeout", "timed out")) or _is_tool_glitch(err)


def research(query: str, provider: str, depth: int, style: str, region: str, timelimit: str | None) -> str:
    if provider == "gemini":
        models = [m.strip() for m in _secret("GEMINI_MODELS", DEFAULT_GEMINI).split(",") if m.strip()]
        chain = [("gemini", m) for m in models] + [("groq", None)]
    else:
        chain = [("groq", None)]

    last: Exception | None = None
    for prov, model in chain:
        try:
            llm = build_llm(prov, model)
            for attempt in range(3):          # retry random tool-call glitches
                try:
                    answer = _run(llm, query, depth, style, region, timelimit)
                    break
                except Exception as e:
                    if attempt < 2 and _is_tool_glitch(e):
                        continue
                    raise
            label = model or _secret("GROQ_MODEL", "openai/gpt-oss-120b")
            return f"{answer}\n\n<sub>Answered by `{label}`</sub>"
        except RuntimeError as e:      # missing key: skip to next option
            last = e
        except Exception as e:
            last = e
            if not _should_fallback(e):
                raise
    raise last if last else RuntimeError("No model available.")
