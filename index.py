from tweepy.streaming import StreamListener
from tweepy import Stream , OAuthHandler , API
from cred import *


class StListener(StreamListener):
	def on_status(self, status):
		print(status)

	def on_data(self,data):
		print(data)

	def on_error(self,status):
		print(status)

if __name__ == "__main__":
	listener = StListener()
	auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
	api = API(auth)
	stream = Stream(auth =api.auth,listener=listener)
	stream.filter(track=["python","esl_csgo","donald trump","node"])