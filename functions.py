import pandas as pd
import numpy as np
import ast
from datetime import datetime

import pandas as pd

def opciones_impresion(width=1000, expand=False, max_columns=None, max_rows=None, max_colwidth=None, colheader_justify='left'):
    """
    Configura las opciones de visualización de Pandas para imprimir DataFrames.
    
    Parámetros:
      - width (int): Ancho máximo de la salida (por defecto 1000).
      - expand (bool): Si es False, muestra el DataFrame en una sola línea si es posible (por defecto False).
      - max_columns (int o None): Número máximo de columnas a mostrar; None muestra todas.
      - max_rows (int o None): Número máximo de filas a mostrar; None muestra todas.
      - max_colwidth (int o None): Ancho máximo de cada columna; None no trunca.
      - colheader_justify (str): Justificación de las cabeceras de columna (por ejemplo, 'left', 'right' o 'center').
    """
    pd.set_option('display.expand_frame_repr', expand)
    pd.set_option('display.max_columns', max_columns)
    pd.set_option('display.width', width)
    pd.set_option('display.max_rows', max_rows)
    pd.set_option('display.max_colwidth', max_colwidth)
    pd.set_option('display.colheader_justify', colheader_justify)

def renombrar_campos(df_dict, nuevos_nombres):
    """
    Renombra columnas de las hojas contenidas en df_dict según los renombramientos definidos en nuevos_nombres.
    
    Parámetros:
      - df_dict (dict): Diccionario donde cada clave es el nombre de la hoja y cada valor es un DataFrame.
      - nuevos_nombres (dict): Diccionario de mapeo, donde cada clave es el nombre de la hoja y el valor 
                         es otro diccionario con el mapeo de columnas (llave: nombre original, valor: nuevo nombre).
                         
    Retorna:
      dict: El mismo diccionario df_dict, con las hojas que se encuentran en nuevos_nombres renombradas según lo indicado.
    """
    for hoja, mapping in nuevos_nombres.items():
        if hoja in df_dict:
            df_dict[hoja] = df_dict[hoja].rename(columns=mapping)
        else:
            print(f"La hoja '{hoja}' no se encontró en el diccionario.")
    return df_dict

def load_excel_sheets(file_path):
    """
    Carga un archivo Excel y devuelve un diccionario con los nombres de las hojas y sus respectivos dataframes.
    """
    try:
        # Cargar todas las hojas en un diccionario
        sheets = pd.read_excel(file_path, sheet_name=None, engine="openpyxl")
        return sheets
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return {}

# Función para validar un DataFrame, generando un resumen con información relevante de cada columna.
"""def validar_df(df):
    res = pd.DataFrame({
        "Tipo de Dato": df.dtypes,
        "Valores No Nulos": df.count(),
        "Valores Nulos": df.isna().sum(),
        "Valores Únicos": df.astype(str).nunique(dropna=True),
        "Valores Cero": (df == 0).sum(),
        "Inconsistentes ('?')": df.isin(['?']).sum(),
        "Valores Vacíos (string)": df.isin(["", " ", "NA", "NULL", "None"]).sum(),
        "valores_negativos": (df.select_dtypes(include=['int64', 'float64']) < 0).sum()
    })
    res = res.reindex(df.columns)
    return res"""

"""def validar_df(df):
    
    Valida un DataFrame, generando un resumen con información relevante de cada columna.
    Se omite la reindexación para evitar errores con etiquetas duplicadas.
    
    res = pd.DataFrame({
        "Tipo de Dato": df.dtypes,
        "Valores No Nulos": df.count(),
        "Valores Nulos": df.isna().sum(),
        "Valores Únicos": df.astype(str).nunique(dropna=True),
        "Valores Cero": (df == 0).sum(),
        "Inconsistentes ('?')": df.isin(['?']).sum(),
        "Valores Vacíos (string)": df.isin(["", " ", "NA", "NULL", "None"]).sum(),
        "valores_negativos": (df.select_dtypes(include=['int64', 'float64']) < 0).sum()
    })
    return res"""


