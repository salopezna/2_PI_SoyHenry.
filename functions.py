import pandas as pd
import numpy as np
import ast
from datetime import datetime

def opciones_impresion(width=1000, expand=False, max_columns=None):
    """
    Configura las opciones de visualización de Pandas para imprimir DataFrames.

    Parámetros:
      - width (int): Ancho máximo de la salida (por defecto 1000).
      - expand (bool): Si es False, muestra el DataFrame en una sola línea si es posible (por defecto False).
      - max_columns (int o None): Número máximo de columnas a mostrar; None muestra todas.
    """
    pd.set_option('display.expand_frame_repr', expand)
    pd.set_option('display.max_columns', max_columns)
    pd.set_option('display.width', width)

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

def validar_df(df):
    """
    Valida un DataFrame, generando un resumen con información relevante de cada columna.
    Se omite la reindexación para evitar errores con etiquetas duplicadas.
    """
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
    return res

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
    
    