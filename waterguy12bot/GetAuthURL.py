import praw
import Config

r = praw.Reddit('Gets an OAuth URL for the provided app')

r.set_oauth_app_info(client_id=Config.REDDITAPPID, client_secret=Config.REDDITAPPSECRET, redirect_uri='http://127.0.0.1/authorize_callback')

print(r.get_authorize_url('dfgsd', 'read submit edit identity', True))
