'''
Created on 08-Jan-2019

@author: user
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.set_page_load_timeout(60)
ele1 = driver.find_element_by_xpath("//span[text()='Hello. Sign in']")
ele2 = driver.find_element_by_xpath("//span[text()='Your Wish List']")

action = ActionChains(driver)
action.move_to_element(ele1).perform()
driver.implicitly_wait(60)
ele2.click()









if __name__ == '__main__':
    pass