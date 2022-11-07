from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://bsgroup.eu/contact/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.NAME, value="your-firstname").send_keys("Patryk")
driver.find_element(By.NAME, value="your-lastname").send_keys("Stopczyński")
driver.find_element(By.NAME, value="your-email").send_keys("stopczynskipat@gmail.com")
driver.find_element(By.NAME, value="your-message").send_keys("Hi! I want to join your team !")
driver.find_element(By.NAME, value="accept-this-1").click()

sleep(5)
driver.close()