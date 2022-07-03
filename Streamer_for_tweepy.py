from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import Credentials

class TweetListener(StreamListener):
    #Will take in data from tweets
    def on_data(self, data):
        print(data)
        #Return boolean to ensure everything goes well
        return True
    
    def on_error(self, status):
        #Print error message
        print(status)
        
if __name__ == "__main__":
    listener = TweetListener()
    authentication = OAuthHandler(Credentials.Consumer_Key, Credentials.Consumer_Secret)
    authentication.set_access_token(Credentials.Access_Token, Credentials.Acess_Token_Secret)

    stream = Stream(authentication, listener)
    #Filter tweets by key word
    #TO-DO: Filter these tweets by location!
    stream.filter(track=['venezolanos', 'venecos', 'venezolanas', 'venecas', 'de Venezuela'])