#######################################################
# Funciones para validar DataFrames
#######################################################

import pandas as pd
import numpy as np
import datetime
import ast

def validar_df(df):
    """
    Valida un DataFrame generando un resumen con información clave de cada columna.
    
    Para cada columna se calcula:
      - Tipo de Dato
      - Int: Cantidad de valores no nulos que sean de tipo entero (usando isinstance(x, int)).
      - Int64: Conteo de valores no nulos si la columna tiene dtype "Int64" (tipo entero nullable de pandas).
      - Float: Cantidad de valores no nulos de tipo float.
      - Bool: Cantidad de valores no nulos de tipo bool.
      - DateT: Cantidad de valores no nulos de tipo datetime (pd.Timestamp o datetime.datetime).
      - Str: Cantidad de valores no nulos de tipo str.
      - Ctgory: Cantidad de valores no nulos en columnas categóricas (si la columna es de tipo category).
      - No_Nulos: Número de valores no nulos.
      - Nulos: Número de valores nulos.
      - Únicos: Número de valores únicos (tras convertir a str).
      - Ceros: Conteo de valores iguales a cero (solo para columnas numéricas).
      - Vacíos (string): Conteo de valores vacíos o equivalentes ("" o "NA", "NULL", "None") en columnas de texto.
      - Media, Desviación_Std, Mínimo, Q1_25%, Q2_50% (Mediana), Q3_75%, Máximo, Negativos: Estadísticas numéricas para columnas numéricas 
        (NaN en otros casos).
      
    Retorna:
      pd.DataFrame: Un resumen transpuesto, donde cada fila corresponde a una columna del DataFrame original.
    """
    summary = {}
    
    for col in df.columns:
        s = df[col]
        # Si 's' es un DataFrame (por nombres duplicados), tomamos la primera columna.
        if isinstance(s, pd.DataFrame):
            print(f"Advertencia: La columna '{col}' aparece duplicada. Se usará la primera aparición.")
            s = s.iloc[:, 0]
        
        # Tipo de dato de la columna.
        tipo = s.dtype
        
        # Conteo de valores no nulos y nulos.
        val_no_nulos = s.count()
        val_nulos = s.isna().sum()
        
        # Número de valores únicos (tras convertir a str para homogeneizar).
        val_unicos = s.astype(str).nunique(dropna=True)
        
        # Conteo de ceros (solo para columnas numéricas).
        val_cero = (s == 0).sum() if pd.api.types.is_numeric_dtype(s) else np.nan
        
        # Conteo de valores vacíos en columnas de texto.
        if pd.api.types.is_string_dtype(s):
            val_vacios = s.apply(lambda x: x.strip() if isinstance(x, str) else x).isin(["", "NA", "NULL", "None"]).sum()
        else:
            val_vacios = np.nan
        
        # Conteo de tipos en los valores no nulos.
        # Usamos np.issubdtype para detectar valores de tipo entero o flotante
        count_int = sum(isinstance(x, int) for x in s.dropna())
        count_float = sum(isinstance(x, float) for x in s.dropna())
        count_bool = sum(isinstance(x, bool) for x in s.dropna())
        count_datetime = sum(isinstance(x, (pd.Timestamp, datetime.datetime)) for x in s.dropna())
        count_str = sum(isinstance(x, str) for x in s.dropna())
        count_category = s.dropna().shape[0] if pd.api.types.is_categorical_dtype(s) else np.nan
        
        # Nuevo campo: conteo de valores enteros de tipo "Int64"
        # Se verifica si la columna tiene dtype "Int64" (el tipo nullable de pandas)
        count_int64 = s.dropna().shape[0] if s.dtype.name == "Int64" else 0
        
        # Estadísticas numéricas (solo para columnas numéricas)
        if pd.api.types.is_numeric_dtype(s):
            media = s.mean()
            std = s.std()
            minimo = s.min()
            q1 = s.quantile(0.25)
            mediana = s.median()
            q3 = s.quantile(0.75)
            maximo = s.max()
            negativos = (s < 0).sum()
        else:
            media = std = minimo = q1 = mediana = q3 = maximo = negativos = np.nan
        
        summary[col] = {
            "Tipo de Dato": tipo,
            "Int": count_int,
            "Int64": count_int64,
            "Float": count_float,
            "Bool": count_bool,
            "DateT": count_datetime,
            "Str": count_str,
            "Ctgory": count_category,
            "No_Nulos": val_no_nulos,
            "Nulos": val_nulos,
            "Únicos": val_unicos,
            "Ceros": val_cero,
            "Vacíos (string)": val_vacios,
            "Media": media,
            "Desviación_Std": std,
            "Mínimo": minimo,
            "Q1_25%": q1,
            "Q2_50%": mediana,
            "Q3_75%": q3,
            "Máximo": maximo,
            "Negativos": negativos
        }
    
    return pd.DataFrame(summary).T

