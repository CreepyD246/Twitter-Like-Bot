import tweepy

# Authentication and Initialization code
auth = tweepy.OAuthHandler("API_KEY", "API_SECRET_KEY")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
api = tweepy.API(auth)

# Creating a StreamListener class
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        print("Tweet Found!")
        print(f"TWEET: {tweet.author.screen_name} - {tweet.text}")
        if tweet.in_reply_to_status_id is None and not tweet.favorited:
            try:
                print("Attempting like...")
                api.create_favorite(tweet.id)
                print("Tweet successfully liked :)")
            except Exception as err:
                print(err)

# Creating StreamListener
stream_listener = MyStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["Python"], languages=["en"])
