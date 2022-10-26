from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.CLASS_NAME, value="_42ft._4jy0._9xo6._4jy3._4jy1.selected._51sy").click()
sleep(2)

driver.find_element(By.ID, value="email").send_keys("randomemail@gmail.com")
sleep(1)
driver.find_element(By.ID, value="pass").send_keys("randompassword")
sleep(1)
driver.find_element(By.XPATH, value="//button[@type='submit']").click()
sleep(1)

driver.close()