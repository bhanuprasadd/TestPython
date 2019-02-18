'''
Created on 06-Jan-2019

@author: user
'''
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.toolsqa.com/iframe-practice-page/")
driver.maximize_window()
e = driver.find_element_by_id("IF1")
driver.switch_to_frame(e)
driver.find_element_by_xpath("//input[@name='firstname']").send_keys("bhanu")

driver.switch_to_default_content()
driver.switch_to_frame("iframe2")
driver.find_element_by_xpath("//a[text()='Hello world!']").click()




if __name__ == '__main__':
    pass