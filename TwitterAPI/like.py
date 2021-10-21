#including contents about like or unlike a tweet and getting a user's like list
import os
import tweepy
import requests, json

#like/unlike a tweet
url = "https://api.twitter.com/2/users//likes"

payload = "// Replace tweet-id-you-want-to-like with the ID you wish to like\n{\n    \"tweet_id\": \"tweet-id-you-want-to-like\"\n}"
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)
#response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

#like a tweet
#get user's info
consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"

person = tweepy.OAuthHandle(consumer, c_secret)
person.set_access_token(token, at_secret)

#this will create a "like" 
api = tweepy.API(person)
t = api.create_favorite("this is id")

#unlike a tweet
t_1 = api.destroy_favorite("this is id")

#get a user's like list, print all tweets that the user likes from one list
screen = "this is screen name"
#get all "like" tweets
f = api.favorites(screen)
for i in f:
    print(status.user.screen)



