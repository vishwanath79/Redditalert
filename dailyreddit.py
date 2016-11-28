from datetime import datetime
import praw
import pytz
import smtplib
from lib import redditcon





subbredditnames = ['learnpython','Python','bigdata']

fmt = "%Y-%m-%d %H:%M:%S %Z%z"
user_agent = ('LearnReddit 0.1(by /u/ingvay7)')
r = praw.Reddit(user_agent=user_agent)
n = 20
allposts = []
def get_posts():
    for sub in subbredditnames:
        #print("\n ############# " + sub + " ############# \n" )
        subreddit = r.get_subreddit(sub)
        titles = "\n ############# " + str(sub) + " ############# \n"
        allposts.append(titles)
        for count, submission in enumerate(subreddit.get_top_from_day(limit=n)):

            #print(count, submission.title, ':', submission.url, submission.score, datetime.utcfromtimestamp(submission.created_utc).replace(tzinfo=pytz.utc).strftime(fmt)))
            posts = count, submission.title, ':', submission.url, submission.score, datetime.utcfromtimestamp(submission.created_utc).replace(tzinfo=pytz.utc).strftime(fmt)
            allposts.append(str(posts).replace(':', ' '))

    return '\n'.join(allposts).encode('utf-8')
    #print('\n'.join(allposts))
""" Convert UTC timestamp to Local Time"""
            #now_time = datetime.utcfromtimestamp(submission.created_utc).replace(tzinfo=pytz.utc)
            #print(now_time.strftime(fmt))


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(redditcon.sender, redditcon.key)
    msg = get_posts()
    server.sendmail(redditcon.sender, redditcon.receiver, msg)
    server.quit()

if __name__ == '__main__':
    #get_posts()
    send_mail()
    # check for all possible calls
    #print(i for i in dir(r.get_subreddit('learnpython')))

git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch lib/redditcon.py' --prune-empty --tag-name-filter cat -- --all