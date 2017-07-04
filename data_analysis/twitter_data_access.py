import json

from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

consumer_key = '8zhY3gkSuNxnUvQVlLxxYYwGv'
consumer_secret = 'IcnG9YQY6hGYp2q9cWKW6Dfp7EDFKJWMnekSjNGAWsXPy2hr4u'
access_token = '84374247-7fIBIm0wzJa5e3TMenjkdtIVo5TFsnOLvl6yQdqPm'
access_token_secret = 'PHcOTjc0L46MfnYhE6uQQlleBW90VdzMoQvczycaIx9jP'


auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)


class PrintListener(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':
            print(status.text)
            print(status.author.screen_name,
                  status.created_at,
                  status.source,
                  '\n')

    def on_error(self, status_code):
        print("Error code: {}".format(status_code))
        return True  # keep stream alive

    def on_timeout(self):
        print('Listener timed out!')
        return True  # keep stream alive


def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ('en',)
    stream.sample(languages=languages)


def pull_down_tweets(screen_name):
    api = API(auth)
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    for tweet in tweets:
        print(json.dumps(tweet._json, indent=4))


if __name__ == '__main__':
    # print_to_terminal()
    pull_down_tweets(auth.username)
