"""
============================================================================
FASE 1: COMPRENSION DEL NEGOCIO
============================================================================
Proyecto: Prediccion de la Cantidad de Turistas en Ayacucho
Curso: Investigacion e Inteligencia de Negocios
Escuela Superior La Pontificia - Ayacucho

Esta fase define el contexto, los objetivos y los criterios de exito
del proyecto de analitica predictiva.
"""


def mostrar_contexto_negocio():
    """Muestra el contexto del negocio y la justificacion del proyecto."""
    print("\n" + "=" * 70)
    print("FASE 1: COMPRENSION DEL NEGOCIO")
    print("=" * 70)

    print("\n[CONTEXTO]")
    print("-" * 70)
    print(
        "La region Ayacucho recibe flujos turisticos estacionales asociados\n"
        "a festividades religiosas, eventos culturales y condiciones\n"
        "climaticas. La Semana Santa ayacuchana es reconocida como una de\n"
        "las celebraciones mas importantes del Peru y America Latina,\n"
        "generando picos de demanda hotelera, de transporte y servicios."
    )

    print("\n[PROBLEMA DE NEGOCIO]")
    print("-" * 70)
    print(
        "Las instituciones de gestion turistica (DIRCETUR Ayacucho) y los\n"
        "operadores privados no cuentan con un modelo cuantitativo que les\n"
        "permita anticipar con precision la cantidad de turistas esperados\n"
        "en periodos determinados. Esto genera problemas como:\n"
        "  - Insuficiente oferta hotelera en periodos de alta demanda\n"
        "  - Subutilizacion de recursos en temporadas bajas\n"
        "  - Ausencia de estrategias de marketing focalizadas"
    )

    print("\n[CIFRAS RELEVANTES MINCETUR 2023]")
    print("-" * 70)
    print("  - Arribos 2023: 457,800 (+20.4% vs 2022)")
    print("  - Solo 65.4% de los niveles pre-pandemia 2019")
    print("  - 98.7% turistas nacionales / 1.3% extranjeros")
    print("  - Reduccion del 21.9% en oferta hotelera 2019-2024")


def mostrar_objetivos():
    """Muestra los objetivos generales y especificos del proyecto."""
    print("\n[OBJETIVO GENERAL]")
    print("-" * 70)
    print(
        "Desarrollar un modelo predictivo de la cantidad de turistas en\n"
        "Ayacucho utilizando series temporales (SARIMA) y regresion\n"
        "multiple, incorporando variables de festividades, mes, clima y\n"
        "eventos culturales, bajo la metodologia CRISP-DM."
    )

    print("\n[OBJETIVOS ESPECIFICOS]")
    print("-" * 70)
    objetivos = [
        "Analizar el conjunto de datos historicos 2010-2024",
        "Preparar las variables explicativas",
        "Aplicar modelos SARIMA y regresion multiple",
        "Evaluar el desempeno con RMSE, MAE, MAPE y R^2",
        "Interpretar resultados para la toma de decisiones",
    ]
    for i, obj in enumerate(objetivos, 1):
        print(f"  {i}. {obj}")


def mostrar_hipotesis():
    """Presenta las hipotesis de investigacion."""
    print("\n[HIPOTESIS DE INVESTIGACION]")
    print("-" * 70)
    print(
        "H_G: Las variables de festividades, mes, clima, eventos y pandemia\n"
        "     permiten predecir significativamente los arribos con MAPE<20%.\n"
        "\n"
        "H_1: La serie temporal presenta estacionalidad anual significativa.\n"
        "H_2: Semana Santa tiene efecto positivo significativo (p<0.05).\n"
        "H_3: La pandemia produjo reduccion significativa en el flujo.\n"
        "H_4: SARIMA supera a la regresion multiple en desempeno predictivo.\n"
        "H_5: Las variables climaticas tienen efecto secundario."
    )


def mostrar_criterios_exito():
    """Define los criterios de exito del proyecto."""
    print("\n[CRITERIOS DE EXITO]")
    print("-" * 70)
    print("  - MAPE < 20% (criterio principal)")
    print("  - Mejora respecto al modelo naive (MASE < 1)")
    print("  - Residuos del modelo SARIMA compatibles con ruido blanco")
    print("  - Coeficientes de variables clave estadisticamente significativos")


def ejecutar():
    """Funcion principal de la fase 1, ejecutada desde el menu."""
    mostrar_contexto_negocio()
    mostrar_objetivos()
    mostrar_hipotesis()
    mostrar_criterios_exito()
    print("\n" + "=" * 70)
    print("FASE 1 COMPLETADA")
    print("=" * 70)


if __name__ == "__main__":
    ejecutar()
