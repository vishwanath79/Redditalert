import time
import praw
user_agent = ('LearnReddit 0.1(by /u/ingvay7)')
r = praw.Reddit(user_agent=user_agent)
n = 10
subreddit = r.get_subreddit('learnpython')
for count, submission in enumerate(subreddit.get_top_from_day(limit=n)):
    print(count, submission.title, ':', submission.url, submission.score)



