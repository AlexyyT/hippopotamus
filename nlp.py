import pickle
import torch
import seaborn
import pandas as pd
from sklearn import metrics
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from transformers import CamembertForSequenceClassification, CamembertTokenizer, AdamW

filename = 'C:\\Users\\ATOU\\OneDrive - Axess OnLine\\Documents\\1. PROJETS\\PYTHON - ANALYSE DE SENTIMENTS\\CODE\\DATA\\df_Yext'
infile = open(filename, 'rb')
df = pickle.load(infile)
infile.close()

reviews = df["Review"].values.tolist()
print(reviews)

sentiments = df['Rating'].values.tolist()

for i in range(len(sentiments)):
    if sentiments[i] == 1:
        sentiments[i]="Insatisfait"
    elif sentiments[i] == 5:
        sentiments[i]="Satisfait"
    else:
        sentiments[i]="Neutre"

# On charge l'objet "tokenizer"de camemBERT qui va servir a encoder
# 'camebert-base' est la version de camembert qu'on choisit d'utiliser
# 'do_lower_case' à True pour qu'on passe tout en miniscule
TOKENIZER = CamembertTokenizer.from_pretrained(
    'camembert-base',
    do_lower_case=True)

# La fonction batch_encode_plus encode un batch de donnees
encoded_batch = TOKENIZER.batch_encode_plus(reviews,
                                            add_special_tokens=True,
                                            max_length=MAX_LENGTH,
                                            padding=True,
                                            truncation=True,
                                            return_attention_mask=True,
                                            return_tensors='pt')

# On transforme la liste des sentiments en tenseur
sentiments = torch.tensor(sentiments)
print(sentiments)