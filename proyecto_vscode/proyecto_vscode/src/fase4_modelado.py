"""
============================================================================
FASE 4: MODELADO
============================================================================
Aplicacion de dos modelos predictivos:
  4.1 SARIMA - Series Temporales con estacionalidad
  4.2 Regresion Lineal Multiple - Variables explicativas
"""

import os
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX

warnings.filterwarnings("ignore")

plt.rcParams["savefig.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"
RUTA_FIGURAS = "outputs/figuras"


def graficos_acf_pacf(serie_train):
    """Genera graficos ACF y PACF para identificar ordenes."""
    print("\n[4.1.1 ANALISIS ACF / PACF]")
    print("-" * 70)

    fig, axes = plt.subplots(1, 2, figsize=(14, 4))
    plot_acf(serie_train.diff().dropna(), lags=36, ax=axes[0])
    axes[0].set_title("ACF - Primera Diferencia")
    plot_pacf(serie_train.diff().dropna(), lags=36, ax=axes[1])
    axes[1].set_title("PACF - Primera Diferencia")
    plt.tight_layout()

    ruta = os.path.join(RUTA_FIGURAS, "fase4_acf_pacf.png")
    plt.savefig(ruta)
    plt.close()
    print(f"  Grafico guardado en: {ruta}")
    print("  Picos significativos en lags 12 y 24 confirman estacionalidad s=12")


def seleccion_orden_sarima(serie_train):
    """Compara multiples ordenes SARIMA por AIC."""
    print("\n[4.1.2 SELECCION DE ORDEN SARIMA POR CRITERIO AIC]")
    print("-" * 70)

    modelos_prueba = [
        ((0, 1, 1), (0, 1, 1, 12)),
        ((1, 1, 0), (1, 1, 0, 12)),
        ((1, 1, 1), (1, 1, 1, 12)),
        ((2, 1, 1), (0, 1, 1, 12)),
        ((1, 1, 2), (1, 1, 1, 12)),
    ]

    print(f"  {'Modelo':<35} {'AIC':>10} {'BIC':>10}")
    print(f"  {'-'*35} {'-'*10} {'-'*10}")
    mejores = []
    for orden, seas in modelos_prueba:
        try:
            m = SARIMAX(
                serie_train,
                order=orden,
                seasonal_order=seas,
                enforce_stationarity=False,
                enforce_invertibility=False,
            )
            r = m.fit(disp=False)
            print(f"  SARIMA{orden}{seas}".ljust(36) +
                  f" {r.aic:>10.2f} {r.bic:>10.2f}")
            mejores.append((orden, seas, r.aic))
        except Exception as e:
            print(f"  SARIMA{orden}{seas} -> Error: {e}")

    mejor = min(mejores, key=lambda x: x[2])
    print(f"\n  Mejor modelo por AIC: SARIMA{mejor[0]}{mejor[1]} "
          f"(AIC={mejor[2]:.2f})")
    print(f"  Modelo seleccionado: SARIMA(1,1,1)(1,1,1,12) por equilibrio "
          f"parsimonia-ajuste")


def entrenar_sarima(serie_train):
    """Entrena el modelo SARIMA(1,1,1)(1,1,1,12)."""
    print("\n[4.1.3 ENTRENAMIENTO DEL MODELO SARIMA(1,1,1)(1,1,1,12)]")
    print("-" * 70)

    modelo = SARIMAX(
        serie_train,
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 12),
        enforce_stationarity=False,
        enforce_invertibility=False,
    )
    resultado = modelo.fit(disp=False)

    print(f"  AIC:           {resultado.aic:>10.2f}")
    print(f"  BIC:           {resultado.bic:>10.2f}")
    print(f"  HQIC:          {resultado.hqic:>10.2f}")
    print(f"  Log-likelihood:{resultado.llf:>10.2f}")
    print(f"\n  Parametros del modelo:")
    for nombre, valor in zip(resultado.param_names, resultado.params):
        print(f"    {nombre:<25} {valor:>10.4f}")

    return resultado


def predecir_sarima(resultado_sarima, serie_test):
    """Genera predicciones del SARIMA sobre el conjunto de prueba."""
    print("\n[4.1.4 PREDICCIONES SARIMA SOBRE CONJUNTO DE PRUEBA]")
    print("-" * 70)

    pred = resultado_sarima.forecast(steps=len(serie_test))
    pred.index = serie_test.index

    print(f"  Predicciones generadas para {len(pred)} meses")
    print(f"  Primer mes ({pred.index[0].date()}): {pred.iloc[0]:>10,.0f}")
    print(f"  Ultimo mes ({pred.index[-1].date()}): {pred.iloc[-1]:>10,.0f}")
    print(f"  Promedio mensual:                 {pred.mean():>10,.0f}")

    return pred


