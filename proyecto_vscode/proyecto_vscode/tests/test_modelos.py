"""
Tests basicos del proyecto.
Verifica que las funciones principales se ejecutan sin errores.

Ejecucion:
    python -m pytest tests/test_modelos.py -v
"""

import os
import sys

import pandas as pd
import pytest

# Anadir el directorio del proyecto al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_dataset_existe():
    """Verifica que el archivo CSV del dataset esta presente."""
    ruta = "data/turismo_ayacucho_2010_2024.csv"
    assert os.path.exists(ruta), f"No se encuentra {ruta}"


def test_dataset_estructura():
    """Verifica que el dataset tenga la estructura esperada."""
    df = pd.read_csv("data/turismo_ayacucho_2010_2024.csv",
                     parse_dates=["fecha"])

    columnas_esperadas = {
        "fecha", "anio", "mes", "arribos", "semana_santa",
        "feriado_largo", "temperatura_c", "precipitacion_mm",
        "evento_cultural", "pandemia_covid",
    }
    assert set(df.columns) == columnas_esperadas, "Columnas no coinciden"
    assert len(df) == 180, f"Se esperaban 180 registros, hay {len(df)}"
    assert df["arribos"].min() > 0, "Hay arribos no positivos"


def test_fase3_devuelve_estructura():
    """Verifica que la fase 3 devuelva la estructura esperada."""
    from src.fase3_preparacion import ejecutar
    datos = ejecutar()

    assert "X_train" in datos
    assert "X_test" in datos
    assert "y_train" in datos
    assert "y_test" in datos
    assert len(datos["y_train"]) == 168
    assert len(datos["y_test"]) == 12


def test_fase4_ajusta_modelos():
    """Verifica que la fase 4 ajuste ambos modelos sin errores."""
    from src.fase3_preparacion import ejecutar as fase3
    from src.fase4_modelado import ejecutar as fase4

    datos = fase3()
    modelos = fase4(datos)

    assert "resultado_sarima" in modelos
    assert "pred_sarima" in modelos
    assert "modelo_rlm" in modelos
    assert "pred_rlm" in modelos
    assert len(modelos["pred_sarima"]) == 12
    assert len(modelos["pred_rlm"]) == 12


if __name__ == "__main__":
    print("Ejecutando tests basicos...\n")
    test_dataset_existe()
    print("[OK] test_dataset_existe")
    test_dataset_estructura()
    print("[OK] test_dataset_estructura")
    test_fase3_devuelve_estructura()
    print("[OK] test_fase3_devuelve_estructura")
    test_fase4_ajusta_modelos()
    print("[OK] test_fase4_ajusta_modelos")
    print("\nTodos los tests pasaron correctamente!")
