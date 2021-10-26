import like
import os
import tweepy
import requests, json


# this file will test all functions in like.py

# get user's info and enter the account
consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"

person = tweepy.OAuthHandle(consumer, c_secret)
person.set_access_token(token, at_secret)

userID = "the ID you want to test"

# get user's username and id
api = tweepy.API(person)
screen = api.screen_name
userinfo = api.get_user(screen)
ID = userinfo.id_str

# test like a tweet
like.likeTweet(person, userID)

like.simpleLike(person, ID, userID)

# test unlike a tweet
like.unlikeTweet(person, userID)

like.simpleUnlike(person, ID, userID)

# test get like list
like.likeList(screen)

like.getLiked(person)
