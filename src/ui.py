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
    .stApp {{ background:{p['bg']}; color:{p['text']}; }}
    [data-testid="stSidebar"] {{ background:{p['panel']}; border-right:1px solid {p['border']}; }}
    [data-testid="stHeader"] {{ background:transparent; }}
    .stApp, .stApp p, .stApp label, .stApp span, .stApp li, .stApp h1, .stApp h2, .stApp h3 {{ color:{p['text']}; }}
    .muted {{ color:{p['muted']} !important; font-size:.9rem; }}
    .brand {{ display:flex; align-items:center; gap:12px; }}
    .brand b {{ font-size:1.25rem; background:linear-gradient(90deg,#6C5CE7,#00CEC9); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }}
    [data-testid="stChatMessage"] {{ background:{p['panel']}; border:1px solid {p['border']}; border-radius:16px; padding:.9rem 1rem; }}
    [data-testid="stChatInput"] textarea {{ color:{p['text']}; }}
    [data-testid="stChatInput"] > div {{ background:{p['panel']}; border:1px solid {p['border']}; border-radius:14px; }}
    div[data-baseweb="select"] > div {{ background:{p['panel']}; border-color:{p['border']}; border-radius:10px; }}
    .stButton > button, .stDownloadButton > button {{ border-radius:10px; border:1px solid {p['border']}; background:{p['panel']}; color:{p['text']}; }}
    .stButton > button:hover, .stDownloadButton > button:hover {{ border-color:#6C5CE7; color:#6C5CE7; }}
    .stButton > button[kind="primary"] {{ background:linear-gradient(90deg,#6C5CE7,#8E7DFF); color:#fff; border:none; }}
    .tag {{ display:inline-block; padding:2px 10px; border-radius:99px; font-size:.75rem; background:#6C5CE722; color:#6C5CE7 !important; }}
    </style>""", unsafe_allow_html=True)
