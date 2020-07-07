import unittest
from models import article
Article = article.Article


class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_article = Article('https://s.abcnews.com/images/US/WireAP_bf8cec6afa1d4c5e99f80f3b6143e126_16x9_992.jpg', 'A custom casket is being built for the funeral of the world’s longest-surviving conjoined twins, who died July 4 in Ohio of natural causes', '2020-07-07T17:48:32Z', 'https://abcnews.go.com/US/wireStory/brother-longest-surviving-conjoined-twins-made-68-71653548')

    def test_instance(self):
        '''
        test that checks if our object is an instance of the Article class
        '''
        self.assertTrue(isinstance(self.new_article,Article)) 

    def test_init(self):
        '''
        test case to test if the object is instantiated correctly
        '''
        self.assertEqual(self.new_article.image,'https://s.abcnews.com/images/US/WireAP_bf8cec6afa1d4c5e99f80f3b6143e126_16x9_992.jpg')
        self.assertEqual(self.new_article.description,'A custom casket is being built for the funeral of the world’s longest-surviving conjoined twins, who died July 4 in Ohio of natural causes')
        self.assertEqual(self.new_article.time,'2020-07-07T17:48:32Z')
        self.assertEqual(self.new_article.url,'https://abcnews.go.com/US/wireStory/brother-longest-surviving-conjoined-twins-made-68-71653548')
        
               
if __name__=='__main__':
    unittest.main()        
