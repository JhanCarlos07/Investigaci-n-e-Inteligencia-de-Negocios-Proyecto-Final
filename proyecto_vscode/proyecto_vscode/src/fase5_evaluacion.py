"""
============================================================================
FASE 5: EVALUACION
============================================================================
Calculo de metricas RMSE, MAE, MAPE, R^2 y MASE para ambos modelos.
Diagnostico de residuos del SARIMA.
"""

import json
import os
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (mean_absolute_error, mean_squared_error,
                             r2_score)
from statsmodels.stats.diagnostic import acorr_ljungbox

warnings.filterwarnings("ignore")

plt.rcParams["savefig.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"
RUTA_FIGURAS = "outputs/figuras"
RUTA_OUTPUTS = "outputs"


def calcular_metricas(y_real, y_pred, nombre, train_values=None):
    """Calcula todas las metricas de evaluacion para un modelo."""
    rmse = np.sqrt(mean_squared_error(y_real, y_pred))
    mae = mean_absolute_error(y_real, y_pred)
    r2 = r2_score(y_real, y_pred)
    mape = np.mean(np.abs((y_real - y_pred) / y_real)) * 100

    mase = None
    if train_values is not None:
        naive_diff = np.abs(np.diff(train_values))
        denom = naive_diff.mean()
        if denom > 0:
            mase = np.abs(y_real - y_pred).mean() / denom

    return {
        "modelo": nombre,
        "RMSE": rmse,
        "MAE": mae,
        "MAPE": mape,
        "R2": r2,
        "MASE": mase,
    }


def mostrar_metricas(metricas):
    """Imprime metricas en formato tabla."""
    print(f"\n  {metricas['modelo']}")
    print(f"  {'-' * len(metricas['modelo'])}")
    print(f"    RMSE:  {metricas['RMSE']:>12,.2f}")
    print(f"    MAE:   {metricas['MAE']:>12,.2f}")
    print(f"    MAPE:  {metricas['MAPE']:>11.2f} %")
    print(f"    R^2:   {metricas['R2']:>12.4f}")
    if metricas["MASE"] is not None:
        print(f"    MASE:  {metricas['MASE']:>12.4f}")


def comparar_modelos(y_test, pred_sarima, pred_rlm, serie_train):
    """Compara metricas de ambos modelos."""
    print("\n[5.1 CALCULO DE METRICAS - CONJUNTO DE PRUEBA 2024]")
    print("-" * 70)

    train_values = serie_train.values

    metricas_sarima = calcular_metricas(
        y_test, pred_sarima.values,
        "SARIMA(1,1,1)(1,1,1,12)",
        train_values=train_values,
    )
    metricas_rlm = calcular_metricas(
        y_test, pred_rlm,
        "Regresion Lineal Multiple",
        train_values=train_values,
    )

    mostrar_metricas(metricas_sarima)
    mostrar_metricas(metricas_rlm)

    print("\n[5.2 COMPARACION DE DESEMPENO]")
    print("-" * 70)
    mejora_rmse = ((metricas_rlm["RMSE"] - metricas_sarima["RMSE"])
                   / metricas_rlm["RMSE"] * 100)
    mejora_mae = ((metricas_rlm["MAE"] - metricas_sarima["MAE"])
                  / metricas_rlm["MAE"] * 100)
    print(f"  SARIMA reduce el RMSE en {mejora_rmse:.1f}% respecto a regresion")
    print(f"  SARIMA reduce el MAE en  {mejora_mae:.1f}% respecto a regresion")
    print(f"  Cumplimiento del criterio MAPE < 20%: "
          f"{'SI' if metricas_sarima['MAPE'] < 20 else 'NO'}")
    print(f"  SARIMA supera al naive estacional (MASE<1): "
          f"{'SI' if metricas_sarima['MASE'] < 1 else 'NO'}")

    return metricas_sarima, metricas_rlm


def diagnostico_residuos(resultado_sarima):
    """Diagnostico de residuos del modelo SARIMA."""
    print("\n[5.3 DIAGNOSTICO DE RESIDUOS DEL SARIMA]")
    print("-" * 70)

    residuos = resultado_sarima.resid

    print("\n  Test Ljung-Box (independencia de residuos):")
    for lag in [10, 20, 30]:
        try:
            lb = acorr_ljungbox(residuos, lags=[lag], return_df=True)
            stat = lb["lb_stat"].iloc[0]
            pval = lb["lb_pvalue"].iloc[0]
            concl = "Ruido blanco (OK)" if pval > 0.05 else "Autocorrelacion!"
            print(f"    lag={lag:>2}: estadistico={stat:>7.3f}, "
                  f"p-value={pval:.4f} -> {concl}")
        except Exception as e:
            print(f"    lag={lag}: Error - {e}")

    print(f"\n  Estadisticas de los residuos:")
    print(f"    Media:               {residuos.mean():>10,.2f}")
    print(f"    Desviacion estandar: {residuos.std():>10,.2f}")
    print(f"    Asimetria:           {residuos.skew():>10.4f}")
    print(f"    Curtosis:            {residuos.kurtosis():>10.4f}")


def grafico_errores(y_test, pred_sarima, pred_rlm, fechas_test):
    """Grafico de errores absolutos mes a mes."""
    print("\n[5.4 VISUALIZACION DE ERRORES MES A MES]")
    print("-" * 70)

    err_sarima = np.abs(y_test - pred_sarima.values)
    err_rlm = np.abs(y_test - pred_rlm)

    fig, ax = plt.subplots(figsize=(12, 5))
    x = np.arange(len(y_test))
    ancho = 0.35
    ax.bar(x - ancho/2, err_sarima, ancho, label="SARIMA",
           color="#C00000", edgecolor="black", linewidth=0.3)
    ax.bar(x + ancho/2, err_rlm, ancho, label="Regresion",
           color="#FFC000", edgecolor="black", linewidth=0.3)
    ax.set_xticks(x)
    ax.set_xticklabels(
        [pd.Timestamp(f).strftime("%Y-%m") for f in fechas_test],
        rotation=45
    )
    ax.set_ylabel("Error absoluto")
    ax.set_xlabel("Mes")
    ax.set_title("Error Absoluto Mensual por Modelo",
                 fontsize=13, fontweight="bold")
    ax.legend()
    ax.grid(True, alpha=0.3, axis="y")
    plt.tight_layout()

    ruta = os.path.join(RUTA_FIGURAS, "fase5_errores_mensuales.png")
    plt.savefig(ruta)
    plt.close()
    print(f"  Grafico guardado en: {ruta}")


def guardar_metricas(metricas_sarima, metricas_rlm):
    """Guarda las metricas en JSON para uso posterior."""
    print("\n[5.5 EXPORTACION DE METRICAS]")
    print("-" * 70)

    metricas = {
        "SARIMA": {
            "RMSE": float(metricas_sarima["RMSE"]),
            "MAE": float(metricas_sarima["MAE"]),
            "MAPE": float(metricas_sarima["MAPE"]),
            "R2": float(metricas_sarima["R2"]),
            "MASE": float(metricas_sarima["MASE"]) if metricas_sarima["MASE"] else None,
        },
        "Regresion_Multiple": {
            "RMSE": float(metricas_rlm["RMSE"]),
            "MAE": float(metricas_rlm["MAE"]),
            "MAPE": float(metricas_rlm["MAPE"]),
            "R2": float(metricas_rlm["R2"]),
            "MASE": float(metricas_rlm["MASE"]) if metricas_rlm["MASE"] else None,
        }
    }

    ruta = os.path.join(RUTA_OUTPUTS, "metricas.json")
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(metricas, f, indent=2, ensure_ascii=False)
    print(f"  Metricas exportadas a: {ruta}")


def ejecutar(datos, modelos):
    """Funcion principal de la fase 5."""
    print("\n" + "=" * 70)
    print("FASE 5: EVALUACION")
    print("=" * 70)

    metricas_sarima, metricas_rlm = comparar_modelos(
        datos["y_test"],
        modelos["pred_sarima"],
        modelos["pred_rlm"],
        datos["serie_train"],
    )

    diagnostico_residuos(modelos["resultado_sarima"])

    grafico_errores(
        datos["y_test"],
        modelos["pred_sarima"],
        modelos["pred_rlm"],
        datos["serie_test"].index,
    )

    guardar_metricas(metricas_sarima, metricas_rlm)

    print("\n" + "=" * 70)
    print("FASE 5 COMPLETADA")
    print("=" * 70)

    return metricas_sarima, metricas_rlm


if __name__ == "__main__":
    from fase3_preparacion import ejecutar as ejecutar_fase3
    from fase4_modelado import ejecutar as ejecutar_fase4
    datos = ejecutar_fase3()
    modelos = ejecutar_fase4(datos)
    ejecutar(datos, modelos)
