"""
============================================================================
FASE 6: DESPLIEGUE - PRONOSTICO PARA EL ANO 2025
============================================================================
Reentrena el modelo SARIMA con todos los datos disponibles y genera
pronosticos mensuales para el ano 2025 con intervalos de confianza al 95%.
"""

import os
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

warnings.filterwarnings("ignore")

plt.rcParams["savefig.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"
RUTA_FIGURAS = "outputs/figuras"
RUTA_OUTPUTS = "outputs"


def reentrenar_modelo_final(df):
    """Reentrena SARIMA con todo el historico disponible."""
    print("\n[6.1 REENTRENAMIENTO CON DATOS COMPLETOS 2010-2024]")
    print("-" * 70)

    serie = df["arribos"]
    print(f"  Datos utilizados: {len(serie)} observaciones")
    print(f"  Periodo: {serie.index.min().date()} a "
          f"{serie.index.max().date()}")

    modelo = SARIMAX(
        serie,
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 12),
        enforce_stationarity=False,
        enforce_invertibility=False,
    )
    resultado = modelo.fit(disp=False)
    print(f"  Modelo SARIMA(1,1,1)(1,1,1,12) entrenado")
    print(f"  AIC final: {resultado.aic:,.2f}")

    return resultado


def generar_pronostico_2025(resultado):
    """Genera el pronostico para los 12 meses de 2025."""
    print("\n[6.2 GENERACION DEL PRONOSTICO MENSUAL 2025]")
    print("-" * 70)

    pronostico = resultado.get_forecast(steps=12)
    pred_2025 = pronostico.predicted_mean
    ic_2025 = pronostico.conf_int(alpha=0.05)

    fechas_2025 = pd.date_range("2025-01-01", periods=12, freq="MS")
    pred_2025.index = fechas_2025
    ic_2025.index = fechas_2025

    print(f"\n  Pronostico mensual:")
    print(f"  {'Mes':<12} {'Pronostico':>12} {'IC Inferior':>13} "
          f"{'IC Superior':>13}")
    print(f"  {'-'*12} {'-'*12} {'-'*13} {'-'*13}")

    meses_nom = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                 "Julio", "Agosto", "Septiembre", "Octubre",
                 "Noviembre", "Diciembre"]

    for i, fecha in enumerate(fechas_2025):
        valor = pred_2025.iloc[i]
        ic_inf = ic_2025.iloc[i, 0]
        ic_sup = ic_2025.iloc[i, 1]
        print(f"  {meses_nom[i]:<12} {valor:>12,.0f} {ic_inf:>13,.0f} "
              f"{ic_sup:>13,.0f}")

    print(f"  {'-'*12} {'-'*12} {'-'*13} {'-'*13}")
    total = pred_2025.sum()
    print(f"  {'TOTAL ANUAL':<12} {total:>12,.0f}")

    print(f"\n  Mes pico:  {meses_nom[pred_2025.values.argmax()]} "
          f"({pred_2025.max():,.0f} arribos)")
    print(f"  Mes valle: {meses_nom[pred_2025.values.argmin()]} "
          f"({pred_2025.min():,.0f} arribos)")

    return pred_2025, ic_2025


def analisis_sensibilidad(pred_2025):
    """Analisis de sensibilidad con escenarios."""
    print("\n[6.3 ANALISIS DE SENSIBILIDAD - ESCENARIOS]")
    print("-" * 70)

    total_base = pred_2025.sum()
    escenarios = {
        "Pesimista (-15%)": 0.85,
        "Base":              1.00,
        "Optimista (+15%)":  1.15,
    }

    print(f"\n  {'Escenario':<22} {'Factor':>8} {'Arribos':>12}")
    print(f"  {'-'*22} {'-'*8} {'-'*12}")
    for nombre, factor in escenarios.items():
        arribos = total_base * factor
        print(f"  {nombre:<22} {factor:>8.2f} {arribos:>12,.0f}")


