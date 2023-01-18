import pandas as pd
import pickle
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

nltk.download('punkt')

#File Loading
my_file_path = "C:\\Users\\ATOU\\OneDrive - Axess OnLine\\Documents\\1. PROJETS\\PYTHON - ANALYSE DE SENTIMENTS\\CODE\\DATA\\Hippopotamus_Yext.xlsx"
df = pd.read_excel(my_file_path)

#Text Cleaning
df = df[df["Language"] == "French"]
df["Review"].dropna(inplace=True)
df.reset_index(inplace=True)
df["Review"] = df['Review'].astype(str).apply(lambda x: x.lower())
df["Review"] = df['Review'].astype(str).replace("\n", '. ', regex=True)
df["Review"] = df['Review'].astype(str).replace('  ', ' ', regex=True)

#Tokenization
reviews = []
stop_words = set(stopwords.words('french'))
stemmer = SnowballStemmer(language='french')

for index, row in enumerate(df.iterrows()):
    reviews.append(sent_tokenize(df["Review"].values[index]))
    for i in range(len(reviews[index])):
        word_token = []
        for w in word_tokenize(reviews[index][i]):
            if w not in stop_words:
                word_token.append(w)
        reviews[index][i] = word_token
        #Stemming
        reviews[index][i] = [stemmer.stem(reviews[index][i][w]) for w in range(len(reviews[index][i]))]
    df["Review"].iloc[index] = reviews[index]

filename = 'C:\\Users\\ATOU\\OneDrive - Axess OnLine\\Documents\\1. PROJETS\\PYTHON - ANALYSE DE SENTIMENTS\\CODE\\DATA\\df_Yext'
outfile = open(filename, 'wb')
pickle.dump(df, outfile)
outfile.close()
