'''
Created on 07-Jan-2019

@author: user
'''
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")

driver.get("https://spicejet.com")
driver.maximize_window()

driver.find_element_by_xpath("//a[@title='Manage Booking']").click()

driver.back()

driver.forward()

driver.refresh()


if __name__ == '__main__':
    pass