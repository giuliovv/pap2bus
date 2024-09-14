import os
import tweepy
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('TWTR_API_KEY')
api_secret = os.getenv('TWTR_API_SECRET')
access_token = os.getenv('TWTR_ACCESS_TOKEN')
access_token_secret = os.getenv('TWTR_ACCESS_TOKEN_SECRET')

def create_twitter_api():
    client = tweepy.Client(
        consumer_key=api_key, 
        consumer_secret=api_secret,
        access_token=access_token, 
        access_token_secret=access_token_secret
    )
    return client

def split_ideas(ideas):
    return [idea.strip() for idea in ideas.split('|-') if idea.strip()]

def post_to_twitter(ideas, client=create_twitter_api()):
    count = 0
    for item in ideas:
        title = item['title']
        summary = item['summary']
        business_ideas = item['business_ideas']
        
        idea_chunks = split_ideas(business_ideas)

        try:
            first_tweet = f"{title} - {summary}"[:280]
            tweet = client.create_tweet(
                text=f"{title} - {summary}"[:280]
            )
            in_reply_to_tweet_id = tweet.data['id']
            print(f"Tweeted: {first_tweet}")
        except Exception as e:
            print(f"Error tweeting {title}: {e}")
            continue

        for idea in idea_chunks:
            try:
                tweet = client.create_tweet(
                    text=idea,
                    in_reply_to_tweet_id=in_reply_to_tweet_id,
                )
                in_reply_to_tweet_id = tweet.data['id']
                count += 1
                print(f"Tweet #{count}: {idea}")
            except Exception as e:
                print(f"Error tweeting idea for {title}: {e}")

