import nltk
import pandas as pd

def title_identify_tokens(row):
	title = row['title']
	tokens = nltk.word_tokenize(title)
	token_words = [w for w in tokens if w.isalnum()]
	return token_words

def body_identify_tokens(row):
	body = row['body']
	tokens = nltk.word_tokenize(body)
	token_words = [w for w in tokens if w.isalnum()]
	return token_words

def comment_identify_tokens(row):
	comments = row['comments']
	tokens = nltk.word_tokenize(comments)
	token_words = [w for w in tokens if w.isalnum()]
	return token_words

fileloc = "./redditData.csv"
data = pd.read_csv(fileloc)
data['title'] = data['title'].str.lower()
data['body'] = data['body'].str.lower()
data['comments'] = data['comments'].str.lower()


exampletitle = data.iloc[0]
'''
print(exampletitle['title'])
print('____________________________________________')
print(exampletitle['body'])
print('____________________________________________')
print(exampletitle['comments'])
print(nltk.word_tokenize(exampletitle['title']))
'''


data['title_words'] = data.apply(title_identify_tokens,axis=1)
data['body_words'] = data.apply(body_identify_tokens,axis=1)
data['comment_words'] = data.apply(comment_identify_tokens,axis=1)