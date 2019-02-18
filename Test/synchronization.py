'''
Created on 08-Jan-2019

@author: user
'''
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as waits
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")

driver.get("https://facebook.com")

driver.set_page_load_timeout(100)

print(driver.title)

driver.implicitly_wait(60)

driver.find_element_by_id("pass").send_keys("testing")

element = WebDriverWait(driver,10).until(waits.presence_of_element_located((By.ID,"Element")))


 



if __name__ == '__main__':
    pass