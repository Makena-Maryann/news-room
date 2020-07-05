from flask import render_template
from app import app
from .request import get_sources

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    
    news_sources = get_sources()
    print(news_sources)
    title = 'Home - Verified news source'
    return render_template('index.html',title = title,sources = news_sources) 

@app.route('/source/<int:source_id>')
def source(source_id):
    '''
    View source page function that returns the articles page and its data
    '''
    return render_template('source.html',id = source_id)    