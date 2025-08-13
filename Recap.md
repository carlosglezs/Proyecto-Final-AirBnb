# Recap día 1

# 📄 Resumen del archivo `1_data_calendar.ipynb`

## 1️⃣ Objetivo general
Procesar datos de calendarios de Airbnb (capturados en diferentes fechas) para obtener métricas trimestrales de ocupación e ingresos, evitando solapamientos entre periodos, y consolidar los resultados en un archivo único.

---

## 2️⃣ Flujo de trabajo

### **Importaciones iniciales**
- Librerías: `pandas`, `numpy`, `sys`, `ast`, `datetime`.
- Se añade la ruta `..` a `sys.path` para importar funciones personalizadas desde `src/soporte.py`.

### **Carga de datos**
- Se leen 3 datasets de calendario:
  - `calendar_sep.csv` → 11 septiembre 2024
  - `calendar_dec.csv` → 11 diciembre 2024
  - `calendar_mar.csv` → 11 marzo 2025

### **Revisión inicial**
- Búsqueda de registros duplicados en cada DataFrame.
  - Se usan solo reservas de los **siguientes 3 meses** para cada archivo.
  - Cálculos:
    - **Días no disponibles** (`available == "f"`).
    - **Ingresos totales** (suma de `price` en el periodo).
    - **Días realmente reservados** (casos con `"f"` y precio > 0).
    - **Promedio diario** (ingresos / días reservados).

### **Procesamiento con `soporte.py`**
- Se define un diccionario `archivos_fechas` mapeando archivo → fecha de inicio.
- Se recorre cada archivo y se llama a `sp.procesar(...)` para generar un resumen.
  - `procesar_df` (en `soporte.py`) hace:
    - Filtrado al trimestre exacto (fecha inicio a +3 meses).
    - Limpieza de datos (`available` en minúsculas, precios a float).
    - Cálculo de métricas por `listing_id` y trimestre:
      - `busy_days` (días ocupados).
      - `income` (ingreso total).
      - `avg_day` (ingreso medio por día ocupado).
      - `occupancy_rate` (ocupación porcentual del trimestre).
- Los resultados se acumulan y se concatenan en `resumen_anual`.

### **Exportación**
- `resumen_anual` se guarda en `../data/resumen_anual.csv`.
- Se carga de nuevo para exploración (`df_resumen.sample(10)`).

---

## 3️⃣ Funciones clave de `soporte.py` usadas aquí

### `procesar_df(df, fecha_inicio_str, columna_fecha)`
Filtra y procesa un calendario para un trimestre específico, generando métricas de ocupación e ingresos.

---

## 4️⃣ Resultado final
- Un archivo `resumen_anual.csv` con las métricas trimestrales por anuncio (`listing_id`) y variables calculadas (`busy_days`, `income`, `avg_day`, `occupancy_rate`).
- Este archivo consolida los datos de los tres periodos de calendario, sin solapamientos.

---
# Recap día 2

# 📄 Resumen del archivo `2_EDA_preliminar.ipynb`

## 1️⃣ Objetivo general
Realizar un análisis exploratorio inicial de los datos de anuncios de Airbnb en Madrid, a partir de varias extracciones trimestrales, para identificar su estructura, calidad, posibles problemas de duplicados y preparar las variables para análisis posteriores.

---

## 2️⃣ Flujo de trabajo

### **Importaciones iniciales**
- Librerías: `pandas`, `numpy`, `sys`, `ast`, `datetime`.
- Se añade la ruta `..` a `sys.path` para importar funciones personalizadas desde `src/soporte.py`.

### **Carga de datos**
- Se leen tres datasets de anuncios:
  - `airbnb_mad_mar.csv`
  - `airbnb_mad_dec.csv`
  - `airbnb_mad_sep.csv`

### **Preparación inicial**
- Se crean copias de seguridad de cada dataset (`df_mar`, `df_dec`, `df_sep`).
- Se concatenan en un único DataFrame `df_year`.

