from flask import Flask, render_template, request, json
import tweepy, matplotlib.pyplot as plt, pandas as pd, numpy as np
from io import BytesIO
import base64

app = Flask(__name__)

wsgi_app = app.wsgi_app

#Your Token
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# retorna un diccionario con el nombre, tweets, favoritos, seguidores, siguiendo y eficacia 
# del usuario ingresado.
def tweet_info(username, efficiency):    
    print('writing user info.')
    return {'User: ': username.name,
              'Tweets: ': str(username.statuses_count), 
              'Favorites: ': str(username.favourites_count),
              'Following: ': str(username.friends_count),
              'Followers: ': str(username.followers_count),
              'Efficiency of the last 5 posts: ': str(efficiency) + "%"}

#calcula el  promedio de la eficacia de los últimos 5 tweets
#le fórmula utilizada para la eficacia es (Retweets / Likes)
def calculatePostEfficiency(posts):
    print('calculating Efficiency.')
    efficiency = 0
    retweets = 0
    for post in posts:
        if post.favorite_count > 0:
            efficiency += post.retweet_count/post.favorite_count * 100
            print(efficiency)
        else:
            retweets += 1
    print('Efficiency calculated.')
    return round(efficiency / (len(posts) - retweets),2)



    

#página principal
@app.route('/')
def index():	
    input = request.args.get('q')	
    try:
        user = api.get_user(input)
        tweets = api.user_timeline(input, count = 5)
        efficiency = calculatePostEfficiency(tweets)
        return render_template('home.html', tweets=tweet_info(user,efficiency), posts = tweets)
    except Exception as e:
        print(e)
        return render_template('home.html')




if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
