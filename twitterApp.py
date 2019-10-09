import tweepy
import json

CONSUMER_KEY = 'rrGdOqy2bkzI1R0qZDZHQkB5l'
CONSUMER_SECRET = 'UHMkRd5M2EnjJg7qfVHACAPIlwoo43rF7nq1w4FBKbXCNCWdus'

ACCESS_TOKEN = '728370447180550145-qQ3NABtXCqDNJruc5k8nVAxcYofsuhT'
ACCESS_TOKEN_SECRET = 'bpXNnhYSc3eHhnuKdX4NFvNKSYHAZJlaJuvpNas49tCyI'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#screen_name es el alias de la persona en twitter @algo
def analizarAlias():
    nombre = input('Alias del usuario: @')
    twitter= api.get_user(screen_name=nombre)

    print('\n*************')
    print("User: ",twitter.name)
    print("Tweets: ", twitter.statuses_count)
    print("Favorites: ", twitter.favourites_count)
    print("following:", twitter.friends_count)
    print("followers:", twitter.followers_count)
    print('*************')


