import pandas as pd
import numpy as np

# Para mostras todas las columnas del dataframe
pd.set_option('display.max_columns', None)

# Se importa el  archivo en formato .csv
archivo_csv = r"C:\Users\Personal\victimizacion_delito_personas.csv"

# Leer el archivo .csv y  controlar exepciones
try:
    df = pd.read_csv(archivo_csv)
    if df is None or df.empty:
        raise ValueError("DataFrame is None or empty")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    df = pd.DataFrame()  # Se crea un DataFrame vacío para evitar  errores

# Mostramos las primeras filas del DataFrame para verificar su contenido
if not df.empty:
    print("Contenido del DataFrame cargado correctamente:")
    print(df.head())
else:
    print("El DataFrame está vacío o no se pudo leer el archivo correctamente.")
    exit()

# Eliminamos duplicados
df.drop_duplicates(inplace=True)

# Reemplazar 'NULL' y cadenas vacías con NaN
df.replace(['NULL', ' ', ''], np.nan, inplace=True)

# Lista de columnas numéricas que se analizarán
columnas_numericas = ['RP00', 'RP41', 'RP42', 'RP431', 'RP432', 'RP433', 'RP434', 'RP435', 'RP451', 'RP452', 'RP453',
                      'RP454', 'RP455', 'RP461', 'RP462', 'RP463', 'RP464', 'RP465', 'RP471', 'RP472', 'RP473', 'RP474', 'RP475',
                      'RP481', 'RP482', 'RP483', 'RP484', 'RP485', 'RP491', 'RP492', 'RP493', 'RP494', 'RP495', 'RP4101', 'RP4102',
                      'RP4103', 'RP4104', 'RP4105', 'fexph', 'fexpp']

# Nos aseguramos de que todas las columnas especificadas sean de tipo numérico
for columna in columnas_numericas:
    if columna in df.columns:
        df[columna] = pd.to_numeric(df[columna], errors='coerce')

# Reemplazar los valores nulos en columnas numéricas con la mediana de cada columna
for columna in columnas_numericas:
    if columna in df.columns:
        mediana = df[columna].median()
        df[columna] = df[columna].fillna(mediana)

# Función para eliminar outliers en varias columnas
def eliminacion_outliers(df, columnas):
    for columna in columnas:
        if columna in df.columns:
            Q1 = df[columna].quantile(0.25)
            Q3 = df[columna].quantile(0.75)
            IQR = Q3 - Q1
            df = df[~((df[columna] < (Q1 - 1.5 * IQR)) | (df[columna] > (Q3 + 1.5 * IQR)))]
    return df

# Aplicar la función al DataFrame
df_limpieza = eliminacion_outliers(df, columnas_numericas)

# Guardar el DataFrame limpio en un archivo .csv
df_limpieza.to_csv(r"C:\Users\Personal\Desktop\Analisis de Datos\criminalidad_limpio.csv", index=False)

# Mostrar mensaje de confirmación
print("El DataFrame limpio se ha guardado correctamente en 'criminalidad_limpio.csv'")
