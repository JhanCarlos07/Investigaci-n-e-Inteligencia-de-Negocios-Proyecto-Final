"""
============================================================================
FASE 2: COMPRENSION DE LOS DATOS
============================================================================
Carga, exploracion y analisis descriptivo del dataset.
Genera estadisticas descriptivas, matriz de correlacion y visualizaciones.
"""

import os
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

warnings.filterwarnings("ignore")

# Configuracion global
plt.rcParams["figure.figsize"] = (12, 5)
plt.rcParams["font.size"] = 10
plt.rcParams["savefig.dpi"] = 150
plt.rcParams["savefig.bbox"] = "tight"

# Rutas
RUTA_DATOS = "data/turismo_ayacucho_2010_2024.csv"
RUTA_FIGURAS = "outputs/figuras"


def cargar_dataset():
    """Carga el dataset desde el CSV y devuelve un DataFrame ordenado."""
    print("\n[2.1 CARGA DEL DATASET]")
    print("-" * 70)

    if not os.path.exists(RUTA_DATOS):
        raise FileNotFoundError(
            f"No se encuentra el archivo {RUTA_DATOS}. "
            "Verifica la estructura del proyecto."
        )

    df = pd.read_csv(RUTA_DATOS, parse_dates=["fecha"])
    df = df.sort_values("fecha").reset_index(drop=True)

    print(f"  Archivo: {RUTA_DATOS}")
    print(f"  Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
    print(f"  Periodo: {df['fecha'].min().date()} a {df['fecha'].max().date()}")
    print(f"  Variables: {list(df.columns)}")
    return df


def estadisticas_descriptivas(df):
    """Calcula y muestra estadisticas descriptivas completas."""
    print("\n[2.2 ESTADISTICAS DESCRIPTIVAS - Variable: arribos]")
    print("-" * 70)

    arribos = df["arribos"]
    stats = {
        "N (observaciones)": len(arribos),
        "Media": arribos.mean(),
        "Mediana": arribos.median(),
        "Desviacion estandar": arribos.std(),
        "Coef. de variacion (%)": (arribos.std() / arribos.mean()) * 100,
        "Minimo": arribos.min(),
        "Maximo": arribos.max(),
        "Q1": arribos.quantile(0.25),
        "Q3": arribos.quantile(0.75),
        "Rango intercuartilico": arribos.quantile(0.75) - arribos.quantile(0.25),
        "Asimetria (skewness)": arribos.skew(),
        "Curtosis": arribos.kurtosis(),
    }

    for nombre, valor in stats.items():
        if isinstance(valor, float):
            print(f"  {nombre:<28} {valor:>15,.2f}")
        else:
            print(f"  {nombre:<28} {valor:>15,}")

    print("\n  Verificacion de valores faltantes:")
    nulos = df.isnull().sum().sum()
    print(f"  Total de valores nulos: {nulos}")


def matriz_correlacion(df):
    """Calcula la matriz de correlacion de Pearson."""
    print("\n[2.3 MATRIZ DE CORRELACION (Pearson)]")
    print("-" * 70)
    cols = [
        "arribos",
        "mes",
        "semana_santa",
        "feriado_largo",
        "temperatura_c",
        "precipitacion_mm",
        "evento_cultural",
        "pandemia_covid",
    ]
    corr = df[cols].corr()

    print("\n  Correlaciones con 'arribos':")
    correlaciones = corr["arribos"].drop("arribos").sort_values(
        key=abs, ascending=False
    )
    for var, val in correlaciones.items():
        signo = "+" if val >= 0 else ""
        fuerza = (
            "fuerte"
            if abs(val) > 0.5
            else "moderada"
            if abs(val) > 0.3
            else "debil"
        )
        print(f"    {var:<22} {signo}{val:>6.3f}   ({fuerza})")

    return corr


def grafico_serie_temporal(df):
    """Genera el grafico de la serie temporal completa."""
    print("\n[2.4 VISUALIZACION: Serie temporal]")
    print("-" * 70)

    fig, ax = plt.subplots(figsize=(14, 5))
    ax.plot(df["fecha"], df["arribos"], color="#1F4E78", linewidth=1.5)
    ax.fill_between(df["fecha"], df["arribos"], alpha=0.3, color="#1F4E78")
    ax.axvspan(
        pd.Timestamp("2020-03-01"),
        pd.Timestamp("2021-06-01"),
        alpha=0.2,
        color="red",
        label="Pandemia COVID-19",
    )
    ax.set_title(
        "Arribos Mensuales a Hospedajes - Ayacucho (2010-2024)",
        fontsize=13,
        fontweight="bold",
    )
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Numero de arribos")
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()

    ruta = os.path.join(RUTA_FIGURAS, "fase2_serie_temporal.png")
    plt.savefig(ruta)
    plt.close()
    print(f"  Grafico guardado en: {ruta}")


def grafico_estacionalidad(df):
    """Genera el grafico de patron estacional (promedio mensual)."""
    print("\n[2.5 VISUALIZACION: Patron estacional]")
    print("-" * 70)

    df_prepand = df[~df["pandemia_covid"].astype(bool)]
    prom_mensual = df_prepand.groupby("mes")["arribos"].mean()

    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
             "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    colores = [
        "#C00000" if v > prom_mensual.mean() else "#1F4E78"
        for v in prom_mensual.values
    ]

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(meses, prom_mensual.values, color=colores, edgecolor="black",
           linewidth=0.5)
    ax.axhline(
        prom_mensual.mean(),
        color="gray",
        linestyle="--",
        label=f"Media: {prom_mensual.mean():,.0f}",
    )
    ax.set_title(
        "Promedio Mensual de Arribos (sin pandemia)",
        fontsize=13,
        fontweight="bold",
    )
    ax.set_ylabel("Promedio de arribos")
    ax.legend()
    plt.tight_layout()

    ruta = os.path.join(RUTA_FIGURAS, "fase2_estacionalidad.png")
    plt.savefig(ruta)
    plt.close()
    print(f"  Grafico guardado en: {ruta}")

    print("\n  Meses con mayor afluencia (sin pandemia):")
    for mes, val in prom_mensual.sort_values(ascending=False).head(3).items():
        print(f"    Mes {mes:2d} ({meses[mes-1]}): {val:>10,.0f} arribos")


