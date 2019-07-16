#! usr/bin/python3

import praw
import pandas as pd
import datetime as dt
from RedditAPI import accinfo

info = accinfo()
count = 0

flairs = ['AMA','Business/Finance','Food','Sports','Politics','Science Technology','Policy Economy','Photography','Scheduled','[R]eddiquette','Non-Political','AskIndia','Entertainment']

reddit = praw.Reddit(client_id=info[0], client_secret=info[1], user_agent=info[2], username=info[3], password=info[4])

posts_dict = {"id": [], "title":[], "body":[], "comments": [], "flair":[], "url":[], "date":[], "ups":[],"downs":[] , "num_comments":[] }

for submission in reddit.subreddit('India').search('flair:"AMA"', limit=250):
	count+=1
	posts_dict["id"].append(submission.id)
	print(submission.id)
	print(count)
	posts_dict["title"].append(submission.title)
	posts_dict["body"].append(submission.selftext)
	c = []
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		c.append(comment.body)
	posts_dict["comments"].append(c)
	posts_dict["flair"].append(submission.link_flair_css_class)
	posts_dict["url"].append(submission.url)
	posts_dict["date"].append(submission.created)
	posts_dict["ups"].append(submission.ups)
	posts_dict["downs"].append(submission.downs)
	posts_dict["num_comments"].append(submission.num_comments)

for submission in reddit.subreddit('India').search('flair:"Business/Finance"', limit=250):
	count+=1
	posts_dict["id"].append(submission.id)
	print(submission.id)
	print(count)
	posts_dict["title"].append(submission.title)
	posts_dict["body"].append(submission.selftext)
	c = []
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		c.append(comment.body)
	posts_dict["comments"].append(c)
	posts_dict["flair"].append(submission.link_flair_css_class)
	posts_dict["url"].append(submission.url)
	posts_dict["date"].append(submission.created)
	posts_dict["ups"].append(submission.ups)
	posts_dict["downs"].append(submission.downs)
	posts_dict["num_comments"].append(submission.num_comments)

for submission in reddit.subreddit('India').search('flair:"Food"', limit=250):
	count+=1
	posts_dict["id"].append(submission.id)
	print(submission.id)
	print(count)
	posts_dict["title"].append(submission.title)
	posts_dict["body"].append(submission.selftext)
	c = []
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		c.append(comment.body)
	posts_dict["comments"].append(c)
	posts_dict["flair"].append(submission.link_flair_css_class)
	posts_dict["url"].append(submission.url)
	posts_dict["date"].append(submission.created)
	posts_dict["ups"].append(submission.ups)
	posts_dict["downs"].append(submission.downs)
	posts_dict["num_comments"].append(submission.num_comments)

for submission in reddit.subreddit('India').search('flair:"Sports"', limit=250):
	count+=1
	posts_dict["id"].append(submission.id)
	print(submission.id)
	print(count)
	posts_dict["title"].append(submission.title)
	posts_dict["body"].append(submission.selftext)
	c = []
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		c.append(comment.body)
	posts_dict["comments"].append(c)
	posts_dict["flair"].append(submission.link_flair_css_class)
	posts_dict["url"].append(submission.url)
	posts_dict["date"].append(submission.created)
	posts_dict["ups"].append(submission.ups)
	posts_dict["downs"].append(submission.downs)
	posts_dict["num_comments"].append(submission.num_comments)

for submission in reddit.subreddit('India').search('flair:"Politics"', limit=250):
	count+=1
	posts_dict["id"].append(submission.id)
	print(submission.id)
	print(count)
	posts_dict["title"].append(submission.title)
	posts_dict["body"].append(submission.selftext)	
	c = []
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		c.append(comment.body)
	posts_dict["comments"].append(c)
	posts_dict["flair"].append(submission.link_flair_css_class)
	posts_dict["url"].append(submission.url)
	posts_dict["date"].append(submission.created)
	posts_dict["ups"].append(submission.ups)
	posts_dict["downs"].append(submission.downs)
	posts_dict["num_comments"].append(submission.num_comments)

for submission in reddit.subreddit('India').search('flair:"Science Technology"', limit=250):
	count+=1
	posts_dict["id"].append(submission.id)
	print(submission.id)
	print(count)
	posts_dict["title"].append(submission.title)
	posts_dict["body"].append(submission.selftext)
	c = []
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		c.append(comment.body)
	posts_dict["comments"].append(c)
	posts_dict["flair"].append(submission.link_flair_css_class)
	posts_dict["url"].append(submission.url)
	posts_dict["date"].append(submission.created)
	posts_dict["ups"].append(submission.ups)
	posts_dict["downs"].append(submission.downs)
	posts_dict["num_comments"].append(submission.num_comments)

for submission in reddit.subreddit('India').search('flair:"Policy Economy"', limit=250):
	count+=1
	posts_dict["id"].append(submission.id)
	print(submission.id)
	print(count)
	posts_dict["title"].append(submission.title)
	posts_dict["body"].append(submission.selftext)
	c = []
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		c.append(comment.body)
	posts_dict["comments"].append(c)
	posts_dict["flair"].append(submission.link_flair_css_class)
	posts_dict["url"].append(submission.url)
	posts_dict["date"].append(submission.created)
	posts_dict["ups"].append(submission.ups)
	posts_dict["downs"].append(submission.downs)
	posts_dict["num_comments"].append(submission.num_comments)

