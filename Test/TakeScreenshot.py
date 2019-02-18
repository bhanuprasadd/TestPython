'''
Created on 08-Jan-2019

@author: user
'''
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")

driver.get("https://facebook.com")

driver.delete_all_cookies()

driver.maximize_window()

driver.save_screenshot("D:\\my_screen_shot.png")

if __name__ == '__main__':
    pass