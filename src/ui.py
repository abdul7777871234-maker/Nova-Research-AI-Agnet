"""Theme, logo and icons."""

import streamlit as st


# =========================================================
# LOGO (Single-line formatted SVG to prevent Markdown rendering breaks)
# =========================================================

LOGO = (
    '<svg width="{s}" height="{s}" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">'
    '<defs>'
    '<linearGradient id="g" x1="0" y1="0" x2="48" y2="48">'
    '<stop stop-color="#6C5CE7"/>'
    '<stop offset="1" stop-color="#00CEC9"/>'
    '</linearGradient>'
    '</defs>'
    '<rect width="48" height="48" rx="12" fill="url(#g)"/>'
    '<circle cx="22" cy="22" r="8" stroke="#fff" stroke-width="3"/>'
    '<path d="M28 28l8 8" stroke="#fff" stroke-width="3" stroke-linecap="round"/>'
    '<circle cx="22" cy="22" r="2.5" fill="#fff"/>'
    '</svg>'
)


# =========================================================
# ICONS
# =========================================================

SUN = (
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/>'
    '<path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'
    '</svg>'
)


MOON = (
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/>'
    '</svg>'
)


# =========================================================
# COLOR PALETTES
# =========================================================

PALETTES = {
    "light": {
        "bg": "#F7F8FC",
        "panel": "#FFFFFF",
        "text": "#1B1F3B",
        "muted": "#6B7194",
        "border": "#E3E6F3",
    },
    "dark": {
        "bg": "#0E1020",
        "panel": "#171A30",
        "text": "#EDEFFB",
        "muted": "#9AA0C6",
        "border": "#2A2E4D",
    },
}


# =========================================================
# LOGO FUNCTION
# =========================================================

def logo(size=40) -> str:
    return LOGO.format(s=size)


# =========================================================
# THEME / CSS
# =========================================================

