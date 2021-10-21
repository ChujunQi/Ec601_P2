import os
import tweepy
import requests, json

#to get access API, use consumer key, consumer secret, access token, and access token secret
#resource: https://iq.opengenus.org/post-image-twitter-api/

consumer = 'this is your consumer key'
c_secret = "your consumer secret"
token = "your access token"
at_secret = "your access token secret"



person = tweepy.OAuthHandle(consumer, c_secret)
person.set_access_token(token, at_secret)
api = tweepy.API(person, wait_on_rate_limit = True)
#send a tweet
api.update_status("here is your content")

#send media tweets
media = open('your media path here', 'rb')
c = media.read()

send_media = { 'media': c, 'media_category': 'tweet_image'}

base_url = 'https://api.twitter.com/'

auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}
person_data = {'grant type': 'client_credentials'}
person_resp = requests.post(url, headers = person_data)
access_token = person_resp.json()['access_token']

image = {'Authorization': 'Bearer {}'.format(access_token)}

url = 'https://upload.twitter.com/1.1/media/upload.json'


#post the image
final = requests.post(url, headers = image, params = send_media)

tweet_meta = {"media_id": media_id, "alt_text": {"text": "something here"}}
meta_url = 'https://upload.twitter.com/1.1/media/metadata/create.json'
meta_resp = requests.post(meta_url, params = tweet_meta, headers = person_data)

#add words with media, do above and then do the following:
t = {'status': 'your content here', 'media_ids' = final}
post_url = 'https://api.twitter.com/1.1/statuses/update.json'
post_resp = requests.post(post_url, params = t, headers = image)