'''
def validar_df(df):
    """
    Valida un DataFrame generando un resumen con información clave de cada columna.
    
    Para cada columna se calcula:
      - Tipo de Dato
      - Int: Cantidad de valores no nulos de tipo int.
      - Float: Cantidad de valores no nulos de tipo float.
      - Bool: Cantidad de valores no nulos de tipo bool.
      - DateT: Cantidad de valores no nulos de tipo datetime (pd.Timestamp o datetime.datetime).
      - Str: Cantidad de valores no nulos de tipo str.
      - Ctgory: Cantidad de valores no nulos en columnas categóricas (si la columna es de tipo category).
      - Val_No_Nulos: Número de valores no nulos.
      - Val_Nulos: Número de valores nulos.
      - Val_Únicos: Número de valores únicos (tras convertir a str).
      - Val_Cero: Conteo de valores iguales a cero (solo para columnas numéricas).
      - Val_Vacíos (string): Conteo de valores vacíos o equivalentes ("" o "NA", "NULL", "None") en columnas de texto.
      - Media, Desviación_Std, Mínimo, Q1_25%, Q2_50% (Mediana), Q3_75%, Máximo, Negativos: Estadísticas numéricas para columnas numéricas 
        (NaN en otros casos).
      
    Retorna:
      pd.DataFrame: Un resumen transpuesto, donde cada fila corresponde a una columna del DataFrame original.
    """
    summary = {}
    
    for col in df.columns:
        s = df[col]
        # Si 's' es un DataFrame (lo que puede ocurrir si el nombre de la columna está duplicado),
        # tomamos la primera columna.
        if isinstance(s, pd.DataFrame):
            print(f"Advertencia: La columna '{col}' aparece duplicada. Se usará la primera aparición.")
            s = s.iloc[:, 0]
        
        # Tipo de dato de la columna.
        tipo = s.dtype
        
        # Conteo de valores no nulos y nulos.
        val_no_nulos = s.count()
        val_nulos = s.isna().sum()
        
        # Número de valores únicos (tras convertir a str para homogeneizar).
        val_unicos = s.astype(str).nunique(dropna=True)
        
        # Conteo de ceros (solo para columnas numéricas).
        val_cero = (s == 0).sum() if pd.api.types.is_numeric_dtype(s) else np.nan
        
        # Conteo de valores vacíos en columnas de texto.
        if pd.api.types.is_string_dtype(s):
            val_vacios = s.apply(lambda x: x.strip() if isinstance(x, str) else x).isin(["", "NA", "NULL", "None"]).sum()
        else:
            val_vacios = np.nan
        
        # Conteo de tipos en los valores no nulos.
        count_int = sum(isinstance(x, int) for x in s.dropna())
        count_float = sum(isinstance(x, float) for x in s.dropna())
        count_bool = sum(isinstance(x, bool) for x in s.dropna())
        count_datetime = sum(isinstance(x, (pd.Timestamp, datetime.datetime)) for x in s.dropna())
        count_str = sum(isinstance(x, str) for x in s.dropna())
        count_category = s.dropna().shape[0] if pd.api.types.is_categorical_dtype(s) else np.nan
        
        # Estadísticas numéricas (solo para columnas numéricas)
        if pd.api.types.is_numeric_dtype(s):
            media = s.mean()
            std = s.std()
            minimo = s.min()
            q1 = s.quantile(0.25)
            mediana = s.median()
            q3 = s.quantile(0.75)
            maximo = s.max()
            negativos = (s < 0).sum()
        else:
            media = std = minimo = q1 = mediana = q3 = maximo = negativos = np.nan
        
        summary[col] = {
            "Tipo de Dato": tipo,
            "Int": count_int,
            "Float": count_float,
            "Bool": count_bool,
            "DateT": count_datetime,
            "Str": count_str,
            "Ctgory": count_category,
            "No_Nulos": val_no_nulos,
            "Nulos": val_nulos,
            "Únicos": val_unicos,
            "Ceros": val_cero,
            "Vacíos (string)": val_vacios,
            "Media": media,
            "Desvi_Std": std,
            "Mínimo": minimo,
            "Q1_25%": q1,
            "Q2_50%": mediana,
            "Q3_75%": q3,
            "Máximo": maximo,
            "Negativos": negativos
        }
    
    return pd.DataFrame(summary).T
'''
#######################################################

