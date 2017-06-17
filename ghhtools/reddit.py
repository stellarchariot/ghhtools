import praw
import os
from ghh_config_error import GHHConfigError

def get_reddit():
    config_client_id = os.getenv('REDDIT_API_CLIENT_ID')
    config_client_secret = os.getenv('REDDIT_API_CLIENT_SECRET')
    
    if not config_client_id:
        raise GHHConfigError("The Reddit API client_id has not been specified")
    if not config_client_secret:
        raise GHHConfigError("The Reddit API client_secret has not been specified")
    
    reddit = praw.Reddit(user_agent='Comment Extraction (by /u/stellarchariot)',
                     client_id=config_client_id, client_secret=config_client_secret)
    return reddit
