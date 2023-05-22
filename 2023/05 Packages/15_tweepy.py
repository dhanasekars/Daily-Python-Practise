""" 
Created on : 27/04/23 10:35 am
@author : ds  
"""

import tweepy
from config import TwitterDetails

auth = tweepy.OAuthHandler(TwitterDetails.api_key, TwitterDetails.api_secret_key)
auth.set_access_token(TwitterDetails.access_token, TwitterDetails.access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("OK")

except tweepy.TweepyException as e:
    print("Error during authentication:", e)

# text = "Hello, Twitter! This is 275 day of #Pythoncoding. This is from tweepy python package." \
#        "Git Repo  https://github.com/dhanasekars/Daily-Python-Practise"
#
# try:
#     api.update_status(text)
#     print("OK")
# except tweepy.TweepyException as e:
#     print("Error posting tweet:", e)
#
# try:
#     print(api.get_user())
# except tweepy.TweepyException as e:
#     print("Error getting user details", e)

setting_details = api.get_settings()
print(setting_details)
print(api.get_profile_banner())