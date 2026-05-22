"""
Pagina 1: Fase 1 de CRISP-DM - Comprension del Negocio
Tema: oscuro completo, letras bien contrastadas
"""

import streamlit as st

st.set_page_config(
    page_title="Fase 1 - Negocio",
    page_icon="https://cdn-icons-png.flaticon.com/512/3281/3281289.png",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=DM+Sans:wght@400;500&display=swap');

/* ══ FONDO OSCURO COMPLETO ══ */
html, body { background:#0D1B2A !important; color:#C8D8E8 !important; font-family:'DM Sans',sans-serif; }

[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
[data-testid="stHeader"],
section.main,
.main .block-container,
.stApp { background:#0D1B2A !important; }

/* tabs background */
[data-testid="stTabs"],
[data-baseweb="tab-panel"],
div[role="tabpanel"] { background:#0D1B2A !important; }

/* texto general de streamlit */
p, span, label, div, li, td, th { color:#C8D8E8 !important; }
h1,h2,h3,h4,h5,h6 { color:#F0F6FF !important; }
strong, b { color:#FFFFFF !important; }
i, em { color:#A8C0D6 !important; }

/* sidebar */
[data-testid="stSidebar"] {
    background:linear-gradient(180deg,#07111C 0%,#0D1B2A 100%) !important;
    border-right:1px solid rgba(255,255,255,0.06) !important;
}
[data-testid="stSidebar"] * { color:#C8D8E8 !important; }
[data-testid="stSidebarNav"] a:hover { background:rgba(255,255,255,0.07) !important; }
[data-testid="stSidebarNav"] a[aria-selected="true"] {
    background:rgba(192,0,0,0.25) !important; color:#FF8080 !important;
}

/* tabs */
.stTabs [data-baseweb="tab-list"] {
    background:#111E2D !important; border-radius:10px; padding:4px; gap:4px;
}
.stTabs [data-baseweb="tab"] {
    color:#7FA4C0 !important; border-radius:8px !important;
    font-family:'Sora',sans-serif !important; font-weight:600 !important;
    font-size:.88rem !important;
}
.stTabs [aria-selected="true"] { background:#1B3A5C !important; color:#FFFFFF !important; }
.stTabs [data-baseweb="tab-highlight"] { display:none !important; }

/* divisores */
hr { border-color:rgba(255,255,255,0.08) !important; }

/* ══ KEYFRAMES ══ */
@keyframes fadeSlideDown {
    from{opacity:0;transform:translateY(-28px);}
    to  {opacity:1;transform:translateY(0);}
}
@keyframes fadeSlideUp {
    from{opacity:0;transform:translateY(20px);}
    to  {opacity:1;transform:translateY(0);}
}
@keyframes scaleIn {
    from{opacity:0;transform:scale(0.9);}
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
@keyframes pulseRed {
    0%  {box-shadow:0 0 0 0   rgba(192,0,0,.4);}
    70% {box-shadow:0 0 0 10px rgba(192,0,0,0);}
    100%{box-shadow:0 0 0 0   rgba(192,0,0,0);}
}

/* ══ HERO ══ */
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
    background:radial-gradient(ellipse at 80% 50%,rgba(192,0,0,.18) 0%,transparent 60%);
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

/* ══ ACCENT LINE ══ */
.accent-line {
    height:3px; border-radius:2px; margin:18px 0;
    background:linear-gradient(90deg,#C00000,#1B3A5C,#C00000);
    background-size:200% 100%; animation:shimmer 4s linear infinite;
}

/* ══ SECTION TITLE ══ */
.sec-title {
    display:flex; align-items:center; gap:10px; margin-bottom:14px;
    animation:fadeSlideUp .6s cubic-bezier(.22,1,.36,1) both;
}
.sec-title h3 {
    font-family:'Sora',sans-serif; font-weight:700;
    color:#E8F0F8 !important; margin:0; font-size:1.12rem;
}

/* ══ METRICS ══ */
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
    box-shadow:0 12px 32px rgba(0,0,0,.5) !important;
    border-top-color:#FF6B6B !important;
}
[data-testid="metric-container"]:nth-child(1){animation-delay:.05s;}
[data-testid="metric-container"]:nth-child(2){animation-delay:.15s;}
[data-testid="metric-container"]:nth-child(3){animation-delay:.25s;}
[data-testid="metric-container"]:nth-child(4){animation-delay:.35s;}
[data-testid="stMetricLabel"] {
    font-family:'Sora',sans-serif !important; font-weight:600 !important;
    color:#7FA4C0 !important; font-size:.79rem !important;
}
[data-testid="stMetricValue"] {
    font-family:'Sora',sans-serif !important; font-weight:800 !important;
    color:#F0F6FF !important; font-size:1.65rem !important;
}
[data-testid="stMetricDelta"] svg { display:none; }

/* ══ GLASS CARD (ctx-card) ══ */
.glass-card {
    background:rgba(17,34,64,0.80);
    border:1px solid rgba(255,255,255,0.09);
    border-left:4px solid #C00000;
    border-radius:14px; padding:22px 24px;
    box-shadow:0 4px 24px rgba(0,0,0,.30);
    animation:fadeSlideUp .55s cubic-bezier(.22,1,.36,1) both;
    transition:transform .25s, box-shadow .25s;
}
.glass-card:hover { transform:translateY(-3px); box-shadow:0 10px 36px rgba(0,0,0,.40); }
.glass-card h4 {
    font-family:'Sora',sans-serif; font-weight:700;
    color:#F0F6FF !important; margin:0 0 12px; font-size:1rem;
    display:flex; align-items:center; gap:8px;
}
.glass-card p { color:#A8C0D6 !important; line-height:1.80; }
.glass-card b { color:#E8F0F8 !important; }

/* ══ BULLET ITEMS ══ */
.bul-item {
    display:flex; align-items:center; gap:10px;
    padding:10px 14px; border-radius:10px;
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.07);
    margin:5px 0;
    transition:all .22s cubic-bezier(.22,1,.36,1);
    animation:fadeSlideUp .5s cubic-bezier(.22,1,.36,1) both;
}
.bul-item span { color:#C8D8E8 !important; }
.bul-item:hover {
    background:rgba(27,58,92,0.50); border-color:rgba(74,144,217,0.35);
    transform:translateX(5px); box-shadow:0 3px 14px rgba(0,0,0,.25);
}
.bul-item:hover span { color:#F0F6FF !important; }
.bul-item:hover svg { animation:iconBounce .55s ease; }

/* ══ ALERT BOXES ══ */
.alert-warning {
    background:rgba(245,158,11,0.10);
    border:1px solid rgba(245,158,11,0.30); border-left:4px solid #F59E0B;
    border-radius:12px; padding:18px 20px;
    animation:scaleIn .6s cubic-bezier(.22,1,.36,1) both;
    display:flex; gap:14px; align-items:flex-start;
}
.alert-warning, .alert-warning * { color:#E8D5A0 !important; }
.alert-warning b, .alert-warning strong { color:#FFD580 !important; }

.alert-info {
    background:rgba(27,58,92,0.50);
    border:1px solid rgba(74,144,217,0.30); border-left:4px solid #4A90D9;
    border-radius:12px; padding:18px 20px;
    animation:scaleIn .6s .1s cubic-bezier(.22,1,.36,1) both;
    display:flex; gap:14px; align-items:flex-start;
}
.alert-info, .alert-info * { color:#C8D8E8 !important; }
.alert-info b, .alert-info strong { color:#90C8F0 !important; }

.alert-success {
    background:rgba(46,125,50,0.15);
    border:1px solid rgba(76,175,80,0.30); border-left:4px solid #4CAF50;
    border-radius:12px; padding:18px 20px;
    animation:scaleIn .6s cubic-bezier(.22,1,.36,1) both;
    display:flex; gap:14px; align-items:flex-start;
}
.alert-success, .alert-success * { color:#C8E6C9 !important; }
.alert-success b, .alert-success strong { color:#A5D6A7 !important; }

.alert-error {
    background:rgba(192,0,0,0.12);
    border:1px solid rgba(192,0,0,0.25); border-left:4px solid #C00000;
    border-radius:12px; padding:16px 18px;
    animation:fadeSlideUp .5s cubic-bezier(.22,1,.36,1) both;
    transition:transform .22s, box-shadow .22s;
}
.alert-error, .alert-error * { color:#F0C0C0 !important; }
.alert-error b, .alert-error strong { color:#FF8080 !important; }
.alert-error:hover { transform:translateY(-3px); box-shadow:0 6px 20px rgba(192,0,0,.25); }

/* ══ HIPOTESIS CARDS ══ */
.hip-card {
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.08); border-radius:12px;
    padding:16px 20px; margin:8px 0;
    display:flex; gap:14px; align-items:flex-start;
    box-shadow:0 2px 8px rgba(0,0,0,.20);
    animation:fadeSlideUp .5s cubic-bezier(.22,1,.36,1) both;
    transition:all .25s cubic-bezier(.22,1,.36,1);
}
.hip-card:hover {
    border-color:rgba(192,0,0,.45); background:rgba(192,0,0,.08);
    box-shadow:0 6px 22px rgba(0,0,0,.30); transform:translateX(4px);
}
.hip-card span:last-child { color:#C8D8E8 !important; line-height:1.6; }
.hip-card:hover span:last-child { color:#F0F6FF !important; }
.hip-code {
    font-family:'Sora',sans-serif; font-weight:800; font-size:.72rem;
    color:#fff !important; background:#C00000; border-radius:8px;
    padding:4px 10px; white-space:nowrap; flex-shrink:0; margin-top:2px;
}

/* ══ OBJETIVO ITEMS ══ */
.obj-item {
    display:flex; align-items:center; gap:12px;
    padding:12px 16px; border-radius:12px;
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.07); border-left:4px solid #1B3A5C;
    margin:6px 0; box-shadow:0 1px 4px rgba(0,0,0,.15);
    transition:all .25s cubic-bezier(.22,1,.36,1);
    animation:fadeSlideUp .5s cubic-bezier(.22,1,.36,1) both;
}
.obj-item span:last-child { color:#C8D8E8 !important; }
.obj-item:hover {
    border-left-color:#C00000; background:rgba(192,0,0,.08);
    transform:translateX(6px); box-shadow:0 4px 18px rgba(0,0,0,.25);
}
.obj-item:hover span:last-child { color:#F0F6FF !important; }
.obj-item:hover svg { animation:iconBounce .55s ease; }
.obj-num {
    font-family:'Sora',sans-serif; font-weight:800; font-size:.70rem;
    color:#fff !important; background:linear-gradient(135deg,#C00000,#8B0000);
    border-radius:50%; width:26px; height:26px; flex-shrink:0;
    display:flex; align-items:center; justify-content:center;
}

/* ══ FOOTER ══ */
.footer { text-align:center; color:#3A5A7A !important; font-size:.76rem; padding:8px 0; }

/* ══ DELAYS ══ */
.d1{animation-delay:.04s;} .d2{animation-delay:.11s;} .d3{animation-delay:.18s;}
.d4{animation-delay:.25s;} .d5{animation-delay:.32s;} .d6{animation-delay:.39s;}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SVG HELPER
# ══════════════════════════════════════════════════════════════════════════════
def svg(d, size=22, color="#FF6B6B", sw=2):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
            f'viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">{d}</svg>')

IC = {
    "building":    '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22V12h6v10"/><path d="M9 7h1"/><path d="M14 7h1"/>',
    "alert":       '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    "target":      '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "check-circle":'<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>',
    "list":        '<line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>',
    "bar-chart":   '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>',
    "users":       '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "map-pin":     '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "star":        '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "globe":       '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "x-circle":    '<circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/>',
    "info":        '<circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>',
    "cpu":         '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/>',
    "activity":    '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
    "layers":      '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
    "award":       '<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89L17 22l-5-3-5 3 1.523-9.11"/>',
    "eye":         '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>',
    "lightbulb":   '<line x1="9" y1="18" x2="15" y2="18"/><line x1="10" y1="22" x2="14" y2="22"/><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/>',
    "shield":      '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "virus":       '<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>',
    "beaker":      '<path d="M4.5 3h15"/><path d="M6 3v16a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V3"/><path d="M6 14h12"/>',
    "question":    '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
}

def I(name, size=20, color="#FF6B6B", sw=2):
    return svg(IC.get(name,""), size, color, sw)

def sec(icon, title, color="#FF6B6B"):
    st.markdown(f"""
    <div class="sec-title">
        {I(icon,24,color)}
        <h3>{title}</h3>
    </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="phase-hero">
    <div class="phase-badge">
        {I("layers",13,"#FF8080",2)} &nbsp;CRISP-DM &nbsp;·&nbsp; FASE 1 DE 6
    </div>
    <div style="display:flex;align-items:center;gap:18px;">
        <div style="animation:spinOnce .8s cubic-bezier(.22,1,.36,1) both;">
            {I("building",50,"#FF6B6B",1.6)}
        </div>
        <div>
            <h1 class="phase-title">Comprension del <span>Negocio</span></h1>
            <p class="phase-sub">Definicion del contexto, problema, objetivos e hipotesis del proyecto</p>
        </div>
    </div>
</div>
<div class="accent-line"></div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TABS
# ══════════════════════════════════════════════════════════════════════════════
tab1, tab2, tab3, tab4 = st.tabs([
    "  Contexto  ", "  Problema  ", "  Objetivos  ", "  Hipotesis  "
])

# ── TAB 1 ─────────────────────────────────────────────────────────────────────
with tab1:
    sec("globe", "Contexto del Negocio")
    col1, col2 = st.columns([2, 1], gap="large")

    with col1:
        st.markdown(f"""
        <div class="glass-card d1">
            <h4>{I("map-pin",18,"#FF6B6B")} Region Ayacucho — Turismo Estacional</h4>
            <p>
            La region <b>Ayacucho</b> recibe flujos turisticos estacionales asociados a
            festividades religiosas, eventos culturales y condiciones climaticas particulares.<br><br>
            La <b>Semana Santa ayacuchana</b> es reconocida como una de las celebraciones mas
            importantes del Peru y America Latina, generando picos de demanda hotelera,
            de transporte y servicios complementarios.
            </p>
        </div><br>
        """, unsafe_allow_html=True)

        sec("star", "Importancia del Sector", "#4A90D9")
        for (icon, txt), dc in zip([
            ("users",    "Genera empleo directo e indirecto en la region"),
            ("bar-chart","Aporta significativamente al PBI regional"),
            ("shield",   "Contribuye a la preservacion del patrimonio cultural"),
            ("globe",    "Posiciona a Ayacucho como destino turistico nacional"),
        ], ["d1","d2","d3","d4"]):
            st.markdown(f"""
            <div class="bul-item {dc}">
                {I(icon,17,"#4A90D9")}
                <span>{txt}</span>
            </div>""", unsafe_allow_html=True)

    with col2:
        st.metric("Arribos 2023",        "457,800", "+20.4% vs 2022")
        st.metric("vs Prepandemia 2019", "65.4%",   "Recuperando")
        st.metric("Turistas nacionales", "98.7%")
        st.metric("Turistas extranjeros","1.3%")

# ── TAB 2 ─────────────────────────────────────────────────────────────────────
with tab2:
    sec("alert", "Problema de Negocio", "#FF6B6B")
    st.markdown(f"""
    <div class="alert-warning">
        {I("alert",30,"#F59E0B",2)}
        <div>
            <b>Las instituciones de gestion turistica (DIRCETUR Ayacucho) y los operadores
            privados no cuentan con un modelo cuantitativo</b> que les permita anticipar
            con precision la cantidad de turistas esperados en periodos determinados.
        </div>
    </div><br>
    """, unsafe_allow_html=True)

    sec("x-circle", "Consecuencias del Problema", "#FF6B6B")
    col1, col2, col3 = st.columns(3, gap="medium")
    for col_st, (dc, titulo, desc) in zip([col1,col2,col3], [
        ("d1","Insuficiente oferta hotelera",   "Sin modelo predictivo, los hoteles no pueden anticipar la demanda en temporada alta."),
        ("d2","Subutilizacion de recursos",     "Costos fijos sin retorno durante meses de baja afluencia turistica."),
        ("d3","Ausencia de marketing focalizado","Campanas genericas en lugar de estrategias diferenciadas por temporada."),
    ]):
        with col_st:
            st.markdown(f"""
            <div class="alert-error {dc}">
                <div style="display:flex;gap:8px;align-items:center;margin-bottom:7px;">
                    {I("x-circle",16,"#FF6B6B")}
                    <b>{titulo}</b>
                </div>
                <span style="font-size:.87rem;">{desc}</span>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    sec("question", "Pregunta de Investigacion", "#4A90D9")
    st.markdown(f"""
    <div class="alert-info">
        {I("info",30,"#4A90D9",2)}
        <div>
            ¿En que medida las variables de festividades (Semana Santa), mes del año, clima,
            eventos culturales y pandemia permiten predecir la cantidad de turistas que arriban
            a la region Ayacucho mediante modelos de series temporales y regresion multiple
            bajo la metodologia <b>CRISP-DM</b>?
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── TAB 3 ─────────────────────────────────────────────────────────────────────
with tab3:
    sec("target", "Objetivo General")
    st.markdown(f"""
    <div class="alert-success">
        {I("check-circle",30,"#4CAF50",2)}
        <div>
            <b>Desarrollar un modelo predictivo</b> de la cantidad de turistas en Ayacucho
            utilizando series temporales (SARIMA) y regresion multiple, incorporando variables
            de festividades, mes, clima, eventos culturales y pandemia, bajo la metodologia
            <b>CRISP-DM</b>.
        </div>
    </div><br>
    """, unsafe_allow_html=True)

    sec("list", "Objetivos Especificos", "#4A90D9")
    for i, ((icon, txt), dc) in enumerate(zip([
        ("bar-chart", "Analizar el conjunto de datos historicos 2010-2024"),
        ("layers",    "Preparar las variables explicativas del modelo"),
        ("cpu",       "Aplicar modelos SARIMA y Regresion Lineal Multiple"),
        ("activity",  "Evaluar el desempeno con RMSE, MAE, MAPE y R²"),
        ("lightbulb", "Interpretar resultados para la toma de decisiones estrategicas"),
    ], ["d1","d2","d3","d4","d5"])):
        st.markdown(f"""
        <div class="obj-item {dc}">
            <span class="obj-num">{i+1}</span>
            {I(icon,18,"#4A90D9")}
            <span>{txt}</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    sec("award", "Criterios de Exito", "#FF6B6B")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Criterio Principal",  "MAPE < 20%", help="Error porcentual medio absoluto")
        st.metric("Criterio Secundario", "MASE < 1",   help="Error escalado medio absoluto")
    with col2:
        st.metric("Mejora vs Modelo Base",  "Reduccion MAE")
        st.metric("Validacion estadistica", "Residuos Ruido Blanco")

# ── TAB 4 ─────────────────────────────────────────────────────────────────────
with tab4:
    sec("beaker", "Hipotesis de Investigacion", "#4A90D9")
    st.markdown(f"""
    <div class="alert-info" style="margin-bottom:20px;">
        {I("eye",30,"#4A90D9",2)}
        <div>
            <b>H_G — Hipotesis General:</b><br>
            Las variables de festividades, mes, clima, eventos culturales y pandemia,
            en combinacion con modelos SARIMA y regresion multiple, permiten predecir
            significativamente la cantidad de turistas con un <b>MAPE inferior al 20%</b>.
        </div>
    </div>
    """, unsafe_allow_html=True)

    sec("list", "Hipotesis Especificas", "#FF6B6B")
    for (code, icon, texto), dc in zip([
        ("H₁","activity", "La serie temporal presenta estacionalidad anual significativa"),
        ("H₂","star",     "La Semana Santa tiene efecto positivo significativo (p < 0.05)"),
        ("H₃","virus",    "La pandemia produjo una reduccion significativa en el flujo turistico"),
        ("H₄","cpu",      "SARIMA supera a la regresion multiple en todas las metricas de desempeno"),
        ("H₅","globe",    "Las variables climaticas tienen un efecto secundario sobre el flujo"),
    ], ["d1","d2","d3","d4","d5"]):
        st.markdown(f"""
        <div class="hip-card {dc}">
            <span class="hip-code">{code}</span>
            {I(icon,18,"#4A90D9")}
            <span>{texto}</span>
        </div>""", unsafe_allow_html=True)

st.divider()
st.markdown("""
<p class="footer">
    Fase 1 de CRISP-DM &nbsp;&#183;&nbsp; Comprension del Negocio
    &nbsp;&#183;&nbsp; Investigacion e Inteligencia de Negocios &nbsp;&#183;&nbsp; 2026
</p>
""", unsafe_allow_html=True)