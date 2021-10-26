#including contents about like or unlike a tweet and getting a user's like list
import os
import tweepy
import requests, json

#like a tweet, two methods: likeTweet and simpleLike
def likeTweet(person, likeID):
    api = tweepy.API(person)
    like = api.create_favorite("likeID")
    print(f"you like {likeID}'s tweet ", likeID)


def simpleLike(users, tweet_id, tweet_id_like):
    url = "https://api.twitter.com/2/users//likes"

    payload = "// Replace tweet_id_like with the ID you wish to like\n{\n    \"tweet_id\": \"tweet_id_like\"\n}"
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)



#unlike a tweet
def unlikeTweet(person, unlikeID):
    api = tweepy.API(person)
    unlike = api.destroy_favorite("unlikeID")
    print(f"you like {unlikeID}'s tweet ", unlikeID)

def simpleUnlike(users, tweet_id, tweet_id_like):
    url = "https://api.twitter.com/2/users//likes"

    payload = "// Replace tweet_id_like with the ID you wish to unlike\n{\n    \"tweet_id\": \"tweet_id_like\"\n}"
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


#get a user's like list, two methods to get: likeList and getLiked
def likeList(screen):
    likes = api.favorites(screen)
    for i in likes:
        print(status.user.screen)


def getLiked(users):
    url = "https://api.twitter.com/2/users//liked_tweets"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

