# **Proyecto Individual Nº2: Telecomunicaciones**

<p align="justify">
¡Bienvenidos al último proyecto individual de la etapa de labs! En este proyecto, asumimos el rol de Data Analyst para analizar el sector de las telecomunicaciones en Argentina. El objetivo principal es comprender el comportamiento del mercado, identificar oportunidades de crecimiento y plantear soluciones que mejoren la calidad de los servicios de Internet y comunicaciones.
</p>

---

## **Tabla de Contenidos**
1. [Contexto y Descripción del Problema](#contexto-y-descripción-del-problema)  
2. [Objetivos del Proyecto](#objetivos-del-proyecto)  
3. [Estructura del Repositorio](#estructura-del-repositorio)  
4. [Metodología y Herramientas Utilizadas](#metodología-y-herramientas-utilizadas)  
5. [Análisis Exploratorio de Datos (EDA)](#análisis-exploratorio-de-datos-eda)  
6. [Dashboard y KPIs](#dashboard-y-kpis)  
7. [Hallazgos y Conclusiones](#hallazgos-y-conclusiones)  
8. [Siguientes Pasos y Mejores Prácticas](#siguientes-pasos-y-mejores-prácticas)  
9. [Referencias](#referencias)

---

## **1. Contexto y Descripción del Problema**
<p align="justify">
Las telecomunicaciones engloban la transmisión de información a través de medios electrónicos (telefonía, TV, radio, internet, etc.). Argentina se destaca por tener una alta adopción de servicios de internet, con más de 62 millones de conexiones para el año 2020.
</p>

### **Rol a Desarrollar**
<p align="justify">
Una empresa prestadora de servicios de telecomunicaciones nos encarga realizar un análisis completo para entender el comportamiento de este sector a nivel nacional. Su interés principal es optimizar el acceso a internet, pero también debemos tener en cuenta otras dimensiones (calidad de servicio, velocidad de descarga, penetración en hogares, etc.) para orientar la estrategia de negocio.
</p>

---

## **2. Objetivos del Proyecto**
- **Explorar y limpiar** los datos de telecomunicaciones (valores faltantes, outliers, duplicados).  
- **Analizar las tendencias** y relaciones entre velocidad, penetración, accesos e ingresos.  
- **Desarrollar un Dashboard** interactivo que refleje los principales hallazgos.  
- **Proponer KPIs** clave para el negocio, incluyendo el KPI obligatorio de aumento de un 2% de accesos por cada 100 hogares a nivel provincial.  
- **Generar conclusiones** fundamentadas que permitan a la empresa mejorar la calidad de sus servicios e identificar oportunidades de crecimiento.

---

## **3. Estructura del Repositorio**
- **EDA.ipynb**  
  Notebook con el Análisis Exploratorio de Datos (EDA). Se documentan los pasos de limpieza, tratamiento de valores nulos, outliers y gráficos para cada variable.

- **README.md**  
  Archivo principal de presentación del proyecto, incluyendo el contexto, objetivos, metodología, resultados y conclusiones.

- **Carpeta de datos** (si aplica)  
  Podría contener los archivos originales de Excel o CSV con información de accesos, penetración, velocidad, etc. (no se incluyen aquí si exceden el tamaño o confidencialidad).

- **functions.py** (opcional)  
  Módulo con funciones auxiliares para imputación de datos, visualizaciones personalizadas y cálculos de correlación.

- **Dashboard/** (opcional)  
  Carpeta que contiene el archivo del dashboard (ej. `.pbix` si se usó Power BI), así como capturas de pantalla del mismo.

---

## **4. Metodología y Herramientas Utilizadas**
1. **Python y Librerías Principales**  
   - *pandas, numpy*: para manipulación y limpieza de datos.  
   - *matplotlib, seaborn*: para visualizaciones y análisis exploratorio.  
   - *scipy*: para estadística descriptiva y pruebas de hipótesis.  

2. **Power BI (o la herramienta elegida)**  
   - Creación de un Dashboard interactivo con filtros que permiten explorar penetración, velocidad media, accesos y otros indicadores.

3. **Metodología de Trabajo**  
   - **Extracción de datos**: se partió de hojas de Excel que contenían información de accesos, penetración y velocidad en distintos trimestres y provincias.  
   - **Transformación**: limpieza de datos, imputación de valores faltantes (media, mediana, k-NN), detección y tratamiento de outliers, unificación de campos con casting adecuado (int, float, category).  
   - **Carga** en un DataFrame unificado para su análisis.  
   - **EDA**: análisis univariado (distribuciones), bivariado (correlaciones y scatter plots) y multivariado (heatmaps, PCA o regresiones simples).  
   - **Dashboard**: se diseñó para presentar insights clave, KPIs y segmentaciones (por provincia, tecnología, trimestre, etc.).

---

## **5. Análisis Exploratorio de Datos (EDA)**
<p align="justify">
El notebook <strong>EDA.ipynb</strong> detalla paso a paso los siguientes aspectos:
</p>

1. **Limpieza de Datos**  
   - Eliminación de duplicados y corrección de nombres de columnas.  
   - Imputación de nulos con métodos apropiados según la distribución (media, mediana o k-NN).

2. **Detección de Outliers**  
   - Se utilizaron métodos IQR y Z-score para identificar valores atípicos en columnas como accesos, velocidad media e ingresos.  
   - Evaluación de la pertinencia de su eliminación o corrección.

3. **Análisis Univariado**  
   - Histogramas, boxplots y violin plots para ver la distribución de cada variable.  
   - Cálculo de estadísticas descriptivas (media, mediana, skewness, kurtosis).

4. **Análisis Bivariado**  
   - Matrices de correlación (Pearson, Spearman) y heatmaps.  
   - Scatter plots para comparar velocidad vs. penetración, accesos vs. ingresos, etc.

5. **Análisis Multivariado**  
   - Visualizaciones con <code>hue</code> (por trimestre o provincia) para ver tendencias.  
   - Estudio preliminar de correlaciones múltiples que sugieren posibles modelos de regresión.

---

## **6. Dashboard y KPIs**
1. **Dashboard**  
   - Se diseñó en Power BI (o herramienta similar) un panel con:
     - Filtros por provincia, trimestre y tecnología.  
     - Visualizaciones de evolución temporal de accesos, penetración y velocidad media.  
     - Mapas (si aplica) para ver la penetración o accesos por provincia.

2. **KPIs**  
   - **KPI propuesto**: Aumentar en un 2% el acceso a internet por cada 100 hogares a nivel provincial para el próximo trimestre.  
     \[
     \text{KPI} = \left(\frac{\text{Nuevo acceso} - \text{Acceso actual}}{\text{Acceso actual}}\right) \times 100
     \]  
   - **KPIs adicionales**:
     - Tasa de crecimiento de velocidad media (quarter-over-quarter).  
     - Tasa de crecimiento de accesos por tecnología (ADSL, FO, Wireless).  
     - Ratio de ingresos por tipo de tecnología (ARPU segmentado).  

Estos KPIs se muestran en el dashboard con tarjetas y gráficos que reflejan su evolución en el tiempo.

---

## **7. Hallazgos y Conclusiones**

### **Hallazgos Destacados**
- **Correlación positiva** entre velocidad media de descarga e ingresos: a medida que la velocidad aumenta, los ingresos tienden a crecer.  
- **Penetración vs. Accesos**: las provincias con mayor penetración (por cada 100 hogares) suelen mostrar un crecimiento sostenido en accesos de banda ancha fija.  
- **Distribución desigual**: Buenos Aires concentra la mayor cantidad de accesos, mientras que provincias como Santa Cruz o Tierra del Fuego presentan menor participación en cifras absolutas pero con tasas de crecimiento interesantes.

### **Resumen de Insights**
- **Segmentación**: los servicios de Fibra Óptica y Cablemodem registran incrementos considerables en provincias con alta densidad poblacional.  
- **Velocidad**: la velocidad media de descarga mantiene una tendencia al alza en trimestres recientes, posiblemente asociada a inversiones en infraestructura.  
- **Oportunidad de Crecimiento**: regiones con menor penetración ofrecen un margen mayor de expansión si se mejora la velocidad y se implementan planes más accesibles.

### **Posibles Líneas de Acción**
1. **Inversión en infraestructura** de fibra óptica en provincias con tasas de crecimiento de penetración prometedoras.  
2. **Segmentación de planes** según velocidad y necesidades locales para maximizar adopción e ingresos.  
3. **Colaboración con gobiernos locales** para aumentar la penetración en provincias con menor nivel de accesos, cumpliendo el KPI de +2% de penetración trimestral.

---

## **8. Siguientes Pasos y Mejores Prácticas**
1. **Modelos de Predicción**  
   - Implementar un modelo de regresión para pronosticar la evolución de accesos e ingresos, usando variables como velocidad, penetración y trimestres.

2. **Profundizar en Segmentación**  
   - Emplear técnicas de clustering para agrupar provincias según similitudes en penetración, velocidad e ingresos.

3. **Fuentes de Datos Externas**  
   - Integrar información socioeconómica o geográfica para refinar estrategias de expansión y segmentación.

---

## **9. Referencias**
- **Repositorio del Proyecto en GitHub**  
- **EDA.ipynb**  
- **Documentación de Pandas**  
- **Documentación de Seaborn**  
- **Documentación de Power BI**  

---

<p align="justify">
**Disclaimer**: Este proyecto se desarrolla con fines exclusivamente pedagógicos y no representa recomendaciones definitivas para la toma de decisiones reales. Henry no se responsabiliza por el uso que se haga de la información aquí contenida.
</p>

<p align="justify">
¡Gracias por visitar este repositorio y revisar nuestro análisis de las telecomunicaciones en Argentina! Si tienes dudas o sugerencias, no dudes en abrir un issue o contactarme. ¡Espero que los hallazgos y visualizaciones te resulten de utilidad!
</p>