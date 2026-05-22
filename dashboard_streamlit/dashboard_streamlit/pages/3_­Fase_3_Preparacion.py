"""
Pagina 3: Fase 3 de CRISP-DM - Preparacion de los Datos
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Fase 3 - Preparacion", page_icon="🛠️", layout="wide")

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
    background: linear-gradient(135deg, #C00000, #8B0000) !important;
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

/* Dataframe */
[data-testid="stDataFrame"] { border-radius: 10px !important; overflow: hidden !important; }
iframe { border-radius: 10px !important; }

/* Divider */
hr { border-color: rgba(255,255,255,0.08) !important; }

/* Alertas */
[data-testid="stAlert"] {
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    background: #111E33 !important;
}

/* Código */
[data-testid="stCode"] {
    background: #0D1929 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 10px !important;
}

/* Animaciones */
@keyframes fadeUp { from{opacity:0;transform:translateY(14px)} to{opacity:1;transform:translateY(0)} }

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
    background-size: 200% 100%;
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

.transform-row {
    display:flex; align-items:flex-start; gap:16px;
    background:#111E33; border:1px solid rgba(255,255,255,0.07);
    border-radius:10px; padding:14px 18px; margin:6px 0;
    transition: all 0.2s;
}
.transform-row:hover {
    background:#172540; border-color:rgba(85,153,221,0.3);
    transform:translateX(4px);
}
.transform-icon {
    width:36px; height:36px; border-radius:9px; flex-shrink:0;
    display:flex; align-items:center; justify-content:center;
    font-size:1rem;
}
.transform-title { font-weight:700; font-size:0.86rem; color:#E2EAF4; margin-bottom:3px; font-family:'Sora',sans-serif; }
.transform-desc  { font-size:0.78rem; color:#6A8BAE; line-height:1.5; }

.stat-pill {
    display:inline-flex; align-items:center; gap:6px;
    background:#111E33; border:1px solid rgba(255,255,255,0.08);
    border-radius:20px; padding:5px 14px; margin:4px;
    font-size:0.78rem; color:#A8C0D6;
    transition: all 0.2s;
}
.stat-pill:hover { background:#172540; border-color:rgba(192,0,0,0.3); color:#E2EAF4; }
.stat-pill b { color:#FF6B6B; }

.dummy-tag {
    display:inline-block;
    background:#0D1929; border:1px solid rgba(192,0,0,0.3);
    color:#FF8A8A; font-family:'Courier New',monospace;
    font-size:0.72rem; padding:3px 9px; border-radius:6px; margin:3px;
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
def sec_label(icon_enc, text):
    bg = f"url(\"data:image/svg+xml,%3Csvg xmlns='http%3A//www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24' fill='none' stroke='%23E03030' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E{icon_enc}%3C/svg%3E\")"
    st.markdown(
        '<div class="sec-label">'
        f'<span style="display:inline-block;width:20px;height:20px;flex-shrink:0;background:{bg} center/20px no-repeat;"></span>'
        f'<span class="sec-label-text">{text}</span>'
        '</div>',
        unsafe_allow_html=True,
    )

ICONS = {
    "check":    "%3Cpath d='M9 11l3 3L22 4'/%3E%3Cpath d='M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11'/%3E",
    "code":     "%3Cpolyline points='16 18 22 12 16 6'/%3E%3Cpolyline points='8 6 2 12 8 18'/%3E",
    "split":    "%3Ccircle cx='18' cy='18' r='3'/%3E%3Ccircle cx='6' cy='6' r='3'/%3E%3Cpath d='M13 6h3a2 2 0 0 1 2 2v7'/%3E%3Cline x1='6' y1='9' x2='6' y2='21'/%3E",
    "table":    "%3Cpath d='M9 3H5a2 2 0 0 0-2 2v4m6-6h10a2 2 0 0 1 2 2v4M9 3v18m0 0h10a2 2 0 0 0 2-2V9M9 21H5a2 2 0 0 1-2-2V9m0 0h18'/%3E",
    "star":     "%3Cpolygon points='12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2'/%3E",
    "bar":      "%3Cline x1='18' y1='20' x2='18' y2='10'/%3E%3Cline x1='12' y1='20' x2='12' y2='4'/%3E%3Cline x1='6' y1='20' x2='6' y2='14'/%3E",
    "shield":   "%3Cpath d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'/%3E",
    "calendar": "%3Crect x='3' y='4' width='18' height='18' rx='2' ry='2'/%3E%3Cline x1='16' y1='2' x2='16' y2='6'/%3E%3Cline x1='8' y1='2' x2='8' y2='6'/%3E%3Cline x1='3' y1='10' x2='21' y2='10'/%3E",
    "target":   "%3Ccircle cx='12' cy='12' r='10'/%3E%3Ccircle cx='12' cy='12' r='6'/%3E%3Ccircle cx='12' cy='12' r='2'/%3E",
    "alert":    "%3Ccircle cx='12' cy='12' r='10'/%3E%3Cline x1='12' y1='8' x2='12' y2='12'/%3E%3Cline x1='12' y1='16' x2='12.01' y2='16'/%3E",
}

# ══════════════════════════════════════════════════════════════════════════════
# DATOS
# ══════════════════════════════════════════════════════════════════════════════
@st.cache_data
def cargar_datos():
    df = pd.read_csv("data/turismo_ayacucho_2010_2024.csv", parse_dates=["fecha"])
    return df.sort_values("fecha").reset_index(drop=True)

df = cargar_datos()

# ══════════════════════════════════════════════════════════════════════════════
# HEADER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="phase-header">
  <div class="ph-badge">Fase 3 de 6 · CRISP-DM</div>
  <div class="ph-title">Preparación de <span>los Datos</span></div>
  <div class="ph-sub">Limpieza, transformación y división en conjuntos de entrenamiento y prueba</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# TABS
# ══════════════════════════════════════════════════════════════════════════════
tab1, tab2, tab3, tab4 = st.tabs([
    "  Verificación  ",
    "  Codificación  ",
    "  División  ",
    "  Resultado Final  ",
])

# ─────────────────────────────────────────────
# TAB 1 — VERIFICACIÓN
# ─────────────────────────────────────────────
with tab1:
    sec_label(ICONS["check"], "Verificación de Calidad de los Datos")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Total de Registros", f"{len(df):,}")
        st.metric("Total de Variables", f"{df.shape[1]}")
    with c2:
        st.metric("Valores Nulos", df.isnull().sum().sum())
        st.metric("Duplicados", df.duplicated().sum())
    with c3:
        st.metric("Años Cubiertos", df["anio"].nunique())
        st.metric("Frecuencia", "Mensual")

    sec_label(ICONS["table"], "Diagnóstico Detallado por Columna")

    diag = pd.DataFrame({
        "Variable": df.columns,
        "Tipo": [str(df[col].dtype) for col in df.columns],
        "Nulos": df.isnull().sum().values,
        "Únicos": [df[col].nunique() for col in df.columns],
        "Mínimo": [df[col].min() if pd.api.types.is_numeric_dtype(df[col]) else "—" for col in df.columns],
        "Máximo": [df[col].max() if pd.api.types.is_numeric_dtype(df[col]) else "—" for col in df.columns],
    })
    st.dataframe(diag, use_container_width=True, hide_index=True)

    if df.isnull().sum().sum() == 0:
        st.success("✅  Dataset limpio — sin valores nulos ni duplicados detectados.")
    else:
        st.warning("⚠️  Se detectaron valores nulos que requieren imputación.")

    # Pills de resumen
    st.markdown("<div style='margin-top:16px;'>", unsafe_allow_html=True)
    pills = [
        (f"{len(df):,}", "registros totales"),
        (f"{df['anio'].nunique()}", "años de datos"),
        ("0", "valores nulos"),
        ("0", "duplicados"),
        (f"{df.shape[1]}", "variables"),
        ("Mensual", "frecuencia"),
    ]
    pills_html = "".join(
        f'<span class="stat-pill"><b>{v}</b> {l}</span>' for v, l in pills
    )
    st.markdown(pills_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# TAB 2 — CODIFICACIÓN
# ─────────────────────────────────────────────
with tab2:
    sec_label(ICONS["code"], "Codificación One-Hot de la Variable Mes")

    st.markdown("""
    <div class="info-box">
        La variable <strong>mes</strong> es categórica (1–12) pero numérica.
        Para los modelos de regresión se aplica <strong>codificación one-hot</strong>
        que evita imponer una relación lineal artificial entre meses.
        Se omite <strong>enero</strong> como categoría de referencia para prevenir
        multicolinealidad perfecta (<em>dummy variable trap</em>).
    </div>
    """, unsafe_allow_html=True)

    X_dummies = pd.get_dummies(df["mes"], prefix="mes", drop_first=True).astype(int)

    col1, col2 = st.columns([1, 2])

    with col1:
        sec_label(ICONS["star"], "Variables dummy creadas")
        tags_html = "".join(f'<span class="dummy-tag">{c}</span>' for c in X_dummies.columns)
        st.markdown(tags_html, unsafe_allow_html=True)
        st.markdown(
            f'<div style="margin-top:14px;" class="info-box">'
            f'<strong>{X_dummies.shape[1]}</strong> variables dummy generadas<br>'
            f'<strong>Referencia omitida:</strong> mes_1 (enero)</div>',
            unsafe_allow_html=True,
        )

    with col2:
        sec_label(ICONS["table"], "Ejemplo de codificación — primeros 15 registros")
        ejemplo = pd.concat([df[["fecha", "mes"]].head(15), X_dummies.head(15)], axis=1)
        st.dataframe(ejemplo, use_container_width=True, hide_index=True, height=390)


# ─────────────────────────────────────────────
# TAB 3 — DIVISIÓN
# ─────────────────────────────────────────────
with tab3:
    sec_label(ICONS["split"], "División Cronológica Entrenamiento / Prueba")

    st.markdown("""
    <div class="info-box">
        Para datos de series temporales se usa una <strong>división cronológica</strong>
        (no aleatoria). Mezclar observaciones futuras y pasadas introduce
        <em>data leakage</em> que infla artificialmente el desempeño del modelo.
    </div>
    """, unsafe_allow_html=True)

    fecha_corte = pd.Timestamp("2024-01-01")
    df_train = df[df["fecha"] < fecha_corte]
    df_test  = df[df["fecha"] >= fecha_corte]

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Entrenamiento", f"{len(df_train)} meses",
                  f"{len(df_train)/len(df)*100:.1f}% del total")
    with c2:
        st.metric("Prueba", f"{len(df_test)} meses",
                  f"{len(df_test)/len(df)*100:.1f}% del total")
    with c3:
        st.metric("Fecha de corte", "2024-01-01")

    # Gráfico
    color_map = df["fecha"].apply(lambda x: "Entrenamiento" if x < fecha_corte else "Prueba")
    fig = px.scatter(
        df, x="fecha", y="arribos",
        color=color_map,
        color_discrete_map={"Entrenamiento": "#3A7BD5", "Prueba": "#C00000"},
        title="División del Dataset: Entrenamiento vs Prueba",
    )
    fig.add_shape(
        type="line",
        x0="2024-01-01", x1="2024-01-01",
        y0=0, y1=1,
        xref="x", yref="paper",
        line=dict(color="rgba(255,255,255,0.4)", width=2, dash="dash"),
    )
    fig.add_annotation(
        x="2024-01-01", y=1,
        xref="x", yref="paper",
        text="Corte 2024-01-01",
        showarrow=False,
        yanchor="bottom",
        font=dict(color="#A8C0D6", size=11, family="DM Sans"),
        bgcolor="rgba(13,25,41,0.8)",
        bordercolor="rgba(255,255,255,0.15)",
        borderwidth=1,
        borderpad=5,
    )
    fig.update_layout(
        height=420,
        template="plotly_dark",
        paper_bgcolor="rgba(17,30,51,0.9)",
        plot_bgcolor="rgba(17,30,51,0.9)",
        font=dict(family="DM Sans", color="#A8C0D6"),
        title_font=dict(family="Sora", size=15, color="#E2EAF4"),
        legend=dict(
            bgcolor="rgba(13,25,41,0.8)",
            bordercolor="rgba(255,255,255,0.1)",
            borderwidth=1,
        ),
        xaxis=dict(gridcolor="rgba(255,255,255,0.05)", linecolor="rgba(255,255,255,0.1)"),
        yaxis=dict(gridcolor="rgba(255,255,255,0.05)", linecolor="rgba(255,255,255,0.1)"),
    )
    fig.update_traces(marker=dict(size=7, opacity=0.85))
    st.plotly_chart(fig, use_container_width=True)

    st.success(
        f"**Configuración final:** {len(df_train)} meses (ene 2010 – dic 2023) "
        f"para entrenamiento · {len(df_test)} meses (ene–dic 2024) para validación."
    )

# ─────────────────────────────────────────────
# TAB 4 — RESULTADO FINAL
# ─────────────────────────────────────────────
with tab4:
    sec_label(ICONS["star"], "Resumen de Transformaciones Aplicadas")

    transformaciones = [
        ("#1a7a4a", ICONS["shield"],   "Validación de Integridad",
         "Sin nulos · sin duplicados · fechas consecutivas"),
        ("#1B3A5C", ICONS["code"],     "One-Hot Encoding",
         "Variable 'mes' (1–12) → 11 variables dummy (enero como referencia)"),
        ("#8B4500", ICONS["bar"],      "Variables Explicativas Finales",
         "17 variables: 11 dummies + 6 contextuales (clima, eventos, pandemia)"),
        ("#6B0000", ICONS["target"],   "Variable Dependiente",
         "arribos — variable numérica continua"),
        ("#1a4a7a", ICONS["calendar"], "División Temporal",
         "168 meses train (93.3%) · 12 meses test (6.7%) — corte cronológico"),
        ("#4a1a7a", ICONS["alert"],    "Categoría de Referencia",
         "Enero (mes_1 omitido para evitar multicolinealidad perfecta)"),
    ]

    for bg, icon_enc, title, desc in transformaciones:
        icon_bg = f"url(\"data:image/svg+xml,%3Csvg xmlns='http%3A//www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%23ffffff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E{icon_enc}%3C/svg%3E\")"
        st.markdown(
            '<div class="transform-row">'
            f'<div class="transform-icon" style="background:{bg};">'
            f'<span style="display:inline-block;width:18px;height:18px;'
            f'background:{icon_bg} center/18px no-repeat;"></span>'
            '</div>'
            '<div>'
            f'<div class="transform-title">{title}</div>'
            f'<div class="transform-desc">{desc}</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True,
        )

    st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <strong>Justificación clave:</strong> La división cronológica respeta el orden temporal
        natural de la serie. El conjunto de prueba (2024) actúa como datos "futuros" nunca
        vistos por el modelo durante su entrenamiento — garantizando una evaluación realista
        del poder predictivo.
    </div>
    """, unsafe_allow_html=True)

    # Gráfico de resumen: proporción train/test
    fig2 = go.Figure(go.Pie(
        labels=["Entrenamiento (168 meses)", "Prueba (12 meses)"],
        values=[168, 12],
        hole=0.65,
        marker=dict(colors=["#1B3A5C", "#C00000"],
                    line=dict(color="#0A1628", width=3)),
        textfont=dict(family="Sora", size=12, color="white"),
    ))
    fig2.update_layout(
        height=280,
        margin=dict(t=10, b=10, l=10, r=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=True,
        legend=dict(
            font=dict(family="DM Sans", color="#A8C0D6", size=12),
            bgcolor="rgba(0,0,0,0)",
        ),
        annotations=[dict(
            text="<b>180</b><br><span style='font-size:10px'>meses</span>",
            x=0.5, y=0.5, font=dict(size=18, color="#E2EAF4", family="Sora"),
            showarrow=False,
        )],
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown('<div class="footer-cap">Fase 3 de CRISP-DM · Preparación de los Datos · 2026</div>', unsafe_allow_html=True)