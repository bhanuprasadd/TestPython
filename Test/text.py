'''
Created on 06-Jan-2019

@author: user
'''
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element_by_id("email").send_keys("testing")

val = driver.find_element_by_id("email").get_attribute('value')
print(val)

txt = driver.find_element_by_xpath("//*[@id='u_0_11']").text
print(txt)



if __name__ == '__main__':
    pass