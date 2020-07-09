import urllib.request,json
from .models import Source,Article

api_key = None
source_url = None
articles_url = None

def configure_request(app):
    global api_key,source_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config["NEWS_API_SOURCE_URL"]
    articles_url = app.config["NEWS_API_ARTICLES_URL"]

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_url.format(api_key)

    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)

    return source_results            

def process_results(source_list):
    '''
    Function that processes the sources result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns:
        source_results: A list of source objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        country = source_item.get('country')

        if country:
            source_object = Source(id,name,description,url,country)
            source_results.append(source_object)

    return source_results   

def get_articles(sources_id):
    '''
    Function that gets the json response to our url request
    '''

    get_articles_url = articles_url.format(sources_id,api_key) 

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results = None

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_data(article_results_list)

    return article_results        

def process_data(article_list):
    '''
    Function that processes the article result and transform them to a list of Objects

    Args: 
        article_list: A list of dictionaries that contain article details

    Returns:
        article_results: A list of article objects    
    '''
    article_results = []
    for article_item in article_list:
        image = article_item.get('urlToImage')
        description = article_item.get('description')
        time = article_item.get('publishedAt')
        main_page_url = article_item.get('url')

        if image:
            article_object = Article(image,description,time,main_page_url)
            
            article_results.append(article_object)

    return article_results        




