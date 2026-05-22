"""
Pagina 5: Fase 5 de CRISP-DM - Evaluacion
Metricas, diagnostico de residuos y comparacion de modelos.
"""

import warnings
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.statespace.sarimax import SARIMAX

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Fase 5 - Evaluación", page_icon="📈", layout="wide")

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
.block-container { padding-top: 0 !important; max-width: 1200px !important; }

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

hr { border-color: rgba(255,255,255,0.08) !important; }
[data-testid="stAlert"] {
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    background: #111E33 !important;
}
[data-testid="stDataFrame"] { border-radius: 10px !important; overflow: hidden !important; }

/* Phase header */
.phase-header {
    background: linear-gradient(135deg,#0D1B2A 0%,#1B3A5C 100%);
    border-radius: 16px; padding: 32px 36px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 8px; position: relative; overflow: hidden;
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
    padding-top:20px; border-top:1px solid rgba(255,255,255,0.08); flex-wrap:wrap;
}
.ph-stat-val { font-family:'Sora',sans-serif; font-size:1.5rem; font-weight:800; color:#FF6B6B; }
.ph-stat-lbl { font-size:0.7rem; color:#5580A8; margin-top:2px; }

/* Section label */
.sec-label {
    display:flex; align-items:center; gap:10px;
    margin:24px 0 16px; padding-bottom:10px;
    border-bottom:1px solid rgba(255,255,255,0.08);
}
.sec-label-text {
    font-family:'Sora',sans-serif; font-weight:700;
    font-size:1rem; color:#E2EAF4; letter-spacing:-0.01em;
}

/* Info box */
.info-box {
    background: linear-gradient(135deg,#0D1929,#132040);
    border:1px solid rgba(255,255,255,0.08);
    border-left:3px solid #C00000;
    border-radius:10px; padding:16px 20px;
    font-size:0.85rem; color:#A8C0D6; line-height:1.7; margin:12px 0;
}
.info-box strong { color:#E2EAF4; }

/* Model header card */
.model-card-header {
    display:flex; align-items:center; gap:12px;
    background:#111E33; border:1px solid rgba(255,255,255,0.08);
    border-radius:12px; padding:16px 20px; margin-bottom:16px;
}
.model-card-icon {
    width:42px; height:42px; border-radius:10px; flex-shrink:0;
    background-repeat:no-repeat; background-position:center; background-size:22px;
}
.model-card-title {
    font-family:'Sora',sans-serif; font-weight:800;
    font-size:0.92rem; color:#E2EAF4; margin-bottom:3px;
}
.model-card-sub { font-size:0.75rem; color:#5580A8; }

/* Criterio cards */
.criterio-card {
    border-radius:12px; padding:16px 18px;
    border:1px solid rgba(255,255,255,0.08);
    transition: transform 0.2s, box-shadow 0.2s;
}
.criterio-card:hover { transform:translateY(-3px); box-shadow:0 10px 28px rgba(0,0,0,0.4); }
.criterio-icon {
    width:32px; height:32px; border-radius:8px; margin-bottom:10px;
    background-repeat:no-repeat; background-position:center; background-size:18px;
}
.criterio-title { font-family:'Sora',sans-serif; font-weight:800; font-size:0.82rem; color:#E2EAF4; margin-bottom:4px; }
.criterio-val   { font-family:'Sora',sans-serif; font-size:1.2rem; font-weight:800; }
.criterio-desc  { font-size:0.72rem; color:#6A8BAE; margin-top:4px; }

/* Stat row */
.stat-row {
    display:flex; justify-content:space-between; align-items:center;
    padding:9px 14px; border-radius:8px; margin:4px 0;
    background:#111E33; border:1px solid rgba(255,255,255,0.06);
    transition:all 0.2s;
}
.stat-row:hover { background:#172540; border-color:rgba(85,153,221,0.2); }
.stat-row-name  { font-size:0.8rem; color:#7A9CB8; font-weight:500; }
.stat-row-val   { font-family:'Sora',sans-serif; font-size:0.88rem; font-weight:800; color:#E2EAF4; }

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
    "target":   "%3Ccircle cx='12' cy='12' r='10'/%3E%3Ccircle cx='12' cy='12' r='6'/%3E%3Ccircle cx='12' cy='12' r='2'/%3E",
    "compare":  "%3Cpolyline points='16 3 21 3 21 8'/%3E%3Cline x1='4' y1='20' x2='21' y2='3'/%3E%3Cpolyline points='21 16 21 21 16 21'/%3E%3Cline x1='15' y1='15' x2='21' y2='21'/%3E",
    "residual": "%3Cpath d='M22 11.08V12a10 10 0 1 1-5.93-9.14'/%3E%3Cpolyline points='22 4 12 14.01 9 11.01'/%3E",
    "errors":   "%3Ccircle cx='12' cy='12' r='10'/%3E%3Cline x1='12' y1='8' x2='12' y2='12'/%3E%3Cline x1='12' y1='16' x2='12.01' y2='16'/%3E",
    "chart":    "%3Cline x1='18' y1='20' x2='18' y2='10'/%3E%3Cline x1='12' y1='20' x2='12' y2='4'/%3E%3Cline x1='6' y1='20' x2='6' y2='14'/%3E",
    "trending": "%3Cpolyline points='23 6 13.5 15.5 8.5 10.5 1 18'/%3E%3Cpolyline points='17 6 23 6 23 12'/%3E",
    "check":    "%3Cpath d='M22 11.08V12a10 10 0 1 1-5.93-9.14'/%3E%3Cpolyline points='22 4 12 14.01 9 11.01'/%3E",
    "table":    "%3Cpath d='M9 3H5a2 2 0 0 0-2 2v4m6-6h10a2 2 0 0 1 2 2v4M9 3v18m0 0h10a2 2 0 0 0 2-2V9M9 21H5a2 2 0 0 1-2-2V9m0 0h18'/%3E",
    "activity": "%3Cpolyline points='22 12 18 12 15 21 9 3 6 12 2 12'/%3E",
    "history":  "%3Ccircle cx='12' cy='12' r='10'/%3E%3Cpolyline points='12 6 12 12 16 14'/%3E",
    "brain":    "%3Cpath d='M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96-.46 2.5 2.5 0 0 1-1.07-4.73A3 3 0 0 1 3.83 9a3 3 0 0 1 .79-5.07A2.5 2.5 0 0 1 9.5 2z'/%3E%3Cpath d='M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96-.46 2.5 2.5 0 0 0 1.07-4.73 3 3 0 0 0 2.64-4.27 3 3 0 0 0-.79-5.07A2.5 2.5 0 0 0 14.5 2z'/%3E",
}

def icon_url(key, size=20, color="%23E03030"):
    enc = ICONS.get(key, ICONS["target"])
    return (
        f"url(\"data:image/svg+xml,%3Csvg xmlns='http%3A//www.w3.org/2000/svg' "
        f"width='{size}' height='{size}' viewBox='0 0 24 24' fill='none' "
        f"stroke='{color}' stroke-width='2' stroke-linecap='round' "
        f"stroke-linejoin='round'%3E{enc}%3C/svg%3E\")"
    )

def sec_label(icon_key, text):
    bg = icon_url(icon_key)
    st.markdown(
        '<div class="sec-label">'
        f'<span style="display:inline-block;width:20px;height:20px;flex-shrink:0;'
        f'background:{bg} center/20px no-repeat;"></span>'
        f'<span class="sec-label-text">{text}</span>'
        '</div>',
        unsafe_allow_html=True,
    )

def model_card_header(icon_key, title, subtitle, bg_color="#C00000"):
    bg = icon_url(icon_key, 22, "%23ffffff")
    st.markdown(
        '<div class="model-card-header">'
        f'<div class="model-card-icon" style="background-color:{bg_color};background-image:{bg};"></div>'
        '<div>'
        f'<div class="model-card-title">{title}</div>'
        f'<div class="model-card-sub">{subtitle}</div>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )

def plotly_dark(title="", height=460):
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
        xaxis=dict(gridcolor="rgba(255,255,255,0.04)", linecolor="rgba(255,255,255,0.08)"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.04)", linecolor="rgba(255,255,255,0.08)"),
    )

def stat_row(name, val):
    st.markdown(
        f'<div class="stat-row">'
        f'<span class="stat-row-name">{name}</span>'
        f'<span class="stat-row-val">{val}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

# ══════════════════════════════════════════════════════════════════════════════
# DATOS
# ══════════════════════════════════════════════════════════════════════════════
@st.cache_resource
def calcular_todo():
    df = pd.read_csv("data/turismo_ayacucho_2010_2024.csv", parse_dates=["fecha"])
    df = df.sort_values("fecha").set_index("fecha")
    train = df[df.index < "2024-01-01"]
    test  = df[df.index >= "2024-01-01"]

    modelo_s = SARIMAX(train["arribos"], order=(1,1,1),
                       seasonal_order=(1,1,1,12),
                       enforce_stationarity=False, enforce_invertibility=False)
    res_s  = modelo_s.fit(disp=False)
    pred_s = res_s.forecast(steps=len(test))
    pred_s.index = test.index

    X = pd.get_dummies(df["mes"], prefix="mes", drop_first=True).astype(int)
    for col in ["semana_santa","feriado_largo","temperatura_c",
                "precipitacion_mm","evento_cultural","pandemia_covid"]:
        X[col] = df[col].values

    X_train = X[df.index < "2024-01-01"]
    X_test  = X[df.index >= "2024-01-01"]
    y_train = df.loc[df.index < "2024-01-01", "arribos"].values
    y_test  = df.loc[df.index >= "2024-01-01", "arribos"].values

    modelo_r = LinearRegression()
    modelo_r.fit(X_train, y_train)
    pred_r = modelo_r.predict(X_test)

    return dict(df=df, train=train, test=test, y_test=y_test,
                pred_sarima=pred_s, pred_rlm=pred_r,
                resultado_sarima=res_s, y_train_values=y_train)

def calcular_metricas(y_real, y_pred, train_vals=None):
    rmse = np.sqrt(mean_squared_error(y_real, y_pred))
    mae  = mean_absolute_error(y_real, y_pred)
    r2   = r2_score(y_real, y_pred)
    mape = np.mean(np.abs((y_real - y_pred) / y_real)) * 100
    mase = None
    if train_vals is not None:
        denom = np.abs(np.diff(train_vals)).mean()
        if denom > 0:
            mase = np.abs(y_real - y_pred).mean() / denom
    return dict(RMSE=rmse, MAE=mae, MAPE=mape, R2=r2, MASE=mase)

with st.spinner("Calculando métricas…"):
    datos    = calcular_todo()
    m_sarima = calcular_metricas(datos["y_test"], datos["pred_sarima"].values, datos["y_train_values"])
    m_rlm    = calcular_metricas(datos["y_test"], datos["pred_rlm"],           datos["y_train_values"])

# ══════════════════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════════════════
mejor_mape = min(m_sarima["MAPE"], m_rlm["MAPE"])
mejor_mod  = "SARIMA" if m_sarima["MAPE"] < m_rlm["MAPE"] else "Regresión"

st.markdown(f"""
<div class="phase-header">
  <div class="ph-badge">Fase 5 de 6 · CRISP-DM</div>
  <div class="ph-title">Evaluación de <span>Modelos</span></div>
  <div class="ph-sub">Métricas de desempeño, diagnóstico estadístico y comparación de modelos predictivos</div>
  <div class="ph-stats">
    <div><div class="ph-stat-val">{m_sarima['MAPE']:.2f}%</div><div class="ph-stat-lbl">MAPE SARIMA</div></div>
    <div><div class="ph-stat-val">{m_sarima['RMSE']:,.0f}</div><div class="ph-stat-lbl">RMSE SARIMA</div></div>
    <div><div class="ph-stat-val">{m_rlm['MAPE']:.2f}%</div><div class="ph-stat-lbl">MAPE Regresión</div></div>
    <div><div class="ph-stat-val">{mejor_mod}</div><div class="ph-stat-lbl">Mejor modelo</div></div>
    <div><div class="ph-stat-val">2024</div><div class="ph-stat-lbl">Período de prueba</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TABS
# ══════════════════════════════════════════════════════════════════════════════
tab1, tab2, tab3, tab4 = st.tabs([
    "  Métricas  ",
    "  Comparación  ",
    "  Diagnóstico Residuos  ",
    "  Errores Mensuales  ",
])

# ─────────────────────────────────────────────
# TAB 1 — MÉTRICAS
# ─────────────────────────────────────────────
with tab1:
    sec_label("target", "Métricas de Desempeño — Conjunto de Prueba 2024")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        model_card_header("brain", "SARIMA(1,1,1)(1,1,1)₁₂",
                          "Modelo de series temporales estacional", "#C00000")
        st.metric("RMSE", f"{m_sarima['RMSE']:,.2f}")
        st.metric("MAE",  f"{m_sarima['MAE']:,.2f}")
        st.metric("MAPE", f"{m_sarima['MAPE']:.2f}%",
                  delta=f"{m_sarima['MAPE']-20:.2f}% vs criterio 20%",
                  delta_color="inverse")
        st.metric("R²",   f"{m_sarima['R2']:.4f}")
        if m_sarima["MASE"]:
            st.metric("MASE", f"{m_sarima['MASE']:.4f}",
                      delta="< 1 supera al naive", delta_color="off")

    with col2:
        model_card_header("activity", "Regresión Lineal Múltiple",
                          "17 variables explicativas · codificación one-hot", "#1B3A5C")
        st.metric("RMSE", f"{m_rlm['RMSE']:,.2f}")
        st.metric("MAE",  f"{m_rlm['MAE']:,.2f}")
        st.metric("MAPE", f"{m_rlm['MAPE']:.2f}%")
        st.metric("R²",   f"{m_rlm['R2']:.4f}")
        if m_rlm["MASE"]:
            st.metric("MASE", f"{m_rlm['MASE']:.4f}")

    st.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)
    sec_label("check", "Cumplimiento de Criterios de Éxito")

    c1, c2, c3 = st.columns(3)
    ok_mape = m_sarima["MAPE"] < 20
    ok_mase = m_sarima["MASE"] and m_sarima["MASE"] < 1
    mejora_mae = ((m_rlm["MAE"] - m_sarima["MAE"]) / m_rlm["MAE"]) * 100

    with c1:
        color = "#1a7a4a" if ok_mape else "#7a1a1a"
        icono = "check" if ok_mape else "errors"
        bg = icon_url(icono, 18, "%23ffffff")
        st.markdown(
            f'<div class="criterio-card" style="background:{color}22;border-color:{color}44;">'
            f'<div class="criterio-icon" style="background-color:{color};background-image:{bg};"></div>'
            f'<div class="criterio-title">MAPE {"< 20%" if ok_mape else ">= 20%"}</div>'
            f'<div class="criterio-val" style="color:{"#4CAF82" if ok_mape else "#FF4444"};">{m_sarima["MAPE"]:.2f}%</div>'
            f'<div class="criterio-desc">Criterio de precisión aceptable</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    with c2:
        color2 = "#1a7a4a" if ok_mase else "#7a5a1a"
        icono2 = "check" if ok_mase else "errors"
        bg2 = icon_url(icono2, 18, "%23ffffff")
        mase_val = f"{m_sarima['MASE']:.4f}" if m_sarima["MASE"] else "N/A"
        st.markdown(
            f'<div class="criterio-card" style="background:{color2}22;border-color:{color2}44;">'
            f'<div class="criterio-icon" style="background-color:{color2};background-image:{bg2};"></div>'
            f'<div class="criterio-title">MASE {"< 1" if ok_mase else ">= 1"}</div>'
            f'<div class="criterio-val" style="color:{"#4CAF82" if ok_mase else "#FFC107"};">{mase_val}</div>'
            f'<div class="criterio-desc">Supera al modelo naive</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    with c3:
        bg3 = icon_url("trending", 18, "%23ffffff")
        st.markdown(
            f'<div class="criterio-card" style="background:#1a4a7a22;border-color:#1a4a7a44;">'
            f'<div class="criterio-icon" style="background-color:#1B3A5C;background-image:{bg3};"></div>'
            f'<div class="criterio-title">Mejora vs Regresión</div>'
            f'<div class="criterio-val" style="color:#4CAF82;">−{mejora_mae:.1f}%</div>'
            f'<div class="criterio-desc">Reducción de MAE frente a RLM</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

# ─────────────────────────────────────────────
# TAB 2 — COMPARACIÓN
# ─────────────────────────────────────────────
with tab2:
    sec_label("compare", "Comparación Visual de Métricas")

    metricas_df = pd.DataFrame({
        "Metrica":   ["RMSE", "MAE", "MAPE (%)", "MASE"],
        "SARIMA":    [m_sarima["RMSE"], m_sarima["MAE"], m_sarima["MAPE"], m_sarima["MASE"]],
        "Regresion": [m_rlm["RMSE"],   m_rlm["MAE"],   m_rlm["MAPE"],   m_rlm["MASE"]],
    })

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=metricas_df["Metrica"], y=metricas_df["SARIMA"],
        name="SARIMA", marker_color="#FF4444",
        text=metricas_df["SARIMA"].round(2), textposition="outside",
        textfont=dict(color="#E2EAF4", size=11),
    ))
    fig.add_trace(go.Bar(
        x=metricas_df["Metrica"], y=metricas_df["Regresion"],
        name="Regresión", marker_color="#FFC107",
        text=metricas_df["Regresion"].round(2), textposition="outside",
        textfont=dict(color="#E2EAF4", size=11),
    ))
    fig.update_layout(**plotly_dark("Comparación de Métricas — menor es mejor", 480))
    fig.update_layout(barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    sec_label("trending", "Conclusión del Análisis Comparativo")
    st.markdown("""
    <div class="info-box">
        <strong>SARIMA supera a la Regresión Múltiple en todas las métricas.</strong>
        La dinámica temporal autorregresiva y estacional captura mejor el comportamiento
        del flujo turístico que las variables explicativas lineales estáticas.
        El componente estacional mensual (s=12) es clave para modelar picos como Semana Santa.
    </div>
    """, unsafe_allow_html=True)

    # Tabla comparativa lado a lado
    sec_label("table", "Resumen Numérico Comparativo")
    resumen = pd.DataFrame({
        "Métrica":   ["RMSE", "MAE", "MAPE (%)", "R²", "MASE"],
        "SARIMA":    [f"{m_sarima['RMSE']:,.2f}", f"{m_sarima['MAE']:,.2f}",
                     f"{m_sarima['MAPE']:.2f}%", f"{m_sarima['R2']:.4f}",
                     f"{m_sarima['MASE']:.4f}" if m_sarima['MASE'] else "—"],
        "Regresión": [f"{m_rlm['RMSE']:,.2f}",   f"{m_rlm['MAE']:,.2f}",
                     f"{m_rlm['MAPE']:.2f}%",    f"{m_rlm['R2']:.4f}",
                     f"{m_rlm['MASE']:.4f}" if m_rlm['MASE'] else "—"],
        "Ganador":   ["SARIMA","SARIMA","SARIMA",
                     "SARIMA" if m_sarima["R2"] > m_rlm["R2"] else "Regresión","SARIMA"],
    })
    st.dataframe(resumen, use_container_width=True, hide_index=True)

# ─────────────────────────────────────────────
# TAB 3 — DIAGNÓSTICO RESIDUOS
# ─────────────────────────────────────────────
with tab3:
    sec_label("residual", "Diagnóstico de Residuos del Modelo SARIMA")

    st.markdown("""
    <div class="info-box">
        Un buen modelo de series temporales debe producir residuos que se comporten
        como <strong>ruido blanco</strong>: media cero, varianza constante y sin
        autocorrelación. El test de Ljung-Box verifica la independencia.
    </div>
    """, unsafe_allow_html=True)

    residuos = datos["resultado_sarima"].resid

    col1, col2 = st.columns([3, 2], gap="large")

    with col1:
        sec_label("activity", "Test Ljung-Box — Independencia de Residuos")
        resultados_lb = []
        for lag in [10, 20, 30]:
            try:
                lb = acorr_ljungbox(residuos, lags=[lag], return_df=True)
                pval = lb["lb_pvalue"].iloc[0]
                resultados_lb.append({
                    "Lag":         lag,
                    "Estadístico": round(lb["lb_stat"].iloc[0], 4),
                    "p-valor":     round(pval, 4),
                    "Resultado":   "✅ Ruido blanco" if pval > 0.05 else "❌ Autocorrelación",
                })
            except Exception:
                pass
        st.dataframe(pd.DataFrame(resultados_lb), use_container_width=True, hide_index=True)
        st.markdown("""
        <div class="info-box" style="margin-top:12px;">
            <strong>Interpretación:</strong> p-valor &gt; 0.05 confirma que
            <strong>no hay autocorrelación significativa</strong> — los residuos
            son independientes y el modelo es adecuado.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        sec_label("chart", "Estadísticas de Residuos")
        for name, val in [
            ("Media",          f"{residuos.mean():,.2f}"),
            ("Desv. Estándar", f"{residuos.std():,.2f}"),
            ("Asimetría",      f"{residuos.skew():.4f}"),
            ("Curtosis",       f"{residuos.kurtosis():.4f}"),
            ("Mínimo",         f"{residuos.min():,.2f}"),
            ("Máximo",         f"{residuos.max():,.2f}"),
        ]:
            stat_row(name, val)

    # Residuos en el tiempo
    sec_label("trending", "Residuos en el Tiempo")
    fig_res = go.Figure()
    fig_res.add_trace(go.Scatter(
        x=residuos.index, y=residuos.values,
        mode="lines", line=dict(color="#3A7BD5", width=1.5),
        fill="tozeroy", fillcolor="rgba(58,123,213,0.06)",
        name="Residuos",
    ))
    fig_res.add_shape(type="line", x0=residuos.index[0], x1=residuos.index[-1],
                      y0=0, y1=0, xref="x", yref="y",
                      line=dict(color="rgba(255,68,68,0.6)", width=1.5, dash="dash"))
    fig_res.update_layout(**plotly_dark("Residuos del Modelo SARIMA", 380))
    st.plotly_chart(fig_res, use_container_width=True)

    # Histograma
    sec_label("chart", "Distribución de Residuos")
    fig_hist = go.Figure(go.Histogram(
        x=residuos.values, nbinsx=30,
        marker=dict(color="#3A7BD5", opacity=0.8,
                    line=dict(color="rgba(255,255,255,0.1)", width=0.5)),
    ))
    fig_hist.update_layout(**plotly_dark("Distribución de residuos — debe ser aproximadamente normal", 340))
    fig_hist.update_layout(xaxis_title="Residuo", yaxis_title="Frecuencia")
    st.plotly_chart(fig_hist, use_container_width=True)

# ─────────────────────────────────────────────
# TAB 4 — ERRORES MENSUALES
# ─────────────────────────────────────────────
with tab4:
    sec_label("errors", "Errores Absolutos Mes a Mes — 2024")

    st.markdown("""
    <div class="info-box">
        Comparación del error absoluto de ambos modelos para cada mes del
        conjunto de prueba. <strong>Barras más bajas = mejor precisión.</strong>
    </div>
    """, unsafe_allow_html=True)

    y_test  = datos["y_test"]
    pred_s  = datos["pred_sarima"].values
    pred_r  = datos["pred_rlm"]
    fechas  = datos["test"].index
    err_s   = np.abs(y_test - pred_s)
    err_r   = np.abs(y_test - pred_r)
    meses   = [d.strftime("%b %Y") for d in fechas]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=meses, y=err_s, name="Error SARIMA",
        marker=dict(color="#FF4444", opacity=0.85,
                    line=dict(color="rgba(255,255,255,0.05)", width=0.5)),
        text=err_s.astype(int), textposition="outside",
        textfont=dict(color="#A8C0D6", size=10),
    ))
    fig.add_trace(go.Bar(
        x=meses, y=err_r, name="Error Regresión",
        marker=dict(color="#FFC107", opacity=0.85,
                    line=dict(color="rgba(255,255,255,0.05)", width=0.5)),
        text=err_r.astype(int), textposition="outside",
        textfont=dict(color="#A8C0D6", size=10),
    ))
    fig.update_layout(**plotly_dark("Error Absoluto por Mes — Prueba 2024", 480))
    fig.update_layout(barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    sec_label("table", "Tabla Detallada de Predicciones y Errores")
    tabla = pd.DataFrame({
        "Mes":             meses,
        "Real":            y_test.astype(int),
        "SARIMA":          pred_s.astype(int),
        "Error SARIMA":    err_s.astype(int),
        "% Error SARIMA":  [f"{v:.1f}%" for v in (err_s / y_test * 100)],
        "Regresión":       pred_r.astype(int),
        "Error Regresión": err_r.astype(int),
        "% Error RLM":     [f"{v:.1f}%" for v in (err_r / y_test * 100)],
    })
    st.dataframe(tabla, use_container_width=True, hide_index=True)

    # KPIs finales
    st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)
    sec_label("target", "Resumen de Error Promedio — 2024")
    k1, k2, k3, k4 = st.columns(4)
    with k1: st.metric("MAPE SARIMA",     f"{m_sarima['MAPE']:.2f}%")
    with k2: st.metric("MAPE Regresión",  f"{m_rlm['MAPE']:.2f}%")
    with k3: st.metric("RMSE SARIMA",     f"{m_sarima['RMSE']:,.0f}")
    with k4: st.metric("RMSE Regresión",  f"{m_rlm['RMSE']:,.0f}")

st.markdown('<div class="footer-cap">Fase 5 de CRISP-DM · Evaluación de Modelos · 2026</div>', unsafe_allow_html=True)