import pandas as pd

def generar_diccionario_tipos(df_dict, sheet_name):
    """
    Genera un string que representa un diccionario de tipos de datos para cada columna de la hoja 
    especificada en el diccionario de DataFrames.

    La salida tendrá un formato similar a:
    
    diccionario_tipos_Dial-BAf = {
        "Año": "Int64",
        "Trimestre": "Int64",
        "Provincia": "category",
        "Tot_B_Ancha_Fija_x_Prov": "Int64",
        "Tot_DialUp_x_Prov": float,
        "Tot_DialUp_+_B_Ancha_Fija_x_Prov": "Int64"
    }
    
    Parámetros:
      - df_dict (dict): Diccionario de DataFrames (por ejemplo, el resultado de pd.read_excel(..., sheet_name=None)).
      - sheet_name (str): El nombre de la hoja a procesar.
    
    Retorna:
      str: Un string con la asignación del diccionario de tipos.
    """
    # Extrae el DataFrame correspondiente a la hoja
    if sheet_name not in df_dict:
        raise KeyError(f"El diccionario no contiene la hoja '{sheet_name}'")
    df = df_dict[sheet_name]
    
    header = f"diccionario_tipos_{sheet_name}"
    result = f"{header} = {{\n"
    
    for col in df.columns:
        dtype = df[col].dtype
        
        # Determinar la representación deseada según el tipo de dato.
        if isinstance(dtype, pd.CategoricalDtype):
            tipo_str = '"category"'
        elif pd.api.types.is_object_dtype(df[col]):
            tipo_str = "str"
        else:
            if dtype.name in ['int64', 'Int64']:
                tipo_str = '"Int64"'
            elif dtype.name in ['float64']:
                tipo_str = "float"
            elif pd.api.types.is_datetime64_any_dtype(df[col]):
                tipo_str = "pd.Timestamp"
            else:
                tipo_str = f'"{dtype.name}"'
        result += f'    "{col}": {tipo_str},\n'
    result += "}"
    return result

#######################################################

