#! usr/bin/python3

import praw
import pandas as pd
import datetime as dt
from RedditAPI import accinfo

info = accinfo()

reddit = praw.Reddit(client_id=info[0], client_secret=info[1], user_agent=info[2], username=info[3], password=info[4])
subreddit = reddit.subreddit('India')
posts_dict = {"title":[], "score":[], "id":[], "url":[], "num_comments":[], "date":[], "body":[]}
for submission in subreddit.top(limit=2000):
	posts_dict["title"].append(submission.title)
	posts_dict["score"].append(submission.score)
	posts_dict["id"].append(submission.id)
	posts_dict["url"].append(submission.url)
	posts_dict["num_comments"].append(submission.num_comments)
	posts_dict["date"].append(submission.created)
	posts_dict["body"].append(submission.selftext)

posts_data = pd.DataFrame(posts_dict)