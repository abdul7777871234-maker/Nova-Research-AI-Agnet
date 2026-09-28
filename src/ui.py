"""Theme, logo and icons."""
import streamlit as st

LOGO = """<svg width="{s}" height="{s}" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="g" x1="0" y1="0" x2="48" y2="48"><stop stop-color="#6C5CE7"/><stop offset="1" stop-color="#00CEC9"/></linearGradient></defs>
<rect width="48" height="48" rx="12" fill="url(#g)"/>
<circle cx="22" cy="22" r="8" stroke="#fff" stroke-width="3"/><path d="M28 28l8 8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
<circle cx="22" cy="22" r="2.5" fill="#fff"/></svg>"""

SUN = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
MOON = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/></svg>'

PALETTES = {
    "light": dict(bg="#F7F8FC", panel="#FFFFFF", text="#1B1F3B", muted="#6B7194", border="#E3E6F3"),
    "dark": dict(bg="#0E1020", panel="#171A30", text="#EDEFFB", muted="#9AA0C6", border="#2A2E4D"),
}


def logo(size=40) -> str:
    return LOGO.format(s=size)


def inject_css(mode: str):
    p = PALETTES[mode]
    st.markdown(f"""<style>
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{ background:{p['bg']} !important; }}
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div {{ background:{p['panel']} !important; border-right:1px solid {p['border']}; }}
    [data-testid="stHeader"] {{ background:transparent !important; }}
    [data-testid="stBottom"], [data-testid="stBottom"] > div,
    [data-testid="stBottomBlockContainer"] {{ background:{p['bg']} !important; }}
    .stApp, .stApp p, .stApp label, .stApp span, .stApp li,
    .stApp h1, .stApp h2, .stApp h3, .stApp div[data-testid="stMarkdownContainer"] {{ color:{p['text']}; }}
    .muted {{ color:{p['muted']} !important; font-size:.9rem; }}
    .icon {{ color:{p['text']} !important; display:flex; justify-content:center; align-items:center; }}
    .brand {{ display:flex; align-items:center; gap:12px; }}
    .brand b {{ font-size:1.25rem; background:linear-gradient(90deg,#6C5CE7,#00CEC9); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }}

    [data-testid="stExpander"] {{ background:{p['panel']} !important; border:1px solid {p['border']} !important; border-radius:12px; }}
    [data-testid="stExpander"] summary, [data-testid="stExpander"] details {{ background:transparent !important; }}
    [data-testid="stExpander"] summary p, [data-testid="stExpander"] summary span,
    [data-testid="stExpander"] summary svg {{ color:{p['text']} !important; fill:{p['text']} !important; }}

    .stApp [data-testid="stSelectbox"] [data-baseweb="select"] > div,
    .stApp [data-testid="stSelectbox"] [data-baseweb="select"] > div > div,
    .stApp [data-testid="stSelectbox"] div[role="combobox"] {{ background:{p['bg']} !important; background-color:{p['bg']} !important; border-color:{p['border']} !important; border-radius:10px; }}
    .stApp [data-testid="stSelectbox"] [data-baseweb="select"] * {{ color:{p['text']} !important; -webkit-text-fill-color:{p['text']} !important; }}
    .stApp [data-testid="stSelectbox"] svg {{ fill:{p['text']} !important; }}
    div[data-baseweb="popover"] div[data-baseweb="menu"], div[data-baseweb="popover"] ul {{ background:{p['panel']} !important; }}
    div[data-baseweb="popover"] li, div[data-baseweb="popover"] li * {{ background:transparent !important; color:{p['text']} !important; -webkit-text-fill-color:{p['text']} !important; }}
    div[data-baseweb="popover"] li:hover {{ background:#6C5CE733 !important; }}

    [data-testid="stToggle"] label, [data-testid="stToggle"] p {{ color:{p['text']} !important; }}

    [data-testid="stChatMessage"] {{ background:{p['panel']} !important; border:1px solid {p['border']}; border-radius:16px; padding:.9rem 1rem; }}
    [data-testid="stChatInput"], [data-testid="stChatInput"] > div {{ background:{p['panel']} !important; border:1px solid {p['border']}; border-radius:14px; }}
    [data-testid="stChatInput"] textarea {{ color:{p['text']} !important; -webkit-text-fill-color:{p['text']} !important; background:transparent !important; }}
    [data-testid="stChatInput"] textarea::placeholder {{ color:{p['muted']} !important; -webkit-text-fill-color:{p['muted']} !important; }}
    [data-testid="stChatInput"] button {{ background:#6C5CE7 !important; }}
    [data-testid="stChatInput"] button svg {{ fill:#fff !important; color:#fff !important; }}

    .stButton > button, .stDownloadButton > button {{ border-radius:10px; border:1px solid {p['border']}; background:{p['panel']}; color:{p['text']}; }}
    .stButton > button:hover, .stDownloadButton > button:hover {{ border-color:#6C5CE7; color:#6C5CE7; }}
    .stButton > button[kind="primary"] {{ background:linear-gradient(90deg,#6C5CE7,#8E7DFF); color:#fff; border:none; }}
    .stButton > button[kind="primary"] p {{ color:#fff !important; }}
    [data-testid="stAlert"] {{ background:{p['panel']} !important; border:1px solid {p['border']}; }}
    .tag {{ display:inline-block; padding:2px 10px; border-radius:99px; font-size:.75rem; background:#6C5CE722; color:#6C5CE7 !important; }}
    </style>""", unsafe_allow_html=True)
