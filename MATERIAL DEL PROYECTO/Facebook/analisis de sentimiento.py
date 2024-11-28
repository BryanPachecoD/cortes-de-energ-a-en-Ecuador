import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Leer datos
df= pd.read_csv('COMENTARIOS.CSV')

# Numero de Comentarios
num_comentarios= len(df)

# Analisis de Sentimiento
df['sentimiento'] = df['Comentarios'].apply(lambda x : TextBlob(x).sentiment.polarity)

# Frecuencia de Palabras
wordcloud= WordCloud(width= 800, height= 400, background_color= 'white').generate("".join(df['Comentarios']))
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Longitud de los Comentarios
df['longitud']= df['Comentarios'].apply(len)

# Resultados
print(f"Número de comentarios: {num_comentarios}")
print(f"Promedio de sentimiento: {df['sentimiento'].mean()}")
print(f"Longitud promedio de los comentarios: {df['longitud'].mean()}")
