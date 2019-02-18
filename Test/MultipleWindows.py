'''
Created on 06-Jan-2019

@author: user
'''
from selenium import webdriver


driver = webdriver.Chrome("C:\\Users\\user\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(150000)
driver.get("http://addmefast.com/login")

driver.maximize_window()
driver.find_element_by_name("email").send_keys("automation.testingtechie@gmail.com")
driver.find_element_by_name("password").send_keys("Anitha@143")
driver.find_element_by_name("login_button").click()
driver.find_element_by_xpath("/html/body/div[3]/div[5]/div/div/div/div[1]/div[1]/div[18]/a").click()

driver.find_element_by_xpath("//*[@id='fbSingle_5246d8b6e7f23d1786ce00161614704']/div/center[2]/a/div").click()

handle = driver.window_handles
for window in handle:
    driver.switch_to_window(window)
    print(driver.title)
    
        
        

    

if __name__ == '__main__':
    pass