### **Análisis preliminar general**
- Uso de `sp.eda_preliminar(df_year)` para:
  - Mostrar muestra de datos.
  - Resumen de información (`info()`).
  - Conteo de nulos y duplicados.
  - Distribución de valores para columnas categóricas.

### **Selección de columnas relevantes**
Se filtra a:
['id', 'review_scores_rating', 'last_scraped', 'neighbourhood_cleansed',
'property_type', 'accommodates', 'bathrooms', 'bedrooms', 'beds', 'amenities',
'price', 'minimum_nights', 'number_of_reviews', 'review_scores_accuracy',
'review_scores_cleanliness', 'review_scores_checkin',
'review_scores_communication', 'review_scores_location', 'review_scores_value']

### **Generación de columnas de servicios**
A través de la columna `amenities` se generan en relación a si continen los servicios en las columnas:
("Kitchen", "TV", "Air conditioning","Pets allowed", "Dryer", "Patio or balcony", "Iron", "Microwave", "Cooking basics", "hot tub", "Self check-in",  "Washer",   Heating, "Hair dryer")

### **Preparación de fechas**
- Conversión de `last_scraped` a tipo `datetime`.

### **Inspección y limpieza**
- Se convierten las columnas en minusculas y se sustituyen los espacios de las columnas por guiones
- Conteo de duplicados.
- Nuevo análisis exploratorio (`sp.eda_preliminar(df_rows)`).
- Limpieza de `price`: eliminación de símbolos `$`, conversión a `float` y luego a `int`.
- Verificación de decimales en `price` antes de la conversión.

### **Agregación por trimestre**
- Creación de columna `trimester` a partir de `last_scraped`.
- Eliminación de la columna `amenities` porque ya se extrajeron los servicios 

### **Control de duplicados**
- Búsqueda de duplicados considerando `id` y `trimestre`.

### **Integración con métricas de calendario**
- Lectura del archivo `resumen_anual.csv` (generado en `1_data_calendar.ipynb`).
- Conversión de `trimester` a string tanto en `df_rows` como en `df_resumen`.
- Unión (`merge`) de ambos datasets usando:
  - Claves: `id` (anuncios) y `trimestre`.
  - Unión interna (`inner join`).
- El resultado se guarda en `df_merged`.

### **Cálculo de nuevas métricas**
- Creación de columna `price_person` = `promedio_diario` / `accommodates`, para medir el precio medio diario por persona.

---

## 🎯 Resultado final
- `df_merged`: dataset combinado con:
  - Información del anuncio (tipo de propiedad, ubicación, capacidad, puntuaciones, precio).
  - Métricas trimestrales de ocupación e ingresos.
  - Precio medio diario por persona.

# Recap día 3

# 📄 Resumen del archivo `3_columnas_categoricas.ipynb`

## 1️⃣ Objetivo general
Analizar la calidad de los datos y la distribución de las variables, especialmente las categóricas y numéricas, en el dataset anual consolidado de Airbnb (`data_anual.csv`).

---

## 2️⃣ Flujo de trabajo

### **Importaciones iniciales**
- Librerías de análisis: `pandas`, `numpy`, `datetime`, `matplotlib`, `seaborn`.
- Herramientas de imputación: `IterativeImputer`, `KNNImputer` de `sklearn`.
- Funciones personalizadas desde `src/soporte.py`.

### **Carga del dataset**
- Se lee `data_anual.csv` con `last_scraped` como fecha.
- El dataset contiene información consolidada de tres trimestres

### **Análisis de nulos**
- Uso de `sp.calcular_nulos(df_limpio)` para obtener número y porcentaje de nulos.
- Resultado: **no existen nulos en las columnas categóricas**.

### **Análisis descriptivo general**
- Resumen estadístico (`describe().T`) para todas las variables numéricas.

