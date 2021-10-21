import os
import tweepy
import requests, json


#get users that a user blocks
consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"

person = tweepy.OAuthHandle(consumer, c_secret)
person.set_access_token(token, at_secret)

screen = "this is screen name"
api = tweepy.API(person)
t = api.blocks()
 for i in t:
    print(i.screen)

#get total number of the user's blocks
print(len(t))

