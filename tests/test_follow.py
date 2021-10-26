# this file will test all functions in follow.py
import follow as FW 
import os
import tweepy
import requests, json


# get user's info and access his/her account
consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"

# Authenticate to Twitter
person = tweepy.OAuthHandle(consumer, c_secret)
person.set_access_token(token, at_secret)

api = tweepy.API(person)
screen = "the screen_name that the user you want to check"

# get all followers
all_f = tweepy.Cursor(api.followers, screen)

u_id = "here is the user id that you want to check"

# test follower a user
print("You have followed: ")
FW.becomeFollower(person, u_id)

# test get followers
print("Your followers: ")
FW.getFollower(person)

# test getting a user's following
print("Your following: ")
FW.getFollowing(person)

# test count 
print("here is the number of followers that you have: ")
mycount = FW.counting(all_f)

# test get all follower's id
print("Your follower's id: ")
FW.getFollowerName(api, screen, mycount)

# test get all following's id
print("You are following: ")
FW.getFollowingName(api)


