import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#Variables that contains the user credentials to access Twitter API
access_token = "360352221-e2oxvLe97TNGQZuM2vdCEy8zBx2JBGItPClOxsFv"
access_token_secret = "hUjCvYHdPLppWeRfidaf0Yfo4Xbu61uZ8ze64rtqnVNC1"
consumer_key = "eAuQoYw9ffXtY5LdZm4Gmksfx"
consumer_secret = "5KiTpWGbTG8dtRaBuhcLdoT1jp12vRnr3pJ4yAUDXKLUkoMVk8"


#This is a basic listener that just prints received tweets to stdout.
class Streaming(StreamListener):
    # def on_connect(self):
    #     print("you are connected to the streaming server")
    tweetList = []
    def on_data(self, data):
        #print("started streaming process......")

        # save the tweets to a csv file.
        fileLocation = './tweets.json'

        self.tweetList.append(data)
        print(data,',')
        with open(fileLocation , 'w') as f:
            json.dump(self.tweetList, f)

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