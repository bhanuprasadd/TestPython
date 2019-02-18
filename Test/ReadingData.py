'''
Created on 08-Jan-2019

@author: user
'''
from selenium import webdriver

from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")

driver.maximize_window()

driver.delete_all_cookies()

driver.get("https://www.facebook.com/")

driver.set_page_load_timeout(60)

select = Select(driver.find_element_by_id("day"))

select.select_by_index(15)

selOption = select.first_selected_option

print(selOption)

print(selOption.get_attribute("value"))

if __name__ == '__main__':
    pass