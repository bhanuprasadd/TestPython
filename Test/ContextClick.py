'''
Created on 08-Jan-2019

@author: user
'''
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")

driver.delete_all_cookies()

driver.get("https://facebook.com")

driver.maximize_window()

driver.set_page_load_timeout(60)

driver.implicitly_wait(60)

ele = driver.find_element_by_xpath("//label[text()='Female']")
'''
action = ActionChains(driver)
action.context_click(ele).perform()
'''
action = ActionChains(driver)
action.double_click(ele).perform()




if __name__ == '__main__':
    pass