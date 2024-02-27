from app import app, cache
from flask import render_template
from .request import publishedArticles
from apscheduler.schedulers.background import BackgroundScheduler

@app.route('/')
@cache.cached(timeout=60*60)
def home():
    print("Inside home")
    articles = publishedArticles()
    return  render_template('home.html', articles = articles)

@app.route('/headlines')
def headlines():
    headlines = publishedArticles()

    return  render_template('headlines.html', headlines = headlines)

def update_cache():
    # Update cache with new data
    cache['data'] = publishedArticles()

