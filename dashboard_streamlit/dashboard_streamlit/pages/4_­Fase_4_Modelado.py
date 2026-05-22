"""
Pagina 4: Fase 4 de CRISP-DM - Modelado
Entrenamiento de SARIMA y Regresion Multiple con visualizacion interactiva.
"""

import warnings
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.statespace.sarimax import SARIMAX

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Fase 4 - Modelado", page_icon="🤖", layout="wide")

# ══════════════════════════════════════════════════════════════════════════════
# ESTILOS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;700;800&family=DM+Sans:wght@400;500&display=swap');

[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
section.main, .main .block-container,
[data-testid="stMain"] {
    background: #0A1628 !important;
    font-family: 'DM Sans', system-ui, sans-serif !important;
    color: #E2EAF4 !important;
}
[data-testid="stSidebar"] > div:first-child {
    background: #060E1A !important;
    border-right: 1px solid rgba(255,255,255,0.06) !important;
}
[data-testid="stSidebar"] * { color: #C4D4E8 !important; }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { color:#A8C0D6 !important; }
.block-container { padding-top: 0 !important; max-width: 1200px !important; }

/* Sliders */
[data-testid="stSlider"] > div > div > div { background: #C00000 !important; }
[data-testid="stSlider"] label { color: #A8C0D6 !important; font-size:0.82rem !important; }

/* Tabs */
[data-testid="stTabs"] [role="tablist"] {
    background: #111E33 !important;
    border-radius: 12px !important;
    padding: 4px !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    gap: 4px !important;
}
[data-testid="stTabs"] [role="tab"] {
    background: transparent !important;
    color: #6A8BAE !important;
    border-radius: 8px !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.02em !important;
    padding: 8px 18px !important;
    border: none !important;
    transition: all 0.2s !important;
}
[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
    background: linear-gradient(135deg,#C00000,#8B0000) !important;
    color: #fff !important;
    box-shadow: 0 4px 14px rgba(192,0,0,0.35) !important;
}
[data-testid="stTabs"] [role="tab"]:hover:not([aria-selected="true"]) {
    background: rgba(255,255,255,0.06) !important;
    color: #E2EAF4 !important;
}

/* Métricas */
[data-testid="metric-container"] {
    background: #111E33 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-top: 3px solid #C00000 !important;
    border-radius: 12px !important;
    padding: 18px 20px !important;
    transition: transform 0.2s, box-shadow 0.2s !important;
}
[data-testid="metric-container"]:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 28px rgba(0,0,0,0.4) !important;
}
[data-testid="stMetricLabel"] {
    font-family:'Sora',sans-serif !important; font-weight:700 !important;
    font-size:0.68rem !important; color:#6A8BAE !important;
    letter-spacing:0.07em !important; text-transform:uppercase !important;
}
[data-testid="stMetricValue"] {
    font-family:'Sora',sans-serif !important; font-weight:800 !important;
    font-size:1.7rem !important; color:#F0F6FF !important;
}
[data-testid="stMetricDelta"] { font-weight:600 !important; font-size:0.72rem !important; }

/* Expander */
[data-testid="stExpander"] {
    background: #111E33 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 10px !important;
}
[data-testid="stExpander"] summary {
    color: #A8C0D6 !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.82rem !important;
}

/* Dataframe */
[data-testid="stDataFrame"] { border-radius: 10px !important; overflow: hidden !important; }

/* Divider */
hr { border-color: rgba(255,255,255,0.08) !important; }

/* Alertas */
[data-testid="stAlert"] {
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    background: #111E33 !important;
}

/* Spinner */
[data-testid="stSpinner"] { color: #FF6B6B !important; }

/* Cards */
.phase-header {
    background: linear-gradient(135deg,#0D1B2A 0%,#1B3A5C 100%);
    border-radius: 16px; padding: 32px 36px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 8px;
    position: relative; overflow: hidden;
}
.phase-header::before {
    content:''; position:absolute; inset:0;
    background-image: radial-gradient(circle,rgba(255,255,255,0.03) 1px,transparent 1px);
    background-size: 24px 24px; pointer-events:none;
}
.phase-header::after {
    content:''; position:absolute; bottom:0; left:0; right:0; height:2px;
    background: linear-gradient(90deg,#C00000,#FF6B6B,#C00000);
}
.ph-badge {
    display:inline-block; font-size:0.62rem; font-weight:700;
    letter-spacing:0.14em; color:#FF6B6B;
    background:rgba(192,0,0,0.18); padding:4px 12px; border-radius:20px;
    border:1px solid rgba(192,0,0,0.3); text-transform:uppercase; margin-bottom:14px;
}
.ph-title {
    font-family:'Sora',sans-serif; font-size:1.9rem; font-weight:800;
    color:#fff; margin:0 0 8px; letter-spacing:-0.02em; line-height:1.2;
}
.ph-title span { color:#FF6B6B; }
.ph-sub { color:#7A9CB8; font-size:0.9rem; line-height:1.6; }

.ph-stats {
    display:flex; gap:32px; margin-top:20px;
    padding-top:20px; border-top:1px solid rgba(255,255,255,0.08);
    flex-wrap:wrap;
}
.ph-stat-val {
    font-family:'Sora',sans-serif; font-size:1.5rem; font-weight:800;
    color:#FF6B6B; letter-spacing:-0.02em;
}
.ph-stat-lbl { font-size:0.7rem; color:#5580A8; margin-top:2px; }

.sec-label {
    display:flex; align-items:center; gap:10px;
    margin:24px 0 16px; padding-bottom:10px;
    border-bottom:1px solid rgba(255,255,255,0.08);
}
.sec-label-text {
    font-family:'Sora',sans-serif; font-weight:700;
    font-size:1rem; color:#E2EAF4; letter-spacing:-0.01em;
}

.info-box {
    background: linear-gradient(135deg,#0D1929,#132040);
    border:1px solid rgba(255,255,255,0.08);
    border-left:3px solid #C00000;
    border-radius:10px; padding:16px 20px;
    font-size:0.85rem; color:#A8C0D6; line-height:1.7;
    margin:12px 0;
}
.info-box strong { color:#E2EAF4; }

.sidebar-section {
    background:#0D1929;
    border:1px solid rgba(255,255,255,0.08);
    border-radius:10px; padding:14px 16px; margin:10px 0;
}
.sidebar-section-title {
    font-family:'Sora',sans-serif; font-size:0.72rem; font-weight:700;
    color:#FF6B6B; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:10px;
}
.model-badge {
    display:inline-block;
    background:linear-gradient(135deg,#C00000,#8B0000);
    color:#fff; font-family:'Sora',sans-serif;
    font-size:0.72rem; font-weight:700;
    padding:5px 14px; border-radius:20px;
    letter-spacing:0.04em; margin-top:6px;
    box-shadow:0 4px 12px rgba(192,0,0,0.35);
}

.footer-cap {
    text-align:center; color:#3A5878; font-size:0.74rem;
    padding:14px 0 6px; border-top:1px solid rgba(255,255,255,0.07); margin-top:8px;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════════════════
ICONS = {
    "brain":    "%3Cpath d='M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96-.46 2.5 2.5 0 0 1-1.07-4.73A3 3 0 0 1 3.83 9a3 3 0 0 1 .79-5.07A2.5 2.5 0 0 1 9.5 2z'/%3E%3Cpath d='M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96-.46 2.5 2.5 0 0 0 1.07-4.73 3 3 0 0 0 2.64-4.27 3 3 0 0 0-.79-5.07A2.5 2.5 0 0 0 14.5 2z'/%3E",
    "chart":    "%3Cline x1='18' y1='20' x2='18' y2='10'/%3E%3Cline x1='12' y1='20' x2='12' y2='4'/%3E%3Cline x1='6' y1='20' x2='6' y2='14'/%3E",
    "trending": "%3Cpolyline points='23 6 13.5 15.5 8.5 10.5 1 18'/%3E%3Cpolyline points='17 6 23 6 23 12'/%3E",
    "compare":  "%3Cline x1='18' y1='20' x2='18' y2='10'/%3E%3Cline x1='12' y1='20' x2='12' y2='4'/%3E%3Cline x1='6' y1='20' x2='6' y2='14'/%3E",
    "settings": "%3Ccircle cx='12' cy='12' r='3'/%3E%3Cpath d='M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z'/%3E",
    "table":    "%3Cpath d='M9 3H5a2 2 0 0 0-2 2v4m6-6h10a2 2 0 0 1 2 2v4M9 3v18m0 0h10a2 2 0 0 0 2-2V9M9 21H5a2 2 0 0 1-2-2V9m0 0h18'/%3E",
    "params":   "%3Cline x1='4' y1='21' x2='4' y2='14'/%3E%3Cline x1='4' y1='10' x2='4' y2='3'/%3E%3Cline x1='12' y1='21' x2='12' y2='12'/%3E%3Cline x1='12' y1='8' x2='12' y2='3'/%3E%3Cline x1='20' y1='21' x2='20' y2='16'/%3E%3Cline x1='20' y1='12' x2='20' y2='3'/%3E%3Cline x1='1' y1='14' x2='7' y2='14'/%3E%3Cline x1='9' y1='8' x2='15' y2='8'/%3E%3Cline x1='17' y1='16' x2='23' y2='16'/%3E",
    "activity": "%3Cpolyline points='22 12 18 12 15 21 9 3 6 12 2 12'/%3E",
    "target":   "%3Ccircle cx='12' cy='12' r='10'/%3E%3Ccircle cx='12' cy='12' r='6'/%3E%3Ccircle cx='12' cy='12' r='2'/%3E",
}

def sec_label(icon_key, text):
    enc = ICONS.get(icon_key, ICONS["target"])
    bg = (
        f"url(\"data:image/svg+xml,%3Csvg xmlns='http%3A//www.w3.org/2000/svg' "
        f"width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23E03030' "
        f"stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E{enc}%3C/svg%3E\")"
    )
    st.markdown(
        '<div class="sec-label">'
        f'<span style="display:inline-block;width:20px;height:20px;flex-shrink:0;'
        f'background:{bg} center/20px no-repeat;"></span>'
        f'<span class="sec-label-text">{text}</span>'
        '</div>',
        unsafe_allow_html=True,
    )

def plotly_dark_layout(title="", height=480):
    return dict(
        title=title,
        title_font=dict(family="Sora", size=14, color="#E2EAF4"),
        height=height,
        template="plotly_dark",
        paper_bgcolor="rgba(13,25,41,0.95)",
        plot_bgcolor="rgba(13,25,41,0.95)",
        font=dict(family="DM Sans", color="#A8C0D6", size=12),
        hovermode="x unified",
        legend=dict(
            bgcolor="rgba(10,22,40,0.85)",
            bordercolor="rgba(255,255,255,0.1)",
            borderwidth=1,
            font=dict(family="DM Sans", color="#C4D4E8", size=11),
        ),
        xaxis=dict(gridcolor="rgba(255,255,255,0.04)", linecolor="rgba(255,255,255,0.08)", tickfont=dict(size=11)),
        yaxis=dict(gridcolor="rgba(255,255,255,0.04)", linecolor="rgba(255,255,255,0.08)", tickfont=dict(size=11)),
    )

# ══════════════════════════════════════════════════════════════════════════════
# DATOS
# ══════════════════════════════════════════════════════════════════════════════
@st.cache_data
def cargar_y_dividir():
    df = pd.read_csv("data/turismo_ayacucho_2010_2024.csv", parse_dates=["fecha"])
    df = df.sort_values("fecha").set_index("fecha")
    train = df[df.index < "2024-01-01"]
    test  = df[df.index >= "2024-01-01"]
    return df, train, test

@st.cache_data
def entrenar_sarima(_train, p, d, q, P, D, Q, s):
    modelo = SARIMAX(
        _train["arribos"],
        order=(p, d, q),
        seasonal_order=(P, D, Q, s),
        enforce_stationarity=False,
        enforce_invertibility=False,
    )
    return modelo.fit(disp=False)

@st.cache_data
def entrenar_regresion(_X_train, _y_train):
    modelo = LinearRegression()
    modelo.fit(_X_train, _y_train)
    return modelo

df, train, test = cargar_y_dividir()

# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════

# CSS extra solo para el sidebar
st.markdown("""
<style>
/* ── Logo sidebar ── */
.sb-logo {
    display:flex; align-items:center; gap:10px;
    padding:18px 16px 14px;
    border-bottom:1px solid rgba(255,255,255,0.08);
    margin-bottom:16px;
}
.sb-logo-icon {
    width:38px; height:38px; border-radius:10px; flex-shrink:0;
    background:linear-gradient(135deg,#C00000,#8B0000);
    display:flex; align-items:center; justify-content:center;
    box-shadow:0 4px 14px rgba(192,0,0,0.4);
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http%3A//www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3Cpath d='M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z'/%3E%3C/svg%3E");
    background-repeat:no-repeat;
    background-position:center;
    background-size:20px;
}
.sb-logo-title {
    font-family:'Sora',sans-serif; font-weight:800;
    font-size:0.82rem; color:#E2EAF4 !important; line-height:1.2;
}
.sb-logo-sub {
    font-size:0.63rem; color:#3A5878 !important; margin-top:2px;
}

/* ── Sección header ── */
.sb-section {
    margin: 8px 0 4px;
}
.sb-section-header {
    display:flex; align-items:center; gap:8px;
    padding:8px 12px;
    background:rgba(255,255,255,0.04);
    border-radius:8px;
    border-left:3px solid #C00000;
    margin-bottom:8px;
}
.sb-section-dot {
    width:16px; height:16px; flex-shrink:0;
    background-repeat:no-repeat;
    background-position:center;
    background-size:16px;
}
.sb-section-title {
    font-family:'Sora',sans-serif; font-size:0.68rem; font-weight:700;
    color:#FF6B6B !important; letter-spacing:0.1em; text-transform:uppercase;
}

/* ── Param rows ── */
.sb-param-row {
    display:flex; justify-content:space-between; align-items:center;
    padding:4px 0;
}
.sb-param-name { font-size:0.72rem; color:#7A9CB8 !important; }
.sb-param-val  {
    font-family:'Sora',sans-serif; font-size:0.82rem; font-weight:800;
    color:#FF6B6B !important; min-width:20px; text-align:right;
}

/* ── Badge modelo activo ── */
.sb-model-box {
    margin:14px 0 0;
    background:linear-gradient(135deg,#0D1B2A,#1B3A5C);
    border:1px solid rgba(255,255,255,0.1);
    border-radius:12px; padding:14px 16px;
    text-align:center;
}
.sb-model-label {
    font-size:0.62rem; color:#5580A8 !important; font-family:'Sora',sans-serif;
    letter-spacing:0.1em; text-transform:uppercase; margin-bottom:8px;
}
.sb-model-name {
    font-family:'Sora',sans-serif; font-size:1rem; font-weight:800;
    color:#FFFFFF !important; letter-spacing:-0.01em;
}
.sb-model-name span { color:#FF6B6B !important; }
.sb-model-pill {
    display:inline-block; margin-top:8px;
    font-size:0.62rem; font-weight:700; letter-spacing:0.06em;
    color:#A8C0D6 !important;
    background:rgba(255,255,255,0.06);
    border:1px solid rgba(255,255,255,0.1);
    padding:3px 10px; border-radius:20px;
}

/* ── Divider sidebar ── */
.sb-divider {
    height:1px; background:rgba(255,255,255,0.07);
    margin:14px 0;
}

/* ── Info pill ── */
.sb-info {
    background:rgba(192,0,0,0.1);
    border:1px solid rgba(192,0,0,0.2);
    border-radius:8px; padding:10px 12px;
    font-size:0.74rem; color:#A8C0D6 !important;
    line-height:1.6; margin-top:8px;
}
.sb-info b { color:#FF8A8A !important; }
</style>
""", unsafe_allow_html=True)

# ── Logo
st.sidebar.markdown("""
<div class="sb-logo">
  <div class="sb-logo-icon"></div>
  <div>
    <div class="sb-logo-title">Hiperparámetros</div>
    <div class="sb-logo-sub">Modelo SARIMA · Ajuste interactivo</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Sección No Estacional
ICON_WAVES = "%3Cpolyline points='22 12 18 12 15 21 9 3 6 12 2 12'/%3E"
st.sidebar.markdown(
    '<div class="sb-section">'
    '<div class="sb-section-header">'
    f'<span class="sb-section-dot" style="background-image:url(\'data:image/svg+xml,%3Csvg xmlns=%22http%3A//www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22%23FF6B6B%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22%3E{ICON_WAVES}%3C/svg%3E\');"></span>'
    '<span class="sb-section-title">No Estacional</span>'
    '</div>'
    '</div>',
    unsafe_allow_html=True,
)
p = st.sidebar.slider("p — Orden AR (rezagos pasados)", 0, 3, 1)
d = st.sidebar.slider("d — Diferenciación (estacionariedad)", 0, 2, 1)
q = st.sidebar.slider("q — Orden MA (errores pasados)", 0, 3, 1)

st.sidebar.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)

# ── Sección Estacional
ICON_SEASON = "%3Ccircle cx='12' cy='12' r='10'/%3E%3Cline x1='12' y1='8' x2='12' y2='12'/%3E%3Cline x1='12' y1='16' x2='12.01' y2='16'/%3E"
st.sidebar.markdown(
    '<div class="sb-section">'
    '<div class="sb-section-header">'
    f'<span class="sb-section-dot" style="background-image:url(\'data:image/svg+xml,%3Csvg xmlns=%22http%3A//www.w3.org/2000/svg%22 width=%2216%22 height=%2216%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22%23FF6B6B%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22%3E{ICON_SEASON}%3C/svg%3E\');"></span>'
    '<span class="sb-section-title">Estacional · s = 12</span>'
    '</div>'
    '</div>',
    unsafe_allow_html=True,
)
P = st.sidebar.slider("P — AR Estacional", 0, 2, 1)
D = st.sidebar.slider("D — Dif. Estacional", 0, 1, 1)
Q = st.sidebar.slider("Q — MA Estacional", 0, 2, 1)
s = 12

st.sidebar.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)

# ── Resumen parámetros actuales
st.sidebar.markdown(
    '<div style="padding:0 2px;">'
    + "".join([
        f'<div class="sb-param-row">'
        f'<span class="sb-param-name">{name}</span>'
        f'<span class="sb-param-val">{val}</span>'
        f'</div>'
        for name, val in [
            ("p (AR)", p), ("d (Dif.)", d), ("q (MA)", q),
            ("P (AR est.)", P), ("D (Dif. est.)", D), ("Q (MA est.)", Q), ("s (periodo)", s),
        ]
    ])
    + '</div>',
    unsafe_allow_html=True,
)

# ── Badge modelo activo
st.sidebar.markdown(
    f'<div class="sb-model-box">'
    f'<div class="sb-model-label">Modelo activo</div>'
    f'<div class="sb-model-name">'
    f'SARIMA<span>({p},{d},{q})</span>'
    f'<span style="color:#A8C0D6!important;">({P},{D},{Q})</span>'
    f'<span style="font-size:0.75rem;color:#5580A8!important;">₁₂</span>'
    f'</div>'
    f'<div class="sb-model-pill">Datos mensuales · 2010–2024</div>'
    f'</div>',
    unsafe_allow_html=True,
)

# ── Nota informativa
st.sidebar.markdown("""
<div class="sb-info">
  <b>Tip:</b> Cambia los sliders y el modelo se re-entrena automáticamente.
  Valores recomendados: <b>p=1, d=1, q=1, P=1, D=1, Q=1</b>.
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="phase-header">
  <div class="ph-badge">Fase 4 de 6 · CRISP-DM</div>
  <div class="ph-title">Modelado <span>Predictivo</span></div>
  <div class="ph-sub">Entrenamiento y comparación de modelos SARIMA y Regresión Lineal Múltiple</div>
  <div class="ph-stats">
    <div><div class="ph-stat-val">SARIMA</div><div class="ph-stat-lbl">Modelo de series temporales</div></div>
    <div><div class="ph-stat-val">RLM</div><div class="ph-stat-lbl">Regresión Lineal Múltiple</div></div>
    <div><div class="ph-stat-val">17</div><div class="ph-stat-lbl">Variables explicativas</div></div>
    <div><div class="ph-stat-val">{len(train)}</div><div class="ph-stat-lbl">Meses de entrenamiento</div></div>
    <div><div class="ph-stat-val">{len(test)}</div><div class="ph-stat-lbl">Meses de prueba</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TABS
# ══════════════════════════════════════════════════════════════════════════════
tab1, tab2, tab3 = st.tabs([
    "  SARIMA  ",
    "  Regresión Múltiple  ",
    "  Comparación  ",
])

# ─────────────────────────────────────────────
# TAB 1 — SARIMA
# ─────────────────────────────────────────────
with tab1:
    sec_label("brain", f"Modelo SARIMA({p},{d},{q})({P},{D},{Q})₁₂")

    st.markdown("""
    <div class="info-box">
        <strong>SARIMA</strong> (Seasonal AutoRegressive Integrated Moving Average) captura
        tanto la tendencia como los patrones estacionales de la serie temporal de arribos.
        Ajusta los parámetros en el panel lateral y observa el cambio en tiempo real.
    </div>
    """, unsafe_allow_html=True)

    with st.spinner("Entrenando modelo SARIMA…"):
        try:
            resultado_sarima = entrenar_sarima(train, p, d, q, P, D, Q, s)
            pred_sarima = resultado_sarima.forecast(steps=len(test))
            pred_sarima.index = test.index

            c1, c2, c3 = st.columns(3)
            with c1: st.metric("AIC",            f"{resultado_sarima.aic:.2f}")
            with c2: st.metric("BIC",            f"{resultado_sarima.bic:.2f}")
            with c3: st.metric("Log-Likelihood", f"{resultado_sarima.llf:.2f}")

            sec_label("trending", "Serie Histórica + Predicción 2024")

            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=train.index, y=train["arribos"],
                name="Entrenamiento",
                line=dict(color="#3A7BD5", width=2),
                fill="tozeroy", fillcolor="rgba(58,123,213,0.06)",
            ))
            fig.add_trace(go.Scatter(
                x=test.index, y=test["arribos"],
                name="Real 2024",
                line=dict(color="#4CAF82", width=3),
                mode="lines+markers",
                marker=dict(size=8, symbol="circle"),
            ))
            fig.add_trace(go.Scatter(
                x=pred_sarima.index, y=pred_sarima.values,
                name="SARIMA Predicción",
                line=dict(color="#FF4444", dash="dash", width=2),
                mode="lines+markers",
                marker=dict(size=8, symbol="diamond"),
            ))
            fig.update_layout(**plotly_dark_layout(
                f"SARIMA({p},{d},{q})({P},{D},{Q})₁₂ — Predicción vs Real", 500
            ))
            st.plotly_chart(fig, use_container_width=True)

            sec_label("params", "Parámetros del Modelo")
            with st.expander("Ver tabla completa de parámetros estimados"):
                params_df = pd.DataFrame({
                    "Parámetro":      resultado_sarima.param_names,
                    "Valor":          resultado_sarima.params,
                    "Error Estándar": resultado_sarima.bse,
                    "Estadístico z":  resultado_sarima.tvalues,
                    "p-valor":        resultado_sarima.pvalues,
                })
                st.dataframe(
                    params_df.style.format({
                        "Valor": "{:.4f}", "Error Estándar": "{:.4f}",
                        "Estadístico z": "{:.4f}", "p-valor": "{:.4f}",
                    }),
                    use_container_width=True, hide_index=True,
                )

        except Exception as e:
            st.error(f"Error al entrenar SARIMA: {e}")
            st.info("Prueba con otros valores de hiperparámetros en el panel lateral.")

# ─────────────────────────────────────────────
# TAB 2 — REGRESIÓN MÚLTIPLE
# ─────────────────────────────────────────────
with tab2:
    sec_label("activity", "Modelo de Regresión Lineal Múltiple")

    st.markdown("""
    <div class="info-box">
        La <strong>Regresión Lineal Múltiple</strong> modela los arribos en función de
        variables categóricas (mes codificado one-hot) y contextuales (clima, eventos,
        pandemia). Permite interpretar el impacto individual de cada variable.
    </div>
    """, unsafe_allow_html=True)

    X = pd.get_dummies(df["mes"], prefix="mes", drop_first=True).astype(int)
    for col in ["semana_santa","feriado_largo","temperatura_c",
                "precipitacion_mm","evento_cultural","pandemia_covid"]:
        X[col] = df[col].values

    X_train = X[df.index < "2024-01-01"]
    X_test  = X[df.index >= "2024-01-01"]
    y_train = df.loc[df.index < "2024-01-01", "arribos"].values
    y_test  = df.loc[df.index >= "2024-01-01", "arribos"].values

    with st.spinner("Entrenando regresión múltiple…"):
        modelo_rlm = entrenar_regresion(X_train, y_train)
        pred_rlm   = modelo_rlm.predict(X_test)

        c1, c2, c3 = st.columns(3)
        with c1: st.metric("R² Entrenamiento", f"{modelo_rlm.score(X_train, y_train):.4f}")
        with c2: st.metric("N° Variables",      f"{X_train.shape[1]}")
        with c3: st.metric("Intercepto",        f"{modelo_rlm.intercept_:,.0f}")

        sec_label("chart", "Importancia de Variables — Coeficientes")

        coef_df = pd.DataFrame({
            "Variable":     X.columns,
            "Coeficiente":  modelo_rlm.coef_,
        }).sort_values("Coeficiente", key=abs, ascending=False)

        colors = coef_df["Coeficiente"].apply(
            lambda v: "#FF4444" if v < 0 else "#3A7BD5"
        )

        fig_coef = go.Figure(go.Bar(
            x=coef_df["Coeficiente"],
            y=coef_df["Variable"],
            orientation="h",
            marker=dict(color=colors, opacity=0.85,
                        line=dict(color="rgba(255,255,255,0.05)", width=0.5)),
            text=coef_df["Coeficiente"].round(0).astype(int),
            textposition="outside",
            textfont=dict(color="#A8C0D6", size=11),
        ))
        fig_coef.update_layout(**plotly_dark_layout(
            "Coeficientes ordenados por magnitud absoluta", 520
        ))
        st.plotly_chart(fig_coef, use_container_width=True)

        sec_label("table", "Tabla Completa de Coeficientes")
        with st.expander("Ver tabla de coeficientes"):
            st.dataframe(
                coef_df.style.format({"Coeficiente": "{:,.2f}"}),
                use_container_width=True, hide_index=True,
            )

# ─────────────────────────────────────────────
# TAB 3 — COMPARACIÓN
# ─────────────────────────────────────────────
with tab3:
    sec_label("compare", "Comparación Visual: Real vs SARIMA vs Regresión")

    st.markdown("""
    <div class="info-box">
        Evaluación directa de ambos modelos sobre el conjunto de prueba (2024).
        Se contrasta el valor real con las predicciones de cada modelo mes a mes.
    </div>
    """, unsafe_allow_html=True)

    try:
        resultado_sarima = entrenar_sarima(train, p, d, q, P, D, Q, s)
        pred_sarima = resultado_sarima.forecast(steps=len(test))
        pred_sarima.index = test.index

        X2 = pd.get_dummies(df["mes"], prefix="mes", drop_first=True).astype(int)
        for col in ["semana_santa","feriado_largo","temperatura_c",
                    "precipitacion_mm","evento_cultural","pandemia_covid"]:
            X2[col] = df[col].values
        X_train2 = X2[df.index < "2024-01-01"]
        X_test2  = X2[df.index >= "2024-01-01"]
        y_train2 = df.loc[df.index < "2024-01-01", "arribos"].values
        y_test2  = df.loc[df.index >= "2024-01-01", "arribos"].values
        modelo_rlm2 = entrenar_regresion(X_train2, y_train2)
        pred_rlm2   = modelo_rlm2.predict(X_test2)

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=test.index, y=y_test2,
            name="Real 2024",
            line=dict(color="#4CAF82", width=4),
            mode="lines+markers",
            marker=dict(size=10, symbol="circle"),
        ))
        fig.add_trace(go.Scatter(
            x=test.index, y=pred_sarima.values,
            name="SARIMA",
            line=dict(color="#FF4444", dash="dash", width=2),
            mode="lines+markers",
            marker=dict(size=8, symbol="diamond"),
        ))
        fig.add_trace(go.Scatter(
            x=test.index, y=pred_rlm2,
            name="Regresión Múltiple",
            line=dict(color="#FFC107", dash="dot", width=2),
            mode="lines+markers",
            marker=dict(size=8, symbol="square"),
        ))
        fig.update_layout(**plotly_dark_layout(
            "Comparación: Real vs SARIMA vs Regresión Múltiple (2024)", 500
        ))
        st.plotly_chart(fig, use_container_width=True)

        sec_label("table", "Tabla Comparativa Mes a Mes")

        tabla = pd.DataFrame({
            "Mes":             [d.strftime("%b %Y") for d in test.index],
            "Real":            y_test2.astype(int),
            "SARIMA":          pred_sarima.values.astype(int),
            "Error SARIMA":    (y_test2 - pred_sarima.values).astype(int),
            "Regresión":       pred_rlm2.astype(int),
            "Error Regresión": (y_test2 - pred_rlm2).astype(int),
        })
        st.dataframe(tabla, use_container_width=True, hide_index=True)

        # Mini KPIs de error
        mape_sarima = float(np.mean(np.abs((y_test2 - pred_sarima.values) / y_test2)) * 100)
        mape_rlm    = float(np.mean(np.abs((y_test2 - pred_rlm2) / y_test2)) * 100)
        rmse_sarima = float(np.sqrt(np.mean((y_test2 - pred_sarima.values)**2)))
        rmse_rlm    = float(np.sqrt(np.mean((y_test2 - pred_rlm2)**2)))

        st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)
        sec_label("target", "Métricas de Error — Conjunto de Prueba 2024")

        k1, k2, k3, k4 = st.columns(4)
        with k1: st.metric("MAPE SARIMA",      f"{mape_sarima:.2f}%")
        with k2: st.metric("MAPE Regresión",   f"{mape_rlm:.2f}%")
        with k3: st.metric("RMSE SARIMA",      f"{rmse_sarima:,.0f}")
        with k4: st.metric("RMSE Regresión",   f"{rmse_rlm:,.0f}")

        mejor = "SARIMA" if mape_sarima < mape_rlm else "Regresión Múltiple"
        dif   = abs(mape_sarima - mape_rlm)
        st.success(
            f"**Mejor modelo:** {mejor} · ventaja de **{dif:.2f} pp** en MAPE "
            f"sobre el conjunto de prueba 2024."
        )

    except Exception as e:
        st.error(f"Error en la comparación: {e}")

st.markdown('<div class="footer-cap">Fase 4 de CRISP-DM · Modelado Predictivo · 2026</div>', unsafe_allow_html=True)