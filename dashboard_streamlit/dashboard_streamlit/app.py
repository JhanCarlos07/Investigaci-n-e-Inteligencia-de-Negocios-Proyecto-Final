"""
============================================================================
DASHBOARD - Prediccion de Turistas en Ayacucho (CRISP-DM)
============================================================================
Ejecucion:  streamlit run app.py
"""

import streamlit as st

FAVICON_B64 = "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"

from PIL import Image as _Image
_icon = _Image.open("favicon.png")

st.set_page_config(
    page_title="Predicción Turistas Ayacucho",
    page_icon=_icon,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════════════════════
# ESTILOS GLOBALES
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;700;800&family=DM+Sans:wght@400;500&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css');

/* ══ FONDO OSCURO GLOBAL ══ */
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
section.main, .main .block-container,
[data-testid="stMain"] {
    background: #0A1628 !important;
    font-family: 'DM Sans', system-ui, sans-serif !important;
    color: #E2EAF4 !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] > div:first-child {
    background: #060E1A !important;
    border-right: 1px solid rgba(255,255,255,0.06) !important;
}
[data-testid="stSidebar"] * { color: #C4D4E8 !important; }
[data-testid="stSidebar"] a:hover { background: rgba(255,255,255,0.06) !important; }

/* ── Padding ── */
.block-container { padding-top: 0 !important; max-width: 1200px !important; }

/* ── Métricas ── */
[data-testid="metric-container"] {
    background: #111E33 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-top: 3px solid #E03030 !important;
    border-radius: 12px !important;
    padding: 20px 22px !important;
    transition: transform 0.2s, box-shadow 0.2s !important;
}
[data-testid="metric-container"]:hover {
    transform: translateY(-4px) !important;
    box-shadow: 0 12px 32px rgba(0,0,0,0.4) !important;
    border-top-color: #FF5555 !important;
}
[data-testid="stMetricLabel"] {
    font-family:'Sora',sans-serif !important; font-weight:700 !important;
    font-size:0.68rem !important; color:#6A8BAE !important;
    letter-spacing:0.08em !important; text-transform:uppercase !important;
}
[data-testid="stMetricValue"] {
    font-family:'Sora',sans-serif !important; font-weight:800 !important;
    font-size:1.9rem !important; color:#F0F6FF !important;
    letter-spacing:-0.03em !important;
}
[data-testid="stMetricDelta"] { font-weight:600 !important; font-size:0.74rem !important; }

/* ── Divider ── */
hr { border-color: rgba(255,255,255,0.08) !important; }

/* ── Animaciones ── */
@keyframes fadeDown { from{opacity:0;transform:translateY(-18px)} to{opacity:1;transform:translateY(0)} }
@keyframes fadeUp   { from{opacity:0;transform:translateY(14px)}  to{opacity:1;transform:translateY(0)} }
@keyframes shimmer  { 0%{background-position:-600px 0} 100%{background-position:600px 0} }
@keyframes pulseRed { 0%,100%{opacity:1} 50%{opacity:0.7} }

/* ── Cards de fases ── */
.fase-card {
    display:flex; align-items:flex-start; gap:16px;
    background:#111E33;
    border:1px solid rgba(255,255,255,0.07);
    border-left:4px solid #E03030;
    border-radius:0 10px 10px 0;
    padding:14px 18px; margin:6px 0;
    transition: all 0.2s cubic-bezier(.22,1,.36,1);
}
.fase-card:hover {
    background:#172540;
    border-left-color:#5599DD;
    transform:translateX(5px);
    box-shadow:0 4px 20px rgba(0,0,0,0.35);
}
.fase-num {
    font-family:'Courier New',monospace; font-size:0.68rem;
    font-weight:700; color:#E03030; min-width:28px;
    padding-top:2px; letter-spacing:0.05em;
}
.fase-title { font-weight:700; font-size:0.88rem; color:#E2EAF4; margin-bottom:3px; }
.fase-desc  { font-size:0.78rem; color:#6A8BAE; }

/* ── Info card ── */
.info-card {
    background: linear-gradient(160deg, #0D1E35, #152D4A);
    border:1px solid rgba(255,255,255,0.08);
    border-radius:16px; padding:24px;
    height:100%;
    box-shadow:0 8px 32px rgba(0,0,0,0.35);
    transition:transform 0.2s, box-shadow 0.2s;
}
.info-card:hover {
    transform:translateY(-3px);
    box-shadow:0 16px 44px rgba(0,0,0,0.45);
}
.info-row {
    display:flex; gap:12px;
    padding:10px 0;
    border-bottom:1px solid rgba(255,255,255,0.06);
}
.info-label { font-size:0.69rem; color:#5580A8; font-weight:700; letter-spacing:0.05em; min-width:90px; padding-top:2px; text-transform:uppercase; }
.info-value { font-size:0.82rem; color:#C8D8EA; line-height:1.45; }
.info-badge {
    margin-top:20px; padding:14px 16px;
    background:rgba(224,48,48,0.12);
    border:1px solid rgba(224,48,48,0.22);
    border-radius:10px;
}
.info-badge-title { font-size:0.64rem; color:#FF8080; font-weight:700; letter-spacing:0.09em; text-transform:uppercase; margin-bottom:6px; }
.info-badge-val   { font-size:0.82rem; color:#E2EAF4; font-weight:600; }
.info-badge-sub   { font-size:0.72rem; color:#7A9CC0; margin-top:5px; }

/* ── Tech / fuente items ── */
.tech-item {
    display:flex; align-items:center; gap:14px;
    background:#111E33;
    border:1px solid rgba(255,255,255,0.07);
    border-radius:10px; padding:11px 16px; margin:5px 0;
    transition:all 0.2s;
}
.tech-item:hover {
    border-color:rgba(85,153,221,0.4);
    background:#172540;
    transform:translateX(4px);
    box-shadow:0 4px 16px rgba(0,0,0,0.3);
}
.tech-icon  { font-size:1rem; color:#E03030; }
.tech-name  { font-weight:700; font-size:0.85rem; color:#E2EAF4; min-width:108px; }
.tech-desc  { font-size:0.78rem; color:#6A8BAE; }
.src-badge  {
    font-family:'Sora',sans-serif; font-size:0.63rem; font-weight:800;
    color:#E2EAF4; background:#1E3A5C; padding:4px 10px;
    border:1px solid rgba(85,153,221,0.25);
    border-radius:6px; letter-spacing:0.04em; min-width:76px;
    text-align:center; white-space:nowrap;
}

/* ── Team cards ── */
.team-card {
    display:flex; flex-direction:column; align-items:center;
    text-align:center; padding:24px 12px 18px;
    background:#111E33;
    border:1px solid rgba(255,255,255,0.07);
    border-bottom:3px solid #E03030;
    border-radius:14px; gap:8px;
    transition:all 0.25s; cursor:default;
}
.team-card:hover {
    background:#172540;
    transform:translateY(-6px);
    box-shadow:0 14px 32px rgba(0,0,0,0.45);
    border-bottom-color:#5599DD;
}
.team-avatar {
    width:52px; height:52px; border-radius:50%;
    background:linear-gradient(135deg,#1B3A5C,#0D1B2A);
    border:2px solid rgba(255,255,255,0.1);
    display:flex; align-items:center; justify-content:center;
    font-family:'Sora',sans-serif; font-size:1rem;
    font-weight:800; color:#E2EAF4; letter-spacing:-0.02em;
    margin-bottom:4px;
    transition:all 0.25s;
}
.team-card:hover .team-avatar {
    background:linear-gradient(135deg,#C00000,#8B0000);
    border-color:rgba(224,48,48,0.4);
}
.team-name   { font-size:0.72rem; font-weight:800; color:#E2EAF4; line-height:1.3; }
.team-sub    { font-size:0.7rem; color:#6A8BAE; margin-top:2px; }
.team-badge  {
    font-size:0.57rem; font-weight:700; letter-spacing:0.08em;
    color:#A8C0D6; background:#0D1B2A;
    border:1px solid rgba(255,255,255,0.1);
    padding:3px 10px; border-radius:20px; margin-top:6px;
}

/* ── Sección labels ── */
.sec-label {
    display:flex; align-items:center; gap:10px;
    margin:0 0 16px; padding-bottom:10px;
    border-bottom:1px solid rgba(255,255,255,0.08);
}
.sec-label-dot  { color:#E03030; font-size:1.1rem; }
.sec-label-text {
    font-family:'Sora',sans-serif; font-weight:700;
    font-size:1.05rem; color:#E2EAF4; letter-spacing:-0.01em;
}

/* ── Footer ── */
.footer {
    text-align:center; color:#3A5878; font-size:0.75rem;
    padding:14px 0 6px; border-top:1px solid rgba(255,255,255,0.07); margin-top:8px;
}

/* ── Mini bar chart ── */
.bar-wrap {
    display:flex; align-items:flex-end; gap:4px;
    height:60px; padding:0 4px;
}
.bar-col { display:flex; flex-direction:column; align-items:center; gap:2px; flex:1; }
.bar-fill { border-radius:2px; width:100%; transition:height 0.3s; }
.bar-lbl  { font-size:8px; color:#4A6888; }

/* ── ICONOS FONT AWESOME ── */
.fa-icon-animated {
    display:inline-flex;
    align-items:center;
    justify-content:center;
    transition:all 0.3s cubic-bezier(.22,1,.36,1);
}
.fa-spin-custom {
    animation:spinIcon 2s linear infinite;
}
.fa-float {
    animation:floatIcon 3s ease-in-out infinite;
}
.fa-glow {
    color:#FF6B6B;
    text-shadow:0 0 12px rgba(255,107,107,0.9);
}
.fa-bounce {
    animation:iconBounce 0.6s ease-in-out;
}
@keyframes spinIcon {
    from{transform:rotate(0deg);}
    to{transform:rotate(360deg);}
}
@keyframes floatIcon {
    0%, 100%{transform:translateY(0px);}
    50%{transform:translateY(-8px);}
}
@keyframes iconBounce {
    0%, 100%{transform:translateY(0);}
    50%{transform:translateY(-5px);}
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# DATOS
# ══════════════════════════════════════════════════════════════════════════════
MESES = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
VALS  = [38, 42, 55, 63, 47, 44, 58, 52, 46, 49, 54, 50]
MAX_V = max(VALS)

FASES = [
    ("01", "Comprensión del Negocio",   "Contexto, problema y objetivos del turismo regional"),
    ("02", "Comprensión de los Datos",  "Análisis exploratorio EDA sobre series temporales"),
    ("03", "Preparación de los Datos",  "Transformación, limpieza y enriquecimiento"),
    ("04", "Modelado",                  "SARIMA estacional + Regresión Lineal Múltiple"),
    ("05", "Evaluación",                "Métricas MAPE/RMSE y diagnóstico de residuos"),
    ("06", "Despliegue",                "Pronóstico mensual detallado para 2025"),
]

TECHS = [
    ("Python 3.10+", "Lenguaje principal",              "%3Cpolyline points='4 17 10 11 4 5'/%3E%3Cline x1='12' y1='19' x2='20' y2='19'/%3E"),
    ("pandas",        "Manipulación de datos",           "%3Cpath d='M9 3H5a2 2 0 0 0-2 2v4m6-6h10a2 2 0 0 1 2 2v4M9 3v18m0 0h10a2 2 0 0 0 2-2V9M9 21H5a2 2 0 0 1-2-2V9m0 0h18'/%3E"),
    ("statsmodels",   "Modelo SARIMA y tests",           "%3Cpolyline points='22 12 18 12 15 21 9 3 6 12 2 12'/%3E"),
    ("scikit-learn",  "Regresión múltiple y métricas",   "%3Ccircle cx='12' cy='12' r='10'/%3E%3Ccircle cx='12' cy='12' r='6'/%3E%3Ccircle cx='12' cy='12' r='2'/%3E"),
    ("plotly",        "Visualización interactiva",       "%3Cline x1='18' y1='20' x2='18' y2='10'/%3E%3Cline x1='12' y1='20' x2='12' y2='4'/%3E%3Cline x1='6' y1='20' x2='6' y2='14'/%3E"),
    ("streamlit",     "Framework del dashboard",         "%3Crect x='3' y='3' width='18' height='18' rx='2'/%3E%3Cline x1='3' y1='9' x2='21' y2='9'/%3E%3Cline x1='9' y1='21' x2='9' y2='9'/%3E"),
]

def tech_icon_css(encoded_paths):
    """Genera un data URI SVG para usar como background-image."""
    base = "%3Csvg xmlns='http%3A//www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23E03030' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E"
    return f"url(\"{base}{encoded_paths}%3C/svg%3E\")"

FUENTES = [
    ("MINCETUR", "Sistema de Información Estadística de Turismo"),
    ("INEI",     "Índice temático de turismo"),
    ("SENAMHI",  "Datos meteorológicos estación Huamanga"),
    ("BCRP",     "Síntesis de actividad económica Ayacucho"),
    ("DIRCETUR", "Calendario regional de eventos"),
]

EQUIPO = [
    ("JC", "CCALLOCUNTO GUEVARA", "Jhan Carlos"),
    ("HG", "GÁLVEZ FERNÁNDEZ",    "Harold Jhordi"),
    ("JV", "VILLANUEVA LANDA",    "Joel Jhonatan"),
    ("JQ",  "QUISPE HUAMANI",     "Johne"),
    ("AM",  "ASTUDILLO ALARCON",  "Maria Paz Teresa"),
]


# ══════════════════════════════════════════════════════════════════════════════
# HELPERS HTML
# ══════════════════════════════════════════════════════════════════════════════
SEC_ICON_ENC = {
    "fases":  "%3Cpath d='M9 11l3 3L22 4'/%3E%3Cpath d='M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11'/%3E",
    "info":   "%3Cpath d='M4 19.5A2.5 2.5 0 0 1 6.5 17H20'/%3E%3Cpath d='M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z'/%3E",
    "result": "%3Ccircle cx='12' cy='12' r='10'/%3E%3Ccircle cx='12' cy='12' r='6'/%3E%3Ccircle cx='12' cy='12' r='2'/%3E",
    "tech":   "%3Cpolyline points='16 18 22 12 16 6'/%3E%3Cpolyline points='8 6 2 12 8 18'/%3E",
    "data":   "%3Cellipse cx='12' cy='5' rx='9' ry='3'/%3E%3Cpath d='M21 12c0 1.66-4 3-9 3s-9-1.34-9-3'/%3E%3Cpath d='M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5'/%3E",
    "team":   "%3Cpath d='M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2'/%3E%3Ccircle cx='9' cy='7' r='4'/%3E%3Cpath d='M23 21v-2a4 4 0 0 0-3-3.87'/%3E%3Cpath d='M16 3.13a4 4 0 0 1 0 7.75'/%3E",
}

def sec_icon_bg(key):
    enc = SEC_ICON_ENC.get(key, SEC_ICON_ENC["result"])
    base = "%3Csvg xmlns='http%3A//www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23E03030' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E"
    return f"url(\"{base}{enc}%3C/svg%3E\")"

def sec_label(key, text):
    bg = sec_icon_bg(key)
    st.markdown(
        '<div class="sec-label">'
        f'<span style="display:inline-block;width:20px;height:20px;flex-shrink:0;'
        f'background:{bg} center/20px no-repeat;"></span>'
        f'<span class="sec-label-text">{text}</span>'
        '</div>',
        unsafe_allow_html=True,
    )


def mini_bar_chart():
    bars = ""
    for mes, val in zip(MESES, VALS):
        h = int((val / MAX_V) * 52)
        color = "#C00000" if mes == "Abr" else "rgba(192,0,0,0.25)"
        w = "700" if mes == "Abr" else "400"
        bars += (f'<div class="bar-col">'
                 f'<div class="bar-fill" style="height:{h}px;background:{color};" title="{mes}:{val}k"></div>'
                 f'<span class="bar-lbl" style="font-weight:{w}">{mes}</span>'
                 f'</div>')
    st.markdown(f'<div class="bar-wrap">{bars}</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# LOGO EN SIDEBAR (CSS trick — Streamlit filtra SVG inline en sidebar)
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
/* Logo box en sidebar usando background-image SVG */
[data-testid="stSidebar"] .sidebar-logo-box {
    display:flex; align-items:center; gap:10px;
    padding:18px 16px 14px;
    border-bottom:1px solid rgba(255,255,255,0.08);
    margin-bottom:8px;
}
[data-testid="stSidebar"] .sidebar-logo-icon {
    width:38px; height:38px; border-radius:10px; flex-shrink:0;
    background: linear-gradient(135deg,#C00000,#8B0000)
                url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='22' height='22' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z'/%3E%3Ccircle cx='12' cy='10' r='3'/%3E%3C/svg%3E")
                center/22px no-repeat;
    box-shadow:0 4px 14px rgba(192,0,0,0.4);
}
[data-testid="stSidebar"] .sidebar-logo-title {
    font-family:'Sora',sans-serif; font-weight:800;
    font-size:0.82rem; color:#E2EAF4 !important; line-height:1.2;
}
[data-testid="stSidebar"] .sidebar-logo-sub {
    font-size:0.63rem; color:#3A5878 !important; margin-top:2px;
}
/* Íconos de navegación en sidebar */
[data-testid="stSidebarNav"] li {
    border-radius:8px; transition:background 0.15s;
}
[data-testid="stSidebarNav"] li:hover {
    background:rgba(255,255,255,0.06) !important;
}
</style>
""", unsafe_allow_html=True)

sidebar_logo = (
    '<div class="sidebar-logo-box">'
    '<div style="width:38px;height:38px;border-radius:10px;flex-shrink:0;'
    'background:linear-gradient(135deg,#C00000,#8B0000);'
    'display:flex;align-items:center;justify-content:center;'
    'box-shadow:0 4px 14px rgba(192,0,0,0.4);">'
    f'<img src="data:image/png;base64,{FAVICON_B64}" width="26" height="26" style="display:block;"/>'
    '</div>'
    '<div>'
    '<div class="sidebar-logo-title">Turistas Ayacucho</div>'
    '<div class="sidebar-logo-sub">Dashboard CRISP-DM · 2026</div>'
    '</div>'
    '</div>'
)
st.sidebar.markdown(sidebar_logo, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-wrap" style="
    background:linear-gradient(135deg,#0D1B2A 0%,#1B3A5C 70%,#0D1B2A 100%);
    padding:0; border-radius:0 0 20px 20px; position:relative; overflow:hidden;
    margin:-1rem -1rem 0;
">
  <div style="position:absolute;inset:0;
    background-image:radial-gradient(circle,rgba(255,255,255,0.04) 1px,transparent 1px);
    background-size:28px 28px;pointer-events:none;"></div>
  <div style="position:absolute;right:-60px;top:-40px;width:320px;height:320px;
    background:radial-gradient(circle,rgba(192,0,0,0.22) 0%,transparent 65%);
    pointer-events:none;"></div>
</div>
""", unsafe_allow_html=True)

# Contenido del hero en columnas Streamlit
hero_left, hero_right = st.columns([3, 2], gap="large")

with hero_left:
    icon_html = (
        '<div style="padding:44px 0 10px;">'
        '<div style="display:flex;align-items:center;gap:14px;margin-bottom:20px;">'
        '<div style="width:56px;height:56px;border-radius:14px;flex-shrink:0;'
        'background:linear-gradient(135deg,#C00000,#8B0000);'
        'display:flex;align-items:center;justify-content:center;'
        'box-shadow:0 6px 20px rgba(192,0,0,0.45);">'
        '<i class="fas fa-location-dot" style="color:white;font-size:28px;"></i>'
        '</div>'
        '<div style="display:inline-block;font-size:0.64rem;font-weight:700;'
        'letter-spacing:0.14em;color:#FF6B6B;'
        'background:rgba(192,0,0,0.18);padding:4px 14px;border-radius:20px;'
        'border:1px solid rgba(192,0,0,0.35);text-transform:uppercase;">'
        '<i class="fas fa-chart-line" style="margin-right:6px;"></i>CRISP-DM · SARIMA · Regresión'
        '</div>'
        '</div>'
        '<h1 style="font-family:Sora,sans-serif;font-size:2.5rem;font-weight:800;'
        'color:#fff;margin:0 0 14px;line-height:1.15;letter-spacing:-0.03em;">'
        '<i class="fas fa-chart-area" style="margin-right:12px;color:#FF6B6B;"></i>Predicción de la<br>'
        '<span style="color:#FF6B6B;">Cantidad de Turistas</span><br>'
        'en Ayacucho'
        '</h1>'
        '<p style="color:#A8C0D6;font-size:0.93rem;margin:0 0 28px;line-height:1.65;">'
        '<i class="fas fa-building" style="margin-right:8px;color:#FF6B6B;"></i>Proyecto de analítica predictiva aplicado al sector turístico.<br>'
        '<i class="fas fa-user-tie" style="margin-right:8px;color:#FF6B6B;"></i>Docente: <strong style="color:#E8EDF2;">Ing. Jurado López, Jonathan Pedro</strong> · 2026'
        '</p>'
        '</div>'
    )
    st.markdown(icon_html, unsafe_allow_html=True)

with hero_right:
    st.markdown("""
    <div style="
        margin-top:44px;
        background:rgba(255,255,255,0.06); border-radius:14px; padding:18px 20px 14px;
        border:1px solid rgba(255,255,255,0.1);
    ">
        <div style="font-size:0.67rem;font-weight:700;color:#A8C0D6;
            letter-spacing:0.08em;text-transform:uppercase;margin-bottom:12px;">
            Pronóstico mensual 2025
        </div>
    """, unsafe_allow_html=True)
    mini_bar_chart()
    st.markdown("""
        <div style="font-size:0.67rem;color:#667788;margin-top:10px;text-align:center;">
            <span style="color:#C00000;font-weight:700;">■</span> Pico: Abril (Semana Santa)
        </div>
    </div>
    """, unsafe_allow_html=True)

# KPI strip en el hero
k1, k2, k3, k4 = st.columns(4)
kpis = [
    ("578,069",  "Turistas esperados 2025",   True),
    ("18.61%",   "MAPE del modelo SARIMA",    False),
    ("62,995",   "Pico abril · Semana Santa", False),
    ("6 fases",  "Metodología CRISP-DM",      False),
]
for col, (val, lbl, highlight) in zip([k1, k2, k3, k4], kpis):
    with col:
        vcolor = "#FF6B6B" if highlight else "#E2EAF4"
        kpi_html = (
            '<div style="padding:18px 20px;border-top:1px solid rgba(255,255,255,0.08);'
            'background:rgba(255,255,255,0.03);border-radius:0 0 10px 10px;">'
            '<div style="font-family:Sora,sans-serif;font-size:1.4rem;font-weight:800;'
            'color:' + vcolor + ';letter-spacing:-0.02em;">' + val + '</div>'
            '<div style="font-size:0.7rem;color:#5580A8;margin-top:4px;line-height:1.3;">' + lbl + '</div>'
            '</div>'
        )
        st.markdown(kpi_html, unsafe_allow_html=True)

st.markdown("<div style='margin-top:32px;'></div>", unsafe_allow_html=True)
st.divider()


# ══════════════════════════════════════════════════════════════════════════════
# FASES + INFO ACADÉMICA
# ══════════════════════════════════════════════════════════════════════════════
col_fases, col_info = st.columns([3, 2], gap="large")

with col_fases:
    sec_label("fases", "Fases de la Metodología CRISP-DM")
    fases_html = ""
    fase_icons = ["chart-line", "microscope", "wrench", "brain", "check-circle", "rocket"]
    for i, (num, title, desc) in enumerate(FASES):
        icon = fase_icons[i] if i < len(fase_icons) else "circle"
        fases_html += f"""
        <div class="fase-card">
            <span class="fase-num"><i class="fas fa-{icon}"></i></span>
            <div>
                <div class="fase-title">{title}</div>
                <div class="fase-desc">{desc}</div>
            </div>
        </div>"""
    st.markdown(fases_html, unsafe_allow_html=True)

with col_info:
    sec_label("info", "Información Académica")
    info_html = (
        '<div class="info-card">'
        '<div class="info-row"><span class="info-label">Curso</span>'
        '<span class="info-value">Investigación e Inteligencia de Negocios</span></div>'
        '<div class="info-row"><span class="info-label">Carrera</span>'
        '<span class="info-value">Ing. de Sistemas de Información</span></div>'
        '<div class="info-row"><span class="info-label">Institución</span>'
        '<span class="info-value">Escuela Superior La Pontificia · Ayacucho</span></div>'
        '<div class="info-row"><span class="info-label">Docente</span>'
        '<span class="info-value">Ing. Jurado López, Jonathan Pedro</span></div>'
        '<div class="info-row"><span class="info-label">Año</span>'
        '<span class="info-value">2026</span></div>'
        '<div class="info-badge">'
        '<div class="info-badge-title">Modelos empleados</div>'
        '<div class="info-badge-val">SARIMA + Regresión Lineal Múltiple</div>'
        '<div class="info-badge-sub">Comparativa de precisión predictiva</div>'
        '</div>'
        '</div>'
    )
    st.markdown(info_html, unsafe_allow_html=True)

st.divider()


# ══════════════════════════════════════════════════════════════════════════════
# MÉTRICAS
# ══════════════════════════════════════════════════════════════════════════════
st.markdown('<div class="sec-label"><i class="fas fa-chart-pie" style="color:#FF6B6B;font-size:20px;"></i><h3 style="margin:0;">Resultados Principales del Modelo</h3></div>', unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("📊 MAPE SARIMA",     "18.61%",  "−9% vs Regresión",  delta_color="inverse",
              help="Error porcentual medio absoluto del modelo SARIMA")
with m2:
    st.metric("📈 RMSE SARIMA",     "9,446",   "−28% vs Regresión", delta_color="inverse",
              help="Raíz del error cuadrático medio")
with m3:
    st.metric("🎯 Pronóstico 2025", "578,069", "+18% vs 2024",
              help="Arribos totales esperados para 2025")
with m4:
    st.metric("🏖️ Pico Abril 2025", "62,995",  "Semana Santa",
              help="Pronóstico para el mes pico — Semana Santa 2025")

st.divider()


# ══════════════════════════════════════════════════════════════════════════════
# TECNOLOGÍAS + FUENTES
# ══════════════════════════════════════════════════════════════════════════════
col_tech, col_src = st.columns(2, gap="large")

with col_tech:
    sec_label("tech", "Tecnologías Utilizadas")
    tech_html = ""
    tech_icons = ["python", "table", "chart-line", "brain", "chart-area", "tv"]
    for i, (name, desc, enc_paths) in enumerate(TECHS):
        fa_icon = tech_icons[i] if i < len(tech_icons) else "circle"
        tech_html += f"""
        <div class="tech-item">
            <span class="tech-icon"><i class="fas fa-{fa_icon}" style="color:#FF6B6B;font-size:1.1rem;"></i></span>
            <span class="tech-name">{name}</span>
            <span class="tech-desc">{desc}</span>
        </div>"""
    st.markdown(tech_html, unsafe_allow_html=True)

with col_src:
    sec_label("data", "Fuentes de Datos")
    src_html = ""
    src_icons = ["building", "chart-bar", "cloud", "bank", "calendar"]
    for i, (name, desc) in enumerate(FUENTES):
        fa_icon = src_icons[i] if i < len(src_icons) else "circle"
        src_html += f"""
        <div class="tech-item">
            <span style="color:#FF6B6B;"><i class="fas fa-{fa_icon}"></i></span>
            <span class="src-badge">{name}</span>
            <span class="tech-desc">{desc}</span>
        </div>"""
    st.markdown(src_html, unsafe_allow_html=True)

st.divider()


# ══════════════════════════════════════════════════════════════════════════════
# EQUIPO
# ══════════════════════════════════════════════════════════════════════════════
sec_label("team", "Equipo de Investigación")

cols = st.columns(5, gap="medium")
team_roles = ["👨‍💼", "👨‍💼", "👨‍💼", "❓", "❓"]
for col, (initials, apellido, nombre), role in zip(cols, EQUIPO, team_roles):
    with col:
        st.markdown(f"""
        <div class="team-card">
            <div class="team-avatar" style="font-size:1.8rem;background:linear-gradient(135deg,#C00000,#8B0000);">
                <i class="fas fa-user" style="color:white;"></i>
            </div>
            <div class="team-name">{apellido}</div>
            <div class="team-sub">{nombre}</div>
            <div class="team-badge">
                <i class="fas fa-graduation-cap" style="margin-right:4px;"></i>ING. SISTEMAS
            </div>
        </div>""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    <i class="fas fa-map-marker-alt" style="margin-right:4px;"></i>Ayacucho · Perú · 2026 &nbsp;—&nbsp;
    <i class="fas fa-flask" style="margin-right:4px;"></i>Proyecto Final de Investigación e Inteligencia de Negocios
</div>
""", unsafe_allow_html=True)