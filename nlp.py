import pandas as pd
import sklearn
from sklearn.feature_extraction import *


Filename = "C:\\Users\\ATOU\\OneDrive - Axess OnLine\\Documents\\1. PROJETS\\PYTHON - ANALYSE DE SENTIMENTS\\DATA\\Tweets.csv"
df = pd.read_csv(Filename)

review_df = df[['text', 'airline_sentiment']]
review_df = review_df[review_df['airline_sentiment'] != 'neutral']
review_df.reset_index()
print(review_df)

print(review_df['airline_sentiment'].value_counts())

sentiment_label = review_df.airline_sentiment.factorize()
print(sentiment_label)

tweet = review_df.text.values

from tensorflow.keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(tweet)

encoded_docs = tokenizer.texts_to_sequences(tweet)

from tensorflow.keras.preprocessing.sequence import pad_sequences

padded_sequence = pad_sequences(encoded_docs, maxlen=200)
print(padded_sequence)


# Text Classifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM,Dense, Dropout, SpatialDropout1D
from tensorflow.keras.layers import Embedding

vocab_size = len(tokenizer.word_index) + 1


embedding_vector_length = 32
model = Sequential()
model.add(Embedding(vocab_size, embedding_vector_length, input_length=200))
model.add(SpatialDropout1D(0.25))
model.add(LSTM(50, dropout=0.5, recurrent_dropout=0.5))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])

print(model.summary())


history = model.fit(padded_sequence,sentiment_label[0],validation_split=0.2, epochs=6, batch_size=32)

# import matplotlib.pyplot as plt
#
# plt.plot(history.history['accuracy'], label='acc')
# plt.plot(history.history['val_accuracy'], label='val_acc')
# plt.legend()
# plt.show()
#
# plt.savefig("Accuracy plot.jpg")

# import matplotlib.pyplot as plt
#
# plt.plot(history.history['accuracy'], label='acc')
# plt.plot(history.history['val_accuracy'], label='val_acc')
# plt.legend()
# plt.show()
#
# plt.savefig("Accuracy plot.jpg")
#
#
# plt.plot(history.history['loss'], label='loss')
# plt.plot(history.history['val_loss'], label='val_loss')
#
# plt.legend()
# plt.show()
#
# plt.savefig("Loss plt.jpg")



def predict_sentiment(text):
  tw = tokenizer.texts_to_sequences([text])
  tw = pad_sequences(tw,maxlen=200)
  prediction = int(model.predict(tw).round().item())
  return sentiment_label[1][prediction]


test_sentence1 = "I enjoyed my journey on this flight."
predict_sentiment(test_sentence1)

test_sentence2 = "This is the worst flight experience of my life!"
predict_sentiment(test_sentence2)

yext = pd.read_excel("C:\\Users\\ATOU\\OneDrive - Axess OnLine\\Documents\\1. PROJETS\\PYTHON - ANALYSE DE SENTIMENTS\\DATA\\Hippopotamus_Yext.xlsx")

yext = yext[yext['Language'] == 'English']
yext = yext.reset_index(drop=True)



en_yext = pd.DataFrame(columns=['Review', 'Sentiment_Yext', 'Sentiment_model'])

for index, row in yext.iterrows():
  prediction = predict_sentiment(yext['Review'].values[index])
  new_row = {'Review':yext['Review'].values[index],
             'Sentiment_Yext':yext['Rating'].values[index],
             'Sentiment_model':prediction}
  en_yext = en_yext.append(new_row, ignore_index=True)