for submission in reddit.subreddit('India').search('flair:"Photography"', limit=250):
	count+=1
	posts_dict["id"].append(submission.id)
	print(submission.id)
	print(count)
	posts_dict["title"].append(submission.title)
	posts_dict["body"].append(submission.selftext)
	c = []
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		c.append(comment.body)
	posts_dict["comments"].append(c)
	posts_dict["flair"].append(submission.link_flair_css_class)
	posts_dict["url"].append(submission.url)
	posts_dict["date"].append(submission.created)
	posts_dict["ups"].append(submission.ups)
	posts_dict["downs"].append(submission.downs)
	posts_dict["num_comments"].append(submission.num_comments)

for submission in reddit.subreddit('India').search('flair:"Scheduled"', limit=250):
	count+=1
	posts_dict["id"].append(submission.id)
	print(submission.id)
	print(count)
	posts_dict["title"].append(submission.title)
	posts_dict["body"].append(submission.selftext)
	c = []
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		c.append(comment.body)
	posts_dict["comments"].append(c)
	posts_dict["flair"].append(submission.link_flair_css_class)
	posts_dict["url"].append(submission.url)
	posts_dict["date"].append(submission.created)
	posts_dict["ups"].append(submission.ups)
	posts_dict["downs"].append(submission.downs)
	posts_dict["num_comments"].append(submission.num_comments)

for submission in reddit.subreddit('India').search('flair:"[R]eddiquette"', limit=250):
	count+=1
	posts_dict["id"].append(submission.id)
	print(submission.id)
	print(count)
	posts_dict["title"].append(submission.title)
	posts_dict["body"].append(submission.selftext)
	c = []
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		c.append(comment.body)
	posts_dict["comments"].append(c)
	posts_dict["flair"].append(submission.link_flair_css_class)
	posts_dict["url"].append(submission.url)
	posts_dict["date"].append(submission.created)
	posts_dict["ups"].append(submission.ups)
	posts_dict["downs"].append(submission.downs)
	posts_dict["num_comments"].append(submission.num_comments)
		
for submission in reddit.subreddit('India').search('flair:"Non-Political"', limit=250):
	count+=1
	posts_dict["id"].append(submission.id)
	print(submission.id)
	print(count)
	posts_dict["title"].append(submission.title)
	posts_dict["body"].append(submission.selftext)
	c = []
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		c.append(comment.body)
	posts_dict["comments"].append(c)
	posts_dict["flair"].append(submission.link_flair_css_class)
	posts_dict["url"].append(submission.url)
	posts_dict["date"].append(submission.created)
	posts_dict["ups"].append(submission.ups)
	posts_dict["downs"].append(submission.downs)
	posts_dict["num_comments"].append(submission.num_comments)

for submission in reddit.subreddit('India').search('flair:"AskIndia"', limit=250):
	count+=1
	posts_dict["id"].append(submission.id)
	print(submission.id)
	print(count)
	posts_dict["title"].append(submission.title)
	posts_dict["body"].append(submission.selftext)
	c = []
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		c.append(comment.body)
	posts_dict["comments"].append(c)
	posts_dict["flair"].append(submission.link_flair_css_class)
	posts_dict["url"].append(submission.url)
	posts_dict["date"].append(submission.created)
	posts_dict["ups"].append(submission.ups)
	posts_dict["downs"].append(submission.downs)
	posts_dict["num_comments"].append(submission.num_comments)

for submission in reddit.subreddit('India').search('flair:"Entertainment"', limit=250):
	count+=1
	posts_dict["id"].append(submission.id)
	print(submission.id)
	print(count)
	posts_dict["title"].append(submission.title)
	posts_dict["body"].append(submission.selftext)
	c = []
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		c.append(comment.body)
	posts_dict["comments"].append(c)
	posts_dict["flair"].append(submission.link_flair_css_class)
	posts_dict["url"].append(submission.url)
	posts_dict["date"].append(submission.created)
	posts_dict["ups"].append(submission.ups)
	posts_dict["downs"].append(submission.downs)
	posts_dict["num_comments"].append(submission.num_comments)
		
print("AMA: ",str(posts_dict["flair"].count("AMA")))
print("Food: ",str(posts_dict["flair"].count("Food")))
print("Sports: ",str(posts_dict["flair"].count("Sports")))
print("Politics: ",str(posts_dict["flair"].count("Politics")))
print("Policy/Economy: ",str(posts_dict["flair"].count("Policy Economy")))
print("Photography: ",str(posts_dict["flair"].count("Photography")))
print("AskIndia: ",str(posts_dict["flair"].count("AskIndia")))
print("Non-Political: ",str(posts_dict["flair"].count("Non-Political")))
print("Reddiquette: ",str(posts_dict["flair"].count("Reddiquette")))
print("Science/Technology: ",str(posts_dict["flair"].count("Science Technology")))
print("Business/Finance: ",str(posts_dict["flair"].count("Business Finance Policy")))
print("Entertainment: ",str(posts_dict["flair"].count("Entertainment")))
print("Scheduled: ",str(posts_dict["flair"].count("Scheduled")))
print("Political: ",str(posts_dict["flair"].count("Political")))

posts_data = pd.DataFrame(posts_dict)
posts_data.to_csv(r'./redditData.csv')