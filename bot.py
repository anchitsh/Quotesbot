import csv
import os
import tweepy
from secrets import *
from time import gmtime, strftime
import requests

def getquote():
    r = requests.get('https://favqs.com/api/qotd').json()
    quote = r['quote']['body']
    return quote

def create_tweet():
    """Create the text of the tweet you want to send."""
    text = getquote()
    return text


def tweet(text):
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(text)
   
if __name__ == "__main__":
    tweet_text = create_tweet()
    tweet(tweet_text)
