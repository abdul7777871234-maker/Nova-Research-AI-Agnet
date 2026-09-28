import uuid
import streamlit as st

st.set_page_config(page_title="Nova Research Agent", page_icon="🔎", layout="wide")

from src import cache, ui
from src.agent import PROVIDERS, research

# ---------- state ----------
S = st.session_state
S.setdefault("dark", False)
S.setdefault("chats", {})
S.setdefault("current", None)


def new_chat():
    cid = uuid.uuid4().hex[:8]
    S.chats[cid] = {"title": "New chat", "messages": []}
    S.current = cid


if S.current is None or S.current not in S.chats:
    new_chat()

ui.inject_css("dark" if S.dark else "light")
chat = S.chats[S.current]

# ---------- sidebar ----------
with st.sidebar:
    st.markdown(f'<div class="brand">{ui.logo(40)}<b>Nova Research</b></div>', unsafe_allow_html=True)
    st.markdown('<p class="muted">Web research agent · CrewAI</p>', unsafe_allow_html=True)

    c1, c2 = st.columns([1, 3], vertical_alignment="center")
    c1.markdown(f'<div class="icon">{ui.MOON if S.dark else ui.SUN}</div>', unsafe_allow_html=True)
    c2.toggle("Dark theme", key="dark")

    st.divider()
    with st.expander("⚙️ Model", expanded=True):
        model_label = st.selectbox("LLM provider", list(PROVIDERS))
    with st.expander("🔎 Research", expanded=True):
        depth = st.selectbox("Depth (max searches)", [1, 2, 3, 5], index=1)
        style = st.selectbox("Answer style", ["Concise summary", "Detailed report", "Bullet points", "ELI5"])
        region = st.selectbox("Region", ["wt-wt", "us-en", "uk-en", "in-en", "de-de", "fr-fr"],
                              format_func=lambda r: {"wt-wt": "Worldwide"}.get(r, r))
        tl = st.selectbox("Time range", ["Any time", "Past day", "Past week", "Past month", "Past year"])
        timelimit = {"Any time": None, "Past day": "d", "Past week": "w", "Past month": "m", "Past year": "y"}[tl]

    st.divider()
    if st.button("➕ New chat", use_container_width=True, type="primary"):
        new_chat()
        st.rerun()
    st.markdown("**History**")
    for cid, c in reversed(list(S.chats.items())):
        if c["messages"] and st.button(("● " if cid == S.current else "") + c["title"][:34], key=f"h{cid}", use_container_width=True):
            S.current = cid
            st.rerun()

# ---------- header ----------
h1, h2 = st.columns([6, 1], vertical_alignment="center")
h1.markdown(
    f'<div class="brand">{ui.logo(52)}<div><h2 style="margin:0; padding:0; line-height:1.2;">Nova Research Agent</h2>'
    f'<span class="muted">Ask anything. I search, verify and cite.</span></div></div>',
    unsafe_allow_html=True
)
if h2.button("🧹 Clear chat", use_container_width=True):
    new_chat()
    st.rerun()
# ---------- messages ----------
for m in chat["messages"]:
    with st.chat_message(m["role"]):
        if m.get("cached"):
            st.markdown('<span class="tag">⚡ from cache · 0 tokens</span>', unsafe_allow_html=True)
        st.markdown(m["content"])

if not chat["messages"]:
    st.info("Try: *“Latest breakthroughs in solid-state batteries”*")

# ---------- input ----------
if q := st.chat_input("Research a topic…"):
    chat["messages"].append({"role": "user", "content": q})
    if chat["title"] == "New chat":
        chat["title"] = q
    with st.chat_message("user"):
        st.markdown(q)
    with st.chat_message("assistant"):
        hit = cache.get(q)
        if hit:
            st.markdown('<span class="tag">⚡ from cache · 0 tokens</span>', unsafe_allow_html=True)
            ans, cached = hit, True
        else:
            try:
                with st.spinner("Researching…"):
                    ans = research(q, PROVIDERS[model_label], depth, style, region, timelimit)
                cache.put(q, ans)
            except Exception as e:
                ans = f"⚠️ {e}"
            cached = False
        st.markdown(ans)
    chat["messages"].append({"role": "assistant", "content": ans, "cached": cached})

# ---------- docs download ----------
if chat["messages"]:
    doc = "\n\n".join(f"## {'You' if m['role']=='user' else 'Agent'}\n\n{m['content']}" for m in chat["messages"])
    d1, d2 = st.columns(2)
    d1.download_button("⬇️ Download this chat (.md)", doc, file_name="research.md", mime="text/markdown", use_container_width=True)
    last = next((m["content"] for m in reversed(chat["messages"]) if m["role"] == "assistant"), "")
    d2.download_button("⬇️ Download last answer (.txt)", last, file_name="answer.txt", use_container_width=True)
