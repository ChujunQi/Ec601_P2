import os
import tweepy
import requests, json


key_word = "your key word here"
#if you want to ignore retweet
without_retweet = "your key word here -filter:retweets"

#you can change key_word to without_retweet
yourSearch = tweepy.Cursor(api.search, q = key_word, lang = "en", since = date_since)

for i in yourSearch:
    result = [i.user.screen_name, i.user.location]

'''
you can add multiple keywords at one time. for example:
key_word = "apple + banana" or without_retweet = "apple+banana -filter:retweets"

