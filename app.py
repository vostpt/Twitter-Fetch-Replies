# Import Libraries

import tweepy
import csv
import configparser

#Import API credentials

config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = config.get('Twitter', 'ConsumerKey')
consumer_secret = config.get('Twitter', 'ConsumerSecret')
access_token = config.get('Twitter', 'AccessToken')
access_secret = config.get('Twitter', 'AccessSecret')


# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# Get tweet ID and account name from user
tweet_id = input("Enter the tweet ID: ")
account_name = input("Enter the account name: ")

replies = tweepy.Cursor(api.search_tweets, q=f'to:{account_name}', since_id=tweet_id, tweet_mode='extended').items()

with open('psp_replies.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "user", "text", "url"])
    
    for reply in replies:
        if hasattr(reply, 'in_reply_to_status_id_str'):
            if (reply.in_reply_to_status_id_str == tweet_id):
                url = f"https://twitter.com/{reply.user.screen_name}/status/{reply.id_str}"
                writer.writerow([reply.id_str, reply.user.screen_name, reply.full_text, url])
