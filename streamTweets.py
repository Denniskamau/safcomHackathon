import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#Variables that contains the user credentials to access Twitter API
access_token = 
access_token_secret = 
consumer_key = 
consumer_secret = 


#This is a basic listener that just prints received tweets to stdout.
class Streaming(StreamListener):
    # def on_connect(self):
    #     print("you are connected to the streaming server")

    def on_data(self, data):
        print(data,',')

        return True

    def on_error(self, status):
        print('Error: ' + repr(status))
        return False


start = Streaming()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, start)

#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=['epl'],languages=["en"])
