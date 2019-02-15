import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#Variables that contains the user credentials to access Twitter API
access_token = "360352221-eVqoPAikNUoPc8yEXZLpqvzEBZMGjlJUQ9FRsUXh"
access_token_secret = "CyKahpildPm2UhRVdU3tu5gnfTgWQ0LI63zU6UBsYsI1O"
consumer_key = "c152hflyHQ4kE8EQeYh6sv38D"
consumer_secret = "WArSIMjrKQNL2NMVEvc0ZkqXS9uE3gIMo8Kk21n3icBsSiUWM2"


#This is a basic listener that just prints received tweets to stdout.
class Streaming(StreamListener):
    # def on_connect(self):
    #     print("you are connected to the streaming server")
    def on_data(self, data):
        print("started streaming process......")
        print(data)
        # save the tweets to a csv file.
        fileLocation = './tweets.json'
        with open(fileLocation , 'w') as f:
            json.dump(data, f)
        return True

    def on_error(self, status):
        print('Error: ' + repr(status))
        return False


start = Streaming()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, start)

#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=['kenya'],languages=["en"])