import pandas as pd
import numpy as np



try:
    
    # leer el documento
    df= pd.read_csv('victimizacion_robo_vivienda.csv')
    
    if df is None or df.empty:
        raise ValueError("DataFrame is none or empty")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    df= pd.DataFrame() # se crea una DataFrame vacio para evitar errores.

# verificar contenido
if not df.empty:
    print("El contenido del dataframe esta cargado correctamente")
    print(df.head())
else:
    print("El DataFrame esta vacio o no se puede leer el documento")
    exit()

# Eliminamos duplicados
df.drop_duplicates(inplace=True)

# Si existen valores nulos, se reemplazan con NaN
df.replace(['NULL', '', ' '], np.nan, inplace= True)

# Listas numericas que se analizaran
columnas_numericas= ['RV00','RV32','RV33','RV34','RV35','RV37','RV38','RV39','RV310','fexph','fexpp']

# Nos aseguramos de que todas las columnas especificadas sean de tipo numérico
for columnas in columnas_numericas:
    if columnas in df.columns:
        df[columnas]= pd.to_numeric(df[columnas], errors='coerce')

# Eliminamos los Outliers
def eliminar_outliers(df, columnas):
    for columna in columnas:
        Q1= df[columna].quantile(0.25)
        Q3= df[columna].quantile(0.75)
        IQR= Q3-Q1
        df = df[~((df[columna] < (Q1 - 1.5 * IQR)) | (df[columna] > (Q3 + 1.5 * IQR)))]
    return df

df_limpieza= eliminar_outliers(df, columnas_numericas)

# Guardar el DataFrame limpio en un archivo .csv
df_limpieza.to_csv(r"C:\Users\Personal\Desktop\Analisis de Datos\victimizacion_vivienda_limpio.csv", index=False)

# Mostrar mensaje de confirmación
print("El DataFrame limpio se ha guardado correctamente en 'victimizacion_vivienda_limpio.csv'")