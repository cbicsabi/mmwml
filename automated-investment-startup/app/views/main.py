from flask import render_template, jsonify, request, redirect, url_for
from textblob import TextBlob
import random
import tweepy

from app import app
from app.instance.config_common import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route("/search")
def search():
    return render_template('search.html', title='Search')


@app.route("/search/tweets", methods=["POST"])
def search_tweets():
    search_tweet = request.form.get("search_query")
    t = []
    tweets = api.search(q=search_tweet, tweet_mode="extended")

    for tweet in tweets:
        polarity = TextBlob(tweet._json['full_text']).sentiment.polarity
        subjectivity = TextBlob(tweet._json['full_text']).sentiment.subjectivity
        t.append([tweet._json['full_text'], polarity, subjectivity])
        jsonify({"success": True, "Tweets": t})
        #TODO render t to the HTML page

    return redirect(url_for('search'))


@app.route('/map')
def map():
    return render_template('map.html', title='Map')


@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