def inject_css(mode: str):

    # Safety fallback
    if mode not in PALETTES:
        mode = "light"

    p = PALETTES[mode]

    st.markdown(
        f"""
<style>

/* =========================================================
   GLOBAL APP
   ========================================================= */

html,
body,
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {{
    background-color: {p['bg']} !important;
    color: {p['text']} !important;
}}

[data-testid="stHeader"] {{
    background: transparent !important;
}}

[data-testid="stBottom"],
[data-testid="stBottomBlockContainer"] {{
    background-color: {p['bg']} !important;
}}


/* =========================================================
   SIDEBAR
   ========================================================= */

[data-testid="stSidebar"] {{
    background-color: {p['panel']} !important;
    color: {p['text']} !important;
}}

[data-testid="stSidebar"] > div {{
    background-color: {p['panel']} !important;
    color: {p['text']} !important;
    border-right: 1px solid {p['border']} !important;
}}


/* =========================================================
   TEXT
   ========================================================= */

.stApp p,
.stApp label,
.stApp span,
.stApp li,
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4,
.stApp h5,
.stApp h6 {{
    color: {p['text']} !important;
}}

.muted {{
    color: {p['muted']} !important;
    font-size: 0.9rem;
}}


/* =========================================================
   BRAND & LOGO FIXES
   ========================================================= */

.brand {{
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
}}

.brand svg {{
    display: block !important;
    flex-shrink: 0 !important;
}}

.brand b {{
    font-size: 1.25rem;
    background: linear-gradient(
        90deg,
        #6C5CE7,
        #00CEC9
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.icon {{
    color: {p['text']} !important;
    display: flex;
    align-items: center;
    justify-content: center;
}}


/* =========================================================
   EXPANDERS
   ========================================================= */

[data-testid="stExpander"] {{
    background-color: {p['panel']} !important;
    border: 1px solid {p['border']} !important;
    border-radius: 12px !important;
}}

[data-testid="stExpander"] > details {{
    background-color: transparent !important;
}}

[data-testid="stExpander"] summary {{
    background-color: transparent !important;
    color: {p['text']} !important;
}}

[data-testid="stExpander"] summary * {{
    color: {p['text']} !important;
}}

[data-testid="stExpander"] summary svg {{
    color: {p['text']} !important;
    fill: {p['text']} !important;
}}


/* =========================================================
   SELECTBOX - FIX WHITE DROPDOWN ARROW CONTAINER
   ========================================================= */

/* Main outer selectbox wrapper */
[data-testid="stSelectbox"] {
    background: transparent !important;
    color: {p['text']} !important;
}

/* BaseWeb input container & outer shell */
[data-testid="stSelectbox"] [data-baseweb="select"],
[data-testid="stSelectbox"] [data-baseweb="select"] > div,
[data-testid="stSelectbox"] [data-baseweb="select"] * {
    background-color: {p['panel']} !important;
    color: {p['text']} !important;
    border-color: {p['border']} !important;
    -webkit-text-fill-color: {p['text']} !important;
}

/* BaseWeb right-side arrow container wrapper */
[data-testid="stSelectbox"] [data-baseweb="select"] [role="button"],
[data-testid="stSelectbox"] [data-baseweb="select"] [data-testid="stSelectboxHeader"] {
    background-color: {p['panel']} !important;
}

/* Selectbox inputs */
[data-testid="stSelectbox"] input {
    background-color: {p['panel']} !important;
    color: {p['text']} !important;
    caret-color: {p['text']} !important;
}

/* Dropdown arrow icon color */
[data-testid="stSelectbox"] [data-baseweb="select"] svg {
    fill: {p['text']} !important;
    color: {p['text']} !important;
    stroke: {p['text']} !important;
}

/* Hover and Focus States */
[data-testid="stSelectbox"] [data-baseweb="select"]:hover > div {
    border-color: #6C5CE7 !important;
}

[data-testid="stSelectbox"] [data-baseweb="select"]:focus-within > div {
    border-color: #6C5CE7 !important;
    box-shadow: 0 0 0 1px #6C5CE7 !important;
}

/* =========================================================
   DROPDOWN / POPOVER
   ========================================================= */

[data-baseweb="popover"],
[data-baseweb="popover"] > div,
[data-baseweb="popover"] > div > div,
[data-baseweb="menu"],
[data-baseweb="menu"] > div,
[role="listbox"] {{
    background-color: {p['panel']} !important;
    background-image: none !important;
    color: {p['text']} !important;
}}

[data-baseweb="popover"] li,
[data-baseweb="popover"] li *,
[data-baseweb="menu"] li,
[data-baseweb="menu"] li *,
[role="listbox"] [role="option"],
[role="listbox"] [role="option"] * {{
    background-color: transparent !important;
    color: {p['text']} !important;
    -webkit-text-fill-color: {p['text']} !important;
}}

[data-baseweb="popover"] li:hover,
[data-baseweb="menu"] li:hover,
[role="listbox"] [role="option"]:hover {{
    background-color: #6C5CE733 !important;
    color: {p['text']} !important;
}}

[data-baseweb="popover"] li[aria-selected="true"],
[data-baseweb="menu"] li[aria-selected="true"],
[role="option"][aria-selected="true"] {{
    background-color: #6C5CE722 !important;
    color: {p['text']} !important;
}}


/* =========================================================
   TOGGLE
   ========================================================= */

[data-testid="stToggle"],
[data-testid="stToggle"] label,
[data-testid="stToggle"] p {{
    color: {p['text']} !important;
}}


/* =========================================================
   BUTTONS
   ========================================================= */

.stButton > button,
.stDownloadButton > button {{
    background-color: {p['panel']} !important;
    color: {p['text']} !important;
    border: 1px solid {p['border']} !important;
    border-radius: 10px !important;
}}

.stButton > button:hover,
.stDownloadButton > button:hover {{
    border-color: #6C5CE7 !important;
    color: #6C5CE7 !important;
}}

.stButton > button[kind="primary"] {{
    background: linear-gradient(90deg, #6C5CE7, #8E7DFF) !important;
    color: #FFFFFF !important;
    border: none !important;
}}

.stButton > button[kind="primary"] * {{
    color: #FFFFFF !important;
}}


/* =========================================================
   CHAT MESSAGE & INPUT
   ========================================================= */

[data-testid="stChatMessage"] {{
    background-color: {p['panel']} !important;
    border: 1px solid {p['border']} !important;
    border-radius: 16px !important;
    padding: 0.9rem 1rem;
}}

[data-testid="stChatInput"],
[data-testid="stChatInput"] > div {{
    background-color: {p['panel']} !important;
    border: 1px solid {p['border']} !important;
    border-radius: 14px !important;
}}

[data-testid="stChatInput"] textarea {{
    background: transparent !important;
    color: {p['text']} !important;
    -webkit-text-fill-color: {p['text']} !important;
}}

[data-testid="stChatInput"] textarea::placeholder {{
    color: {p['muted']} !important;
    -webkit-text-fill-color: {p['muted']} !important;
}}

[data-testid="stChatInput"] button {{
    background-color: #6C5CE7 !important;
}}

[data-testid="stChatInput"] button svg {{
    color: #FFFFFF !important;
    fill: #FFFFFF !important;
}}


/* =========================================================
   ALERT & TAG
   ========================================================= */

[data-testid="stAlert"] {{
    background-color: {p['panel']} !important;
    border: 1px solid {p['border']} !important;
    color: {p['text']} !important;
}}

.tag {{
    display: inline-block;
    padding: 2px 10px;
    border-radius: 99px;
    font-size: 0.75rem;
    background: #6C5CE722;
    color: #6C5CE7 !important;
}}

</style>
        """,
        unsafe_allow_html=True,
    )
