# Predicción de Turistas en Ayacucho – CRISP-DM

Proyecto de analítica predictiva aplicado al sector turístico de la región
Ayacucho (Perú), desarrollado siguiendo las seis fases de la metodología
CRISP-DM. Utiliza modelos SARIMA y regresión lineal múltiple para
pronosticar la cantidad mensual de arribos a establecimientos de hospedaje.

## Información Académica

| Campo | Valor |
|---|---|
| **Curso** | Investigación e Inteligencia de Negocios |
| **Carrera** | Ingeniería de Sistemas de Información |
| **Escuela** | Escuela Superior La Pontificia – Ayacucho |
| **Docente** | Ing. Jurado López, Jonathan Pedro |
| **Año** | 2026 |

## Estructura del Proyecto

```
proyecto_turismo_ayacucho/
├── README.md                       Este archivo
├── requirements.txt                Dependencias de Python
├── main.py                         Programa principal con menú interactivo
├── data/
│   └── turismo_ayacucho_2010_2024.csv   Dataset (180 registros mensuales)
├── src/
│   ├── __init__.py
│   ├── fase1_negocio.py            Fase 1: Comprensión del negocio
│   ├── fase2_datos.py              Fase 2: Análisis exploratorio (EDA)
│   ├── fase3_preparacion.py        Fase 3: Preparación de los datos
│   ├── fase4_modelado.py           Fase 4: SARIMA + Regresión múltiple
│   ├── fase5_evaluacion.py         Fase 5: Métricas y diagnóstico
│   └── fase6_despliegue.py         Fase 6: Pronóstico 2025
├── outputs/                        (generada automáticamente)
│   ├── figuras/                    Gráficos PNG
│   ├── metricas.json               Métricas de los modelos
│   └── pronostico_2025.csv         Pronóstico mensual exportado
└── tests/
    └── test_modelos.py             Tests básicos de validación
```

## Requisitos

- **Python 3.10 o superior**
- **Visual Studio Code** (recomendado)
- Sistema operativo: Windows, macOS o Linux

## Instalación Paso a Paso

### Paso 1: Verificar la instalación de Python

Abre una terminal (PowerShell en Windows, Terminal en Mac/Linux) y ejecuta:

```bash
python --version
```

