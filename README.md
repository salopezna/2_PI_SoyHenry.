# **Proyecto Individual Nº2: Telecomunicaciones**

<p align="justify">
La industria de las telecomunicaciones ha desempeñado un papel crucial en nuestra sociedad, facilitando la información a escala global y permitiendo la comunicación continua. La transferencia de datos y la comunicación se realizan principalmente a través de internet, líneas telefónicas fijas y móviles. Argentina está a la vanguardia en el desarrollo de las telecomunicaciones, contando con un total de 62,12 millones de conexiones en 2020. Dada la relevancia del tema para el país, he llevado a cabo un análisis exhaustivo que permite identificar el comportamiento de este sector a nivel nacional, enfocándome en el acceso al servicio de Internet y su relación con otros servicios de comunicaciones.
</p>

---

## **Tabla de Contenidos**
1. [Contexto y Descripción del Problema]
2. [Objetivos del Proyecto]
3. [Estructura del Repositorio]
4. [Metodología y Herramientas Utilizadas] 
5. [Análisis Exploratorio de Datos (EDA)]
6. [Dashboard y KPIs]
7. [Hallazgos y Conclusiones]
8. [Siguientes Pasos y Mejores Prácticas] 
9. [Referencias]

---

## **1. Contexto y Descripción del Problema**
<p align="justify">
El objetivo es generar recomendaciones para ofrecer una buena calidad de servicio, identificar oportunidades de crecimiento y plantear soluciones personalizadas para clientes actuales o potenciales.
</p>

### **Rol a Desarrollar**
<p align="justify">
Una empresa prestadora de servicios de telecomunicaciones nos encarga realizar un análisis completo para entender el comportamiento de este sector a nivel nacional. Su interés principal es optimizar el acceso a internet, pero también debemos tener en cuenta otras dimensiones (calidad de servicio, velocidad de descarga, penetración en hogares, etc.) para orientar la estrategia de negocio.
</p>

---

## **2. Objetivos del Proyecto**
- **Explorar y limpiar** el contenido de la data base que contiene informacion historica sobre acceso y prenetracion delservicio de Internet en Argentina a nivel Nacional y provincial (valores faltantes, outliers, duplicados, entre otros).  
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

- **Carpeta de datos** 
  Contiene los archivos originales de Excel con información de accesos, penetración, velocidad, etc. Tabien se almacena allí los archivos procesados en formato .parquet.

- **functions.py** (opcional)  
  Módulo con funciones auxiliares para imputación de datos, visualizaciones personalizadas y cálculos de multiples cosas.

