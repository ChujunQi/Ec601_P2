# this file will show how to delete a tweet

import os
import twitter
import requests, json
import numpy


#delete function to delete tweets
def delete(tweets):
    delete_tweet = []
    # get all tweets that the user wants to delete
    for i in tweets:
        delete_tweet.append(e["tweet"]["id_str"])
    # delete all tweets in the list
    for things in delete_tweet:
        api.DestroyStatus(things)