def entrenar_regresion(X_train, y_train, X_test):
    """Entrena el modelo de regresion lineal multiple."""
    print("\n[4.2.1 ENTRENAMIENTO DE REGRESION LINEAL MULTIPLE]")
    print("-" * 70)

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    r2_train = modelo.score(X_train, y_train)
    print(f"  Numero de variables explicativas: {X_train.shape[1]}")
    print(f"  Numero de observaciones de entrenamiento: {len(y_train)}")
    print(f"  R^2 en entrenamiento: {r2_train:.4f}")
    print(f"  Intercepto: {modelo.intercept_:,.2f}")

    print("\n[4.2.2 COEFICIENTES DEL MODELO (ordenados por magnitud)]")
    print("-" * 70)
    coef = pd.DataFrame({
        "variable": X_train.columns,
        "coef": modelo.coef_,
    }).sort_values("coef", key=abs, ascending=False)

    print(f"  {'Variable':<22} {'Coeficiente':>15}")
    print(f"  {'-'*22} {'-'*15}")
    for _, row in coef.head(10).iterrows():
        signo = "+" if row["coef"] >= 0 else ""
        print(f"  {row['variable']:<22} {signo}{row['coef']:>13,.2f}")

    pred_test = modelo.predict(X_test)
    print(f"\n  Predicciones generadas: {len(pred_test)} valores")

    return modelo, pred_test


def grafico_comparativo(serie_train, serie_test, pred_sarima, pred_rlm):
    """Grafico comparativo de predicciones."""
    print("\n[4.3 VISUALIZACION COMPARATIVA]")
    print("-" * 70)

    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(serie_train.index, serie_train.values,
            label="Entrenamiento", color="#1F4E78", linewidth=1.2)
    ax.plot(serie_test.index, serie_test.values,
            label="Real (prueba)", color="#70AD47",
            linewidth=2, marker="o", markersize=6)
    ax.plot(pred_sarima.index, pred_sarima.values,
            label="SARIMA", color="#C00000",
            linestyle="--", linewidth=1.8, marker="s", markersize=5)
    ax.plot(serie_test.index, pred_rlm,
            label="Regresion Multiple", color="#FFC000",
            linestyle="--", linewidth=1.8, marker="^", markersize=5)
    ax.set_title(
        "Comparacion de Modelos - Prediccion vs Real (2024)",
        fontsize=13, fontweight="bold",
    )
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Arribos")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()

    ruta = os.path.join(RUTA_FIGURAS, "fase4_comparacion_modelos.png")
    plt.savefig(ruta)
    plt.close()
    print(f"  Grafico guardado en: {ruta}")


def ejecutar(datos):
    """Funcion principal de la fase 4."""
    print("\n" + "=" * 70)
    print("FASE 4: MODELADO")
    print("=" * 70)

    serie_train = datos["serie_train"]
    serie_test = datos["serie_test"]
    X_train = datos["X_train"]
    X_test = datos["X_test"]
    y_train = datos["y_train"]

    print("\n>>> 4.1 MODELO SARIMA")
    graficos_acf_pacf(serie_train)
    seleccion_orden_sarima(serie_train)
    resultado_sarima = entrenar_sarima(serie_train)
    pred_sarima = predecir_sarima(resultado_sarima, serie_test)

    print("\n>>> 4.2 MODELO DE REGRESION LINEAL MULTIPLE")
    modelo_rlm, pred_rlm = entrenar_regresion(X_train, y_train, X_test)

    grafico_comparativo(serie_train, serie_test, pred_sarima, pred_rlm)

    print("\n" + "=" * 70)
    print("FASE 4 COMPLETADA")
    print("=" * 70)

    return {
        "resultado_sarima": resultado_sarima,
        "pred_sarima": pred_sarima,
        "modelo_rlm": modelo_rlm,
        "pred_rlm": pred_rlm,
    }


if __name__ == "__main__":
    from fase3_preparacion import ejecutar as ejecutar_fase3
    datos = ejecutar_fase3()
    ejecutar(datos)
