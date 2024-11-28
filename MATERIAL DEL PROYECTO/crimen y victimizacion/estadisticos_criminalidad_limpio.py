import pandas as pd
import matplotlib.pyplot as plt
import  scipy
pd.set_option('display.max_columns', None)
df= pd.read_csv('criminalidad_limpio2.csv')
print(df.head(200))
print(df.describe())

df.plot(kind='density', y='Nº Robo a personas')
plt.xlabel("Nº Robo a Personas")
plt.ylabel("Densiddad")
plt.title("Densidad de Nº Robo a Personas")
plt.show()
'''
df.plot(kind='density', y='expansion_hogar_personas')
plt.xlabel("Expansion hogar y personas")
plt.ylabel("Densiddad")
plt.title("Densidad de expansion hogar y personas")
plt.show()

df.plot(kind='density', y='expansion_16años_mas')
plt.xlabel("Expansion 16 años o mas")
plt.ylabel("Densiddad")
plt.title("Densidad de expansion 16 años o mas")
plt.show()'''