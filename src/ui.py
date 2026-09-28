def inject_css(mode: str):
    p = PALETTES[mode]

    st.markdown(f"""
    <style>

    /* =========================================================
       GLOBAL APP
       ========================================================= */

    .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {{
        background: {p['bg']} !important;
    }}

    [data-testid="stHeader"] {{
        background: transparent !important;
    }}

    [data-testid="stBottom"],
    [data-testid="stBottom"] > div,
    [data-testid="stBottomBlockContainer"] {{
        background: {p['bg']} !important;
    }}


    /* =========================================================
       SIDEBAR
       ========================================================= */

    [data-testid="stSidebar"],
    [data-testid="stSidebar"] > div {{
        background: {p['panel']} !important;
        border-right: 1px solid {p['border']} !important;
    }}


    /* =========================================================
       GLOBAL TEXT
       ========================================================= */

    .stApp,
    .stApp p,
    .stApp label,
    .stApp span,
    .stApp li,
    .stApp h1,
    .stApp h2,
    .stApp h3,
    .stApp h4,
    .stApp h5,
    .stApp h6,
    .stApp div[data-testid="stMarkdownContainer"] {{
        color: {p['text']};
    }}

    .muted {{
        color: {p['muted']} !important;
        font-size: .9rem;
    }}


    /* =========================================================
       BRAND
       ========================================================= */

    .brand {{
        display: flex;
        align-items: center;
        gap: 12px;
    }}

    .brand b {{
        font-size: 1.25rem;
        background: linear-gradient(90deg, #6C5CE7, #00CEC9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .icon {{
        color: {p['text']} !important;
        display: flex;
        justify-content: center;
        align-items: center;
    }}


    /* =========================================================
       EXPANDERS
       ========================================================= */

    [data-testid="stExpander"] {{
        background: {p['panel']} !important;
        border: 1px solid {p['border']} !important;
        border-radius: 12px !important;
    }}

    [data-testid="stExpander"] summary,
    [data-testid="stExpander"] details {{
        background: transparent !important;
    }}

    [data-testid="stExpander"] summary p,
    [data-testid="stExpander"] summary span,
    [data-testid="stExpander"] summary svg {{
        color: {p['text']} !important;
        fill: {p['text']} !important;
    }}


    /* =========================================================
       SELECTBOX — MAIN FIX
       ========================================================= */

    .stApp [data-testid="stSelectbox"] {{
        color: {p['text']} !important;
    }}

    /* Outer BaseWeb select */
    .stApp [data-testid="stSelectbox"] [data-baseweb="select"] {{
        background: transparent !important;
        color: {p['text']} !important;
    }}

    /* Every internal select container */
    .stApp [data-testid="stSelectbox"]
    [data-baseweb="select"] > div,

    .stApp [data-testid="stSelectbox"]
    [data-baseweb="select"] > div > div,

    .stApp [data-testid="stSelectbox"]
    [data-baseweb="select"] > div > div > div,

    .stApp [data-testid="stSelectbox"]
    div[role="combobox"],

    .stApp [data-testid="stSelectbox"]
    div[role="combobox"] > div {{
        background: {p['panel']} !important;
        background-color: {p['panel']} !important;
        color: {p['text']} !important;
        border-color: {p['border']} !important;
        border-radius: 10px !important;
    }}

    /* Selectbox text */
    .stApp [data-testid="stSelectbox"]
    [data-baseweb="select"] *,

    .stApp [data-testid="stSelectbox"]
    div[role="combobox"] * {{
        color: {p['text']} !important;
        -webkit-text-fill-color: {p['text']} !important;
    }}

    /* Selectbox input */
    .stApp [data-testid="stSelectbox"]
    input {{
        background: {p['panel']} !important;
        background-color: {p['panel']} !important;
        color: {p['text']} !important;
        -webkit-text-fill-color: {p['text']} !important;
        caret-color: {p['text']} !important;
    }}

    /* Selectbox arrow */
    .stApp [data-testid="stSelectbox"]
    svg {{
        color: {p['text']} !important;
        fill: {p['text']} !important;
        stroke: {p['text']} !important;
    }}

    /* Hover / focus */
    .stApp [data-testid="stSelectbox"]
    [data-baseweb="select"]:hover > div {{
        border-color: #6C5CE7 !important;
        background: {p['panel']} !important;
        background-color: {p['panel']} !important;
    }}

    .stApp [data-testid="stSelectbox"]
    [data-baseweb="select"]:focus-within > div {{
        border-color: #6C5CE7 !important;
        box-shadow: 0 0 0 1px #6C5CE7 !important;
        background: {p['panel']} !important;
    }}


    /* =========================================================
       SELECTBOX DROPDOWN / POPOVER — MAIN FIX
       ========================================================= */

    div[data-baseweb="popover"],
    div[data-baseweb="popover"] > div,
    div[data-baseweb="popover"] > div > div,

    div[data-baseweb="menu"],
    div[data-baseweb="menu"] > div,

    ul[role="listbox"],
    div[role="listbox"] {{
        background: {p['panel']} !important;
        background-color: {p['panel']} !important;
        color: {p['text']} !important;
    }}

    /* Dropdown options */
    div[data-baseweb="popover"] li,
    div[data-baseweb="popover"] li *,
    div[data-baseweb="menu"] li,
    div[data-baseweb="menu"] li *,
    ul[role="listbox"] li,
    ul[role="listbox"] li *,

    div[role="option"],
    div[role="option"] * {{
        background: transparent !important;
        color: {p['text']} !important;
        -webkit-text-fill-color: {p['text']} !important;
    }}

    /* Dropdown hover */
    div[data-baseweb="popover"] li:hover,
    div[data-baseweb="menu"] li:hover,
    ul[role="listbox"] li:hover,
    div[role="option"]:hover {{
        background: #6C5CE733 !important;
        color: {p['text']} !important;
    }}

    /* Selected option */
    div[data-baseweb="popover"] li[aria-selected="true"],
    div[data-baseweb="menu"] li[aria-selected="true"],
    div[role="option"][aria-selected="true"] {{
        background: #6C5CE722 !important;
        color: {p['text']} !important;
    }}


    /* =========================================================
       TOGGLE
       ========================================================= */

    [data-testid="stToggle"] label,
    [data-testid="stToggle"] p {{
        color: {p['text']} !important;
    }}


    /* =========================================================
       CHAT
       ========================================================= */

    [data-testid="stChatMessage"] {{
        background: {p['panel']} !important;
        border: 1px solid {p['border']} !important;
        border-radius: 16px !important;
        padding: .9rem 1rem;
    }}

    [data-testid="stChatInput"],
    [data-testid="stChatInput"] > div {{
        background: {p['panel']} !important;
        border: 1px solid {p['border']} !important;
        border-radius: 14px !important;
    }}

    [data-testid="stChatInput"] textarea {{
        color: {p['text']} !important;
        -webkit-text-fill-color: {p['text']} !important;
        background: transparent !important;
    }}

    [data-testid="stChatInput"] textarea::placeholder {{
        color: {p['muted']} !important;
        -webkit-text-fill-color: {p['muted']} !important;
    }}

    [data-testid="stChatInput"] button {{
        background: #6C5CE7 !important;
    }}

    [data-testid="stChatInput"] button svg {{
        fill: #fff !important;
        color: #fff !important;
    }}


    /* =========================================================
       BUTTONS
       ========================================================= */

    .stButton > button,
    .stDownloadButton > button {{
        border-radius: 10px !important;
        border: 1px solid {p['border']} !important;
        background: {p['panel']} !important;
        color: {p['text']} !important;
    }}

    .stButton > button:hover,
    .stDownloadButton > button:hover {{
        border-color: #6C5CE7 !important;
        color: #6C5CE7 !important;
    }}

    .stButton > button[kind="primary"] {{
        background: linear-gradient(90deg, #6C5CE7, #8E7DFF) !important;
        color: #fff !important;
        border: none !important;
    }}

    .stButton > button[kind="primary"] p {{
        color: #fff !important;
    }}


    /* =========================================================
       ALERTS
       ========================================================= */

    [data-testid="stAlert"] {{
        background: {p['panel']} !important;
        border: 1px solid {p['border']} !important;
    }}


    /* =========================================================
       TAG
       ========================================================= */

    .tag {{
        display: inline-block;
        padding: 2px 10px;
        border-radius: 99px;
        font-size: .75rem;
        background: #6C5CE722;
        color: #6C5CE7 !important;
    }}

    </style>
    """, unsafe_allow_html=True)
