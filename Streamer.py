import tweepy
import Credentials
import HashtagList


#Variables for search
hashtag_list = []
tweet_amount = 10


#Authentication handler

auth_Handler = tweepy.OAuthHandler(Credentials.Consumer_Key, Credentials.Consumer_Secret)
auth_Handler.set_access_token(Credentials.Access_Token, Credentials.Access_Token_Secret)

api = tweepy.API(auth_Handler)

i = 0
tweet_count = 0
while i < 4:
    tweets = tweepy.Cursor(api.search_tweets, q=hashtags[i], land='es').items(3000)
    for tweet in tweets:
        final_tweet = tweet.text.replace('RT', '')  
        with open("ColombiaTweets.txt", "r+") as file: 
            if (final_tweet not in file.read()):
                tweet_count = tweet_count + 1 
                print("Tweet " + str(tweet_count) + ": " + final_tweet + " \n" , file=file)
    i = i + 1

file.close()








    