# Función para obtener las hojas que contienen todos los campos indicados en 'lista_campos' y sus dimensiones.
def obtener_hojas_validas(lista_campos, df_dict, hojas_excluir=None):
    """
    Valida y crea una lista de hojas que contienen todos los campos indicados en 'lista_campos'.
    
    Parámetros:
      - lista_campos (list): Lista de nombres de campos requeridos.
      - df_dict (dict): Diccionario con DataFrames (clave: nombre de la hoja, valor: DataFrame).
      - hojas_excluir (list): Lista de nombres de hojas a excluir de la validación. 
                              Esta lista puede contener strings o tuplas donde el primer elemento es el nombre.
    
    Retorna:
      - list: Lista de tuplas (nombre de hoja, dimensionalidad) para las hojas que cumplen con tener todos los campos requeridos.
    """
    if hojas_excluir is None:
        hojas_excluir = []
    
    # Asegurarse de que la lista de exclusión sea solo de nombres (strings)
    hojas_excluir_nombres = []
    for item in hojas_excluir:
        if isinstance(item, tuple):
            hojas_excluir_nombres.append(item[0])
        else:
            hojas_excluir_nombres.append(item)
    
    hojas_validas = []
    for hoja, df in df_dict.items():
        # Si la hoja ya está en la lista de exclusión, la omitimos.
        if hoja in hojas_excluir_nombres:
            continue
        
        # Verificamos que la hoja contenga todos los campos requeridos.
        if all(campo in df.columns for campo in lista_campos):
            hojas_validas.append((hoja, df.shape))
    
    return hojas_validas

# Función para fusionar dataframes incluidos en un listado y que se guian por un campo id en comun:
"""def fusionar_por_campo(campo_id, lista_hojas, df_dict):
    
    Fusiona (merge) las hojas especificadas en 'lista_hojas' usando el campo único 'campo_id' como llave de unión.
    
    Parámetros:
      - campo_id (str): Nombre del campo que se usará como llave para realizar la fusión entre DataFrames 
                        (por ejemplo, "id_año_trimestre").
      - lista_hojas (list): Lista de nombres (strings) de las hojas (o claves) a fusionar.
      - df_dict (dict): Diccionario que contiene los DataFrames, donde la clave es el nombre de la hoja y el valor es el DataFrame.
      
    Retorna:
      DataFrame: Resultado de la fusión externa (outer join) de los DataFrames que cumplen con las condiciones.
    
    # Inicializa la variable que contendrá el DataFrame fusionado.
    df_fusionado = None
    
    # Recorre cada hoja en la lista proporcionada.
    for hoja in lista_hojas:
        # Verifica si la hoja se encuentra en el diccionario; si no, la omite.
        if hoja not in df_dict:
            print(f"La hoja '{hoja}' no se encuentra en el diccionario. Se omite.")
            continue
        
        # Obtiene el DataFrame correspondiente a la hoja.
        df = df_dict[hoja]
        
        # Verifica que el DataFrame contenga el campo clave indicado; de lo contrario, la omite.
        if campo_id not in df.columns:
            print(f"La hoja '{hoja}' no contiene el campo '{campo_id}'. Se omite.")
            continue
        
        # Si es el primer DataFrame válido, lo copia en df_fusionado.
        if df_fusionado is None:
            df_fusionado = df.copy()
        else:
            # Para los siguientes DataFrames, realiza una fusión externa usando el campo clave.
            # La opción suffixes=('', '_dup') se utiliza para agregar un sufijo a las columnas duplicadas.
            df_fusionado = pd.merge(df_fusionado, df, on=campo_id, how='outer', suffixes=('', '_dup'))
    
    # Si no se fusionó ningún DataFrame (ninguna hoja era válida), se retorna un DataFrame vacío.
    if df_fusionado is None:
        return pd.DataFrame()
    
    # Retorna el DataFrame fusionado resultante.
    return df_fusionado"""

######################################################
# Función para validar y contar datos en campos especificos de un df:
import pandas as pd

