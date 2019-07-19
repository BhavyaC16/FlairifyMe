import pandas as pd
import collections
from pymongo import MongoClient
from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import decomposition, ensemble


client = MongoClient('mongodb+srv://BhavyaC16:nancydrew@flairifyme-jji1m.mongodb.net/test?retryWrites=true&w=majority')
db = client['CSV']
train = db.train
test = db.test
train = pd.DataFrame(list(train.find()))
test = pd.DataFrame(list(test.find()))

train_x = train['title_words']
train_x = train_x.as_matrix()
train_y = train['flair']
test_x = test['title_words']
test_x = test_x.as_matrix()
test_y = test['flair']

#label encoding target variables(flairs)
encoder = preprocessing.LabelEncoder()
train_y = encoder.fit_transform(train_y)
test_y = encoder.fit_transform(test_y)
#print(collections.Counter(train_y))
#print(collections.Counter(test_y))

#creating count vectorizer
countVect = CountVectorizer(analyzer='word')
countVect.fit(train_x)
print(train_x)