- **Dashboard/** (opcional)  
  Archivo del dashboard desarrollado en PowerBI, así como capturas de pantalla del mismo.

---

## **4. Metodología y Herramientas Utilizadas**
1. **Python y Librerías Principales**  
   - *pandas, numpy*: para manipulación y limpieza de datos.  
   - *matplotlib, seaborn*: para visualizaciones y análisis exploratorio.  
   - *scipy*: para estadística descriptiva y pruebas de hipótesis.  

2. **Power BI**  
   - Creación del Dashboard interactivo con filtros que permiten explorar penetración, velocidad media, accesos y otros indicadores.

3. **Metodología de Trabajo**  
   - **Extracción de datos**: se partió de hojas de Excel que contenían información de accesos, penetración y velocidad en distintos trimestres y provincias.  
   - **Transformación**: limpieza de datos, imputación de valores faltantes (media, mediana, k-NN), detección y tratamiento de outliers, unificación de campos con casting adecuado (int, float, category).  
   - **Carga** en un DataFrame unificado para su análisis.  
   - **EDA**: análisis univariado (distribuciones), bivariado (correlaciones y scatter plots) y multivariado .
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
   - Se diseñó en Power BI un panel con:
     - Filtros por trimestre y otro a nivel de provincias.  
     - Visualizaciones de evolución temporal de accesos, penetración y velocidad media así como comportamiento de los ingresos en el tiempo.  

2. **KPIs**  
   - **KPI propuesto**: Aumentar en un 2% el acceso a internet por cada 100 hogares a nivel provincial para el próximo trimestre.  
   - **KPI FO**: Aumetar 10% la velocidad media de acceso a internet a traves de Fibra Optica (FO) a nivel Nacional para el proximo trimestre.
   - **KPIs Ingresos**: Aumentar en un 23% los ingresos por accessos a Internet a nivel Nacional para el proximo trimestre.  
     \[
     \text{KPI} = \left(\frac{\text{Nuevo acceso} - \text{Acceso actual}}{\text{Acceso actual}}\right) \times 100
     \]  
   - **KPIs adicionales**:
     - Tasa de crecimiento de velocidad media (trimestre a trimestre).  
     - Tasa de crecimiento de accesos por tecnología (ADSL, FO, Wireless).  
     - Ratio de ingresos por tipo de tecnología (ARPU segmentado).  

Estos KPIs se muestran en el dashboard con tarjetas y gráficos que reflejan su evolución en el tiempo.

---

## **7. Hallazgos y Conclusiones**

### **Hallazgos Destacados**
- **Correlación positiva** entre velocidad media de descarga e ingresos: a medida que la velocidad aumenta, los ingresos tienden a crecer pero mayoritariamente sobre la tecnologia de fibra optica.  
- **Penetración vs. Accesos**: las provincias con mayor penetración (por cada 100 hogares) suelen mostrar un crecimiento sostenido en accesos de banda ancha fija.  
- **Distribución desigual**: Buenos Aires concentra la mayor cantidad de accesos, mientras que provincias como Santa Cruz o Tierra del Fuego presentan menor participación en cifras absolutas pero con tasas de crecimiento interesantes.

### **Resumen de Insights**
- **Segmentación**: los servicios de Fibra Óptica y Cablemodem registran incrementos considerables en provincias con posible alta densidad poblacional.  
- **Velocidad**: la velocidad media de descarga mantiene una tendencia al alza en trimestres recientes, posiblemente asociada a inversiones en infraestructura.  
- **Oportunidad de Crecimiento**: regiones con menor penetración ofrecen un margen mayor de expansión si se mejora la velocidad y se implementan planes más accesibles.
- No se debe seguir ampliando la tecnologia de ADSL ya que no se ve una tendencia de crecimiento en los ingresos y penetración.
- 

### **Posibles Líneas de Acción**
1. **Inversión en infraestructura** de fibra óptica en provincias con tasas de crecimiento de penetración prometedoras.  
2. **Segmentación de planes** según velocidad y necesidades locales para maximizar adopción e ingresos.  
3. **Colaboración con gobiernos locales** para aumentar la penetración en provincias con menor nivel de accesos, cumpliendo el KPI de +2% de penetración trimestral.
3. **Implementar una estrategia de migración de ADSL a Fibra Optica** para retener esos usuarios y salir de la red de cobre que tiene una baja rentabilidad y podría significar una recapitalización por la venta del cobre aprovechando el alto precio en el percado actual.

---

## **8. Siguientes Pasos y Mejores Prácticas**
1. **Modelos de Predicción**  
   - Se trabaja en la implementar un modelo de regresión para pronosticar la evolución de accesos e ingresos, usando variables como velocidad, penetración y trimestres.

2. **Profundizar en Segmentación**  
   - Se emplearan técnicas de clustering para agrupar provincias según similitudes en penetración, velocidad e ingresos.

3. **Fuentes de Datos Externas**  
   - Se complementara a futuro con información socioeconómica o geográfica para refinar estrategias de expansión y segmentación.

---

## **9. Referencias**
- **Repositorio del Proyecto en GitHub**  
- **EDA.ipynb**  
- **Documentación de Pandas**  
- **Documentación de Seaborn**  
- **Documentación de Power BI**  

---
