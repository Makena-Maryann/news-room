class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&apiKey={}'

class prodConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configurations class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
        '''
    DEBUG = True          