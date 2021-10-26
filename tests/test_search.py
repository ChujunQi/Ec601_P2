# this file will test searchTimeline, searchContent
import searchTimeline as ST 
import searchContent as SC 

import os, tweepy
import twitter
import datetime
import json

# get user's info
consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"

api = twitter.Api(consumer_key = consumer, consumer_secret = c_secret, 
                    access_token_key = token, access_token_secret = at_secret)

# get all the tweets that the user published
AllTweets = None
with open('editedTweet.json') as json_file:
    AllTweets = json.load(json_file)

# test search by timeline
ST.getByTimeline(AllTweets)

# test search by content
keyword = "banana apple orange"
no_retweet = True
SC.getByContent(api, keyword, no_retweet)



