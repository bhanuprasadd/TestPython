'''
Created on 04-Jan-2019

@author: user
'''
from selenium import webdriver
browser= webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")
browser.get("https://github.com/")
browser.maximize_window()
browser.find_element_by_class_name("btn-primary-mktg").click()
'''automation.testingtechie@gmail.com'''
browser.quit()

if __name__ == '__main__':
    pass

