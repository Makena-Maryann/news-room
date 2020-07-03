from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Verified news source'
    return render_template('index.html',title = title) 

@app.route('/source/<int:source_id>')
def source(source_id):
    '''
    View source page function that returns the articles page and its data
    '''
    return render_template('source.html',id = source_id)    