from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import Credentials


class TwitterStreamer():
#Streams + Processes Tweets    
    def stream_tweets(self, filename_of_where_we_want_it, hashtags):
        #Handling authentication and connection to API
        listener = TweetListener()
        authentication = OAuthHandler(Credentials.Consumer_Key, Credentials.Consumer_Secret)
        authentication.set_access_token(Credentials.Access_Token, Credentials.Acess_Token_Secret)

        stream = Stream(authentication, listener)
        #Filter tweets by key word
        #TO-DO: Filter these tweets by location!
        #Hashtags must be a list that had to be passed later
        stream.filter(track=hashtags)


class TweetListener(StreamListener):
#Prints tweets

    #This is a constructor!
    def init (self, tweets_filename):
        self.tweets_filename = tweets_filename

    #Will take in data from tweets
    def on_data(self, data):
        try:
            print(data)
            #Write into file and the append
            with open(self.tweets_filename, 'a') as tf:
                tf.write(data) 
            #Return boolean to ensure everything goes well
            return True
        except BaseException as e:
            print("Error on data to print" % str(e))
        return true
    
    def on_error(self, status):
        #Print error message
        print(status)

    
        
if __name__ == "__main__":
    hashtags = ["venezonalos", "venecos", "venezolanas", "venecas"]
    filename_for_tweets = "tweets_analyzed.txt"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(filename_for_tweets, hashtags)