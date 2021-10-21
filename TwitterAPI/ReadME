# EC601_P2_TwitterAPI
As a social media application, Twitter has about 1.45 million users, including companies, restaurants, people, and so on. Twitter provides a platform for users to do a lot of things, such as sending tweets, searching tweets, and following other people's twitter. All of these functions rely on API so that deelopers can collect those data and deal with it. There are some examples to show how API works for different function. 

## Send and Delete
Here is a file called sendTweet.py to show the basic process the API do when a user sends a tweet. When a user sends a tweet, the API will grab the user's consumer key, consumer seceret key, access token key, and access token secret key. After getting those info, API can access the user's account and update the status of this account. And Twitter also let users upload medias, and the process is easy. However, sending a media is complicated for Twitter API. First, it will get the media's information, like url and size. Second, it will request to post the media by sending data to post. Finally, the API will use the same url and let users to send words with the media. 

In deleteTweet.py file, it shows a basic process to delete tweets. In order to delete a tweet or multiple tweets, API also needs to access user's account, which would grab four keys we mentioned before. The API will have a list to collect tweets that needs to be deleted. After collecting those tweets, it will send those tweet ids into delet function. 

## Search - by timeline, by content
In order to search tweets by timeline, we need to have a start time and a end time using datetime library. After getting the period, we will search tweets that fit this condition and grab them into a list. Finally, print the list to users. File searchTimeline.py gives an example how to search tweets by timeline. After execute the file, it will print tweets in this period.

For searching tweets by content, users can choose if they want to search both tweets and retweets or only tweets. To ignore retweets, using a filter retweet to filter them out. And users also can search for more than one keywords to get more accurate tweets, such as boston and restaurants. API will also create a list to contain tweets that fit the information, and users can see who send those tweets and their location, which is convenient to get some information about a specific thing. Finally, the system will give you a list of tweets that contains the content.

## Follow, Unfollow, Like, Block
In the follow.py file, it includes many conditions for following. At first, it gives a basic idea on following a user and get a user's followers and followings. And then the file contains code about counting the number of a user's followers, and specific python code on geting a user's followers and followings. In order to count followers, we will use a function tweepy.Cursor() to grab all the users can fit the situation, and then send those users to a list and count them. After counting those followers, we can then print the list to get the followers of the user. To get the user's following, it is very similar with getting followers. 

For unfollow.py, it also gives a basic instruction on how to unfollow a user. And in the specific code part, the api will get the screen name that you do not want to follow and destroy the relationship using api.destroy_friends(). And there is also a method the check all the followers that not follows back and unfollow them, too. In order to approach this goal, we use two for loops to filter users out, and then use api.destroy_friends() to unfollow.

In the like.py file, it contains examples about how to like or unlike a tweet and how to get a user's like list. To like a tweet, using api.create_favorite() method; to unlike a tweet, using api.destroy_favorite() method. And to get a like list, we can use api.favorites() by providing a screen name. 

Finally, block.py is pretty simply since it is similar with like.py. In order to get a user's block, use api.blocks() to get a list that contains the user's blocks. And just use for loop to print the list out. Then a list of blocking user will come out. 

## Tweet Counts - recent or full-archive
In count.py file, it contains to situation for rencent count and full-archive count. Full-archive count is easier because it does not need additonal information. Just use user.statues_count() to get the number that the user tweeted. For recent count, we can count by having a start time. To count by time, just use api.Cursor(......, since = 'start time') to get all tweets since that date. And we also can count recent tweets by content, just add one more condition, q = "things you want to search". 

## Conclusion
If the twitter is not responding, maybe there is no new data to return or data not found with the user's request, or the request is unvalid. For instance, if a user want to grab more than 900 tweets at one time, the API will not let user do this because the API has a rate limit. For the format of the code, it will request the user's information first to access account, and then the user can do any request on it. In my opinion, those datas can be used for researches, like collecting people's thought about a new product, or people's feelings about something. 

After exploring the Twitter API, I already have an idea about how to use API and how to use the specific libraries. It is amazing that we can use API to communicate with twitter, and I learn how the system works while I am using Twitter. And it is a good experience to have a basic understanding about modular design. 

