# this file can count number of tweets that the user update by giving different search conditions

import os
import tweepy
import requests, json

#get user's info
consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"

# get the user's name
person = tweepy.OAuthHandle(consumer, c_secret)
person.set_access_token(token, at_secret)

api = tweepy.API(person)

u = api.get_user("user id")

#get all tweets
count = user.statuses_count()

print(count)

#get recent 500 tweets
t = tweepy.Cursor(api.search, lang = "en").items(500)

#get recent tweets by time
t_1 = tweepy.Cursor(api.search, lang = "en", since = 'time such as 2019-01-01')

#get recent tweets by content
t_2 = tweepy.Cursor(api.search, q = "content you want search", lang = "en", since = 'time such as 2019-01-01')

