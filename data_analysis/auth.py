from tweepy import OAuthHandler

consumer_key = '8zhY3gkSuNxnUvQVlLxxYYwGv'
consumer_secret = 'IcnG9YQY6hGYp2q9cWKW6Dfp7EDFKJWMnekSjNGAWsXPy2hr4u'
access_token = '84374247-7fIBIm0wzJa5e3TMenjkdtIVo5TFsnOLvl6yQdqPm'
access_token_secret = 'PHcOTjc0L46MfnYhE6uQQlleBW90VdzMoQvczycaIx9jP'

auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)