def datos_unicos_hoja(item, campos):
    """
    Extrae los valores únicos de las columnas especificadas en 'campos' a partir de un item, y también
    cuenta cuántas veces aparece cada valor único. El parámetro 'item' es una tupla (sheet_name, data),
    donde data puede ser un DataFrame o un diccionario de DataFrames.
    
    Parámetros:
      - item (tuple): Una tupla (sheet_name, data) donde:
             * sheet_name (str): El nombre de la hoja.
             * data: Puede ser un DataFrame o un diccionario de DataFrames.
      - campos (dict): Diccionario donde cada clave es el nombre de la columna y el valor es 1 (imprimir)
                       o 0 (no imprimir) la información.
    
    Retorna:
      dict: Un diccionario donde cada clave es el nombre del campo y el valor es una tupla:
            (lista ordenada de valores únicos, diccionario de conteo de cada valor).
            Para columnas numéricas, se convierten los valores a enteros; de lo contrario, a cadenas.
    """
    sheet_name, data = item
    # Si data es un diccionario, extrae el DataFrame correspondiente a sheet_name.
    if isinstance(data, dict):
        if sheet_name in data:
            df = data[sheet_name]
        else:
            raise KeyError(f"El diccionario no contiene la hoja '{sheet_name}'")
    else:
        df = data

    result = {}
    for campo, imprimir_flag in campos.items():
        if campo in df.columns:
            # Convertir valores y obtener conteo
            if pd.api.types.is_numeric_dtype(df[campo]):
                # Para valores numéricos, convertir a int
                valores = sorted([int(x) for x in df[campo].dropna().unique()])
                # Obtenemos los conteos, convirtiendo las claves a int
                counts = {int(k): v for k, v in df[campo].dropna().value_counts().items()}
            else:
                valores = sorted([str(x) for x in df[campo].dropna().unique()])
                counts = {str(k): v for k, v in df[campo].dropna().value_counts().items()}
            result[campo] = (valores, counts)
            if imprimir_flag == 1:
                print(f"En la hoja '{sheet_name}', el campo {campo} tiene {len(valores)} valores únicos y son:\n{counts}\n")
        else:
            result[campo] = ([], {})
            if imprimir_flag == 1:
                print(f"En la hoja '{sheet_name}', el campo {campo} no se encuentra en el DataFrame.\n")
    return result

#######################################################

import unicodedata

def normalizar_texto(texto):
    """
    Elimina acentos y otros signos diacríticos de una cadena.
    """
    # Normaliza a forma 'NFKD' y codifica en ASCII ignorando errores, luego decodifica.
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

#######################################################

import pandas as pd
import re

def reemplazar_valor_en_hojas(df_dict, campo, cambio):
    """
    Recorre un diccionario de DataFrames (hojas de un Excel) y reemplaza en cada hoja
    los valores de la columna especificada que contengan la palabra a buscar, sustituyéndola
    por el nuevo valor.
    
    Parámetros:
      - df_dict (dict): Diccionario de DataFrames, donde la clave es el nombre de la hoja y 
                        el valor es el DataFrame.
      - campo (str): El nombre de la columna en la que se realizará la búsqueda y el reemplazo.
      - cambio (tuple): Una tupla (buscar, reemplazo) donde:
            * buscar (str): La palabra a buscar (la búsqueda es insensible a mayúsculas).
            * reemplazo (str): El valor con el que se reemplazará la palabra encontrada.
            
    Retorna:
      dict: El mismo diccionario de DataFrames, con la modificación aplicada a cada hoja donde exista la columna.
    """
    buscar, reemplazo = cambio
    for hoja, df in df_dict.items():
        if campo in df.columns:
            # Convertir la columna a string para asegurarse de que el método .str.replace funcione.
            df[campo] = df[campo].astype(str).str.replace(r'(?i)' + re.escape(buscar), reemplazo, regex=True)
            #print(f"En la hoja '{hoja}', se cambia '{buscar}' por '{reemplazo}' en el campo '{campo}'.")
        else:
            print(f"En la hoja '{hoja}', el campo '{campo}' no se encuentra.")
    return df_dict

#######################################################

import pandas as pd
import datetime
import re

