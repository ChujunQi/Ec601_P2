# EC601_GoogleNLP
GoogleNLP API mainly focus on machine learning and cloud, which is a good tool for users to understand basic contents about AI. Today we will discuss the sentiment analysis. Sentiment analysis can detect the sentiment in the text and to determine if the overall text is positive, neutral, or negative. 

## Rule of Sentiment Analysis
The rule-based sentiment analysis will count the number of words with sentiment and separate them to mainly three types: positive, neutral, and negative. After counting, the system will compare the results and give an overall score of the text. For example, a text includes 2 negative words and 6 positive words, and then the result will define it has a positive score. Besides that, the score of different words is a little different, such as ok and excellent. 

## Functions of Sentiment Analysis
Almost all companies in the world need to get user's feedback to develop their products. Using sentiment analysis is a good choice to analyze user's reviews. For instance, a restaurant needs to collect user's review and analyze them so that they can get an overall positive or negative evaluation. And if the restaurant get an overall positive evaluation, they also need to check the score since the score, which determines a very positive or a little positive result. 

## The Way to Approach Sentiment Analysis
The file sentiment.py is an example to achieve this goal. In this file, the system will read the txt file that user provided and then count words with sentiment in each sentence with a score and a magnitude, and then calculate an overall score and magnitude for the whole file. The score means the positive or negative attitude, and the magnitude determine if the evaluation is emotional. For instance, if a file get a 2.5 score and a 5 magnitude, it means the content of the file is positive and it may contain higher number of emotional words. 
