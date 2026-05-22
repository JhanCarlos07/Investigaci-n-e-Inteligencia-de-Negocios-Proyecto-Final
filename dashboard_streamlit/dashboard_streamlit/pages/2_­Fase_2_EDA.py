"""
Pagina 2: Fase 2 de CRISP-DM - Comprension de los Datos (EDA)
Tema oscuro profesional con iconos SVG y animaciones.
"""

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Fase 2 - EDA",
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
section.main, .main .block-container,
.stApp { background:#0D1B2A !important; }

[data-baseweb="tab-panel"],
div[role="tabpanel"] { background:#0D1B2A !important; }

p, span, label, div, li { color:#C8D8E8 !important; }
h1,h2,h3,h4,h5,h6 { color:#F0F6FF !important; }
strong, b { color:#FFFFFF !important; }

[data-testid="stSidebar"] {
    background:linear-gradient(180deg,#07111C 0%,#0D1B2A 100%) !important;
    border-right:1px solid rgba(255,255,255,0.06) !important;
}
[data-testid="stSidebar"] * { color:#C8D8E8 !important; }
[data-testid="stSidebarNav"] a:hover { background:rgba(255,255,255,0.07) !important; }
[data-testid="stSidebarNav"] a[aria-selected="true"] {
    background:rgba(192,0,0,0.25) !important; color:#FF8080 !important;
}

.stTabs [data-baseweb="tab-list"] {
    background:#111E2D !important; border-radius:10px; padding:4px; gap:4px;
}
.stTabs [data-baseweb="tab"] {
    color:#7FA4C0 !important; border-radius:8px !important;
    font-family:'Sora',sans-serif !important; font-weight:600 !important; font-size:.87rem !important;
}
.stTabs [aria-selected="true"] { background:#1B3A5C !important; color:#FFFFFF !important; }
.stTabs [data-baseweb="tab-highlight"] { display:none !important; }

[data-testid="stDataFrame"] { background:#112240 !important; border-radius:12px; }
[data-testid="stDataFrame"] * { color:#C8D8E8 !important; }

[data-testid="stDownloadButton"] button {
    background:linear-gradient(90deg,#C00000,#8B0000) !important;
    color:#fff !important; border:none !important; border-radius:10px !important;
    font-family:'Sora',sans-serif !important; font-weight:600 !important;
    padding:10px 20px !important;
    transition:transform .2s, box-shadow .2s !important;
}
[data-testid="stDownloadButton"] button:hover {
    transform:translateY(-2px) !important;
    box-shadow:0 6px 20px rgba(192,0,0,.35) !important;
}

hr { border-color:rgba(255,255,255,0.08) !important; }

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

.phase-hero {
    background:linear-gradient(135deg,#07111C 0%,#112240 55%,#07111C 100%);
    border-radius:18px; padding:34px 40px 26px;
    margin-bottom:6px; position:relative; overflow:hidden;
    border:1px solid rgba(255,255,255,0.07);
    animation:fadeSlideDown .75s cubic-bezier(.22,1,.36,1) both;
    box-shadow:0 8px 40px rgba(0,0,0,.5);
}
.phase-hero::before {
    content:''; position:absolute; inset:0;
    background:radial-gradient(ellipse at 75% 50%,rgba(74,144,217,.15) 0%,transparent 60%);
    pointer-events:none;
}
.phase-hero::after {
    content:''; position:absolute; bottom:0; left:0; right:0; height:3px;
    background:linear-gradient(90deg,#4A90D9,#FF6B6B,#FFB347,#4A90D9);
    background-size:300% 100%; animation:shimmer 3s linear infinite;
}
.phase-badge {
    display:inline-flex; align-items:center; gap:6px;
    background:rgba(74,144,217,.20); border:1px solid rgba(74,144,217,.40);
    color:#90C8F0 !important; border-radius:20px;
    padding:4px 14px; font-size:.74rem; font-weight:700;
    font-family:'Sora',sans-serif; letter-spacing:.7px; margin-bottom:12px;
}
.phase-title {
    font-family:'Sora',sans-serif; font-weight:800;
    font-size:2rem; color:#F0F6FF !important; margin:0; line-height:1.2;
}
.phase-title span { color:#4A90D9 !important; }
.phase-sub { color:#7FA4C0 !important; margin-top:8px; font-size:.96rem; }

.accent-line {
    height:3px; border-radius:2px; margin:18px 0;
    background:linear-gradient(90deg,#4A90D9,#C00000,#4A90D9);
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
    border-top:3px solid #4A90D9 !important;
    border-radius:14px !important; padding:18px 20px !important;
    box-shadow:0 4px 20px rgba(0,0,0,.35) !important;
    animation:countUp .6s cubic-bezier(.22,1,.36,1) both;
    transition:transform .25s, box-shadow .25s !important;
}
[data-testid="metric-container"]:hover {
    transform:translateY(-5px) !important;
    box-shadow:0 12px 32px rgba(74,144,217,.20) !important;
    border-top-color:#FF6B6B !important;
}
[data-testid="metric-container"]:nth-child(1){animation-delay:.05s;}
[data-testid="metric-container"]:nth-child(2){animation-delay:.15s;}
[data-testid="metric-container"]:nth-child(3){animation-delay:.25s;}
[data-testid="metric-container"]:nth-child(4){animation-delay:.35s;}
[data-testid="stMetricLabel"]{font-family:'Sora',sans-serif !important;font-weight:600 !important;color:#7FA4C0 !important;font-size:.79rem !important;}
[data-testid="stMetricValue"]{font-family:'Sora',sans-serif !important;font-weight:800 !important;color:#F0F6FF !important;font-size:1.65rem !important;}

.sidebar-section {
    font-family:'Sora',sans-serif; font-weight:700; font-size:.95rem;
    color:#E8F0F8 !important; display:flex; align-items:center;
    gap:8px; margin-bottom:10px; padding:10px 0 6px;
    border-bottom:1px solid rgba(255,255,255,0.08);
}

.obs-card {
    display:flex; align-items:flex-start; gap:12px;
    padding:12px 16px; border-radius:10px;
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.07);
    border-left:4px solid #4A90D9;
    margin:6px 0;
    animation:fadeSlideUp .5s cubic-bezier(.22,1,.36,1) both;
    transition:all .22s cubic-bezier(.22,1,.36,1);
}
.obs-card:hover {
    background:rgba(27,58,92,0.50); border-left-color:#FF6B6B;
    transform:translateX(4px); box-shadow:0 3px 14px rgba(0,0,0,.25);
}
.obs-card:hover svg { animation:iconBounce .55s ease; }
.obs-card span { color:#C8D8E8 !important; line-height:1.6; }
.obs-card:hover span { color:#F0F6FF !important; }
.obs-card b { color:#E8F0F8 !important; }

.corr-row {
    display:flex; align-items:center; gap:12px;
    padding:10px 14px; border-radius:10px;
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.07);
    margin:5px 0;
    animation:fadeSlideUp .5s cubic-bezier(.22,1,.36,1) both;
    transition:all .22s;
}
.corr-row:hover { background:rgba(27,58,92,.4); transform:translateX(4px); }
.corr-var { font-family:'Sora',sans-serif; font-weight:700; color:#E8F0F8 !important; min-width:160px; }
.corr-bar-wrap { flex:1; background:rgba(255,255,255,0.08); border-radius:4px; height:8px; overflow:hidden; }
.corr-bar { height:100%; border-radius:4px; }
.corr-val { font-family:'Sora',sans-serif; font-weight:700; font-size:.88rem; min-width:60px; text-align:right; }

.stat-group {
    background:rgba(17,34,64,0.70);
    border:1px solid rgba(255,255,255,0.09);
    border-radius:14px; padding:18px 20px; margin-bottom:12px;
    animation:scaleIn .55s cubic-bezier(.22,1,.36,1) both;
    transition:transform .25s, box-shadow .25s;
}
.stat-group:hover { transform:translateY(-3px); box-shadow:0 8px 28px rgba(0,0,0,.35); }
.stat-group-title {
    font-family:'Sora',sans-serif; font-weight:700; font-size:.85rem;
    color:#4A90D9 !important; margin-bottom:12px;
    display:flex; align-items:center; gap:7px;
    text-transform:uppercase; letter-spacing:.5px;
}

.footer { text-align:center; color:#3A5A7A !important; font-size:.76rem; padding:8px 0; }

.d1{animation-delay:.04s;} .d2{animation-delay:.11s;} .d3{animation-delay:.18s;}
.d4{animation-delay:.25s;} .d5{animation-delay:.32s;} .d6{animation-delay:.39s;}
</style>
""", unsafe_allow_html=True)

# ══ SVG HELPERS ══
def svg(d, size=22, color="#4A90D9", sw=2):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
            f'viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">{d}</svg>')

IC = {
    "search":      '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>',
    "database":    '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/>',
    "filter":      '<polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/>',
    "bar-chart":   '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>',
    "trending-up": '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
    "grid":        '<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/>',
    "activity":    '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
    "layers":      '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
    "table":       '<path d="M9 3H5a2 2 0 0 0-2 2v4m6-6h10a2 2 0 0 1 2 2v4M9 3v18m0 0h10a2 2 0 0 0 2-2V9M9 21H5a2 2 0 0 1-2-2V9m0 0h18"/>',
    "star":        '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "eye":         '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>',
    "cpu":         '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/>',
    "target":      '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "info":        '<circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>',
    "hash":        '<line x1="4" y1="9" x2="20" y2="9"/><line x1="4" y1="15" x2="20" y2="15"/><line x1="10" y1="3" x2="8" y2="21"/><line x1="16" y1="3" x2="14" y2="21"/>',
    "sliders":     '<line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/>',
    "virus":       '<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>',
    "globe":       '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
}

def I(name, size=20, color="#4A90D9", sw=2):
    return svg(IC.get(name, ""), size, color, sw)

def sec(icon, title, color="#4A90D9"):
    st.markdown(f"""
    <div class="sec-title">
        {I(icon, 24, color)}
        <h3>{title}</h3>
    </div>""", unsafe_allow_html=True)

# ══ CARGA DE DATOS ══
@st.cache_data
def cargar_datos():
    df = pd.read_csv("data/turismo_ayacucho_2010_2024.csv", parse_dates=["fecha"])
    return df.sort_values("fecha").reset_index(drop=True)

df = cargar_datos()

# ══ SIDEBAR ══
# ══ SIDEBAR ══
st.sidebar.markdown(f"""
<style>
/* ── sidebar mejorado ── */
[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #07111C 0%, #0D1B2A 100%) !important;
}}

/* titulo sidebar */
.sb-title {{
    font-family:'Sora',sans-serif; font-weight:800; font-size:1rem;
    color:#F0F6FF !important; display:flex; align-items:center; gap:9px;
    padding:14px 0 10px; border-bottom:1px solid rgba(74,144,217,0.25);
    margin-bottom:16px; letter-spacing:.3px;
}}

/* label de cada filtro */
.sb-label {{
    font-family:'Sora',sans-serif; font-weight:600; font-size:.78rem;
    color:#7FA4C0 !important; text-transform:uppercase; letter-spacing:.6px;
    margin-bottom:4px; display:flex; align-items:center; gap:6px;
}}

/* separador entre filtros */
.sb-sep {{
    height:1px; background:rgba(255,255,255,0.06); margin:14px 0;
}}

/* badge de rango */
.sb-badge {{
    display:inline-flex; align-items:center; gap:5px;
    background:rgba(74,144,217,0.15); border:1px solid rgba(74,144,217,0.30);
    color:#90C8F0 !important; border-radius:20px;
    padding:3px 10px; font-size:.73rem; font-weight:700;
    font-family:'Sora',sans-serif; margin-bottom:8px;
}}

/* sliders */
[data-testid="stSidebar"] .stSlider [data-baseweb="slider"] {{
    padding:0 !important;
}}
[data-testid="stSidebar"] .stSlider [role="slider"] {{
    background:#C00000 !important;
    border:2px solid #FF6B6B !important;
    box-shadow:0 0 8px rgba(192,0,0,.5) !important;
    width:18px !important; height:18px !important;
}}
[data-testid="stSidebar"] .stSlider [data-testid="stSliderTrackActive"] {{
    background:linear-gradient(90deg,#C00000,#FF6B6B) !important;
}}

/* checkbox */
[data-testid="stSidebar"] .stCheckbox {{
    background:rgba(192,0,0,0.08);
    border:1px solid rgba(192,0,0,0.25);
    border-radius:10px; padding:10px 12px !important;
    transition:all .2s;
}}
[data-testid="stSidebar"] .stCheckbox:hover {{
    background:rgba(192,0,0,0.15);
    border-color:rgba(192,0,0,0.45);
}}
[data-testid="stSidebar"] .stCheckbox label {{
    font-family:'DM Sans',sans-serif !important;
    font-weight:500 !important; color:#C8D8E8 !important;
    font-size:.88rem !important;
}}

/* multiselect tags */
[data-testid="stSidebar"] [data-baseweb="tag"] {{
    background:linear-gradient(90deg,#C00000,#8B0000) !important;
    color:#fff !important; border-radius:6px !important;
    font-family:'Sora',sans-serif !important;
    font-size:.72rem !important; font-weight:600 !important;
    border:none !important;
    box-shadow:0 2px 6px rgba(192,0,0,.3) !important;
}}
[data-testid="stSidebar"] [data-baseweb="tag"] span {{
    color:#fff !important;
}}

/* multiselect container */
[data-testid="stSidebar"] [data-baseweb="select"] > div {{
    background:#112240 !important;
    border:1px solid rgba(74,144,217,0.25) !important;
    border-radius:10px !important;
    transition:border-color .2s !important;
}}
[data-testid="stSidebar"] [data-baseweb="select"] > div:hover {{
    border-color:rgba(74,144,217,0.55) !important;
}}

/* info box sidebar */
.sb-info {{
    background:rgba(74,144,217,0.10);
    border:1px solid rgba(74,144,217,0.20);
    border-radius:10px; padding:10px 12px;
    margin-top:16px; font-size:.80rem;
    color:#A8C0D6 !important; line-height:1.6;
}}
.sb-info b {{ color:#90C8F0 !important; }}
</style>

<div class="sb-title">
    {I("sliders", 18, "#4A90D9")} Filtros Interactivos
</div>
""", unsafe_allow_html=True)

# ── Rango de años ──
st.sidebar.markdown(f"""
<div class="sb-label">{I("calendar", 13, "#7FA4C0")} Rango de Años</div>
""", unsafe_allow_html=True)

anios_disponibles = sorted(df["anio"].unique())
anio_min = st.sidebar.select_slider(
    "Año inicial", options=anios_disponibles,
    value=anios_disponibles[0], label_visibility="collapsed"
)
anio_max = st.sidebar.select_slider(
    "Año final", options=anios_disponibles,
    value=anios_disponibles[-1], label_visibility="collapsed"
)

st.sidebar.markdown(f"""
<div class="sb-badge">
    {I("calendar", 12, "#90C8F0")} {anio_min} &nbsp;→&nbsp; {anio_max}
    &nbsp;·&nbsp; {anio_max - anio_min + 1} años
</div>
<div class="sb-sep"></div>
""", unsafe_allow_html=True)

# ── Pandemia ──
st.sidebar.markdown(f"""
<div class="sb-label">{I("virus", 13, "#7FA4C0")} Periodo Pandemico</div>
""", unsafe_allow_html=True)

incluir_pandemia = st.sidebar.checkbox(
    "Incluir 2020-2021 (COVID-19)", value=True
)

st.sidebar.markdown('<div class="sb-sep"></div>', unsafe_allow_html=True)

# ── Meses ──
st.sidebar.markdown(f"""
<div class="sb-label">{I("calendar", 13, "#7FA4C0")} Meses a Incluir</div>
""", unsafe_allow_html=True)

meses_filtro = st.sidebar.multiselect(
    "Meses",
    options=list(range(1, 13)),
    default=list(range(1, 13)),
    format_func=lambda x: ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
                            "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"][x-1],
    label_visibility="collapsed"
)

# ── Info box ──
total_meses = len(meses_filtro)
st.sidebar.markdown(f"""
<div class="sb-info">
    {I("info", 14, "#4A90D9")}
    <b>{total_meses}</b> de 12 meses seleccionados<br>
    <b>{len(df[(df['anio'] >= anio_min) & (df['anio'] <= anio_max)]):,}</b> registros en rango
</div>
""", unsafe_allow_html=True)

# ── Aplicar filtros ──
df_filtrado = df[
    (df["anio"] >= anio_min) &
    (df["anio"] <= anio_max) &
    (df["mes"].isin(meses_filtro))
]
if not incluir_pandemia:
    df_filtrado = df_filtrado[df_filtrado["pandemia_covid"] == 0]

# ══ METRICAS ══
sec("database", "Resumen del Dataset Filtrado")
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("Observaciones",    f"{len(df_filtrado):,}")
with col2: st.metric("Media de arribos", f"{df_filtrado['arribos'].mean():,.0f}")
with col3: st.metric("Maximo",           f"{df_filtrado['arribos'].max():,}")
with col4: st.metric("Minimo",           f"{df_filtrado['arribos'].min():,}")

st.divider()

meses_nom = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]

# ══ TABS ══
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "  Serie Temporal  ",
    "  Estacionalidad  ",
    "  Correlaciones  ",
    "  Estadisticas  ",
    "  Datos Crudos  ",
])

# ── TAB 1 ──
with tab1:
    sec("trending-up", "Serie Temporal de Arribos")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_filtrado["fecha"], y=df_filtrado["arribos"],
        mode="lines", name="Arribos mensuales",
        line=dict(color="#4A90D9", width=2),
        fill="tozeroy", fillcolor="rgba(74,144,217,0.15)",
    ))
    if incluir_pandemia:
        fig.add_vrect(
            x0="2020-03-01", x1="2021-06-01",
            fillcolor="#C00000", opacity=0.15,
            annotation_text="Pandemia COVID-19",
            annotation_position="top left",
            annotation_font_color="#FF8080",
            line_width=0,
        )
    fig.update_layout(
        title=dict(text="Evolucion de Arribos a Hospedajes en Ayacucho", font=dict(color="#E8F0F8", size=15)),
        xaxis_title="Fecha", yaxis_title="Numero de arribos",
        hovermode="x unified", height=500,
        paper_bgcolor="#0D1B2A", plot_bgcolor="#112240",
        font=dict(color="#C8D8E8"),
        xaxis=dict(gridcolor="rgba(255,255,255,0.06)", color="#7FA4C0"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.06)", color="#7FA4C0"),
    )
    st.plotly_chart(fig, use_container_width=True)

    sec("eye", "Observaciones Clave", "#FF6B6B")
    for (icon, color, txt), dc in zip([
        ("trending-up", "#4CAF50", "<b>2010-2019:</b> Tendencia creciente sostenida (+197%)"),
        ("virus",       "#FF6B6B", "<b>2020:</b> Caida del 86% por la pandemia COVID-19"),
        ("activity",    "#4A90D9", "<b>2021-2024:</b> Recuperacion progresiva (65% del nivel pre-pandemia)"),
        ("star",        "#FFB347", "<b>Patron estacional:</b> Picos en Semana Santa, Fiestas Patrias y Diciembre"),
    ], ["d1","d2","d3","d4"]):
        st.markdown(f"""
        <div class="obs-card {dc}">
            {I(icon, 18, color)}
            <span>{txt}</span>
        </div>""", unsafe_allow_html=True)

# ── TAB 2 ──
with tab2:
    sec("bar-chart", "Analisis de Estacionalidad")
    col1, col2 = st.columns(2)

    with col1:
        prom_mes = df_filtrado.groupby("mes")["arribos"].mean().reset_index()
        prom_mes["mes_nombre"] = prom_mes["mes"].apply(lambda x: meses_nom[x-1])
        media_global = prom_mes["arribos"].mean()
        colors = ["#C00000" if v > media_global else "#4A90D9" for v in prom_mes["arribos"]]
        fig_bar = go.Figure(go.Bar(
            x=prom_mes["mes_nombre"], y=prom_mes["arribos"],
            marker_color=colors,
            text=prom_mes["arribos"].round(0).astype(int),
            textposition="outside",
            textfont=dict(color="#C8D8E8", size=10),
        ))
        fig_bar.add_hline(y=media_global, line_dash="dash", line_color="#7FA4C0",
                          annotation_text=f"Media: {media_global:,.0f}",
                          annotation_font_color="#A8C0D6")
        fig_bar.update_layout(
            title=dict(text="Promedio Mensual de Arribos", font=dict(color="#E8F0F8", size=14)),
            xaxis_title="Mes", yaxis_title="Promedio", height=450, showlegend=False,
            paper_bgcolor="#0D1B2A", plot_bgcolor="#112240", font=dict(color="#C8D8E8"),
            xaxis=dict(gridcolor="rgba(255,255,255,0.06)", color="#7FA4C0"),
            yaxis=dict(gridcolor="rgba(255,255,255,0.06)", color="#7FA4C0"),
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        pivot = df_filtrado.pivot_table(values="arribos", index="anio", columns="mes", aggfunc="sum")
        fig_heat = px.imshow(
            pivot, labels=dict(x="Mes", y="Año", color="Arribos"),
            x=meses_nom, color_continuous_scale="Blues",
            aspect="auto", text_auto=".0f",
        )
        fig_heat.update_layout(
            title=dict(text="Heatmap: Arribos por Año y Mes", font=dict(color="#E8F0F8", size=14)),
            height=450,
            paper_bgcolor="#0D1B2A", plot_bgcolor="#112240", font=dict(color="#C8D8E8"),
        )
        st.plotly_chart(fig_heat, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    sec("star", "Top 3 Meses con Mayor Afluencia", "#FFB347")
    top3 = prom_mes.sort_values("arribos", ascending=False).head(3)
    medals = ["🥇","🥈","🥉"]
    cols = st.columns(3)
    for i, (col, (_, row)) in enumerate(zip(cols, top3.iterrows()), 1):
        with col:
            st.metric(f"{medals[i-1]} {row['mes_nombre']}", f"{row['arribos']:,.0f}", "Mes pico")

# ── TAB 3 ──
with tab3:
    sec("grid", "Matriz de Correlaciones (Pearson)")
    cols_corr = ["arribos","mes","semana_santa","feriado_largo",
                 "temperatura_c","precipitacion_mm","evento_cultural","pandemia_covid"]
    corr = df_filtrado[cols_corr].corr()
    fig_corr = px.imshow(
        corr, text_auto=".2f",
        color_continuous_scale="RdBu_r", zmin=-1, zmax=1, aspect="auto",
    )
    fig_corr.update_layout(
        title=dict(text="Correlacion entre Variables", font=dict(color="#E8F0F8", size=14)),
        height=520,
        paper_bgcolor="#0D1B2A", plot_bgcolor="#112240", font=dict(color="#C8D8E8"),
    )
    st.plotly_chart(fig_corr, use_container_width=True)

    sec("activity", "Correlaciones con 'arribos'", "#4A90D9")
    corr_arribos = corr["arribos"].drop("arribos").sort_values(key=abs, ascending=False)
    for var, val in corr_arribos.items():
        if pd.isna(val):
            continue
        bar_color = "#4A90D9" if val > 0 else "#C00000"
        pct = int(abs(val) * 100)
        label_color = "#A5D6A7" if val > 0.3 else ("#FF8080" if val < -0.3 else "#7FA4C0")
        strength = "Fuerte" if abs(val) > 0.5 else ("Moderada" if abs(val) > 0.3 else "Debil")
        st.markdown(f"""
        <div class="corr-row">
            {I("hash", 16, bar_color)}
            <span class="corr-var">{var}</span>
            <div class="corr-bar-wrap">
                <div class="corr-bar" style="width:{pct}%;background:{bar_color};"></div>
            </div>
            <span class="corr-val" style="color:{label_color};">{val:+.3f}</span>
            <span style="font-size:.78rem;color:#7FA4C0;min-width:70px;">{strength}</span>
        </div>""", unsafe_allow_html=True)

# ── TAB 4 ──
with tab4:
    sec("cpu", "Estadisticas Descriptivas Completas")
    arribos = df_filtrado["arribos"]
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown(f"""
        <div class="stat-group d1">
            <div class="stat-group-title">{I("target", 16, "#4A90D9")} Tendencia Central</div>
        </div>""", unsafe_allow_html=True)
        st.metric("Media",         f"{arribos.mean():,.2f}")
        st.metric("Mediana",       f"{arribos.median():,.2f}")
        st.metric("Moda (aprox.)", f"{arribos.mode().iloc[0]:,.0f}")

    with col2:
        st.markdown(f"""
        <div class="stat-group d2">
            <div class="stat-group-title">{I("activity", 16, "#FF6B6B")} Dispersion</div>
        </div>""", unsafe_allow_html=True)
        st.metric("Desv. estandar", f"{arribos.std():,.2f}")
        st.metric("Varianza",       f"{arribos.var():,.2f}")
        cv = (arribos.std() / arribos.mean()) * 100
        st.metric("Coef. variacion",f"{cv:.2f}%")

    with col3:
        st.markdown(f"""
        <div class="stat-group d3">
            <div class="stat-group-title">{I("sliders", 16, "#FFB347")} Forma</div>
        </div>""", unsafe_allow_html=True)
        st.metric("Asimetria (skew)", f"{arribos.skew():.4f}")
        st.metric("Curtosis",         f"{arribos.kurtosis():.4f}")
        iqr = arribos.quantile(0.75) - arribos.quantile(0.25)
        st.metric("Rango IQR",        f"{iqr:,.2f}")

    st.markdown("<br>", unsafe_allow_html=True)
    sec("bar-chart", "Distribucion de Arribos", "#4A90D9")
    fig_hist = px.histogram(
        df_filtrado, x="arribos", nbins=40,
        marginal="box", color_discrete_sequence=["#4A90D9"],
    )
    fig_hist.update_layout(
        height=400,
        title=dict(text="Histograma y Boxplot de Arribos", font=dict(color="#E8F0F8", size=14)),
        paper_bgcolor="#0D1B2A", plot_bgcolor="#112240", font=dict(color="#C8D8E8"),
        xaxis=dict(gridcolor="rgba(255,255,255,0.06)", color="#7FA4C0"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.06)", color="#7FA4C0"),
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# ── TAB 5 ──
with tab5:
    sec("table", "Tabla de Datos Filtrados")
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:10px;padding:10px 14px;
                background:rgba(74,144,217,0.10);border:1px solid rgba(74,144,217,0.25);
                border-radius:10px;margin-bottom:16px;">
        {I("info", 18, "#4A90D9")}
        <span>Mostrando <b>{len(df_filtrado):,} registros</b> segun los filtros aplicados.</span>
    </div>
    """, unsafe_allow_html=True)

    st.dataframe(
        df_filtrado.style.format({
            "arribos": "{:,.0f}",
            "temperatura_c": "{:.1f}",
            "precipitacion_mm": "{:.1f}",
        }),
        use_container_width=True, height=500,
    )

    csv = df_filtrado.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="  Descargar datos filtrados (CSV)",
        data=csv, file_name="datos_filtrados.csv", mime="text/csv",
    )

st.divider()
st.markdown("""
<p class="footer">
    Fase 2 de CRISP-DM &nbsp;&#183;&nbsp; Comprension de los Datos
    &nbsp;&#183;&nbsp; Analisis Exploratorio Interactivo &nbsp;&#183;&nbsp; 2026
</p>
""", unsafe_allow_html=True)