def convertidor_tipo_dato_campo(df_dict, campo, tipo_objetivo):
    """
    Recorre un diccionario de DataFrames y, para cada hoja que contenga la columna especificada (campo),
    convierte esa columna al tipo indicado (tipo_objetivo).

    Parámetros:
      - df_dict (dict): Diccionario de DataFrames (por ejemplo, el resultado de pd.read_excel(..., sheet_name=None)).
      - campo (str): Nombre de la columna a convertir.
      - tipo_objetivo: Tipo al que se desea convertir la columna. Por ejemplo, int o "Int64" (para enteros nullable),
                       float, bool, datetime, etc.
    
    Retorna:
      dict: El mismo diccionario de DataFrames, con la conversión aplicada en las hojas que contienen la columna.
    """
    for sheet, df in df_dict.items():
        if campo in df.columns:
            # Para enteros, se asume que la columna puede tener valores con caracteres extraños,
            # por lo que se extraen únicamente los dígitos y se convierte al tipo entero nullable "Int64".
            if tipo_objetivo in [int, "Int64"]:
                # Se convierte la columna a string, se extrae la primera secuencia de dígitos (uno o más)
                # y se convierte a número. Luego se asigna el tipo "Int64".
                df[campo] = pd.to_numeric(
                    df[campo].astype(str).str.extract(r'(\d+)')[0],
                    errors='coerce'
                ).astype("Int64")
            elif tipo_objetivo == float:
                df[campo] = pd.to_numeric(df[campo], errors='coerce')
            elif tipo_objetivo == bool:
                df[campo] = df[campo].apply(lambda x: str(x).strip().lower() in ['true', '1'] if pd.notna(x) else False)
            elif tipo_objetivo in [datetime.datetime, pd.Timestamp]:
                df[campo] = pd.to_datetime(df[campo], errors='coerce')
            else:
                # Para otros tipos, se usa la conversión estándar.
                df[campo] = df[campo].astype(tipo_objetivo)
        else:
            print(f"En la hoja '{sheet}', el campo '{campo}' no se encuentra.")
    return df_dict

#######################################################


def fusionar_por_campos(campo_id, lista_hojas, df_dict):
    """
    Fusiona (merge) las hojas indicadas en 'lista_hojas' usando los campos en 'campo_id'
    como llaves para la unión a nivel de cada fila.
    
    Para cada DataFrame en la lista, se verifica que contenga todos los campos indicados en 
    'campo_id'. Luego, se fusionan los DataFrames mediante un outer join, de modo que se combinan 
    aquellas filas donde el valor de cada campo en 'campo_id' coincide en ambos DataFrames.
    
    Por ejemplo, si 'campo_id' es ["Año", "Trimestre"] y se tienen tres DataFrames que incluyen una fila 
    con Año = 2024 y Trimestre = 3, entonces las filas correspondientes a esos valores se fusionarán en 
    una única fila, combinando la información de las hojas involucradas.
    
    Parámetros:
      - campo_id (list): Lista de nombres de campos que se utilizarán como llaves para la fusión 
                         (por ejemplo, ["Año", "Trimestre"]).
      - lista_hojas (list): Lista de nombres (strings) de las hojas (claves) a fusionar.
      - df_dict (dict): Diccionario que contiene los DataFrames, donde la clave es el nombre de la hoja 
                        y el valor es el DataFrame.
      
    Retorna:
      DataFrame: Resultado de la fusión externa (outer join) de los DataFrames, combinando las filas 
                 donde los valores de los campos en 'campo_id' coinciden.
    """
    df_fusionado = None

    for hoja in lista_hojas:
        # Verifica si la hoja se encuentra en el diccionario; si no, la omite.
        if hoja not in df_dict:
            print(f"La hoja '{hoja}' no se encuentra en el diccionario. Se omite.")
            continue

        # Obtiene el DataFrame correspondiente a la hoja.
        df = df_dict[hoja]

        # Verifica que el DataFrame contenga todos los campos indicados en 'campo_id'.
        if not all(campo in df.columns for campo in campo_id):
            print(f"La hoja '{hoja}' no contiene alguno de los campos {campo_id}. Se omite.")
            continue

        # Si es el primer DataFrame válido, lo copia en df_fusionado.
        if df_fusionado is None:
            df_fusionado = df.copy()
        else:
            # Fusiona el DataFrame actual con el acumulado usando un outer join.
            # Esto combina las filas donde los valores en los campos de 'campo_id' coinciden.
            df_fusionado = pd.merge(df_fusionado, df, on=campo_id, how='outer', suffixes=('', '_dup'))

    # Si no se fusionó ningún DataFrame, retorna un DataFrame vacío.
    if df_fusionado is None:
        return pd.DataFrame()
    
    return df_fusionado





