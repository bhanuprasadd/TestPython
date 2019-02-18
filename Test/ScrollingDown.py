'''
Created on 08-Jan-2019

@author: user
'''
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")

driver.get("https://facebook.com")
driver.maximize_window()

'''
execute_script()
'''
driver.set_page_load_timeout(60)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


if __name__ == '__main__':
    pass