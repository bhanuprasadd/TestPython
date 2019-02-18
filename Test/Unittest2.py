'''
Created on 09-Jan-2019

@author: user
'''
import unittest
from selenium import webdriver



class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://facebook.com")


    def tearDown(self):
        self.driver.close()


    def testName(self):
        self.assertEqual("Facebook–log in or sign up", self.driver.title, "title is not matched")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()