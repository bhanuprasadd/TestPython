'''
Created on 08-Jan-2019

@author: user
'''
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")

driver.get("https://spicejet.com")

driver.maximize_window()

lst = driver.get_cookies()

for cookie in lst:
    print (cookie)

driver.delete_all_cookies()





if __name__ == '__main__':
    pass