from flask import render_template
from app import app
from .request import get_sources,get_articles

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    news_sources = get_sources()
    print(news_sources)
    title = 'Home - Verified news sources'
    return render_template('index.html',title = title,sources = news_sources) 

@app.route('/articles')
def articles():
    '''
    View source page function that returns the articles page and its data
    '''
    #Getting articles from a specific source
    news_articles = get_articles('abc-news')
    print(news_articles)
    title = 'Latest news from verified sources'
    return render_template('articles.html', title = title, articles = news_articles)

#@app.route('/source/<source_id>')
#def source(source_id):
    #'''
   # View source page function that returns the articles page and its data
    #'''
   # return render_template('source.html',id = source_id)    