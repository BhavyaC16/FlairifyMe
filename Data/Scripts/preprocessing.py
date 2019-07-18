import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import pandas as pd

stemming = PorterStemmer()
stops = set(stopwords.words("english"))

def title_preprocessing(row):
	title = row['title']
	tokens = nltk.word_tokenize(title)
	token_words = [w for w in tokens if w.isalnum()]
	key_words = [word for word in token_words if not word in stops]
	joined = (" ".join(key_words))
	return(joined)

def body_preprocessing(row):
	body = row['body']
	tokens = nltk.word_tokenize(body)
	token_words = [w for w in tokens if w.isalnum()]
	stemmed_list = [stemming.stem(word) for word in token_words]
	key_words = [W for W in stemmed_list if not W in stops]
	joined = (" ".join(key_words))
	return(joined)
	

def comment_preprocessing(row):
	comments = row['comments']
	tokens = nltk.word_tokenize(comments)
	token_words = [w for w in tokens if w.isalnum()]
	stemmed_list = [stemming.stem(word) for word in token_words]
	key_words = [W for W in stemmed_list if not W in stops]
	joined = (" ".join(key_words))
	return(joined)
	

fileloc = "./redditData.csv"
data = pd.read_csv(fileloc)
data['title'] = data['title'].str.lower()
data['body'] = data['body'].str.lower()
data['comments'] = data['comments'].str.lower()

data['title_words'] = data.apply(title_preprocessing,axis=1)
print(data['title_words'])
data['body_words'] = data.apply(body_preprocessing,axis=1)
print(data['body_words'])
data['comment_words'] = data.apply(comment_preprocessing,axis=1)
print(data['comment_words'])

data.to_csv('./preprocessedData_withStemming.csv', index=False)