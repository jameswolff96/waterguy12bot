import praw
import re
import traceback
import time
import datetime

import DatabaseHandler
import Search

try:
    import Config
    USERNAME = Config.USERNAME
    PASSWORD = Config.PASSWORD
    USERAGENT = Config.USERAGENT
    REDDITAPPID = Config.REDDITAPPID
    REDDITAPPSECRET = Config.REDDITAPPSECRET
    SUBREDDITLIST = Config.getSubList()
except ImportError:
    pass

reddit = None

def setupReddit():
    global reddit
    try:
        print('Setting things up')
        reddit = praw.Reddit(client_id=REDDITAPPID, client_secret=REDDITAPPSECRET, password=PASSWORD, user_agent=USERAGENT, username=USERNAME)
        print(reddit.user.me())
        print('All done!')
    except Exception as e:
        print('Oops: ' + str(e))
	traceback.print_exc()

setupReddit()

print(SUBREDDITLIST)
print(reddit.subreddit(SUBREDDITLIST))

subreddit = reddit.subreddit(SUBREDDITLIST)
print(subreddit)

for submission in subreddit.stream.submissions():
  print(submission)
  print(submission.title)
  print(submission.created)
  time = submission.created
  print(time > Config.START_TIMESTAMP)

