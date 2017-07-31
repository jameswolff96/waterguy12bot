import praw
import re
import traceback
import time
from datetime import datetime

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
    START_TIMESTAMP = Config.START_TIMESTAMP
except ImportError:
    pass

reddit = None

def setupReddit():
    global reddit
    try:
        print('Setting things up')
        reddit = praw.Reddit(client_id=REDDITAPPID, client_secret=REDDITAPPSECRET, user_agent=USERAGENT, username=USERNAME, password=PASSWORD)
        print('All done!')
    except Exception as e:
        print('Oops: ' + str(e))
	traceback.print_exc()

def process_submission(submission):
    if re.search("(me(.)*irl)", submission.title, re.I) is not None and submission.created > START_TIMESTAMP:
        commentReply = Config.MESSAGE
        commentReply += "\n\n-----------\n\n"
        commentReply += Config.SIGNATURE

        try:
            submission.reply(commentReply)
            print('Comment made.\n')
        except praw.exceptions.APIException:
            print('Request from banned subreddit: ' + str(submission.subreddit) + '\n')
        except Exception:
            traceback.print_exc()

        try:
            DatabaseHandler.addSubmission(submission.id, submission.author.name, submission.subreddit, True)
        except Exception:
            traceback.print_exc()
    else:
        try:
            DatabaseHandler.addSubmission(submission.id, submission.author.name, submission.subreddit, False)
        except:
            traceback.print_exc()

def start():
    print('Starting submission stream:')

    for submission in reddit.subreddit(SUBREDDITLIST).stream.submissions():
        if not (Search.isValidSubmission(submission, reddit)):
            try:
                if not (DatabaseHandler.submissionExists(submission.id)):
                    DatabaseHandler.addSubmission(submission.id, submission.author.name, submission.subreddit, False)
            except:
                pass
            continue

        print('New Post in: /r/{0} by /u/{1}: {2}'.format(submission.subreddit, submission.author.name, submission.shortlink))
        process_submission(submission)
        if datetime.now() > datetime(2017,8,14,00,00,00):
          break

setupReddit()

while datetime.now() < datetime(2017,8,14,00,00,00):
    try:
        start()
    except Exception as e:
        traceback.print_exc()
        pass
    print('Looping')
