# test Wikipedia with proper title, content

import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
from urllib.parse import unquote

class TestWikipedia(unittest.TestCase):
    # the global object bs is shared between tests
    bs = None

    # the unittest-specified function setUpClass, which is run only once at the start of the class 
    # (unlike setUp, which is run before every individual test)
    # setUpClass() is a static method belongs to the Class, not each instance, which is different from setUp()
    def setUpClass():
        print('Setting up the test Class')
        url = 'http://en.wikipedia.org/wiki/Monty_Python'
        TestWikipedia.bs = BeautifulSoup(urlopen(url), 'html.parser')
    
    # run before each individual test
    def setUp(self):
        print('Setting up the test')

    # run after each individual test
    def tearDown(self):
        print('Tearing down the test')

    # tests whether the title of the page is the expected “Monty Python”
    def test_titleText(self):
        print('Test title')
        pageTitle = TestWikipedia.bs.find('h1').get_text()
        self.assertEqual('Monty Python', pageTitle)

    # test makes sure that the page has a content div
    def test_contentExists(self):
        print('Test content')
        content = TestWikipedia.bs.find('div',{'id':'mw-content-text'})
        self.assertIsNotNone(content)

    


# make sure the code is executed directly by Python, not any "import" statement
if __name__ == '__main__':
    unittest.main()