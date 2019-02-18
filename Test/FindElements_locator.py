'''
Created on 05-Jan-2019

@author: user
'''
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")

driver.get("https://facebook.com")
driver.maximize_window()

Elements =driver.find_elements_by_xpath("//input[@name='firstname']")

for Element in Elements:
    Element.send_keys("testing")
    


if __name__ == '__main__':
    pass