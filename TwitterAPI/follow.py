# some contents about following, including follow a user, get follower's names or get a user's following, count followers.
import os
import tweepy
import requests, json

# follow a user
def becomeFollower(users, userid):
    url = "https://api.twitter.com/2/users//following"

    #here will get the user that you want to follow
    payload = "{\n    \"userid\": \"2244994945\"\n}"
    my_header = {}

    response = requests.request("POST", url, headers=my_header, data=payload)

    print(response.text)

#get followers of a user
def getFollower(users):
    get_url = "https://api.twitter.com/2/users//followers"

    #here two dict is empty because it will get those info from followers
    get_payload={}
    get_header = {}

    response = requests.request("GET", get_url, headers=get_header, data=get_payload)

    print(response.text)

#get a user's following 
def getFollowing(users):
    url = "https://api.twitter.com/2/users//following"
    u_payload={}
    u_headers = {}

    response = requests.request("GET", url, headers=u_headers, data=u_payload)

    print(response.text)

#count your followers
def counting(myfollower):
    c = 0
    for i in myfollower.items():
        c += 1
    print(str(c))


#get all the followers
def getFollowerName(api, screen, count):
    for x in tweepy.Cursor(api.followers, screen).items(str(count)):
        print(x.screen)


#get users that the user following
def getFollowingName(api):
    for x in tweepy.Cursor(api.friends).items():
        print(x.screen)



