import tweepy
import friends

consumer_key = "################################"
consumer_secret = "##################################"
access_token = "##########################################"
access_token_secret = "##############################"

#######################################################################

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
