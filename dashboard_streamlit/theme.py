"""
Modulo compartido: estilos oscuros + SVG helpers
Importar en cada pagina con: from theme import apply_theme, I, sec
"""

DARK_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=DM+Sans:wght@400;500&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css');

/* ── fondo oscuro global ── */
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"],
section.main, .main .block-container,
[data-testid="stHeader"] {
    background-color: #0D1B2A !important;
    color: #E8EDF2 !important;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#07111C 0%,#0D1B2A 100%) !important;
    border-right: 1px solid rgba(255,255,255,0.06) !important;
}
[data-testid="stSidebar"] * { color:#C8D8E8 !important; }
[data-testid="stSidebarNav"] a         { border-radius:8px !important; }
[data-testid="stSidebarNav"] a:hover   { background:rgba(255,255,255,0.07) !important; }
[data-testid="stSidebarNav"] a[aria-selected="true"] {
    background:rgba(192,0,0,0.25) !important;
    color:#FF8080 !important;
}
.stTabs [data-baseweb="tab-list"]  { background:#111E2D !important; border-radius:10px; padding:4px; }
.stTabs [data-baseweb="tab"]       { color:#8AAAC0 !important; border-radius:8px !important; font-family:'Sora',sans-serif !important; font-weight:600 !important; }
.stTabs [aria-selected="true"]     { background:#1B3A5C !important; color:#FFFFFF !important; }
.stTabs [data-baseweb="tab-highlight"] { display:none !important; }
[data-testid="stMarkdownContainer"] p { color:#C8D8E8; }
[data-testid="stMarkdownContainer"] b,
[data-testid="stMarkdownContainer"] strong { color:#FFFFFF; }
hr { border-color:rgba(255,255,255,0.08) !important; }

html, body { font-family:'DM Sans',sans-serif; background:#0D1B2A; }

/* ── keyframes ── */
@keyframes fadeSlideDown {
    from{opacity:0;transform:translateY(-28px);}
    to  {opacity:1;transform:translateY(0);}
}
@keyframes fadeSlideUp {
    from{opacity:0;transform:translateY(22px);}
    to  {opacity:1;transform:translateY(0);}
}
@keyframes scaleIn {
    from{opacity:0;transform:scale(0.88);}
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
@keyframes pulseGlow {
    0%  {box-shadow:0 0 0 0    rgba(192,0,0,.4);}
    70% {box-shadow:0 0 0 12px rgba(192,0,0,0);}
    100%{box-shadow:0 0 0 0    rgba(192,0,0,0);}
}
@keyframes countUp {
    from{opacity:0;transform:translateY(10px);}
    to  {opacity:1;transform:translateY(0);}
}
@keyframes iconBounce {
    0%,100%{transform:translateY(0);}
    50%    {transform:translateY(-5px);}
}
@keyframes glowPulse {
    0%,100%{opacity:.7;} 50%{opacity:1;}
}
@keyframes spinIcon {
    from{transform:rotate(0deg);}
    to{transform:rotate(360deg);}
}
@keyframes floatIcon {
    0%, 100%{transform:translateY(0px);}
    50%{transform:translateY(-8px);}
}
@keyframes slideInLeft {
    from{opacity:0; transform:translateX(-30px);}
    to{opacity:1; transform:translateX(0);}
}
@keyframes slideInRight {
    from{opacity:0; transform:translateX(30px);}
    to{opacity:1; transform:translateX(0);}
}
@keyframes pulseShadow {
    0%, 100%{box-shadow:0 0 0 0 rgba(192,0,0,0.4);}
    50%{box-shadow:0 0 0 12px rgba(192,0,0,0);}
}
@keyframes wiggle {
    0%, 100%{transform:rotate(0deg);}
    25%{transform:rotate(-2deg);}
    75%{transform:rotate(2deg);}
}
@keyframes fadeInUp {
    from{opacity:0; transform:translateY(20px);}
    to{opacity:1; transform:translateY(0);}
}

/* ── ICONOS ANIMADOS ── */
.icon-animated {
    display:inline-flex;
    align-items:center;
    justify-content:center;
    transition:all 0.3s cubic-bezier(.22,1,.36,1);
}
.icon-spin { animation:spinIcon 2s linear infinite; }
.icon-float { animation:floatIcon 3s ease-in-out infinite; }
.icon-glow { 
    color:#FF6B6B; 
    text-shadow:0 0 10px rgba(255, 107, 107, 0.8), 0 0 20px rgba(192,0,0,0.4);
}
.icon-bounce {
    animation:iconBounce 0.6s ease-in-out;
}

/* ── BADGE CON ICONO ── */
.badge-icon {
    display:inline-flex;
    align-items:center;
    gap:8px;
    background:rgba(192,0,0,0.15);
    border:1px solid rgba(192,0,0,0.35);
    padding:6px 12px;
    border-radius:20px;
    font-size:0.75rem;
    font-weight:700;
    color:#FF8080;
    transition:all 0.3s cubic-bezier(.22,1,.36,1);
}
.badge-icon:hover {
    background:rgba(192,0,0,0.25);
    box-shadow:0 0 12px rgba(192,0,0,0.3);
    transform:scale(1.05);
}
.badge-icon i { font-size:0.85rem; }

/* ── hero banner ── */
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
    background-size:300% 100%;
    animation:shimmer 3s linear infinite;
}
.phase-badge {
    display:inline-flex; align-items:center; gap:6px;
    background:rgba(192,0,0,.20); border:1px solid rgba(192,0,0,.40);
    color:#FF8080; border-radius:20px;
    padding:4px 14px; font-size:.74rem; font-weight:700;
    font-family:'Sora',sans-serif; letter-spacing:.7px; margin-bottom:12px;
}
.phase-title {
    font-family:'Sora',sans-serif; font-weight:800;
    font-size:2rem; color:#F0F6FF; margin:0; line-height:1.2;
}
.phase-title span { color:#FF6B6B; }
.phase-sub { color:#7FA4C0; margin-top:8px; font-size:.96rem; }

/* ── accent line ── */
.accent-line {
    height:3px; border-radius:2px; margin:18px 0;
    background:linear-gradient(90deg,#C00000,#1B3A5C,#C00000);
    background-size:200% 100%;
    animation:shimmer 4s linear infinite;
}

/* ── section title ── */
.sec-title {
    display:flex; align-items:center; gap:10px; margin-bottom:14px;
    animation:fadeSlideUp .6s cubic-bezier(.22,1,.36,1) both;
}
.sec-title h3 {
    font-family:'Sora',sans-serif; font-weight:700;
    color:#E8F0F8; margin:0; font-size:1.12rem;
}

/* ── metric cards ── */
[data-testid="metric-container"] {
    background:linear-gradient(135deg,#112240 0%,#0D1B2A 100%) !important;
    border:1px solid rgba(255,255,255,0.10) !important;
    border-top:3px solid #C00000 !important;
    border-radius:14px !important;
    padding:18px 20px !important;
    box-shadow:0 4px 20px rgba(0,0,0,.35) !important;
    animation:countUp .6s cubic-bezier(.22,1,.36,1) both;
    transition:transform .25s, box-shadow .25s !important;
}
[data-testid="metric-container"]:hover {
    transform:translateY(-5px) !important;
    box-shadow:0 12px 32px rgba(0,0,0,.5) !important;
    border-color:rgba(192,0,0,.5) !important;
}
[data-testid="metric-container"]:nth-child(1){animation-delay:.05s;}
[data-testid="metric-container"]:nth-child(2){animation-delay:.15s;}
[data-testid="metric-container"]:nth-child(3){animation-delay:.25s;}
[data-testid="metric-container"]:nth-child(4){animation-delay:.35s;}
[data-testid="stMetricLabel"] {font-family:'Sora',sans-serif !important;font-weight:600 !important;color:#7FA4C0 !important;font-size:.79rem !important;}
[data-testid="stMetricValue"] {font-family:'Sora',sans-serif !important;font-weight:800 !important;color:#F0F6FF !important;font-size:1.65rem !important;}
[data-testid="stMetricDelta"] {font-weight:600 !important;}

/* ── glass card ── */
.glass-card {
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.09);
    border-left:4px solid #C00000;
    border-radius:14px; padding:22px 24px;
    backdrop-filter:blur(6px);
    box-shadow:0 4px 24px rgba(0,0,0,.30);
    animation:fadeSlideUp .55s cubic-bezier(.22,1,.36,1) both;
    transition:transform .25s, box-shadow .25s, border-color .25s;
    color:#D8E8F4;
}
.glass-card:hover {
    transform:translateY(-3px);
    box-shadow:0 10px 36px rgba(0,0,0,.40);
    border-left-color:#FF6B6B;
}
.glass-card h4 {
    font-family:'Sora',sans-serif; font-weight:700; color:#F0F6FF;
    margin:0 0 12px; font-size:1rem; display:flex; align-items:center; gap:8px;
}

/* ── info-card dark (academica) ── */
.info-card-dark {
    background:linear-gradient(145deg,#07111C,#0D1B2A);
    border:1px solid rgba(255,255,255,0.10);
    border-radius:16px; padding:22px 24px; line-height:2.1;
    animation:scaleIn .65s cubic-bezier(.22,1,.36,1) both;
    box-shadow:0 8px 32px rgba(0,0,0,.40);
    transition:transform .3s, box-shadow .3s;
}
.info-card-dark:hover { transform:translateY(-3px); box-shadow:0 14px 42px rgba(0,0,0,.55); }
.info-card-dark .ic-row { display:flex; align-items:center; gap:9px; margin:2px 0; color:#C8D8E8; }
.info-card-dark b     { color:#A8C0D6; }
.info-card-dark .ic-title {
    font-family:'Sora',sans-serif; font-weight:700; font-size:1rem;
    color:#F0F6FF; margin-bottom:12px; display:flex; align-items:center; gap:8px;
}

/* ── bullet / list items ── */
.bul-item {
    display:flex; align-items:center; gap:10px;
    padding:10px 14px; border-radius:10px;
    background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.07);
    margin:5px 0; color:#C8D8E8;
    transition:all .22s cubic-bezier(.22,1,.36,1);
    animation:fadeSlideUp .5s cubic-bezier(.22,1,.36,1) both;
}
.bul-item:hover {
    background:rgba(27,58,92,0.45); border-color:rgba(100,160,220,0.35);
    transform:translateX(5px); box-shadow:0 3px 14px rgba(0,0,0,.25);
    color:#F0F6FF;
}
.bul-item:hover svg{animation:iconBounce .55s ease;}
.bul-item svg{flex-shrink:0;}

/* ── fase cards ── */
.fase-card {
    display:flex; align-items:center; gap:12px;
    padding:12px 16px; border-radius:12px;
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.07);
    border-left:4px solid #C00000;
    margin:6px 0; color:#C8D8E8;
    box-shadow:0 2px 8px rgba(0,0,0,.20);
    transition:all .25s cubic-bezier(.22,1,.36,1);
    animation:fadeSlideUp .5s cubic-bezier(.22,1,.36,1) both;
}
.fase-card:hover {
    border-left-color:#4A90D9; background:rgba(27,58,92,0.40);
    transform:translateX(6px); box-shadow:0 6px 20px rgba(0,0,0,.30);
    color:#F0F6FF;
}
.fase-card:hover svg{animation:iconBounce .55s ease;}
.fase-num {
    font-family:'Sora',sans-serif; font-weight:800; font-size:.72rem;
    color:#fff; background:linear-gradient(135deg,#C00000,#8B0000); border-radius:50%;
    width:32px; height:32px; display:flex; align-items:center; justify-content:center; flex-shrink:0;
    box-shadow:0 4px 12px rgba(192,0,0,0.4);
    font-size:1rem;
    transition:all 0.3s cubic-bezier(.22,1,.36,1);
}
.fase-card:hover .fase-num {
    transform:scale(1.15) rotate(5deg);
    box-shadow:0 6px 20px rgba(192,0,0,0.6);
}

/* ── tech items ── */
.tech-item {
    display:flex; align-items:center; gap:11px;
    padding:10px 14px; border-radius:10px;
    background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.07);
    margin:5px 0; color:#C8D8E8;
    box-shadow:0 1px 4px rgba(0,0,0,.15);
    transition:all .22s cubic-bezier(.22,1,.36,1);
    animation:fadeSlideUp .5s cubic-bezier(.22,1,.36,1) both;
}
.tech-item:hover {
    background:rgba(27,58,92,0.45); border-color:rgba(100,160,220,0.35);
    transform:translateX(5px); box-shadow:0 4px 16px rgba(0,0,0,.25); color:#F0F6FF;
}
.tech-item:hover i {
    animation:floatIcon 0.6s ease-in-out;
}
.tech-item i {
    transition:all 0.3s cubic-bezier(.22,1,.36,1);
}
.t-name { font-weight:700; color:#E8F0F8; }
.t-desc { color:#7FA4C0; font-size:.88rem; }

/* ── member cards ── */
.member-card {
    display:flex; flex-direction:column; align-items:center;
    text-align:center; padding:22px 12px 18px; border-radius:16px;
    background:linear-gradient(160deg,#112240,#0D1B2A);
    border:1px solid rgba(255,255,255,0.08);
    border-bottom:3px solid #C00000;
    box-shadow:0 4px 18px rgba(0,0,0,.35);
    transition:all .3s cubic-bezier(.22,1,.36,1);
    animation:scaleIn .55s cubic-bezier(.22,1,.36,1) both;
}
.member-card:hover {
    transform:translateY(-7px);
    box-shadow:0 16px 40px rgba(0,0,0,.50);
    border-bottom-color:#4A90D9;
    animation:pulseGlow 1.3s ease;
}
.m-ico {
    width:56px; height:56px; border-radius:50%;
    background:linear-gradient(135deg,#C00000,#8B0000);
    display:flex; align-items:center; justify-content:center;
    margin-bottom:10px; box-shadow:0 4px 16px rgba(192,0,0,.35);
    font-size:1.8rem;
    color:white;
    transition:all 0.3s cubic-bezier(.22,1,.36,1);
}
.member-card:hover .m-ico {
    transform:scale(1.12) translateY(-4px);
    box-shadow:0 8px 24px rgba(192,0,0,.5);
}
.m-name  { font-family:'Sora',sans-serif; font-weight:700; font-size:.78rem; color:#E8F0F8; line-height:1.35; }
.m-sub   { font-size:.73rem; color:#7FA4C0; margin-top:3px; }
.m-badge {
    margin-top:10px; font-size:.65rem; font-weight:700;
    background:linear-gradient(90deg,#1B3A5C,#112240);
    color:#A8C0D6; padding:3px 10px; border-radius:20px;
    border:1px solid rgba(255,255,255,0.10); letter-spacing:.5px;
}

/* ── custom alerts dark ── */
.alert-warning {
    background:rgba(245,158,11,0.10); border:1px solid rgba(245,158,11,0.30);
    border-left:4px solid #F59E0B; border-radius:12px;
    padding:18px 20px; color:#E8D5A0; font-size:.95rem; line-height:1.75;
    animation:scaleIn .6s cubic-bezier(.22,1,.36,1) both;
    display:flex; gap:14px; align-items:flex-start;
}
.alert-warning b { color:#FFD580; }
.alert-info {
    background:rgba(27,58,92,0.40); border:1px solid rgba(74,144,217,0.30);
    border-left:4px solid #4A90D9; border-radius:12px;
    padding:18px 20px; color:#C8D8E8; font-size:.95rem; line-height:1.75;
    animation:scaleIn .6s .1s cubic-bezier(.22,1,.36,1) both;
    display:flex; gap:14px; align-items:flex-start;
}
.alert-info b { color:#90C8F0; }
.alert-success {
    background:rgba(46,125,50,0.15); border:1px solid rgba(76,175,80,0.30);
    border-left:4px solid #4CAF50; border-radius:12px;
    padding:18px 20px; color:#C8E6C9; font-size:.95rem; line-height:1.75;
    animation:scaleIn .6s cubic-bezier(.22,1,.36,1) both;
    display:flex; gap:14px; align-items:flex-start;
}
.alert-success b { color:#A5D6A7; }
.alert-error {
    background:rgba(192,0,0,0.12); border:1px solid rgba(192,0,0,0.25);
    border-left:4px solid #C00000; border-radius:12px;
    padding:16px 18px; color:#F0C0C0; font-size:.90rem; line-height:1.65;
    animation:fadeSlideUp .5s cubic-bezier(.22,1,.36,1) both;
    transition:transform .22s, box-shadow .22s;
}
.alert-error:hover { transform:translateY(-3px); box-shadow:0 6px 20px rgba(192,0,0,.25); }
.alert-error b { color:#FF8080; }

/* ── hipotesis ── */
.hip-card {
    background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08);
    border-radius:12px; padding:16px 20px; margin:8px 0;
    display:flex; gap:14px; align-items:flex-start;
    box-shadow:0 2px 8px rgba(0,0,0,.20);
    animation:fadeSlideUp .5s cubic-bezier(.22,1,.36,1) both;
    transition:all .25s cubic-bezier(.22,1,.36,1); color:#C8D8E8;
}
.hip-card:hover {
    border-color:rgba(192,0,0,.45); background:rgba(192,0,0,.08);
    box-shadow:0 6px 22px rgba(0,0,0,.30); transform:translateX(4px); color:#F0F6FF;
}
.hip-code {
    font-family:'Sora',sans-serif; font-weight:800; font-size:.72rem;
    color:#fff; background:#C00000; border-radius:8px;
    padding:4px 10px; white-space:nowrap; flex-shrink:0; margin-top:2px;
}

/* ── objetivo items ── */
.obj-item {
    display:flex; align-items:center; gap:12px;
    padding:12px 16px; border-radius:12px;
    background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.07);
    border-left:4px solid #1B3A5C; margin:6px 0;
    box-shadow:0 1px 4px rgba(0,0,0,.15);
    transition:all .25s cubic-bezier(.22,1,.36,1);
    animation:fadeSlideUp .5s cubic-bezier(.22,1,.36,1) both; color:#C8D8E8;
}
.obj-item:hover {
    border-left-color:#C00000; background:rgba(192,0,0,.08);
    transform:translateX(6px); box-shadow:0 4px 18px rgba(0,0,0,.25); color:#F0F6FF;
}
.obj-item:hover svg{animation:iconBounce .55s ease;}
.obj-num {
    font-family:'Sora',sans-serif; font-weight:800; font-size:.70rem;
    color:#fff; background:linear-gradient(135deg,#C00000,#8B0000);
    border-radius:50%; width:26px; height:26px;
    display:flex; align-items:center; justify-content:center; flex-shrink:0;
}

/* ── footer ── */
.footer { text-align:center; color:#3A5A7A; font-size:.76rem; padding:8px 0; animation:fadeSlideUp 1s .4s both; }

/* ── delays ── */
.d1{animation-delay:.04s;} .d2{animation-delay:.11s;} .d3{animation-delay:.18s;}
.d4{animation-delay:.25s;} .d5{animation-delay:.32s;} .d6{animation-delay:.39s;}
</style>
"""

IC = {
    "bar-chart":   '<line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>',
    "dashboard":   '<rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/>',
    "target":      '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "users":       '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "user":        '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "code":        '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    "database":    '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/>',
    "search":      '<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>',
    "wrench":      '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "cpu":         '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/>',
    "trending-up": '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
    "broadcast":   '<path d="M4.9 19.1C1 15.2 1 8.8 4.9 4.9"/><path d="M7.8 16.2c-2.3-2.3-2.3-6.1 0-8.5"/><circle cx="12" cy="12" r="2"/><path d="M16.2 7.8c2.3 2.3 2.3 6.1 0 8.5"/><path d="M19.1 4.9C23 8.8 23 15.2 19.1 19.1"/>',
    "terminal":    '<polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/>',
    "table":       '<path d="M9 3H5a2 2 0 0 0-2 2v4m6-6h10a2 2 0 0 1 2 2v4M9 3v18m0 0h10a2 2 0 0 0 2-2V9M9 21H5a2 2 0 0 1-2-2V9m0 0h18"/>',
    "activity":    '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
    "brain":       '<path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96-.46 2.5 2.5 0 0 1-1.07-4.73A3 3 0 0 1 3.83 9a3 3 0 0 1 .79-5.07A2.5 2.5 0 0 1 9.5 2z"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96-.46 2.5 2.5 0 0 0 1.07-4.73 3 3 0 0 0 2.64-4.27 3 3 0 0 0-.79-5.07A2.5 2.5 0 0 0 14.5 2z"/>',
    "line-chart":  '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>',
    "layout":      '<rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/>',
    "globe":       '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "landmark":    '<line x1="3" y1="22" x2="21" y2="22"/><line x1="6" y1="18" x2="6" y2="11"/><line x1="10" y1="18" x2="10" y2="11"/><line x1="14" y1="18" x2="14" y2="11"/><line x1="18" y1="18" x2="18" y2="11"/><polygon points="12 2 20 7 4 7"/>',
    "cloud-rain":  '<line x1="16" y1="13" x2="16" y2="21"/><line x1="8" y1="13" x2="8" y2="21"/><line x1="12" y1="15" x2="12" y2="23"/><path d="M20 16.58A5 5 0 0 0 18 7h-1.26A8 8 0 1 0 4 15.25"/>',
    "banknote":    '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2"/><path d="M6 12h.01M18 12h.01"/>',
    "map-pin":     '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "book":        '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
    "graduation":  '<path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>',
    "school":      '<path d="M14 22v-4a2 2 0 1 0-4 0v4"/><path d="m18 10 4 2v8a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-8l4-2"/><path d="M18 5v17"/><path d="m4 6 8-4 8 4"/><path d="M6 5v17"/><circle cx="12" cy="9" r="2"/>',
    "building":    '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22V12h6v10"/><path d="M9 7h1"/><path d="M14 7h1"/>',
    "alert":       '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    "check-circle":'<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>',
    "list":        '<line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/>',
    "x-circle":    '<circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/>',
    "info":        '<circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>',
    "star":        '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "layers":      '<polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>',
    "award":       '<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89L17 22l-5-3-5 3 1.523-9.11"/>',
    "eye":         '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>',
    "lightbulb":   '<line x1="9" y1="18" x2="15" y2="18"/><line x1="10" y1="22" x2="14" y2="22"/><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/>',
    "shield":      '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "virus":       '<circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/>',
    "beaker":      '<path d="M4.5 3h15"/><path d="M6 3v16a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V3"/><path d="M6 14h12"/>',
    "question":    '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
    "shield-check": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/>',
}

def I(name, size=20, color="#FF6B6B", sw=2):
    d = IC.get(name,"")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
            f'viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">{d}</svg>')

def sec(icon, title, color="#FF6B6B"):
    import streamlit as st
    st.markdown(f"""
    <div class="sec-title">
        {I(icon,24,color)}
        <h3>{title}</h3>
    </div>""", unsafe_allow_html=True)

def apply_theme():
    import streamlit as st
    st.markdown(DARK_CSS, unsafe_allow_html=True)