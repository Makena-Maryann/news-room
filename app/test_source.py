import unittest
from models import source
Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_source = Source('abc-news', 'ABC News', 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.', 'https://abcnews.go.com', 'us')

    def test_instance(self):
        '''
        test that checks if our object is an instance of the Source class
        '''
        self.assertTrue(isinstance(self.new_source,Source)) 

    def test_init(self):
        '''
        test case to test if the object is instantiated correctly
        '''
        self.assertEqual(self.new_source.id,'abc-news')
        self.assertEqual(self.new_source.name,'ABC News')
        self.assertEqual(self.new_source.description,'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.')
        self.assertEqual(self.new_source.url,'https://abcnews.go.com')
        self.assertEqual(self.new_source.country,'us')
               

if __name__=='__main__':
    unittest.main()        
