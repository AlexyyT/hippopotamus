# import numpy as np
# import pandas as pd
# import matplotlib
# import seaborn as sns
# import re
# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
#
#
#
# Filename = "C:\\Users\\ATOU\\OneDrive - Axess OnLine\\Documents\\1. PROJETS\\PYTHON - ANALYSE DE SENTIMENTS\\DATA\\Tweets.csv"
# df = pd.read_csv(Filename)
#
# verbatim = df.iloc[:, 10].values
# sentiment = df.iloc[:, 1].values
#
# processed_tweets = []
# for tweet in range(0, len(verbatim)):
#     # Remove all the special characters
#     processed_tweet = re.sub(r'\W', ' ', str(verbatim[tweet]))
#     # remove all single characters
#     processed_tweet = re.sub(r'\s+[a-zA-Z]\s+', ' ', processed_tweet)
#     # Remove single characters from the start
#     processed_tweet = re.sub(r'\^[a-zA-Z]\s+', ' ', processed_tweet)
#     # Substituting multiple spaces with single space
#     processed_tweet= re.sub(r'\s+', ' ', processed_tweet, flags=re.I)
#     # Removing prefixed 'b'
#     processed_tweet = re.sub(r'^b\s+', '', processed_tweet)
#     # Converting to Lowercase
#     processed_tweet = processed_tweet.lower()
#     processed_tweets.append(processed_tweet)
#
#
# #print(processed_tweets)
#
#
# tfidfconverter = TfidfVectorizer(max_features=2000, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
# verbatim = tfidfconverter.fit_transform(processed_tweets).toarray()
#
# # print(verbatim)
#
# X_train, X_test, y_train, y_test = train_test_split(verbatim, sentiment, test_size=0.2, random_state=0)
#
#
# text_classifier = RandomForestClassifier(n_estimators=100, random_state=0)
# text_classifier.fit(X_train, y_train)
#
# predictions = text_classifier.predict(X_test)
#
# for i in range(len(X_test[:20])):
#     print(f' le mot : {X_test[i]} est prédit comme étant {predictions[i]} et il est réellement {y_test[i]}')
#
#
# # from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
# #
# # print(confusion_matrix(y_test, predictions))
# # print(classification_report(y_test, predictions))
# # print(accuracy_score(y_test, predictions))


import pandas as pd
import sklearn
from sklearn.feature_extraction import *


Filename = "C:\\Users\\ATOU\\OneDrive - Axess OnLine\\Documents\\1. PROJETS\\PYTHON - ANALYSE DE SENTIMENTS\\DATA\\Hippopotamus_Yext.xlsx"
df = pd.read_excel(Filename)

df = df[df['Language'] == 'French']
print(df[:10])

yext_train = df[:35000]
yext_test = df[35000:]

#Create Features
vectorizer = sklearn.feature_extraction.text.TfidfVectorizer(use_idf=True,ngram_range=(1,1))

# tfidf_features_train = vectorizer.fit_transform(yext_train['review'])
# tfidf_features_test = vectorizer.transform(yext_test['review'])
#
# print(tfidf_features_train.shape, tfidf_features_test.shape)
#
#
# # train model
# clf = sklearn.linear_model.LogisticRegression()
# clf.fit(tfidf_features_train, train_labels)
#
# # evaluation
# predictions = clf.predict(tfidf_features_test)
# print(sklearn.metrics.classification_report(test_labels, predictions, target_names=['Negative', 'Positive']))
# print(sklearn.metrics.confusion_matrix(test_labels, predictions, labels=[0, 1]))
