from flask import Flask, render_template, request, json
import tweepy
app = Flask(__name__)

wsgi_app = app.wsgi_app

CONSUMER_KEY = 'rrGdOqy2bkzI1R0qZDZHQkB5l'
CONSUMER_SECRET = 'UHMkRd5M2EnjJg7qfVHACAPIlwoo43rF7nq1w4FBKbXCNCWdus'

ACCESS_TOKEN = '728370447180550145-qQ3NABtXCqDNJruc5k8nVAxcYofsuhT'
ACCESS_TOKEN_SECRET = 'bpXNnhYSc3eHhnuKdX4NFvNKSYHAZJlaJuvpNas49tCyI'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


def tweet_info(username):
    return {'User: ': username.name,
              'Tweets: ': str(username.statuses_count), 
              'Favorites: ': str(username.favourites_count),
              'Following: ': str(username.friends_count),
              'Followers: ': str(username.followers_count)}


@app.route('/')
def index():	
    search = request.args.get('q')	
    try:
        user = api.get_user(search)
        print(user)
        return render_template('home.html', tweets=tweet_info(user))
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
