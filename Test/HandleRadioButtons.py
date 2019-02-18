'''
Created on 06-Jan-2019

@author: user
'''
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")

driver.get("https://facebook.com")

elem = driver.find_element_by_xpath("//input[@value='1']")

driver.find_element_by_xpath("//input[@value='1']").click()

if(elem.is_selected() == True):
    print("clicking on Male Element ")
    driver.find_element_by_xpath("//input[@value='2']").click()
else:
    print("clicking on fe-Male Element ")
    elem.click()
    





if __name__ == '__main__':
    pass