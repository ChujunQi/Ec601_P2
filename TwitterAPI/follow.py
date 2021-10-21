import os
import tweepy
import requests, json
#resource: https://documenter.getpostman.com/view/9956214/T1LMiT5U#2a12978f-ebf2-4eb3-8331-c7f4bcb1e32c

# follow a user
url = "https://api.twitter.com/2/users//following"

payload = "{\n    \"user id that you want to follow\": \"2244994945\"\n}"
my_header = {}

response = requests.request("POST", url, headers=my_header, data=payload)

print(response.text)

#get followers of a user
get_url = "https://api.twitter.com/2/users//followers"

get_payload={}
get_header = {}

response = requests.request("GET", get_url, headers=get_header, data=get_payload)

print(response.text)

#get a user's following 
u_payload={}
u_headers = {}

response = requests.request("GET", url, headers=u_headers, data=u_payload)

print(response.text)

#count your followers
consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"

person = tweepy.OAuthHandle(consumer, c_secret)
person.set_access_token(token, at_secret)

api = tweepy.API(person)
screen = "the screen_name that the user you want to check"

all_f = tweepy.Cursor(api.followers, screen)

c = 0
for i in all_f.items():
    c += 1
print(str(c))

#get all the followers
for x in tweepy.Cursor(api.followers, screen).items(str(c)):
    print(x.screen)

#get users that the user following
for x in tweepy.Cursor(api.friends).items():
    print(x.screen)


