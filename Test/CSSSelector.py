'''
Created on 05-Jan-2019

@author: user
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.get("https://facebook.com")
driver.maximize_window()
driver.find_element_by_css_selector("#email").send_keys("testing@gmail.com")





if __name__ == '__main__':
    pass