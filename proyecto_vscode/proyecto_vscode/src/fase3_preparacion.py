"""
============================================================================
FASE 3: PREPARACION DE LOS DATOS
============================================================================
Codificacion de variables categoricas, generacion de variables derivadas,
y division en conjuntos de entrenamiento y prueba.
"""

import os

import pandas as pd

RUTA_DATOS = "data/turismo_ayacucho_2010_2024.csv"
FECHA_CORTE = "2024-01-01"


def cargar_y_preparar():
    """Carga el dataset, aplica one-hot encoding y divide en train/test."""
    print("\n" + "=" * 70)
    print("FASE 3: PREPARACION DE LOS DATOS")
    print("=" * 70)

    print("\n[3.1 CARGA DEL DATASET]")
    print("-" * 70)
    df = pd.read_csv(RUTA_DATOS, parse_dates=["fecha"])
    df = df.sort_values("fecha").set_index("fecha")
    print(f"  Registros cargados: {len(df)}")

    print("\n[3.2 VERIFICACION DE CALIDAD]")
    print("-" * 70)
    nulos = df.isnull().sum()
    print(f"  Valores nulos por columna:")
    for col, n in nulos.items():
        print(f"    {col:<22} {n}")
    duplicados = df.duplicated().sum()
    print(f"  Registros duplicados: {duplicados}")

    print("\n[3.3 ONE-HOT ENCODING DE LA VARIABLE MES]")
    print("-" * 70)
    X = pd.get_dummies(df["mes"], prefix="mes", drop_first=True).astype(int)
    print(f"  Variable 'mes' transformada en {X.shape[1]} variables dummy")
    print(f"  Categoria de referencia: enero (mes_1, omitida)")
    print(f"  Columnas dummy generadas: {list(X.columns)}")

    print("\n[3.4 INCORPORACION DE VARIABLES EXPLICATIVAS]")
    print("-" * 70)
    X["semana_santa"] = df["semana_santa"].values
    X["feriado_largo"] = df["feriado_largo"].values
    X["temperatura_c"] = df["temperatura_c"].values
    X["precipitacion_mm"] = df["precipitacion_mm"].values
    X["evento_cultural"] = df["evento_cultural"].values
    X["pandemia_covid"] = df["pandemia_covid"].values
    print(f"  Total de variables explicativas: {X.shape[1]}")
    print(f"  Variable dependiente (Y): arribos")

    print("\n[3.5 DIVISION TRAIN / TEST]")
    print("-" * 70)
    print(f"  Criterio: division temporal (no aleatoria)")
    print(f"  Fecha de corte: {FECHA_CORTE}")

    train_mask = df.index < FECHA_CORTE
    test_mask = df.index >= FECHA_CORTE

    X_train = X[train_mask]
    X_test = X[test_mask]
    y_train = df.loc[train_mask, "arribos"].values
    y_test = df.loc[test_mask, "arribos"].values
    serie_train = df.loc[train_mask, "arribos"]
    serie_test = df.loc[test_mask, "arribos"]

    print(f"  Entrenamiento: {len(y_train)} meses "
          f"({serie_train.index.min().date()} a "
          f"{serie_train.index.max().date()})")
    print(f"  Prueba:        {len(y_test)} meses "
          f"({serie_test.index.min().date()} a "
          f"{serie_test.index.max().date()})")
    print(f"  Proporcion:    {len(y_train)/len(X)*100:.1f}% train / "
          f"{len(y_test)/len(X)*100:.1f}% test")

    print("\n" + "=" * 70)
    print("FASE 3 COMPLETADA")
    print("=" * 70)

    return {
        "df": df,
        "X": X,
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
        "serie_train": serie_train,
        "serie_test": serie_test,
    }


def ejecutar():
    """Funcion principal de la fase 3."""
    return cargar_y_preparar()


if __name__ == "__main__":
    ejecutar()
