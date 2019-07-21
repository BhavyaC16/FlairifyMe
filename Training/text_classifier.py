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
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import re

flairs = ['AMA','Business Finance Policy','Food','Sports','Politics','Science Technology','Policy Economy','Photography','Scheduled','Reddiquette','Non-Political','AskIndia','Entertainment']

def naiveBayes(x_train,y_train,x_test,y_test):
	nb = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])
	nb.fit(x_train,y_train)
	y_pred = nb.predict(x_test)
	print("Naive Bayes: "+str(accuracy_score(y_pred,y_test)))
	print(classification_report(y_test, y_pred,target_names=flairs))

def linear_SVM(x_train,y_train,x_test,y_test):
	sgd = Pipeline([('vect',CountVectorizer()),('tfidf',TfidfTransformer()),('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None))])
	sgd.fit(x_train,y_train)
	y_pred = sgd.predict(x_test)
	print("Linear SVM: "+str(accuracy_score(y_pred,y_test)))
	print(classification_report(y_test, y_pred,target_names=flairs))

def logicalRegression(x_train,y_train,x_test,y_test):
	logreg = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', LogisticRegression(n_jobs=1, C=1e5))])
	logreg.fit(x_train,y_train)
	y_pred = logreg.predict(x_test)
	print("Logical Regression: "+str(accuracy_score(y_pred,y_test)))
	print(classification_report(y_test, y_pred,target_names=flairs))	



client = MongoClient('mongodb+srv://BhavyaC16:nancydrew@flairifyme-jji1m.mongodb.net/test?retryWrites=true&w=majority')
db = client['RedditData']
preprocessedData = db.preprocessedData
preprocessedData_withStemming = db.preprocessedData_withStemming
df = pd.DataFrame(list(preprocessedData.find()))
df = df.fillna("")
df_withStemming = pd.DataFrame(list(preprocessedData_withStemming.find()))
df_withStemming = df_withStemming.fillna("")

x = df.title_words
y = df.flair
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25, random_state=10)

naiveBayes(x_train,y_train,x_test,y_test)
linear_SVM(x_train,y_train,x_test,y_test)
logicalRegression(x_train,y_train,x_test,y_test)