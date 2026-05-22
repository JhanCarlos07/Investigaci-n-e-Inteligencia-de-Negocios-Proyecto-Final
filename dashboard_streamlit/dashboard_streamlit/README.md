# Dashboard Streamlit - Predicción de Turistas en Ayacucho

Dashboard web interactivo que muestra los resultados del proyecto de
analítica predictiva del turismo en Ayacucho, organizado por las 6 fases
de CRISP-DM.

## Estructura

```
dashboard_streamlit/
├── app.py                              Página principal
├── requirements.txt                    Dependencias
├── README.md                           Este archivo
├── data/
│   └── turismo_ayacucho_2010_2024.csv  Dataset (180 registros)
└── pages/
    ├── 1_🏢_Fase_1_Negocio.py
    ├── 2_🔍_Fase_2_EDA.py
    ├── 3_🛠️_Fase_3_Preparacion.py
    ├── 4_🤖_Fase_4_Modelado.py
    ├── 5_📈_Fase_5_Evaluacion.py
    └── 6_🔮_Fase_6_Pronostico.py
```

## Instalación y Ejecución

### Paso 1: Abrir el dashboard en VS Code

Tras descomprimir el ZIP, abre la carpeta `dashboard_streamlit/` en VS Code.

### Paso 2: Activar el entorno virtual

Si vas a usar el mismo `venv` del proyecto principal:

```powershell
..\proyecto_vscode\venv\Scripts\Activate.ps1
```

O bien, crear uno nuevo solo para el dashboard:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Paso 3: Instalar dependencias

```powershell
pip install -r requirements.txt
```

### Paso 4: Ejecutar el dashboard

```powershell
streamlit run app.py
```

El dashboard se abrirá automáticamente en tu navegador en
**http://localhost:8501**

Para detenerlo: presiona `Ctrl + C` en la terminal.

## Características Interactivas

### Página 1 - Comprensión del Negocio
- Tabs navegables: Contexto, Problema, Objetivos, Hipótesis
- Métricas clave del sector turístico

### Página 2 - EDA (Análisis Exploratorio)
- **Filtros laterales**: rango de años, meses específicos, incluir/excluir pandemia
- 5 tabs: Serie Temporal, Estacionalidad, Correlaciones, Estadísticas, Datos
- Heatmap interactivo año vs mes
- Descarga de datos filtrados en CSV

### Página 3 - Preparación de Datos
- Visualización del split train/test
- Demostración del one-hot encoding paso a paso
- Resumen visual de transformaciones

### Página 4 - Modelado
- **Sliders para hiperparámetros SARIMA** (p, d, q, P, D, Q)
- Reentrenamiento en vivo al cambiar parámetros
- Comparación visual SARIMA vs Regresión
- Tabla de coeficientes con p-valores

### Página 5 - Evaluación
- Métricas RMSE, MAE, MAPE, R², MASE
- Diagnóstico de residuos con test Ljung-Box
- Comparación visual de ambos modelos
- Errores absolutos mes a mes

### Página 6 - Pronóstico 2025
- **Selector de escenario**: Pesimista / Base / Optimista
- Niveles de confianza ajustables (80% o 95%)
- Sliders de gasto turístico y estancia
- Cálculo en vivo del impacto económico
- Caso de aplicación Semana Santa 2025
- Descarga del pronóstico en CSV

## Para la Sustentación al Docente

1. Ejecuta `streamlit run app.py`
2. El navegador abrirá el dashboard automáticamente
3. Navega por el menú lateral mostrando cada fase
4. **Demuestra interactividad**:
   - En Fase 2: cambia los filtros y observa cómo se actualizan los gráficos
   - En Fase 4: cambia los hiperparámetros SARIMA y observa cómo cambia el AIC
   - En Fase 6: cambia el escenario y observa el cambio del pronóstico

## Solución de Problemas

### "ModuleNotFoundError: No module named 'streamlit'"

Instala las dependencias:
```
pip install -r requirements.txt
```

### El dashboard no se abre automáticamente

Abre tu navegador manualmente en: http://localhost:8501

### "Address already in use"

Otra instancia de Streamlit ya está corriendo. Detenla con Ctrl+C o usa
otro puerto:
```
streamlit run app.py --server.port 8502
```

### Los gráficos se ven cortados

Maximiza la ventana del navegador. El dashboard está diseñado para
pantalla completa.
