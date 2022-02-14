import tweepy
import credentials
import requests
#get a random quote and its author from quotable api
response = requests.get('https://api.quotable.io/random')
data = response.json()
quote = data['content']
author = data['author']
toTweet = quote + ' - ' + author
#get the twitter api keys from the credentials file
consumer_key = credentials.API_KEY
consumer_secret_key = credentials.API_SECRET_KEY
access_token = credentials.ACCESS_TOKEN
access_token_secret = credentials.ACCESS_TOKEN_SECRET
bearer_token = credentials.BEARER_TOKEN
#authenticate with the twitter api
client = tweepy.Client(bearer_token, consumer_key, consumer_secret_key, access_token,  access_token_secret)
#post the quote to twitter
response = client.create_tweet(text=toTweet)
print("Tweeted: " + toTweet)