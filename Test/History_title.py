'''
Created on 08-Jan-2019

@author: user
'''
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.delete_all_cookies()

driver.get("https://facebook.com")

driver.set_page_load_timeout(60)

driver.execute_script("history.go(0);")








if __name__ == '__main__':
    pass