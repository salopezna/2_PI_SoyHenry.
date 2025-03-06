# **✅ PROYECTO DE DATASCIENCE**
## **Análisis del Sector de Internet en Argentina (2014 a 3er Trim. 2024)**
### **Descripción**
<p align="justify">
La industria de las telecomunicaciones ha desempeñado un papel crucial en nuestra sociedad, facilitando la información a escala global y permitiendo la comunicación continua. La transferencia de datos y la comunicación se realizan principalmente a través de internet, líneas telefónicas fijas y móviles. Argentina está a la vanguardia en el desarrollo de las telecomunicaciones, contando con un total de 62,12 millones de conexiones en 2020. Dada la relevancia del tema para el país, he llevado a cabo un análisis exhaustivo que permite identificar el comportamiento de este sector a nivel nacional, enfocándome en el acceso al servicio de Internet y su relación con otros servicios de comunicaciones. El objetivo es generar recomendaciones para ofrecer una buena calidad de servicio, identificar oportunidades de crecimiento y plantear soluciones personalizadas para clientes actuales o potenciales.
</p>
### **Objetivos**

- **Extracción de datos:** Importar y leer datos de diversas fuentes en un único workbook.
- **Transformación y limpieza:** 
  - Normalizar y estandarizar nombres de campos.
  - Convertir y castear tipos de datos (por ejemplo, convertir cadenas a enteros).
  - Integrar información de diferentes hojas en una única estructura.
- **Análisis Exploratorio de Datos (EDA):** 
  - Generar gráficos y tablas para visualizar tendencias.
  - Calcular estadísticas descriptivas que permitan evaluar la calidad y consistencia de los datos.

### **Stack Tecnológico**

- **Lenguaje:** Python 3.12
- **Entorno:** Jupyter Notebook en Visual Studio Code
- **Librerías:**  
  - **Pandas**: Manipulación de datos.  
  - **NumPy**: Operaciones numéricas.  
  - **Matplotlib/Seaborn**: Visualización de datos.
- **Control de Versiones:** Git y GitHub

```markdown
# Estructura del Proyecto

mvp_pi2/
│
├── 📁 data/                    # 📂 Carpeta para almacenamiento general de los datos
│   ├── 📁 raw/                 # 📄 Datos originales (sin modificar)
│   ├── 📁 processed/           # 📄 Datos limpios y listos para análisis
│
├── 📁 virtualenv/              # 📂 Carpeta para almacenamiento de la data del entorno virtual
├── ETL.ipynb                   # 📊 Notebook para Exploración, Transformación y Carga inicial
├── EDA.ipynb                   # 📊 Notebook para Análisis exploratorio            
│
├── functions.py                # 📄 Compendio de Funciones usadas en el ETL y EDA
│
├── requirements.txt            # 📋 Lista de librerias y dependencias requeridas
├── .gitignore                  # 🚫 Archivos/carpetas a ignorar en Git
├── README.md                   # 📖 Descripción general del proyecto
└── Dashboard_KPI_PI_2.pbix     # 📊 Archivo de Power BI con el Dashboard
---
1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/salopezna/2_PI_SoyHenry..git

<p align="justify">
A partir de fuentes de información como el portal de ENACOM (https://indicadores.enacom.gob.ar/datos-abiertos), se obtienen datos asociados al comportamiento histórico trimestral desde el año 2014 hasta el tercer trimestre de 2024 a nivel nacional y, en algunos casos, a nivel provincial. Todos estos datos están concentrados en múltiples hojas dentro de un solo archivo de Excel.
</p>
