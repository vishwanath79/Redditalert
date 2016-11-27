from datetime import datetime
import praw
import pytz

subbredditnames = ['learnpython','Python']

fmt = "%Y-%m-%d %H:%M:%S %Z%z"
user_agent = ('LearnReddit 0.1(by /u/ingvay7)')
r = praw.Reddit(user_agent=user_agent)
n = 20

def get_posts():
    for sub in subbredditnames:
        print("\n ############# " + sub + " ############# \n" )
        subreddit = r.get_subreddit(sub)
        for count, submission in enumerate(subreddit.get_top_from_day(limit=n)):

            print(count, submission.title, ':', submission.url, submission.score, datetime.utcfromtimestamp(submission.created_utc).replace(tzinfo=pytz.utc).strftime(fmt))
            """ Convert UTC timestamp to Local Time"""
            #now_time = datetime.utcfromtimestamp(submission.created_utc).replace(tzinfo=pytz.utc)
            #print(now_time.strftime(fmt))



if __name__ == '__main__':
    #get_posts()
    # check for all possible calls
    print(i for i in dir(r.get_subreddit('learnpython')))

