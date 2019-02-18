'''
Created on 06-Jan-2019

@author: user
'''
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")

driver.get("https://spicejet.com")

driver.find_element_by_id("ctl00_mainContent_ddl_originStation1_CTXT").click()

driver.find_element_by_xpath("//a[text()=' Hyderabad (HYD)']").click()

driver.find_element_by_xpath("(//a[@value='GOI'])[2]").click()





if __name__ == '__main__':
    pass