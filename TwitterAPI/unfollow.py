import requests, tweepy

#unfollow a user
url = "https://api.twitter.com/2/users//following/"

payload = ""
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

#unfollow a user specfic code
consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"

person = tweepy.OAuthHandle(consumer, c_secret)
person.set_access_token(token, at_secret)

api = tweepy.API(person)
screen = "the screen_name that the user you want to check"

api.destroy_friendship(screen)

#unfollow a user that no following back
follower = api.followers_ids(screen)
friend = api.friends_ids(screen)

for i in friends:
    for j not in followers:
        api.destroy_friendship(j)