# Función para convertir los tipos de datos de las columnas de un DataFrame según un diccionario de tipos.
def convertir_tipos(df, diccionario):
    """
    Convierte los tipos de datos de las columnas de un DataFrame según un diccionario de tipos.
    Parámetros:
    ------------
    df : pd.DataFrame - DataFrame a convertir.
    diccionario : dict - Diccionario con los tipos de datos esperados para cada columna.
    Retorno:
    ---------
    pd.DataFrame - DataFrame con los tipos de datos convert
    """
    for columna, tipo_esperado in diccionario.items():
        # Primero se verifica que la columna exista en el DataFrame.
        if columna in df.columns:
            # Si el tipo esperado es 'int', se convierte la columna a número entero:
            # 1. pd.to_numeric intenta convertir a número; en caso de error, reemplaza con NaN.
            # 2. fillna(0) reemplaza los NaN por 0.
            # 3. astype(int) convierte la columna a entero.
            if tipo_esperado == int:
                df[columna] = pd.to_numeric(df[columna], errors='coerce').fillna(0).astype(int)
            # Si el tipo esperado es 'float', se convierte la columna a número flotante.
            elif tipo_esperado == float:
                df[columna] = pd.to_numeric(df[columna], errors='coerce')
            # Si el tipo esperado es 'bool', se convierte la columna a booleano.
            # La conversión se hace comparando el valor (tras limpiarlo) con 'true' o '1'.
            elif tipo_esperado == bool:
                df[columna] = df[columna].apply(lambda x: str(x).strip().lower() in ['true', '1'] if pd.notna(x) else False)
            # Si el tipo esperado es una lista o un diccionario, se verifica si el valor es una cadena
            # y se utiliza la función auxiliar 'convertir_a_estructura' para intentar convertirlo.
            elif tipo_esperado in [list, dict]:
                df[columna] = df[columna].apply(lambda x: convertir_a_estructura(x, tipo_esperado) if isinstance(x, str) else x)
            # Si el tipo esperado es una fecha (ya sea 'datetime' o 'pd.Timestamp'),
            # se convierte la columna a formato datetime usando pd.to_datetime.
            elif tipo_esperado in [datetime, pd.Timestamp]:
                df[columna] = pd.to_datetime(df[columna], errors='coerce')
            # En caso de que no se trate de un tipo especial, se convierte la columna a cadena de texto.
            else:
                df[columna] = df[columna].astype(str).fillna("")
    # Se retorna el DataFrame con las conversiones aplicadas.
    return df

# Función auxiliar para convertir strings en listas o diccionarios de forma segura
def convertir_a_estructura(valor, tipo_esperado):
    """
    Convierte un valor string en una lista o diccionario si es posible, de lo contrario retorna el valor original.

    Parámetros:
    -----------
    valor : str
        Valor que potencialmente es una lista o un diccionario en formato string.
    tipo_esperado : type
        Tipo esperado (list o dict).

    Retorno:
    --------
    list/dict/None
        Retorna el objeto convertido o None si la conversión falla.
    """
    try:
        if isinstance(valor, str):
            resultado = ast.literal_eval(valor)
            return resultado if isinstance(resultado, tipo_esperado) else None
        return valor  # Si ya es list o dict, lo devuelve tal cual
    except (ValueError, SyntaxError):
        return None
    
    