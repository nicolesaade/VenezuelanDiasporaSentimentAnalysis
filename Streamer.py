import tweepy
import Credentials
import HashtagList
import nltk
import nltk.corpus
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys



def searcher(hashtags, filename):
    translator = Translator(['translate.googleapis.com'])
    auth_Handler = tweepy.OAuthHandler(Credentials.Consumer_Key, Credentials.Consumer_Secret)
    auth_Handler.set_access_token(Credentials.Access_Token, Credentials.Access_Token_Secret)
    api = tweepy.API(auth_Handler)
    i = 0
    tweet_count = 0
    analyzer = SentimentIntensityAnalyzer()
    while i < 4:
        tweets = tweepy.Cursor(api.search_tweets, q=hashtags[i], lang='es').items(3000)
        for tweet in tweets:
            untrans_final_tweet = tweet.text.replace('RT', '') 
            final_tweet =  translator.translate(untrans_final_tweet, dest='en')
            final_tweet = str(final_tweet)
            with open(filename, "r+") as file: 
                if str(final_tweet) not in file.read():
                    tweet_count = tweet_count + 1 
                    comp = analyzer.polarity_scores(final_tweet)['compound']
                    print(str(comp) + "  | Tweet " + str(tweet_count) + ": " + final_tweet + " \n" , file=file)
        i = i + 1
        file.close()


def main():
    

    searcher(HashtagList.hashtags_Ecuador, 'EcuadorTweets.txt')
    searcher(HashtagList.hashtags_Peru, 'PeruTweets.txt')
    searcher(HashtagList.hashtags_Argentina, 'ArgentinaTweets.txt')
    searcher(HashtagList.hashtags_Chile, 'ChileTweets.txt')
    searcher(HashtagList.hashtags_Colombia, 'ColombiaTweets.txt')



if __name__ == '__main__':
    sys.exit(main())









    
