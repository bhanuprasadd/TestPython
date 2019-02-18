'''
Created on 06-Jan-2019

@author: user
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.get("https://facebook.com")
driver.maximize_window()

select = Select(driver.find_element_by_id("day"))
select.select_by_visible_text("10")
select.select_by_value("27")
select.select_by_index(12)






if __name__ == '__main__':
    pass