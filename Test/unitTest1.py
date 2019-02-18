'''
Created on 08-Jan-2019

@author: user
'''
import unittest
from selenium import webdriver



class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://facebook.com")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()


    def testName(self):
      
        self.assertEqual('Facebook – log in or sign up', self.driver.title, "the title is not equal")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()