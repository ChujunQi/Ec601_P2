# search tweets by timeline
import os, tweepy, pandas
import twitter
import datetime


# this function will get tweets between start time and end time
def getByTimeline(tweetList):
    # get start time and end time 
    start = datetime.strptime('your start time', '%b %d %H:%M:%S %z %Y')
    end = datetime.strptime('your end time', '%b %d %H:%M:%S %z %Y')

    myTweet = []
    #save all tweets between the timeline in myTweet
    for item in tweetList:
        tweet_time = datetime.strptime(item["tweet"]["created_at"], '%a %b %d %H:%M:%S %z %Y')
        if (tweet_time >= start and tweet_time <= end):
            myTweet.append(item["tweet"]["id_str"])

    print(myTweet)

