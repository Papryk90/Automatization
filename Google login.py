from telnetlib import EC
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\Webdriver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://google.pl")
driver.maximize_window()
driver.implicitly_wait(10)
#my_cookies = driver.get_cookie()

coockies_button = driver.find_element(by=By.ID, value="L2AGLb")
sleep(3)
coockies_button.click()

login_button = driver.find_element(by=By.CLASS_NAME, value="gb_2.gb_3.gb_9d.gb_9c").click()
sleep(2)

driver.find_element(By.CLASS_NAME, value="whsOnd.zHQkBf").send_keys("patrykstopczynski@gmail.com")
sleep(2)

driver.find_element(By.CLASS_NAME, value="VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.LQeN7.qIypjc.TrZEUc.lw1w4b").click()
sleep(2)

driver.close()