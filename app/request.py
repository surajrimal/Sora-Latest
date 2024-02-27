from .models import Articles
from .models import Sources
from newsapi import NewsApiClient
from .config import Config
import urllib.request,json
from datetime import datetime


api_key=None
base_url=None
base_url_for_everything=None
base_url_top_headlines=None
base_source_list=None

def publishedArticles():
    newsapi = NewsApiClient(api_key= Config.API_KEY)
    #get_articles = newsapi.get_everything(sources= 'bbc, cnn, reuters, cnbc, the-verge, gizmodo, the-next-web, techradar, recode, ars-technica', q='Sora')
    get_articles = newsapi.get_everything(q='Sora', language='en', sort_by='publishedAt', page_size=10)

    all_articles = get_articles['articles']
    articles_results = []
    source = []
    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []
    for i in range(len(all_articles)):
        article = all_articles[i]

        source.append(article['source'])
        title.append(article['title'])
        desc.append(article['description'])
        author.append(article['author'])
        img.append(article['urlToImage'])
        date_obj = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
        formatted_date = date_obj.strftime('%B %d, %Y')
        p_date.append(formatted_date)
        
        url.append(article['url'])

        article_object = Articles(source, title, desc, author, img, p_date, url)

        articles_results.append(article_object)

        contents = zip(source, title, desc, author, img, p_date, url)

    return  contents

