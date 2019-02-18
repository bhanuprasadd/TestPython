'''
Created on 06-Jan-2019

@author: user
'''
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.toolsqa.com/handling-alerts-using-selenium-webdriver/")

driver.maximize_window()
driver.find_element_by_xpath("//button[text()='Simple Alert']").click()

Alert = driver.switch_to_alert()
Alert.accept()

driver.find_element_by_xpath("//button[text()='Prompt Pop up']").click()

conform = driver.switch_to_alert()
conform.send_keys("Yes")
conform.accept()







if __name__ == '__main__':
    pass