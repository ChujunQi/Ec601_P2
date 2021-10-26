#search tweets that contains the content that user searches
import os
import tweepy
import requests, json


# this function will search tweets by content
def getByContent(api, keyword, no_retweet):
    # user can input multiple keywords represent by a string, like "banana apple orange"
    #split keywords and save in a list
    keylist = keyword.split()
    myWord = []
    # if user does not want to see retweets
    if no_retweet == True:
        for key in keylist:
            # get keywords one by one
            myWord[key] = "keyword -filter:retweets"
            search = tweepy.Cursor(api.search, q = myWord[key], lang = "en", since = date_since)
            # get location and username of the user who tweet the content
            for i in search:
                result = [i.user.screen_name, i.user.location]
                print(result)
    # if user wants to see retweets
    else:
        for key in keylist:
            # get keyword one by one
            myWord[key] = "keyword"
            search = tweepy.Cursor(api.search, q = myWord[key], lang = "en", since = date_since)
            # get location and username of the user who tweet the content
            for i in search:
                result = [i.user.screen_name, i.user.location]
                print(result)




