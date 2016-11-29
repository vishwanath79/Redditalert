from datetime import datetime

import praw
import pytz

subbredditnames = ['learnpython', 'Python', 'bigdata']
fmt = "%Y-%m-%d %H:%M:%S %Z%z"
user_agent = ('LearnReddit 0.1(by /u/ingvay7)')
r = praw.Reddit(client_id='gKKxVJc9vJgvrg',
                     client_secret='    yYSe-u68S_0zzst1_0BnwP43_K8',
                    user_agent= user_agent,
                     username='ingvay7')
n = 20
allposts = []


def get_posts():
    for sub in subbredditnames:
        # print("\n ############# " + sub + " ############# \n" )
        subreddit = r.get_subreddit(sub)
        titles = "\n ############# " + str(sub) + " ############# \n"
        allposts.append(titles)
        for count, submission in enumerate(subreddit.get_top_from_day(limit=n)):
            posts = count, submission.title, ':', submission.url, submission.score, datetime.utcfromtimestamp(
                submission.created_utc).replace(tzinfo=pytz.utc).strftime(fmt)
            allposts.append(str(posts).replace(':', '').replace("'",''))

    print('\n'.join(allposts))


""" Convert UTC timestamp to Local Time"""

# now_time = datetime.utcfromtimestamp(submission.created_utc).replace(tzinfo=pytz.utc)
# print(now_time.strftime(fmt))

# 0 17  * * * sh reddit.sh |mail -E -r "email" -s "$(echo -e "Daily Reddit\nContent-Type: text/html")"  "email"


if __name__ == '__main__':
    get_posts()
