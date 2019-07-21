import joblib
import nltk
from nltk.corpus import stopwords
import praw
from RedditAPI import accinfo
import pandas as pd
import sklearn
#nltk.download('all')
info = accinfo()
stops = set(stopwords.words("english"))
c = []
s = ''

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
	key_words = [W for W in token_words if not W in stops]
	joined = (" ".join(key_words))
	return(joined)
	

def comment_preprocessing(row):
	comments = row['comments']
	tokens = nltk.word_tokenize(comments)
	token_words = [w for w in tokens if w.isalnum()]
	key_words = [W for W in token_words if not W in stops]
	joined = (" ".join(key_words))
	return(joined)

model = joblib.load("./Models/finalized_model.sav")
post_dict = {"id": [], "title":[], "body":[], "comments": []}

reddit = praw.Reddit(client_id=info[0], client_secret=info[1], user_agent=info[2], username=info[3], password=info[4])

print("enter url:")
url = input()
submission = reddit.submission(url = url)
post_dict['id']=submission.id
post_dict['title']=submission.title
post_dict['body']=submission.selftext
submission.comments.replace_more(limit=0)
for comment in submission.comments.list():
	c.append(comment.body)
post_dict['comments'].append(c)

data = pd.DataFrame(post_dict)
data.fillna("")

data['title'] = data['title'].str.lower()
data['body'] = data['body'].str.lower()
for a in data['comments'][0]:
	s+=str(a)+" "
data['comments']=s


data['title_words'] = data.apply(title_preprocessing,axis=1)
#print(data['title_words'])
data['body_words'] = data.apply(body_preprocessing,axis=1)
#print(data['body_words'])
data['comment_words'] = data.apply(comment_preprocessing,axis=1)
#print(data['comment_words'])

combine = data['title_words']+data['body_words']+data['comment_words']
data = data.assign(combined=combine)
print(model.predict(data['combined']))