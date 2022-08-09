import tweepy
import Credentials
import HashtagList
import nltk
import nltk.corpus
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import sys
import openpyxl



def searcher(hashtags, filename):
    translator = Translator(['translate.googleapis.com'])
    auth_Handler = tweepy.OAuthHandler(Credentials.Consumer_Key, Credentials.Consumer_Secret)
    auth_Handler.set_access_token(Credentials.Access_Token, Credentials.Access_Token_Secret)
    api = tweepy.API(auth_Handler, wait_on_rate_limit=True)
    tweet_count = 425
    analyzer = SentimentIntensityAnalyzer()
    i = 0
    while i < len(hashtags):
        tweets = tweepy.Cursor(api.search_tweets, q=hashtags[i], lang='es').items(500000)
        for tweet in tweets:
            untrans_final_tweet = tweet.text.replace('RT', '') 
            final_tweet =  translator.translate(untrans_final_tweet, dest='en')
            final_tweet = str(final_tweet)
            with open(filename, "r+") as file: 
                if str(final_tweet) not in file.read():
                    tweet_count = tweet_count + 1 
                    comp = analyzer.polarity_scores(final_tweet)['compound']
                    print(str(comp) + "  | Tweet " + str(tweet_count) + ": " + final_tweet + " \n" , file=file)
                    print("Tweet retreived \n")
        i = i + 1
    file.close()

def total_sentiment_calculator(filename, list):
    with open(filename, "r+") as file: 
        pos_average = 0.0
        pos_raw = 0.0
        pos_count = 0
        neg_average = 0.0
        neg_raw = 0.0
        neg_count = 0
        overall_average = 0.0
        Lines = file.readlines()
        for line in Lines:
            if (line != '\n' and line != ' \n'):
                try:
                    score = float(line.split()[0])
                    if score > 0:
                        pos_count = pos_count + 1
                        pos_raw = pos_raw + score
                    elif score < 0:
                        neg_count = neg_count + 1
                        neg_raw = neg_raw + score
                except ValueError:
                    pass
        overall_average = (pos_raw + neg_raw) / (pos_count + neg_count)
        pos_average = pos_raw / pos_count
        neg_average = neg_raw / neg_count
        sent_list = [ int(pos_count), pos_average, int(neg_count), neg_average, overall_average]
        list[:] = sent_list

def main():
    
    #Calling searcher methods to gather data to text files
    
    searcher(HashtagList.hashtags_Ecuador, 'EcuadorTweets.txt')
    searcher(HashtagList.hashtags_Peru, 'PeruTweets.txt')
    searcher(HashtagList.hashtags_Argentina, 'ArgentinaTweets.txt')
    searcher(HashtagList.hashtags_Chile, 'ChileTweets.txt')
    searcher(HashtagList.hashtags_Colombia, 'ColombiaTweets.txt')
    searcher(HashtagList.hashtags_Panama, 'PanamaTweets.txt')
    searcher(HashtagList.hashtags_US, 'USTweets.txt')
    searcher(HashtagList.hashtags_RepDom, 'RepDomTweets.txt')

    
    #Creating lists and calling method

    Ecuador_list = []
    total_sentiment_calculator('EcuadorTweets.txt', Ecuador_list)
    Peru_list = []
    total_sentiment_calculator('PeruTweets.txt', Peru_list)
    Argentina_list = []
    total_sentiment_calculator('ArgentinaTweets.txt', Argentina_list)
    Chile_list = []
    total_sentiment_calculator('ChileTweets.txt', Chile_list)
    Colombia_list = []
    total_sentiment_calculator('ColombiaTweets.txt', Colombia_list)
    Panama_list = []
    total_sentiment_calculator('PanamaTweets.txt', Panama_list)
    US_list = []
    total_sentiment_calculator('USTweets.txt', US_list)
    RepDom_list = []
    total_sentiment_calculator('RepDomTweets.txt', RepDom_list)


    #Creating Dictionary based off the lists
    country_dict = {'Ecuador' : Ecuador_list, 'Peru' : Peru_list, 'Chile' : Chile_list,
    'Panama' : Panama_list, 'US' : US_list, 'Dominican Republic': RepDom_list, 'Colombia' : Colombia_list,
    'Argentina' : Argentina_list}

    df = pd.DataFrame(country_dict, index=[ 'Number of Positive Reviews', 'Postive Score Average',
    'Number of Negative Reviews', 'Negative Score Average', 'Overall Sentiment Average'])

    #Importing to Excel File
    df.to_excel("CountrySentiment(08-09).xlsx")
    print("Excel file successfully created!")


if __name__ == '__main__':
    sys.exit(main())









    
