'''
Created on 06-Jan-2019

@author: user
'''
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.toolsqa.com/automation-practice-table/")

driver.maximize_window()
txt = driver.find_element_by_xpath("//table/tbody/tr[1]/td[2]").text
print(txt)

driver.find_element_by_xpath("//table/tbody/tr[3]/td[6]/a").click()

if __name__ == '__main__':
    pass