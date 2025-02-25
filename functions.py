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
    
    