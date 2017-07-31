import praw
import sys

import Config

if len(sys.argv) > 1:
    r = praw.Reddit('Gets a refresh token from our access token')

    r.set_oauth_app_info(client_id=Config.REDDITAPPID, client_secret=Config.REDDITAPPSECRET, redirect_uri='http://127.0.0.1/authorize_callback')

    print(sys.argv[1])
    print(r.get_access_information(sys.argv[1]))