### **Observaciones sobre variables numéricas** (según texto del notebook):
- **id** → identificador único.
- **review_score_rating** → puntuaciones concentradas en valores altos, con outliers bajos.
- **accommodates** → mayoría entre 1 y 5 huéspedes, outliers hasta 16.
- **bathrooms** → la mayoría con 1 baño, outliers hacia la derecha.
- **bedrooms** → mayoría entre 0 y 2, algunos valores muy altos.
- **beds** → abundancia de alojamientos con 2 camas, outliers hacia la derecha.
- **price** → gran dispersión, media 133€, desviación 340€, mínimo 1€, outliers extremos (máximo 23.124€).
- **minimum_nights** → mayoría entre 1 y 3 noches, outliers que distorsionan la media.
- **number_of_reviews** → valores muy dispersos, con máximos hasta 1.136 reseñas.
- **Review scores (accuracy, cleanliness, checkin, communication, location, value)** → percentiles cercanos y poca dispersión, pocas notas muy bajas.

### **Generación de lista de variables numéricas**
- Se identifican todas las columnas de tipo numérico.

### **Visualización de distribuciones y outliers**
- Uso de `sp.subplot_col_num()` para histogramas y boxplots.
- Uso de `sp.print_outlier_limits()` para mostrar límites inferiores y superiores de outliers por variable.

### **Gestión de los nulos**
- En el caso de columnas con pocos nulos (menos del 10%) sólo tenemos `bedrooms` y los sustituimos con la mediana
- En el caso de las columnas con muchos nulos (más del 10%) usamos el método IterativeImputer para generarlos pero con restricciones que se consideran posibles
---

## 3️⃣ Resultado final
- Dataset revisado en términos de nulos, distribución de valores y outliers.
- Gestión de los nulos.
- Conocimiento detallado de la dispersión y posibles datos atípicos en las columnas numéricas.


# Recap día 4

# 📄 Resumen del archivo `4_KPIS.ipynb`

## 1️⃣ Objetivo general
Calcular y mostrar los principales KPIs (Key Performance Indicators) para el análisis de anuncios de Airbnb en Madrid a partir del dataset limpio y preparado (`data_a_analizar.csv`) que pueden dar un primer análisis.

---

## 2️⃣ Flujo de trabajo

### **Importaciones iniciales**
- Librerías: `pandas`, `sys`, `matplotlib`, `seaborn`, `re`.
- Se añade la ruta `..` a `sys.path` para importar funciones personalizadas desde `src/soporte.py`.

### **Carga del dataset**
- Se lee `data_a_analizar.csv` con `last_scraped` como fecha.

### **KPIs calculados**

1. **Número de propietarios únicos**
   - Cálculo de `id` únicos en todo el dataset.

2. **Número de propietarios únicos por trimestre**
   - Creación de columna `trimestre` a partir de `last_scraped`.
   - Conteo de IDs únicos por trimestre (`groupby`).

3. **Precio medio por persona por trimestre**
   - Promedio de `price_person` agrupado por `trimestre`.

4. **Distribución porcentual por tipo de propiedad**
   - Porcentaje que representa cada valor en `property_type`.

5. **Promedio por alojamiento de camas, habitaciones y baños**
   - Media de `beds`, `bedrooms` y `bathrooms`.

6. **Precio medio por persona (global)**
   - Media de `price_person` para todo el dataset.

7. **Top 10 barrios con mayor precio medio por persona**
   - Promedio de `price_person` por `neighbourhood_cleansed`.

8. **Relación calidad-precio media**
   - Media de `review_scores_value_iterative`.

---

## 3️⃣ Resultado final
- Conjunto de métricas clave que resumen:
  - Volumen de anuncios activos.
  - Evolución trimestral de la oferta.
  - Características físicas promedio de los alojamientos.
  - Distribución de tipos de propiedad.
  - Patrones de precio por persona, globales y por barrio.
  - Indicador de relación calidad-precio.


# Recap día 5

# 📊 Resumen del Dashboard de Airbnb – Tipos de visualizaciones y relevancia

## 1️⃣ Indicadores clave (KPI Cards)
- **Descripción:** Tarjetas con métricas agregadas como ingresos totales, número de alojamientos, capacidad promedio, ocupación media o ingresos por día.
- **Relevancia:** Ofrecen una visión inmediata del estado general del mercado de Airbnb, permitiendo detectar rápidamente tendencias o magnitudes destacadas.

---

