'''
Created on 04-Jan-2019

@author: user
'''
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.facebook.com")
driver.maximize_window()
driver.find_element_by_link_text("Forgotten account?").click()


if __name__ == '__main__':
    pass