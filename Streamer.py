from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import Credentials
import CoordinateList 


###AUTHENTICATION CLASS
class Authenticate():

    def authenticate(self):
        authentication = OAuthHandler(Credentials.Consumer_Key, Credentials.Consumer_Secret)
        authentication.set_access_token(Credentials.Access_Token, Credentials.Acess_Token_Secret)
        return authentication

class TwitterStreamer():
#Streams + Processes Tweets    

    def init(self):
        self.twitter_authenticator = Authenticate()

    def stream_tweets(self, filename_of_where_we_want_it, hashtags):
        #Handling authentication and connection to API
        listener = TweetListener(filename_of_where_we_want_it)
        auth = self.twitter_authenticator.authenticate()
        stream = Stream(auth, listener)
        #Filter tweets by key word
        #TO-DO: Filter these tweets by location!
        #Hashtags must be a list that had to be passed later

        #Apply filter based on vacation
        stream.filter(locations=[CoordinateList.Colombia])


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
        return True
    
    def on_status(self, status):
        hashtags = ["venezolanos", "venecos", "venezolanas", "venecas"]
        i = 0
        while i <  hashtags.len():
            if hashtags[i] in status.text.lower():
                print(status)


    def on_error(self, status):
        #If we mess up on Twitter and it doesn't like it
        if status == 420:
            #Stop it there
            return False
        #Print error message
        print(status)

    
        
if __name__ == '__main__':
    filename_for_tweets = "tweets_analyzed.txt"
    streamer = TwitterStreamer()
    streamer.stream_tweets(filename_for_tweets)