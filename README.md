---
### ✅ **ANÁLISIS DEL SECTOR DE INTERNET EN ARGENTINA**
#### *La industria de las telecomunicaciones ha desempeñado un papel crucial en nuestra sociedad, facilitando la información a escala global y permitiendo la comunicación continua. La transferencia de datos y la comunicación se realizan principalmente a través de internet, líneas telefónicas fijas y móviles. Argentina está a la vanguardia en el desarrollo de las telecomunicaciones, contando con un total de 62,12 millones de conexiones en 2020. Dada la relevancia del tema para el país, he llevado a cabo un análisis exhaustivo que permite identificar el comportamiento de este sector a nivel nacional, enfocándome en el acceso al servicio de Internet y su relación con otros servicios de comunicaciones. El objetivo es generar recomendaciones para ofrecer una buena calidad de servicio, identificar oportunidades de crecimiento y plantear soluciones personalizadas para clientes actuales o potenciales.*
---

# 2_PI_SoyHenry
# 2_PI_SoyHenry..

### 💡 **Organización del Proyecto para el Desarrollo del Análisis del Sector**

Si en **Jupyter Notebook** no se ve bien por los emojis o la alineación:

- **Usa solo caracteres ASCII** para estructuras más simples:
  
```markdown
# Estructura del Proyecto

mvp_pi2/
│
├── datos/                       
│   ├── crudos_raw/              
│   └── transformados_processed/ 
│
├── notebooks/                   
│   └── eda_notebook.ipynb       
│   └── etl_notebook.ipynb       
│
├── services/                         
│   ├── __init__.py              
│   ├── etl.py                   
│   ├── api.py                   
│   └── validation.py            
│
├── tests/                       
│   └── test.py              
│
├── requirements.txt             
├── README.md                    
└── main.py  
#### *A partir de fuentes de información como el portal de ENACOM (https://indicadores.enacom.gob.ar/datos-abiertos), se obtienen datos asociados al comportamiento histórico trimestral desde el año 2014 hasta el tercer trimestre de 2024 a nivel nacional y, en algunos casos, a nivel provincial. Todos estos datos están concentrados en múltiples hojas dentro de un solo archivo de Excel.*