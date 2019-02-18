'''
Created on 06-Jan-2019

@author: user
'''
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.get("https://spicejet.com")
driver.maximize_window()
ele = driver.find_element_by_id("ctl00_mainContent_chk_friendsandfamily")
ele.click()
if(ele.is_selected()== True):
    driver.find_element_by_id("ctl00_mainContent_chk_SeniorCitizenDiscount").click()
    
    driver.find_element_by_id("ctl00_mainContent_chk_SeniorCitizenDiscount").click()
    
else:
    ele.click()
 
    




if __name__ == '__main__':
    pass