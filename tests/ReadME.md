# Project 2 Test

## Twitter API

### Followers Access
#### Test steps:
1. Create a new twitter account
2. Let 20 people follow the twitter account and have 5 people unfollow the account
3. Let code print all the followers

#### Test data:
A new account: aa; 25 other accounts: bb, cc, ...

#### Expected Result:
It shows the number of followers of this new account and also print out followers' usernames


### Like or Unlike a Tweet
#### Test steps:
1. Publish a tweet using an twitter account
2. Have 5 people to like the tweet and other 5 people like and immediate unlike the tweet

#### Test data:
A tweet, 10 users

#### Expected Result:
For 5 people who like the tweet, they will have the "like" sign bright. Other 5 people will see a bright "like" sign and then the sign is unlight.


### Show Tweets that users Searchs 
#### Test steps:
1. Choose an account that publishes many tweets on differnet timeline and contains different contents
2. Let a user search tweets in the account using timeline and then using contents

#### Test data:
Two twitter accounts

#### Expected result:
When searching by timeline, tweets will be shown by the order of time from the start time to the end time. When searching by contents, tweets will also be shoen by the oeder of time, but it will not show tweets that not contains the content.

### Tweet and Untweet
#### Test steps:
1. Accessing an account
2. Publish two tweets
3. After 10 minutes, delete the second tweet

#### Test data:
One twitter account

#### Expected result:
When publishing two tweets, other users will see two tweets under the account; after 10 minutes, they will only see one tweet.

## GoogleNLP
### Sentiment results
#### Test steps:
1. Having two txt files that contains some sentences 
2. Do sentiment analysis
3. Find another sentiment program to analysis the same file and compare the result

#### Test data:
two txt files 

#### Expected result:
The overall sentiment analysis does not have many differneces, and the results are similar.