## 2️⃣ Gráficos de barras horizontales
  - Ingreso promedio trimestral por tipo de hospedaje.
  - Ingreso promedio por día alquilado por barrio.
  - Ingresos totales por barrio.
  - Promedio de pernoctaciones por barrio.
- **Relevancia:** Facilitan la comparación entre categorías (tipos de alojamiento, barrios) y permiten identificar cuáles generan más ingresos o tienen mayor ocupación.

---

## 3️⃣ Gráficos de líneas
  - Evolución de ingresos por trimestre.
  - Promedio de días ocupados por trimestre.
  - Ofertas de hospedaje por trimestre.
- **Relevancia:** Muestran la tendencia temporal de variables clave, permitiendo analizar estacionalidad, crecimiento o caídas en la oferta y demanda.

---

## 4️⃣ Gráfico circular (pie chart)
- Se genera primeramente un variable categorica del número de huespedes de los Airbnb:
    -Bajo: 1 y 2 huéspedes
    -Normal: 3 y 4 huéspedes
    -Alto: Más de 4 huéspedes
  - Distribución de alojamientos por categoría de número de huéspedes.
- **Relevancia:** Representa la proporción de cada categoría, útil para entender la composición de la oferta y el peso relativo de distintos tipos de alojamientos.

---

## 5️⃣ Gráfico de barras agrupadas por rango
- Se genera primeramente un variable categorica de precios por persona en base a sus medidas centrales:
    -Muy bajo: menos de 24.8 (percentil 25)
    -Bajo: entre 24.81 y 33.5 (percentil 50)
    -Medio: entre 33.51 y 46.33 (percentil 75)
    -Alto: superior a 46.34
  - Promedio de días ocupados por precio por persona (rango de precios).
- **Relevancia:** Permite ver cómo varía la ocupación según el nivel de precios, identificando segmentos más rentables o con mayor rotación.

## 6️⃣ Desglose en matriz de los datos
- Por barrio y trimestre
- Se contabiliza: número de ofertas, ingresos, promedio de días ocupados y promedio de ingresos por día

---

## 💡 Conclusión
Este dashboard combina visualizaciones de **comparación**, **tendencia** y **composición**, cubriendo:
- Quién genera más ingresos.
- Cómo se comporta el mercado en el tiempo.
- Cómo se distribuye la oferta.
- Qué segmentos de precio o ubicación tienen mejor rendimiento.

Este enfoque facilita la toma de decisiones estratégicas para anfitriones, inversores o gestores de plataformas de alquiler vacacional.


# Recap día 6

# 📊  Análisis Narrativo


## 1️⃣ Análisis narrativo

Este análisis profundiza en la interpretación de las métricas del dashboard, destacando:

- **Evolución reciente**: Crecimiento de ingresos trimestrales pese a menor oferta, impulsado por mayor ocupación y precio medio por día.
- **Enfoque en ingresos**: La localización es la variable más determinante para ingresos y valoraciones.
- **Análisis por barrios**:
  - **Embajadores**: Mayor facturación por alto volumen, aunque con fuerte competencia.
  - **Atocha**: Mayor ingreso por día, pero baja ocupación.
  - **Vinateros**: Alta ocupación, público reducido.
- **Perfil de huéspedes**: Predominan propiedades para pocos huéspedes, con mayor ocupación y precio por persona.
- **Precio por noche por persona**: Segmentación por percentiles para identificar oferta más rentable.
- **Tipo de propiedad**: El marketing y la nomenclatura (“boutique”, “entire”, “shared”) influyen fuertemente en la rentabilidad.
- **Servicios**:
  - **Piscina**: Aumenta significativamente los ingresos.
  - **Calefacción**: Común pero sin impacto positivo en precios.
- **Proporción de baños/dormitorios/camas**: La disponibilidad de baños por huésped es el factor más influyente en precio.

---

## 2️⃣ Conclusiones
La combinación del dashboard y el análisis narrativo permite:
- Visualizar tendencias y comparaciones clave.
- Comprender los factores que impulsan los ingresos y ocupación.
- Identificar segmentos y estrategias para maximizar rentabilidad.
