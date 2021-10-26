# this file will show how to delete a tweet

import os
import twitter
import requests, json
import numpy

# get user's info
consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"

api = twitter.Api(consumer_key = consumer, consumer_secret = c_secret, 
                    access_token_key = token, access_token_secret = at_secret)

#delete function to delete tweets
def delete(tweets):
    delete_tweet = []
    for i in tweets:
        delete_tweet.append(e["tweet"]["id_str"])

    for things in delete_tweet:
        api.DestroyStatus(things)


def main():
    # get all the tweets 
    myTweet = None
    with open('editedTweet.json') as json_file:
        myTweet = json.load(json_file)

    delete(myTweet)

if __name__ == '__main__':
    main()