def heatmap_correlacion(corr):
    """Genera un heatmap de la matriz de correlacion."""
    print("\n[2.6 VISUALIZACION: Heatmap de correlaciones]")
    print("-" * 70)

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="RdBu_r",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.8},
        ax=ax,
    )
    ax.set_title(
        "Matriz de Correlacion (Pearson)", fontsize=13, fontweight="bold"
    )
    plt.tight_layout()

    ruta = os.path.join(RUTA_FIGURAS, "fase2_heatmap_correlacion.png")
    plt.savefig(ruta)
    plt.close()
    print(f"  Grafico guardado en: {ruta}")


def descomposicion_estacional(df):
    """Aplica descomposicion aditiva de la serie temporal."""
    print("\n[2.7 DESCOMPOSICION ESTACIONAL]")
    print("-" * 70)

    serie = df.set_index("fecha")["arribos"]
    descomp = seasonal_decompose(serie, model="additive", period=12)

    fig, axes = plt.subplots(4, 1, figsize=(14, 10))
    descomp.observed.plot(ax=axes[0], color="#1F4E78")
    axes[0].set_title("Serie Observada")
    descomp.trend.plot(ax=axes[1], color="#C00000")
    axes[1].set_title("Tendencia")
    descomp.seasonal.plot(ax=axes[2], color="#70AD47")
    axes[2].set_title("Estacionalidad")
    descomp.resid.plot(ax=axes[3], color="gray")
    axes[3].set_title("Residuos")
    for ax in axes:
        ax.grid(True, alpha=0.3)
    plt.tight_layout()

    ruta = os.path.join(RUTA_FIGURAS, "fase2_descomposicion.png")
    plt.savefig(ruta)
    plt.close()
    print(f"  Grafico guardado en: {ruta}")


def test_estacionariedad(df):
    """Ejecuta el test de Dickey-Fuller aumentado."""
    print("\n[2.8 TEST DE ESTACIONARIEDAD (Dickey-Fuller aumentado)]")
    print("-" * 70)

    serie = df["arribos"]

    for nombre, s in [
        ("Serie original", serie),
        ("Primera diferencia", serie.diff().dropna()),
        ("Diferencia estacional (lag=12)", serie.diff().diff(12).dropna()),
    ]:
        result = adfuller(s, autolag="AIC")
        print(f"\n  {nombre}:")
        print(f"    Estadistico ADF: {result[0]:>8.4f}")
        print(f"    p-value:         {result[1]:>8.6f}")
        if result[1] < 0.05:
            print(f"    -> Serie ESTACIONARIA (rechaza H0 al 5%)")
        else:
            print(f"    -> Serie NO estacionaria (requiere diferenciacion)")


def ejecutar():
    """Funcion principal de la fase 2."""
    print("\n" + "=" * 70)
    print("FASE 2: COMPRENSION DE LOS DATOS")
    print("=" * 70)

    df = cargar_dataset()
    estadisticas_descriptivas(df)
    corr = matriz_correlacion(df)
    grafico_serie_temporal(df)
    grafico_estacionalidad(df)
    heatmap_correlacion(corr)
    descomposicion_estacional(df)
    test_estacionariedad(df)

    print("\n" + "=" * 70)
    print("FASE 2 COMPLETADA - Graficos guardados en outputs/figuras/")
    print("=" * 70)

    return df


if __name__ == "__main__":
    ejecutar()
