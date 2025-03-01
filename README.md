---
# **✅ PROYECTO DE DATASCIENCE**
---
## **Análisis del Sector de Internet en Argentina (2014 a 3er Trim. 2024)**
### **Descripción**

La industria de las telecomunicaciones ha desempeñado un papel crucial en nuestra sociedad, facilitando la información a escala global y permitiendo la comunicación continua. La transferencia de datos y la comunicación se realizan principalmente a través de internet, líneas telefónicas fijas y móviles. Argentina está a la vanguardia en el desarrollo de las telecomunicaciones, contando con un total de 62,12 millones de conexiones en 2020. Dada la relevancia del tema para el país, he llevado a cabo un análisis exhaustivo que permite identificar el comportamiento de este sector a nivel nacional, enfocándome en el acceso al servicio de Internet y su relación con otros servicios de comunicaciones. El objetivo es generar recomendaciones para ofrecer una buena calidad de servicio, identificar oportunidades de crecimiento y plantear soluciones personalizadas para clientes actuales o potenciales.
---
### **Objetivos**
---
- **Extracción de datos:** Importar y leer datos de diversas fuentes en un único workbook.
- **Transformación y limpieza:** 
  - Normalizar y estandarizar nombres de campos.
  - Convertir y castear tipos de datos (por ejemplo, convertir cadenas a enteros).
  - Integrar información de diferentes hojas en una única estructura.
- **Análisis Exploratorio de Datos (EDA):** 
  - Generar gráficos y tablas para visualizar tendencias.
  - Calcular estadísticas descriptivas que permitan evaluar la calidad y consistencia de los datos.
---
### **Stack Tecnológico**
---
- **Lenguaje:** Python 3.12
- **Entorno:** Jupyter Notebook en Visual Studio Code
- **Librerías:**  
  - **Pandas**: Manipulación de datos.  
  - **NumPy**: Operaciones numéricas.  
  - **Matplotlib/Seaborn**: Visualización de datos.
- **Control de Versiones:** Git y GitHub
---
### **Estructura del Proyecto**
---
- `notebooks/`: Contiene los notebooks de ETL (`etl.ipynb`) y EDA (`eda.ipynb`).
- `data/`:  
  - `raw/`: Datos originales (Excel).
  - `processed/`: Datos transformados.
- `functions/`: Funciones reutilizables para el proceso ETL y EDA.
- `requirements.txt`: Dependencias del proyecto.
---
# Estructura del Proyecto
---

mi_proyecto/
│
├── 📁 data/                    # 📂 Datos crudos y procesados
│   ├── 📁 raw/                 # 📄 Datos originales (sin modificar)
│   ├── 📁 processed/           # 📄 Datos limpios y listos para análisis
│   └── 📁 external/            # 📄 Datos externos o de terceros
│
├── 01_ETL.ipynb            # 📊 Notebook para Exploración, Transformación y Carga inicial
├── 02_EDA.ipynb            # 📊 Notebook para Análisis exploratorio inicial   └── 02_EDA.ipynb            
│
├── 📁 src/                     # 🐍 Código fuente del proyecto
│   └── preprocess_data.py      # 📄 Funciones para cargar, transformación y limpieza de datos
│   └── build_features.py       # 📄 Creación y selección de variables
│   ├── evatrain_model.py       # 📄 Evaluación y Entrenamiento del modelo
│   └── visualize.py            # 📄 Funciones para visualización de gráficos y dashboards
│
├── 📁 models/                  # 🧠 Modelos entrenados y artefactos serializados
│   └── modelo_final.pkl        # 💾 Modelo entrenado
│
├── 📁 reports/                 # 📝 Reportes y resultados del proyecto
│   └── 📁 figures/             # 📊 Gráficos y visualizaciones
│
├── 📁 tests/                   # 🧪 Pruebas unitarias del código
│   └── test_data.py
│
├── 📁 docs/                    # 📖 Documentación adicional
│
├── requirements.txt            # 📋 Lista de dependencias
├── environment.yml             # 📋 Configuración del entorno Conda (opcional)
├── .gitignore                  # 🚫 Archivos/carpetas a ignorar en Git
├── README.md                   # 📖 Descripción general del proyecto
└── main.py                     # 🏁 Script principal para ejecutar el pipeline
---
### **Instrucciones de Uso**
---
1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/salopezna/2_PI_SoyHenry..git
---
