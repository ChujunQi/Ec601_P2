import os, tweepy, pandas
import twitter
import datetime, sys


consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"

api = twitter.Api(consumer_key = consumer, consumer_secret = c_secret, 
                    access_token_key = token, access_token_secret = at_secret)


print("please enter your consumer key: ", sys.argv[0])
print("please enter your consumer secret: ", sys.argv[1])
print("please enter your access token: ", sys.argv[2])
print("please enter your access token secret: ", sys.argv[3])
print("please enter your search type, timeline(T) or content(C): " sys.argv[4])


if(sys.argv[4] == 'T'):
    mylist = None;
    with open('editedTweet.json') as json_file:
    mylist = json.load(json_file)

    start = datetime.strptime('your start time', '%b %d %H:%M:%S %z %Y')
    end = datetime.strptime('your end time', '%b %d %H:%M:%S %z %Y')

    myTweet = []

    for item in mylist:
        tweet_time = datetime.strptime(item["tweet"]["created_at"], '%a %b %d %H:%M:%S %z %Y')
        if (tweet_time >= start and tweet_time <= end):
            myTweet.append(item["tweet"]["id_str"])
    print(myTweet)

if(sys.argv[4] == 'C'):
    print("please enter keyword you want to search: ", sys.argv[8])
    myword = sys.argv[8]
    print("do you want to find retweet? Y or N: ", sys.argv[9])
    if(sys.argv[9] == 'Y'):
        key_word = myword
        yourSearch = tweepy.Cursor(api.search, q = key_word, lang = "en", since = date_since)
        for i in yourSearch:
            result = [i.user.screen_name, i.user.location]
            print(result)
    if(sys.argv[9] == 'N'):
        key_word = myword + "-filter: retweets"
        yourSearch = tweepy.Cursor(api.search, q = key_word, lang = "en", since = date_since)
        for i in yourSearch:
            result = [i.user.screen_name, i.user.location]
            print(result)


