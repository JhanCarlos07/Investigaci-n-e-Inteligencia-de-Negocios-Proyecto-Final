"""
Pagina 6: Fase 6 de CRISP-DM - Despliegue
Pronostico mensual 2025 con escenarios interactivos.
"""

import warnings
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from statsmodels.tsa.statespace.sarimax import SARIMAX

warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Fase 6 - Pronostico",
    page_icon="https://cdn-icons-png.flaticon.com/512/3281/3281289.png",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=DM+Sans:wght@400;500&display=swap');

html, body { background:#0D1B2A !important; color:#C8D8E8 !important; font-family:'DM Sans',sans-serif; }
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
[data-testid="stHeader"],
section.main, .main .block-container, .stApp { background:#0D1B2A !important; }
[data-baseweb="tab-panel"], div[role="tabpanel"] { background:#0D1B2A !important; }
p, span, label, div, li { color:#C8D8E8 !important; }
h1,h2,h3,h4,h5,h6 { color:#F0F6FF !important; }
strong, b { color:#FFFFFF !important; }
hr { border-color:rgba(255,255,255,0.08) !important; }

[data-testid="stSidebar"] {
    background:linear-gradient(180deg,#07111C 0%,#0D1B2A 100%) !important;
    border-right:1px solid rgba(255,255,255,0.06) !important;
}
[data-testid="stSidebar"] * { color:#C8D8E8 !important; }
[data-testid="stSidebarNav"] a[aria-selected="true"] {
    background:rgba(192,0,0,0.25) !important; color:#FF8080 !important;
}

/* radio buttons */
[data-testid="stSidebar"] [data-testid="stRadio"] > div { gap:6px !important; }
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    background:rgba(255,255,255,0.04) !important;
    border:1px solid rgba(255,255,255,0.08) !important;
    border-radius:10px !important; padding:8px 12px !important;
    transition:all .2s !important; width:100% !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background:rgba(192,0,0,0.12) !important;
    border-color:rgba(192,0,0,0.35) !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] + div + label,
[data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] ~ label {
    background:rgba(192,0,0,0.20) !important;
    border-color:rgba(192,0,0,0.50) !important;
    color:#FF8080 !important;
}

/* sliders */
[data-testid="stSidebar"] .stSlider [role="slider"] {
    background:#C00000 !important; border:2px solid #FF6B6B !important;
    box-shadow:0 0 8px rgba(192,0,0,.5) !important;
}
[data-testid="stSidebar"] .stSlider [data-testid="stSliderTrackActive"] {
    background:linear-gradient(90deg,#C00000,#FF6B6B) !important;
}

/* checkbox */
[data-testid="stSidebar"] .stCheckbox {
    background:rgba(74,144,217,0.08); border:1px solid rgba(74,144,217,0.20);
    border-radius:10px; padding:10px 12px !important; transition:all .2s;
}
[data-testid="stSidebar"] .stCheckbox:hover {
    background:rgba(74,144,217,0.15); border-color:rgba(74,144,217,0.40);
}

/* download button */
[data-testid="stDownloadButton"] button {
    background:linear-gradient(90deg,#C00000,#8B0000) !important;
    color:#fff !important; border:none !important; border-radius:10px !important;
    font-family:'Sora',sans-serif !important; font-weight:600 !important;
    padding:10px 20px !important; transition:transform .2s, box-shadow .2s !important;
}
[data-testid="stDownloadButton"] button:hover {
    transform:translateY(-2px) !important;
    box-shadow:0 6px 20px rgba(192,0,0,.35) !important;
}

/* tabs */
.stTabs [data-baseweb="tab-list"] {
    background:#111E2D !important; border-radius:10px; padding:4px; gap:4px;
}
.stTabs [data-baseweb="tab"] {
    color:#7FA4C0 !important; border-radius:8px !important;
    font-family:'Sora',sans-serif !important; font-weight:600 !important; font-size:.87rem !important;
}
.stTabs [aria-selected="true"] { background:#1B3A5C !important; color:#FFFFFF !important; }
.stTabs [data-baseweb="tab-highlight"] { display:none !important; }

/* dataframe */
[data-testid="stDataFrame"] { background:#112240 !important; border-radius:12px; }
[data-testid="stDataFrame"] * { color:#C8D8E8 !important; }

@keyframes fadeSlideDown {
    from{opacity:0;transform:translateY(-28px);}
    to  {opacity:1;transform:translateY(0);}
}
@keyframes fadeSlideUp {
    from{opacity:0;transform:translateY(20px);}
    to  {opacity:1;transform:translateY(0);}
}
@keyframes scaleIn {
    from{opacity:0;transform:scale(0.90);}
    to  {opacity:1;transform:scale(1);}
}
@keyframes shimmer {
    0%  {background-position:-600px 0;}
    100%{background-position: 600px 0;}
}
@keyframes spinOnce {
    from{transform:rotate(-18deg) scale(0.8);opacity:0;}
    to  {transform:rotate(0deg)   scale(1);  opacity:1;}
}
@keyframes countUp {
    from{opacity:0;transform:translateY(10px);}
    to  {opacity:1;transform:translateY(0);}
}
@keyframes iconBounce {
    0%,100%{transform:translateY(0);}
    50%    {transform:translateY(-5px);}
}
@keyframes pulseGlow {
    0%  {box-shadow:0 0 0 0   rgba(192,0,0,.4);}
    70% {box-shadow:0 0 0 12px rgba(192,0,0,0);}
    100%{box-shadow:0 0 0 0   rgba(192,0,0,0);}
}

.phase-hero {
    background:linear-gradient(135deg,#07111C 0%,#1a0a0a 40%,#112240 100%);
    border-radius:18px; padding:34px 40px 26px;
    margin-bottom:6px; position:relative; overflow:hidden;
    border:1px solid rgba(255,255,255,0.07);
    animation:fadeSlideDown .75s cubic-bezier(.22,1,.36,1) both;
    box-shadow:0 8px 40px rgba(0,0,0,.5);
}
.phase-hero::before {
    content:''; position:absolute; inset:0;
    background:radial-gradient(ellipse at 80% 50%,rgba(192,0,0,.20) 0%,transparent 60%);
    pointer-events:none;
}
.phase-hero::after {
    content:''; position:absolute; bottom:0; left:0; right:0; height:3px;
    background:linear-gradient(90deg,#C00000,#FF6B6B,#FFB347,#C00000);
    background-size:300% 100%; animation:shimmer 3s linear infinite;
}
.phase-badge {
    display:inline-flex; align-items:center; gap:6px;
    background:rgba(192,0,0,.20); border:1px solid rgba(192,0,0,.40);
    color:#FF8080 !important; border-radius:20px;
    padding:4px 14px; font-size:.74rem; font-weight:700;
    font-family:'Sora',sans-serif; letter-spacing:.7px; margin-bottom:12px;
}
.phase-title {
    font-family:'Sora',sans-serif; font-weight:800;
    font-size:2rem; color:#F0F6FF !important; margin:0; line-height:1.2;
}
.phase-title span { color:#FF6B6B !important; }
.phase-sub { color:#7FA4C0 !important; margin-top:8px; font-size:.96rem; }

.accent-line {
    height:3px; border-radius:2px; margin:18px 0;
    background:linear-gradient(90deg,#C00000,#FF6B6B,#C00000);
    background-size:200% 100%; animation:shimmer 4s linear infinite;
}

.sec-title {
    display:flex; align-items:center; gap:10px; margin-bottom:14px;
    animation:fadeSlideUp .6s cubic-bezier(.22,1,.36,1) both;
}
.sec-title h3 {
    font-family:'Sora',sans-serif; font-weight:700;
    color:#E8F0F8 !important; margin:0; font-size:1.12rem;
}

[data-testid="metric-container"] {
    background:linear-gradient(135deg,#112240,#0D1B2A) !important;
    border:1px solid rgba(255,255,255,0.10) !important;
    border-top:3px solid #C00000 !important;
    border-radius:14px !important; padding:18px 20px !important;
    box-shadow:0 4px 20px rgba(0,0,0,.35) !important;
    animation:countUp .6s cubic-bezier(.22,1,.36,1) both;
    transition:transform .25s, box-shadow .25s !important;
}
[data-testid="metric-container"]:hover {
    transform:translateY(-5px) !important;
    box-shadow:0 12px 32px rgba(192,0,0,.20) !important;
    border-top-color:#FF6B6B !important;
}
[data-testid="metric-container"]:nth-child(1){animation-delay:.05s;}
[data-testid="metric-container"]:nth-child(2){animation-delay:.15s;}
[data-testid="metric-container"]:nth-child(3){animation-delay:.25s;}
[data-testid="metric-container"]:nth-child(4){animation-delay:.35s;}
[data-testid="stMetricLabel"]{font-family:'Sora',sans-serif !important;font-weight:600 !important;color:#7FA4C0 !important;font-size:.79rem !important;}
[data-testid="stMetricValue"]{font-family:'Sora',sans-serif !important;font-weight:800 !important;color:#F0F6FF !important;font-size:1.65rem !important;}

.sb-title {
    font-family:'Sora',sans-serif; font-weight:800; font-size:.95rem;
    color:#F0F6FF !important; display:flex; align-items:center; gap:9px;
    padding:12px 0 10px; border-bottom:1px solid rgba(192,0,0,0.25);
    margin-bottom:14px;
}
.sb-label {
    font-family:'Sora',sans-serif; font-weight:600; font-size:.74rem;
    color:#7FA4C0 !important; text-transform:uppercase; letter-spacing:.6px;
    margin-bottom:4px; display:flex; align-items:center; gap:6px;
}
.sb-sep { height:1px; background:rgba(255,255,255,0.06); margin:14px 0; }
.sb-badge {
    display:inline-flex; align-items:center; gap:5px;
    background:rgba(192,0,0,0.15); border:1px solid rgba(192,0,0,0.30);
    color:#FF8080 !important; border-radius:20px;
    padding:3px 10px; font-size:.73rem; font-weight:700;
    font-family:'Sora',sans-serif; margin-top:6px;
}
.sb-info {
    background:rgba(192,0,0,0.08); border:1px solid rgba(192,0,0,0.20);
    border-radius:10px; padding:10px 12px; margin-top:14px;
    font-size:.80rem; color:#A8C0D6 !important; line-height:1.7;
}
.sb-info b { color:#FF8080 !important; }

.escenario-card {
    background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08);
    border-radius:12px; padding:14px 16px; margin:6px 0;
    display:flex; align-items:center; gap:12px;
    animation:fadeSlideUp .5s cubic-bezier(.22,1,.36,1) both;
    transition:all .25s;
}
.escenario-card:hover {
    background:rgba(192,0,0,0.10); border-color:rgba(192,0,0,0.35);
    transform:translateX(4px);
}
.escenario-card svg { flex-shrink:0; }
.escenario-card span { color:#C8D8E8 !important; }
.escenario-card b { color:#F0F6FF !important; }

.impl-card {
    background:rgba(17,34,64,0.70); border:1px solid rgba(255,255,255,0.09);
    border-radius:14px; padding:20px 22px;
    animation:scaleIn .55s cubic-bezier(.22,1,.36,1) both;
    transition:transform .25s, box-shadow .25s;
}
.impl-card:hover { transform:translateY(-3px); box-shadow:0 8px 28px rgba(0,0,0,.35); }
.impl-card-title {
    font-family:'Sora',sans-serif; font-weight:700; font-size:.88rem;
    color:#4A90D9 !important; margin-bottom:12px;
    display:flex; align-items:center; gap:7px;
    text-transform:uppercase; letter-spacing:.5px;
}
.impl-item {
    display:flex; align-items:flex-start; gap:9px;
    padding:8px 0; border-bottom:1px solid rgba(255,255,255,0.05);
    color:#C8D8E8 !important; font-size:.88rem; line-height:1.5;
}
.impl-item:last-child { border-bottom:none; }
.impl-item b { color:#E8F0F8 !important; }

.alert-success-dark {
    background:rgba(46,125,50,0.15); border:1px solid rgba(76,175,80,0.30);
    border-left:4px solid #4CAF50; border-radius:12px;
    padding:18px 20px; color:#C8E6C9 !important;
    font-size:.95rem; line-height:1.75;
    animation:scaleIn .6s cubic-bezier(.22,1,.36,1) both;
    display:flex; gap:14px; align-items:flex-start;
}
.alert-success-dark b { color:#A5D6A7 !important; }

.alert-info-dark {
    background:rgba(74,144,217,0.10); border:1px solid rgba(74,144,217,0.25);
    border-left:4px solid #4A90D9; border-radius:12px;
    padding:14px 18px; color:#C8D8E8 !important; font-size:.88rem; line-height:1.7;
    display:flex; gap:12px; align-items:flex-start;
}
.alert-info-dark b { color:#90C8F0 !important; }

.footer { text-align:center; color:#3A5A7A !important; font-size:.76rem; padding:8px 0; }

.d1{animation-delay:.04s;} .d2{animation-delay:.11s;} .d3{animation-delay:.18s;}
.d4{animation-delay:.25s;} .d5{animation-delay:.32s;} .d6{animation-delay:.39s;}
</style>
""", unsafe_allow_html=True)

# ══ SVG HELPERS ══
def svg(d, size=22, color="#FF6B6B", sw=2):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
            f'viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">{d}</svg>')

IC = {
    "radio-tower":  '<path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9"/><path d="M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5"/><circle cx="12" cy="12" r="2"/><path d="M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5"/><path d="M19.1 4.9C23 8.8 23 15.2 19.1 19.1"/>',
    "layers":       '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
    "trending-up":  '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
    "bar-chart":    '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>',
    "table":        '<path d="M9 3H5a2 2 0 0 0-2 2v4m6-6h10a2 2 0 0 1 2 2v4M9 3v18m0 0h10a2 2 0 0 0 2-2V9M9 21H5a2 2 0 0 1-2-2V9m0 0h18"/>',
    "dollar":       '<line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
    "calendar":     '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
    "star":         '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "target":       '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "sliders":      '<line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/>',
    "info":         '<circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>',
    "check-circle": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>',
    "alert-tri":    '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    "trending-down":'<polyline points="23 18 13.5 8.5 8.5 13.5 1 6"/><polyline points="17 18 23 18 23 12"/>',
    "minus-circle": '<circle cx="12" cy="12" r="10"/><line x1="8" y1="12" x2="16" y2="12"/>',
    "zap":          '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
    "building":     '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22V12h6v10"/><path d="M9 7h1"/><path d="M14 7h1"/>',
    "users":        '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "truck":        '<rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/>',
    "shield":       '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "lightbulb":    '<line x1="9" y1="18" x2="15" y2="18"/><line x1="10" y1="22" x2="14" y2="22"/><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/>',
    "activity":     '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
    "map-pin":      '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
}

def I(name, size=20, color="#FF6B6B", sw=2):
    return svg(IC.get(name, ""), size, color, sw)

def sec(icon, title, color="#FF6B6B"):
    st.markdown(f"""
    <div class="sec-title">
        {I(icon, 24, color)}
        <h3>{title}</h3>
    </div>""", unsafe_allow_html=True)

# ══ CARGA DE DATOS ══
@st.cache_resource
def generar_pronostico():
    df = pd.read_csv("data/turismo_ayacucho_2010_2024.csv", parse_dates=["fecha"])
    df = df.sort_values("fecha").set_index("fecha")
    modelo = SARIMAX(df["arribos"], order=(1,1,1), seasonal_order=(1,1,1,12),
                     enforce_stationarity=False, enforce_invertibility=False)
    resultado = modelo.fit(disp=False)
    pron  = resultado.get_forecast(steps=12)
    pred  = pron.predicted_mean
    ic95  = pron.conf_int(alpha=0.05)
    ic80  = pron.conf_int(alpha=0.20)
    fechas = pd.date_range("2025-01-01", periods=12, freq="MS")
    pred.index = fechas; ic95.index = fechas; ic80.index = fechas
    return df, pred, ic95, ic80

with st.spinner("Generando pronostico SARIMA..."):
    df, pred_2025, ic95, ic80 = generar_pronostico()

meses_nom  = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
meses_largo= ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
               "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

# ══ SIDEBAR ══
st.sidebar.markdown(f"""
<div class="sb-title">
    {I("sliders",18,"#FF6B6B")} Configuracion
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown(f"""
<div class="sb-label">{I("zap",13,"#7FA4C0")} Escenario de Pronostico</div>
""", unsafe_allow_html=True)

escenario = st.sidebar.radio(
    "Escenario", ["Pesimista (-15%)", "Base", "Optimista (+15%)"],
    index=1, label_visibility="collapsed"
)

factor = {"Pesimista (-15%)": 0.85, "Base": 1.00, "Optimista (+15%)": 1.15}[escenario]
esc_color = {"Pesimista (-15%)": "#FF6B6B", "Base": "#4A90D9", "Optimista (+15%)": "#4CAF50"}[escenario]
esc_icon  = {"Pesimista (-15%)": "trending-down", "Base": "minus-circle", "Optimista (+15%)": "trending-up"}[escenario]

st.sidebar.markdown(f"""
<div class="sb-badge">{I(esc_icon,12,esc_color)} Factor: {factor:.0%}</div>
<div class="sb-sep"></div>
""", unsafe_allow_html=True)

st.sidebar.markdown(f"""
<div class="sb-label">{I("activity",13,"#7FA4C0")} Intervalos de Confianza</div>
""", unsafe_allow_html=True)

mostrar_ic = st.sidebar.checkbox("Mostrar intervalos de confianza", value=True)
nivel_ic   = st.sidebar.radio("Nivel:", ["80%", "95%"], index=1, horizontal=True)
ic_a_usar  = ic95 if nivel_ic == "95%" else ic80

st.sidebar.markdown('<div class="sb-sep"></div>', unsafe_allow_html=True)

st.sidebar.markdown(f"""
<div class="sb-label">{I("dollar",13,"#7FA4C0")} Parametros Economicos</div>
""", unsafe_allow_html=True)

gasto_diario  = st.sidebar.slider("Gasto por turista (S/. /dia)", 200, 600, 380, 20)
estancia_dias = st.sidebar.slider("Estancia promedio (dias)",     1.0, 5.0, 2.5, 0.5)

impacto_aprox = pred_2025.sum() * factor * estancia_dias * gasto_diario
st.sidebar.markdown(f"""
<div class="sb-info">
    {I("dollar",14,"#FF6B6B")} Impacto anual estimado:<br>
    <b>S/. {impacto_aprox/1e6:.1f} millones</b>
</div>
""", unsafe_allow_html=True)

pred_ajustada = pred_2025 * factor
ic_ajustado   = ic_a_usar * factor

# ══ HERO ══
st.markdown(f"""
<div class="phase-hero">
    <div class="phase-badge">
        {I("layers",13,"#FF8080",2)} &nbsp;CRISP-DM &nbsp;·&nbsp; FASE 6 DE 6
    </div>
    <div style="display:flex;align-items:center;gap:18px;">
        <div style="animation:spinOnce .8s cubic-bezier(.22,1,.36,1) both;">
            {I("radio-tower",50,"#FF6B6B",1.6)}
        </div>
        <div>
            <h1 class="phase-title">Despliegue — <span>Pronostico 2025</span></h1>
            <p class="phase-sub">
                Pronostico mensual con intervalos de confianza y analisis de escenarios
            </p>
        </div>
    </div>
</div>
<div class="accent-line"></div>
""", unsafe_allow_html=True)

# ══ METRICAS ══
total = pred_ajustada.sum()
mes_pico_idx  = pred_ajustada.values.argmax()
mes_valle_idx = pred_ajustada.values.argmin()
valor_pico    = pred_ajustada.iloc[mes_pico_idx]
valor_valle   = pred_ajustada.iloc[mes_valle_idx]
crecimiento   = (total - 490000) / 490000 * 100

sec("bar-chart", f"Resumen del Pronostico — Escenario: {escenario}", esc_color)

col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("Total Anual 2025",   f"{total:,.0f}")
with col2: st.metric("Mes Pico",           meses_nom[mes_pico_idx],  delta=f"{valor_pico:,.0f} arribos")
with col3: st.metric("Mes Valle",          meses_nom[mes_valle_idx], delta=f"{valor_valle:,.0f} arribos")
with col4: st.metric("vs 2024 (490k)",     f"{crecimiento:+.1f}%")

st.divider()

# ══ TABS ══
tab1, tab2, tab3, tab4 = st.tabs([
    "  Pronostico Visual  ",
    "  Tabla Mensual  ",
    "  Impacto Economico  ",
    "  Semana Santa 2025  ",
])

# ── TAB 1 ──────────────────────────────────────────────────────────────────
with tab1:
    sec("trending-up", "Visualizacion del Pronostico")

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df.index[-60:], y=df["arribos"].iloc[-60:],
        name="Historico (5 años)",
        line=dict(color="#4A90D9", width=2),
        fill="tozeroy", fillcolor="rgba(74,144,217,0.10)",
    ))
    fig.add_trace(go.Scatter(
        x=pred_ajustada.index, y=pred_ajustada.values,
        name=f"Pronostico {escenario}",
        line=dict(color=esc_color, width=3, dash="dash"),
        mode="lines+markers",
        marker=dict(size=10, color=esc_color,
                    line=dict(color="#0D1B2A", width=2)),
    ))
    if mostrar_ic:
        fig.add_trace(go.Scatter(
            x=pred_ajustada.index, y=ic_ajustado.iloc[:, 1].values,
            mode="lines", line=dict(width=0), showlegend=False,
        ))
        fig.add_trace(go.Scatter(
            x=pred_ajustada.index, y=ic_ajustado.iloc[:, 0].values,
            mode="lines", line=dict(width=0),
            fill="tonexty", fillcolor=f"rgba(192,0,0,0.12)",
            name=f"IC {nivel_ic}",
        ))
    fig.add_shape(
        type="line",
        x0="2025-01-01", x1="2025-01-01",
        y0=0, y1=1, yref="paper",
        line=dict(color="rgba(255,255,255,0.3)", dash="dot", width=1.5),
    )
    fig.add_annotation(
        x="2025-01-01", y=1, yref="paper",
        text="Inicio 2025", showarrow=False,
        font=dict(color="#7FA4C0", size=11),
        xanchor="left", yanchor="top",
        bgcolor="rgba(13,27,42,0.7)",
        bordercolor="rgba(255,255,255,0.1)",
        borderwidth=1,
    )   
    fig.update_layout(
        title=dict(text=f"Pronostico de Arribos 2025 — {escenario}",
                   font=dict(color="#E8F0F8", size=15)),
        xaxis_title="Fecha", yaxis_title="Numero de Arribos",
        hovermode="x unified", height=520,
        paper_bgcolor="#0D1B2A", plot_bgcolor="#112240",
        font=dict(color="#C8D8E8"),
        xaxis=dict(gridcolor="rgba(255,255,255,0.05)", color="#7FA4C0"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.05)", color="#7FA4C0"),
        legend=dict(bgcolor="rgba(17,34,64,0.8)", bordercolor="rgba(255,255,255,0.1)",
                    borderwidth=1, font=dict(color="#C8D8E8")),
    )
    st.plotly_chart(fig, use_container_width=True)

    # escenarios comparativos
    sec("zap", "Comparacion de Escenarios", "#FFB347")
    scenarios = [
        ("trending-down", "#FF6B6B", "Pesimista (-15%)", pred_2025.sum()*0.85),
        ("minus-circle",  "#4A90D9", "Base",             pred_2025.sum()*1.00),
        ("trending-up",   "#4CAF50", "Optimista (+15%)", pred_2025.sum()*1.15),
    ]
    for (icon, color, label, val), dc in zip(scenarios, ["d1","d2","d3"]):
        active = "border-color:rgba(255,255,255,0.20);" if label == escenario else ""
        st.markdown(f"""
        <div class="escenario-card {dc}" style="{active}">
            {I(icon, 20, color)}
            <div style="flex:1;">
                <span><b>{label}</b></span><br>
                <span style="font-size:.85rem;color:#7FA4C0 !important;">
                    Total anual estimado: <b style="color:{color} !important;">{val:,.0f} arribos</b>
                </span>
            </div>
            {'<span style="color:#FFB347;font-size:.75rem;font-weight:700;font-family:Sora,sans-serif;">ACTIVO</span>' if label==escenario else ''}
        </div>""", unsafe_allow_html=True)

# ── TAB 2 ──────────────────────────────────────────────────────────────────
with tab2:
    sec("table", "Pronostico Mensual Detallado")

    tabla = pd.DataFrame({
        "Mes": meses_largo,
        "Pronostico": pred_ajustada.values.astype(int),
        f"IC {nivel_ic} Inferior": ic_ajustado.iloc[:, 0].values.astype(int),
        f"IC {nivel_ic} Superior": ic_ajustado.iloc[:, 1].values.astype(int),
        "Pernoctaciones Est.": (pred_ajustada.values * estancia_dias).astype(int),
        "Impacto S/.": (pred_ajustada.values * estancia_dias * gasto_diario).astype(int),
    })

    st.dataframe(tabla.style.format({
        "Pronostico": "{:,}",
        f"IC {nivel_ic} Inferior": "{:,}",
        f"IC {nivel_ic} Superior": "{:,}",
        "Pernoctaciones Est.": "{:,}",
        "Impacto S/.": "{:,}",
    }), use_container_width=True, hide_index=True, height=480)

    csv = tabla.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="  Descargar pronostico (CSV)",
        data=csv,
        file_name=f"pronostico_2025_{escenario.split()[0].lower()}.csv",
        mime="text/csv",
    )

# ── TAB 3 ──────────────────────────────────────────────────────────────────
with tab3:
    sec("dollar", "Impacto Economico Estimado del Turismo 2025", "#4CAF50")

    pernoctaciones_total = pred_ajustada.sum() * estancia_dias
    impacto_total        = pernoctaciones_total * gasto_diario
    impacto_mensual_prom = impacto_total / 12

    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Pernoctaciones Totales",    f"{pernoctaciones_total:,.0f}")
    with col2: st.metric("Impacto Anual",             f"S/. {impacto_total:,.0f}")
    with col3: st.metric("Impacto Mensual Promedio",  f"S/. {impacto_mensual_prom:,.0f}")

    st.markdown("<br>", unsafe_allow_html=True)
    impacto_mensual = pred_ajustada * estancia_dias * gasto_diario
    bar_colors = ["#C00000" if v == impacto_mensual.max()
                  else "#4CAF50" if v > impacto_mensual.mean()
                  else "#4A90D9" for v in impacto_mensual.values]

    fig_imp = go.Figure(go.Bar(
        x=meses_nom, y=impacto_mensual.values,
        marker_color=bar_colors,
        text=[f"S/. {v/1e6:.1f}M" for v in impacto_mensual.values],
        textposition="outside",
        textfont=dict(color="#C8D8E8", size=10),
    ))
    fig_imp.update_layout(
        title=dict(text=f"Impacto Economico Mensual — {escenario}",
                   font=dict(color="#E8F0F8", size=14)),
        xaxis_title="Mes", yaxis_title="Impacto en Soles",
        height=450,
        paper_bgcolor="#0D1B2A", plot_bgcolor="#112240",
        font=dict(color="#C8D8E8"),
        xaxis=dict(gridcolor="rgba(255,255,255,0.05)", color="#7FA4C0"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.05)", color="#7FA4C0"),
    )
    st.plotly_chart(fig_imp, use_container_width=True)

    st.markdown(f"""
    <div class="alert-info-dark">
        {I("info",22,"#4A90D9")}
        <div>
            <b>Parametros usados:</b> {estancia_dias} dias de estancia promedio
            x S/. {gasto_diario}/dia. Ajusta los valores en la barra lateral
            para simular diferentes escenarios economicos.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── TAB 4 ──────────────────────────────────────────────────────────────────
with tab4:
    sec("star", "Caso de Aplicacion: Semana Santa 2025", "#FFB347")

    arribos_abril      = pred_ajustada.loc["2025-04-01"]
    pernoctaciones_abril = arribos_abril * estancia_dias
    impacto_abril      = pernoctaciones_abril * gasto_diario
    ocupacion          = pernoctaciones_abril / (8000 * 30) * 100

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        sec("bar-chart", "Cifras Clave — Abril 2025", "#FFB347")
        st.metric("Arribos esperados (Abril)",   f"{arribos_abril:,.0f}")
        st.metric("Pernoctaciones estimadas",    f"{pernoctaciones_abril:,.0f}")
        st.metric("Impacto economico",           f"S/. {impacto_abril:,.0f}")
        st.metric("Ocupacion hotelera estimada", f"{ocupacion:.1f}%",
                  help="Asumiendo 8,000 habitaciones x 30 dias")

    with col2:
        sec("lightbulb", "Implicaciones Operativas", "#4A90D9")

        grupos = [
            ("building", "#4A90D9", "Para la DIRCETUR", [
                ("calendar","Iniciar campanas promocionales en <b>enero 2025</b>"),
                ("users",   "Coordinar con operadores hoteleros en <b>febrero 2025</b>"),
                ("truck",   "Desplegar operativo logistico desde <b>marzo 2025</b>"),
            ]),
            ("building", "#FFB347", "Para los Hoteleros", [
                ("shield",   "Asegurar capacidad antes de febrero"),
                ("users",    "Contratar personal temporal con 30 dias de anticipacion"),
                ("map-pin",  "Coordinar con proveedores locales"),
            ]),
            ("shield", "#4CAF50", "Para las Autoridades", [
                ("shield",   "Reforzar seguridad ciudadana"),
                ("truck",    "Ampliar servicios de transporte publico"),
                ("activity", "Coordinar atencion medica de emergencia"),
            ]),
        ]

        for (g_icon, g_color, g_title, items) in grupos:
            items_html = "".join(
                f'<div class="impl-item">{I(i,15,"#7FA4C0")} <span>{t}</span></div>'
                for i, t in items
            )
            st.markdown(f"""
            <div class="impl-card" style="margin-bottom:12px;">
                <div class="impl-card-title" style="color:{g_color} !important;">
                    {I(g_icon,15,g_color)} {g_title}
                </div>
                {items_html}
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="alert-success-dark">
        {I("check-circle",28,"#4CAF50",2)}
        <div>
            <b>Recomendacion clave:</b> Con el escenario <b>{escenario}</b>,
            se proyectan <b>{arribos_abril:,.0f} turistas</b> en Semana Santa 2025,
            generando un impacto economico de
            <b>S/. {impacto_abril/1e6:.1f} millones</b>.
            Esto justifica una inversion publicitaria proporcional
            para mantener el flujo turistico creciente.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown("""
<p class="footer">
    Fase 6 de CRISP-DM &nbsp;&#183;&nbsp; Despliegue del Modelo
    &nbsp;&#183;&nbsp; Pronostico 2025 &nbsp;&#183;&nbsp; Investigacion e Inteligencia de Negocios
</p>
""", unsafe_allow_html=True)