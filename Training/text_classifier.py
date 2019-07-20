from pymongo import MongoClient
import logging
import pandas as pd
import numpy as np
from numpy import random
import gensim
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
import re

client = MongoClient('mongodb+srv://BhavyaC16:nancydrew@flairifyme-jji1m.mongodb.net/test?retryWrites=true&w=majority')
db = client['RedditData']
preprocessedData = db.preprocessedData
preprocessedData_withStemming = db.preprocessedData_withStemming
df = pd.DataFrame(list(preprocessedData.find()))
df_withStemming = pd.DataFrame(list(preprocessedData_withStemming.find()))

x = df.title_words
y = df.flair
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25, random_state=10)

nb = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])
nb.fit(x_train,y_train)


y_pred = nb.predict(x_test)
print(accuracy_score(y_pred,y_test)) 