import logging
import praw
import time

import Config

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('prawcore')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

reddit = praw.Reddit(client_id=Config.REDDITAPPID, client_secret=Config.REDDITAPPSECRET, password=Config.PASSWORD, user_agent=Config.USERAGENT, username = Config.USERNAME)

print(reddit.user.me())
