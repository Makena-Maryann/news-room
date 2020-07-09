class Source:
    '''
    Source class to define Source Objects
    '''
    def __init__(self,id,name,description,url,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.country = country



class Article:
    '''
    Article class to define Article Objects
    '''
    def __init__(self,image,description,time,main_page_url):
        self.image = image
        self.description = description
        self.time = time
        self.main_page_url = main_page_url
        