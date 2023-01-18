import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

file = "C:\\Users\\ATOU\\OneDrive - Axess OnLine\\Documents\\1. PROJETS\\PYTHON - ANALYSE DE SENTIMENTS\\CODE\\DATA\\Hippopotamus_social.csv"

df = pd.read_csv(file, encoding='utf-16', sep='\t')

#Filtrer les lignes sur les données provennat uniquement des sources Facebook et Twitter => 90% des donnees)
sources = ["Facebook", "Twitter"]
df = df[df["Source"].isin(sources)]

#Liste des colonnes que l'on ne souhaite par garder
colonnes = df.columns.values.tolist()
colonnes.remove('Opening Text')
colonnes.remove('Hit Sentence')
colonnes.remove('Source')


#Création d'un dataframe avec les colonnes qui nous intéresse
df2 = df.drop(columns=colonnes)



text = df2[['Hit Sentence']].to_string()

# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()