import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
df= pd.read_csv('criminalidad_limpio.csv')
renombrar_columnas={'RP00':'Nº Robo a personas', 'RP41':'Victima de delito como:', 'RP42':'Veces que le sucedio el delito', 'RP431':'mes_delito ', 'RP432':'mes_delito2', 
                   'RP433':'mes_delito3', 'RP434':'mes_delito4', 'RP435':'mes_delito5', 'RP451':'ciudad_delito', 'RP452':'ciudad_delito2', 'RP453':'ciudad_delito3',
                    'RP454':'ciudad_delito4', 'RP455':'ciudad_delito5', 'RP461':'preente_momento_delito', 'RP462':'preente_momento_delito2', 'RP463':'preente_momento_delito3', 'RP464':'preente_momento_delito4', 'RP465':'preente_momento_delito5', 
                    'RP471':'se_dio_cuenta', 'RP472':'se_dio_cuenta2', 'RP473':'se_dio_cuenta3', 'RP474':'se_dio_cuenta4', 'RP475':'se_dio_cuenta5',
                    'RP481':'fue_anunciado', 'RP482':'fue_anunciado2', 'RP483':'fue_anunciado3', 'RP484':'fue_anunciado4', 'RP485':'fue_anunciado5', 'RP491':'hubo_averiguacion_previa', 'RP492':'hubo_averiguacion_previa2', 
                    'RP493':'hubo_averiguacion_previa3', 'RP494':'hubo_averiguacion_previa4', 'RP495':'hubo_averiguacion_previa5', 'RP4101':'ultimo_delito_tipo', 'RP4102':'ultimo_delito_tipo2',
                    'RP4103':'ultimo_delito_tipo3', 'RP4104':'ultimo_delito_tipo4', 'RP4105':'ultimo_delito_tipo5', 'fexph':'expansion_hogar_personas', 'fexpp':'expansion_16años_mas'}

df.rename(columns=renombrar_columnas, inplace=True)
df.to_csv(r"C:\Users\Personal\Desktop\Analisis de Datos\criminalidad_limpio2.csv", index=False)
print("El DataFrame limpio se ha guardado correctamente en 'criminalidad_limpio2.csv'")