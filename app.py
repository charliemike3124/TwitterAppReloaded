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
    return [{'User': username.name,
              'Tweets: ': username.statuses_count, 
              'Favorites: ': username.favourites_count,
              'Following: ': username.friends_count,
              'Followers: ': username.followers_count}
           for t in tweets]


@app.route('/')
def index():	
    search = request.args.get('q')	
    try:
        user = api.get_user(search)
        return render_template('home.html', tweets=tweet_info(user))
    except:
        return render_template('home.html')
        print("Error")




def get_tweets(username):
    tweets = api.user_timeline(screen_name=username)                                                                            
    return [{'tweet': t.text,
              'created_at': t.created_at, 
              'username': username,
              'headshot_url': t.user.profile_image_url}
           for t in tweets]

@app.route('/tweet-harvester/<string:username>')
def tweets(username):
  # 'tweets' is passed as a keyword-arg (**kwargs)
  # **kwargs are bound to the 'tweets.html' Jinja Template context
  return render_template("home.html", tweets=get_tweets(username))



if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