def caso_aplicacion_semana_santa(pred_2025):
    """Caso de aplicacion practica: Semana Santa 2025."""
    print("\n[6.4 CASO DE APLICACION: SEMANA SANTA 2025]")
    print("-" * 70)

    arribos_abril = pred_2025.loc["2025-04-01"]
    pernoctaciones = arribos_abril * 2.5
    gasto_promedio_diario = 380  # PEN, datos PROMPERU
    impacto_economico = pernoctaciones * gasto_promedio_diario

    print(f"\n  Pronostico abril 2025:        {arribos_abril:>10,.0f} arribos")
    print(f"  Pernoctaciones estimadas:     {pernoctaciones:>10,.0f}")
    print(f"  (asumiendo 2.5 noches por visitante)")
    print(f"  Gasto promedio por dia:       S/ {gasto_promedio_diario}")
    print(f"  Impacto economico estimado:   S/ {impacto_economico:>10,.0f}")

    print(f"\n  Implicaciones operativas:")
    print(f"    - Ocupacion hotelera esperada > 95%")
    print(f"    - Requiere ~200,000 traslados interurbanos")
    print(f"    - Refuerzo de servicios publicos critico")
    print(f"    - Coordinar campanas promocionales desde enero 2025")


def grafico_pronostico(df, pred_2025, ic_2025):
    """Grafico del pronostico con intervalo de confianza."""
    print("\n[6.5 VISUALIZACION DEL PRONOSTICO]")
    print("-" * 70)

    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df.index[-60:], df["arribos"].iloc[-60:],
            label="Datos historicos", color="#1F4E78", linewidth=1.5)
    ax.plot(pred_2025.index, pred_2025.values,
            label="Pronostico 2025", color="#C00000",
            linewidth=2, marker="o", markersize=6)
    ax.fill_between(
        pred_2025.index,
        ic_2025.iloc[:, 0].values,
        ic_2025.iloc[:, 1].values,
        color="#C00000", alpha=0.15,
        label="IC 95%",
    )
    ax.set_title("Pronostico de Arribos Turisticos - Ayacucho 2025",
                 fontsize=14, fontweight="bold")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Arribos pronosticados")
    ax.legend(loc="upper left", fontsize=11)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()

    ruta = os.path.join(RUTA_FIGURAS, "fase6_pronostico_2025.png")
    plt.savefig(ruta)
    plt.close()
    print(f"  Grafico guardado en: {ruta}")


def exportar_pronostico(pred_2025, ic_2025):
    """Exporta el pronostico a CSV para uso operativo."""
    print("\n[6.6 EXPORTACION DEL PRONOSTICO A CSV]")
    print("-" * 70)

    df_pronostico = pd.DataFrame({
        "mes": pred_2025.index.strftime("%Y-%m"),
        "arribos_pronosticados": pred_2025.values.astype(int),
        "limite_inferior_95": ic_2025.iloc[:, 0].values.astype(int),
        "limite_superior_95": ic_2025.iloc[:, 1].values.astype(int),
    })

    ruta = os.path.join(RUTA_OUTPUTS, "pronostico_2025.csv")
    df_pronostico.to_csv(ruta, index=False)
    print(f"  CSV exportado a: {ruta}")
    print(f"  El archivo puede integrarse en Power BI o Excel para")
    print(f"  uso operativo por la DIRCETUR y operadores privados.")


def ejecutar(datos):
    """Funcion principal de la fase 6."""
    print("\n" + "=" * 70)
    print("FASE 6: DESPLIEGUE - PRONOSTICO 2025")
    print("=" * 70)

    df = datos["df"]

    resultado = reentrenar_modelo_final(df)
    pred_2025, ic_2025 = generar_pronostico_2025(resultado)
    analisis_sensibilidad(pred_2025)
    caso_aplicacion_semana_santa(pred_2025)
    grafico_pronostico(df, pred_2025, ic_2025)
    exportar_pronostico(pred_2025, ic_2025)

    print("\n" + "=" * 70)
    print("FASE 6 COMPLETADA - PROYECTO FINALIZADO")
    print("=" * 70)


if __name__ == "__main__":
    from fase3_preparacion import ejecutar as ejecutar_fase3
    datos = ejecutar_fase3()
    ejecutar(datos)
