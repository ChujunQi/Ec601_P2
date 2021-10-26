import deleteTweet as DT 


consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"

api = twitter.Api(consumer_key = consumer, consumer_secret = c_secret, 
                access_token_key = token, access_token_secret = at_secret)


getTweets = []
with open('editedTweet.json') as json_file:
        myTweet = json.load(json_file)

deletethings = []
deletethings = DT.delete(getTweets)

print("you have delete tweets you want to delete")
print("here are tweets you delete:")

for i in deletethings:
    print(i)

 
