import os
import tweepy
import requests, json
#resources:https://documenter.getpostman.com/view/9956214/T1LMiT5U#d1b48fe8-a190-4587-b286-a23973bf7b47

#like/unlike a tweet
url = "https://api.twitter.com/2/users//likes"

payload = "// Replace tweet-id-you-want-to-like with the ID you wish to like\n{\n    \"tweet_id\": \"tweet-id-you-want-to-like\"\n}"
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)
#response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

#like a tweet
consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"

person = tweepy.OAuthHandle(consumer, c_secret)
person.set_access_token(token, at_secret)

api = tweepy.API(person)
t = api.create_favorite("this is id")

#unlike a tweet
t_1 = api.destroy_favorite("this is id")

#get a user's like list
screen = "this is screen name"
f = api.favorites(screen)
for i in f:
    print(status.user.screen)



