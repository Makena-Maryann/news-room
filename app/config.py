class Config:
    '''
    General configuration parent class
    '''
    pass

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