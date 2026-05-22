"""
============================================================================
PROYECTO: Prediccion de la Cantidad de Turistas en Ayacucho
============================================================================
Curso:    Investigacion e Inteligencia de Negocios
Carrera:  Ingenieria de Sistemas de Informacion
Escuela:  Escuela Superior La Pontificia - Ayacucho
Docente:  Ing. Jurado Lopez, Jonathan Pedro
Ano:      2026

DESCRIPCION
-----------
Programa principal con menu interactivo para ejecutar las seis fases
de la metodologia CRISP-DM aplicada al pronostico turistico de Ayacucho.

EJECUCION
---------
    python main.py
"""

import os
import sys
import time

# Asegurar que el directorio src sea accesible
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Crear directorios de salida si no existen
os.makedirs("outputs/figuras", exist_ok=True)

# Variables globales para compartir entre fases
_datos = None
_modelos = None
_fase2_ejecutada = False
_fase3_ejecutada = False
_fase4_ejecutada = False
_fase5_ejecutada = False


def limpiar_pantalla():
    """Limpia la pantalla segun el sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_banner():
    """Muestra el banner del proyecto."""
    print("=" * 70)
    print("  PREDICCION DE TURISTAS EN AYACUCHO - METODOLOGIA CRISP-DM")
    print("  Escuela Superior La Pontificia - Ayacucho")
    print("  Curso: Investigacion e Inteligencia de Negocios")
    print("=" * 70)


def mostrar_menu():
    """Muestra el menu principal."""
    print()
    mostrar_banner()
    print()
    print("  MENU PRINCIPAL")
    print("  " + "-" * 66)
    print("  1. Fase 1 - Comprension del Negocio")
    print("  2. Fase 2 - Comprension de los Datos (EDA)")
    print("  3. Fase 3 - Preparacion de los Datos")
    print("  4. Fase 4 - Modelado (SARIMA + Regresion)")
    print("  5. Fase 5 - Evaluacion de Modelos")
    print("  6. Fase 6 - Despliegue (Pronostico 2025)")
    print("  " + "-" * 66)
    print("  7. EJECUTAR TODAS LAS FASES (1 a 6)")
    print("  8. Ver estado del proyecto")
    print("  " + "-" * 66)
    print("  0. Salir")
    print()


def ejecutar_fase1():
    """Ejecuta la Fase 1: Comprension del negocio."""
    from src.fase1_negocio import ejecutar
    ejecutar()


def ejecutar_fase2():
    """Ejecuta la Fase 2: Comprension de los datos."""
    global _fase2_ejecutada
    from src.fase2_datos import ejecutar
    ejecutar()
    _fase2_ejecutada = True


def ejecutar_fase3():
    """Ejecuta la Fase 3: Preparacion de los datos."""
    global _datos, _fase3_ejecutada
    from src.fase3_preparacion import ejecutar
    _datos = ejecutar()
    _fase3_ejecutada = True
    return _datos


def ejecutar_fase4():
    """Ejecuta la Fase 4: Modelado. Requiere Fase 3 previa."""
    global _modelos, _fase4_ejecutada
    if not _fase3_ejecutada:
        print("\n  >> Ejecutando primero Fase 3 (requisito previo)...")
        ejecutar_fase3()
    from src.fase4_modelado import ejecutar
    _modelos = ejecutar(_datos)
    _fase4_ejecutada = True
    return _modelos


def ejecutar_fase5():
    """Ejecuta la Fase 5: Evaluacion. Requiere Fases 3 y 4 previas."""
    global _fase5_ejecutada
    if not _fase4_ejecutada:
        print("\n  >> Ejecutando primero Fase 4 (requisito previo)...")
        ejecutar_fase4()
    from src.fase5_evaluacion import ejecutar
    ejecutar(_datos, _modelos)
    _fase5_ejecutada = True


def ejecutar_fase6():
    """Ejecuta la Fase 6: Despliegue. Requiere Fase 3 previa."""
    if not _fase3_ejecutada:
        print("\n  >> Ejecutando primero Fase 3 (requisito previo)...")
        ejecutar_fase3()
    from src.fase6_despliegue import ejecutar
    ejecutar(_datos)


def ejecutar_todas():
    """Ejecuta todas las fases en orden."""
    print("\n" + "=" * 70)
    print("  EJECUTANDO TODAS LAS FASES (1 a 6)")
    print("=" * 70)

    inicio = time.time()
    ejecutar_fase1()
    input("\n  [Presione ENTER para continuar a la Fase 2]")

    ejecutar_fase2()
    input("\n  [Presione ENTER para continuar a la Fase 3]")

    ejecutar_fase3()
    input("\n  [Presione ENTER para continuar a la Fase 4]")

    ejecutar_fase4()
    input("\n  [Presione ENTER para continuar a la Fase 5]")

    ejecutar_fase5()
    input("\n  [Presione ENTER para continuar a la Fase 6]")

    ejecutar_fase6()

    duracion = time.time() - inicio
    print(f"\n\n  TODAS LAS FASES COMPLETADAS en {duracion:.1f} segundos")
    print("  Revise la carpeta outputs/ para los resultados generados")


def mostrar_estado():
    """Muestra el estado de ejecucion de las fases."""
    print("\n" + "=" * 70)
    print("  ESTADO DEL PROYECTO")
    print("=" * 70)

    fases = [
        ("Fase 1 - Comprension del Negocio", True),
        ("Fase 2 - Comprension de los Datos", _fase2_ejecutada),
        ("Fase 3 - Preparacion de los Datos", _fase3_ejecutada),
        ("Fase 4 - Modelado",                _fase4_ejecutada),
        ("Fase 5 - Evaluacion",              _fase5_ejecutada),
        ("Fase 6 - Despliegue",              False),
    ]

    for nombre, ejecutada in fases:
        marca = "[OK]" if ejecutada else "[  ]"
        print(f"  {marca} {nombre}")

    print()
    print("  Archivos generados en outputs/:")
    if os.path.exists("outputs"):
        for raiz, _, archivos in os.walk("outputs"):
            for archivo in archivos:
                ruta_completa = os.path.join(raiz, archivo)
                tamano = os.path.getsize(ruta_completa) // 1024
                print(f"    {ruta_completa} ({tamano} KB)")


def main():
    """Bucle principal del programa."""
    opciones = {
        "1": ejecutar_fase1,
        "2": ejecutar_fase2,
        "3": ejecutar_fase3,
        "4": ejecutar_fase4,
        "5": ejecutar_fase5,
        "6": ejecutar_fase6,
        "7": ejecutar_todas,
        "8": mostrar_estado,
    }

    while True:
        mostrar_menu()
        try:
            opcion = input("  Seleccione una opcion: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Saliendo del programa...")
            break

        if opcion == "0":
            print("\n  Gracias por usar el sistema. Hasta pronto!")
            break

        if opcion in opciones:
            try:
                opciones[opcion]()
                input("\n  [Presione ENTER para volver al menu]")
            except Exception as e:
                print(f"\n  ERROR durante la ejecucion: {e}")
                import traceback
                traceback.print_exc()
                input("\n  [Presione ENTER para continuar]")
        else:
            print(f"\n  Opcion '{opcion}' no valida. Intente nuevamente.")
            time.sleep(1)


if __name__ == "__main__":
    main()