Si no tienes Python instalado, descárgalo desde
[python.org/downloads](https://www.python.org/downloads/) y durante la
instalación marca la opción "Add Python to PATH".

### Paso 2: Clonar o descomprimir el proyecto

Si recibiste un ZIP, descomprímelo en una carpeta de tu preferencia.
Si está en un repositorio Git:

```bash
git clone <url-del-repositorio>
cd proyecto_turismo_ayacucho
```

### Paso 3: Abrir el proyecto en Visual Studio Code

```bash
code .
```

O bien, abre VS Code y selecciona **File > Open Folder...** y elige la
carpeta del proyecto.

### Paso 4: Crear un entorno virtual (recomendado)

Esto aísla las dependencias del proyecto y evita conflictos con otras
instalaciones de Python.

**En Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**En macOS / Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

Cuando el entorno virtual esté activo, verás `(venv)` al inicio de la
línea de comandos.

### Paso 5: Instalar las dependencias

```bash
pip install -r requirements.txt
```

Esto instalará automáticamente: pandas, numpy, matplotlib, seaborn,
statsmodels y scikit-learn.

### Paso 6: Verificar la instalación

Ejecuta los tests básicos para confirmar que todo está bien:

```bash
python tests/test_modelos.py
```

Si todos los tests pasan, el proyecto está listo para usar.

## Ejecución del Proyecto

### Opción 1: Menú interactivo (recomendado para sustentación)

```bash
python main.py
```

Verás un menú como este:

```
======================================================================
  PREDICCION DE TURISTAS EN AYACUCHO - METODOLOGIA CRISP-DM
======================================================================

  MENU PRINCIPAL
  ------------------------------------------------------------------
  1. Fase 1 - Comprension del Negocio
  2. Fase 2 - Comprension de los Datos (EDA)
  3. Fase 3 - Preparacion de los Datos
  4. Fase 4 - Modelado (SARIMA + Regresion)
  5. Fase 5 - Evaluacion de Modelos
  6. Fase 6 - Despliegue (Pronostico 2025)
  ------------------------------------------------------------------
  7. EJECUTAR TODAS LAS FASES (1 a 6)
  8. Ver estado del proyecto
  ------------------------------------------------------------------
  0. Salir

  Seleccione una opcion:
```

Escribe el número de la opción y presiona ENTER.

### Opción 2: Ejecutar fases individualmente desde VS Code

Abre cualquier archivo de la carpeta `src/`, por ejemplo `fase2_datos.py`,
y presiona `F5` o usa el botón "Run Python File" en la esquina superior
derecha.

### Opción 3: Ejecutar desde la terminal directamente

```bash
python src/fase1_negocio.py
python src/fase2_datos.py
```

> **Nota:** Las fases 4, 5 y 6 requieren que se ejecute primero la fase
> 3. El menú interactivo lo hace automáticamente.

## Resultados Esperados

Después de ejecutar las seis fases, encontrarás en la carpeta `outputs/`:

### Gráficos generados (en `outputs/figuras/`)

- `fase2_serie_temporal.png` – Serie temporal completa 2010-2024
- `fase2_estacionalidad.png` – Patrón estacional mensual
- `fase2_heatmap_correlacion.png` – Matriz de correlación visual
- `fase2_descomposicion.png` – Descomposición tendencia/estacionalidad/residuos
- `fase4_acf_pacf.png` – Funciones ACF y PACF
- `fase4_comparacion_modelos.png` – SARIMA vs Regresión vs Real
- `fase5_errores_mensuales.png` – Error absoluto mes a mes
- `fase6_pronostico_2025.png` – Pronóstico 2025 con IC 95%

### Archivos de datos (en `outputs/`)

- `metricas.json` – Métricas de evaluación (RMSE, MAE, MAPE, R², MASE)
- `pronostico_2025.csv` – Pronóstico mensual exportable a Excel/Power BI

### Métricas esperadas

| Modelo | RMSE | MAE | MAPE | R² |
|---|---|---|---|---|
| SARIMA(1,1,1)(1,1,1,12) | ~9,446 | ~7,369 | ~18.6% | ~0.16 |
| Regresión Lineal Múltiple | ~13,175 | ~11,930 | ~27.6% | ~-0.63 |

## Solución de Problemas Comunes

### Error: "ModuleNotFoundError: No module named 'statsmodels'"

No has instalado las dependencias. Activa el entorno virtual y ejecuta:

```bash
pip install -r requirements.txt
```

### Error: "FileNotFoundError: data/turismo_ayacucho_2010_2024.csv"

Estás ejecutando el script desde otra carpeta. Asegúrate de estar en la
raíz del proyecto:

```bash
cd ruta/al/proyecto_turismo_ayacucho
python main.py
```

### Error: "ImportError: No module named 'src'"

Ejecuta los scripts desde la raíz del proyecto, no desde la carpeta
`src/`.

### Los gráficos no se muestran

Los gráficos se guardan automáticamente en `outputs/figuras/` como PNG.
Ábrelos con cualquier visor de imágenes.

## Tecnologías Utilizadas

- **Python 3.10+** – Lenguaje de programación
- **pandas** – Manipulación de datos
- **numpy** – Cálculos numéricos
- **statsmodels** – Modelo SARIMA y tests estadísticos
- **scikit-learn** – Regresión lineal múltiple y métricas
- **matplotlib** y **seaborn** – Visualización de datos

## Recomendaciones para VS Code

### Extensiones recomendadas

- **Python** (Microsoft) – soporte de lenguaje
- **Pylance** – análisis estático
- **Jupyter** – si decides convertir el código a notebooks
- **Rainbow CSV** – visualización mejorada del dataset

### Configuración del intérprete

1. Presiona `Ctrl+Shift+P` (Windows/Linux) o `Cmd+Shift+P` (Mac)
2. Busca **"Python: Select Interpreter"**
3. Selecciona el intérprete dentro de `./venv/`

## Referencias del Proyecto

- MINCETUR (2023). *Reporte regional de turismo Ayacucho 2023*.
- Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3.ª ed.). OTexts.
- Wirth, R., & Hipp, J. (2000). CRISP-DM: Towards a standard process model for data mining.

## Contacto

Para consultas sobre el proyecto, dirigirse a los integrantes del equipo
o al docente del curso.
