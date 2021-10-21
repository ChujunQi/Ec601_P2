import requests, tweepy

#unfollow a user
url = "https://api.twitter.com/2/users//following/"

payload = ""
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

#get user's info
consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"

#get the user
person = tweepy.OAuthHandle(consumer, c_secret)
person.set_access_token(token, at_secret)

api = tweepy.API(person)
screen = "the screen_name that the user you want to check"

# unfollow the user with his or her screen name
api.destroy_friendship(screen)

#unfollow a user that no following back
follower = api.followers_ids(screen)
friend = api.friends_ids(screen)

for i in friends:
    for j not in followers:
        api.destroy_friendship(j)


