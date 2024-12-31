from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
try:
     driver.get("https://www.google.com/")
     nameTextbox = driver.find_element(By.NAME,"q")
     nameTextbox.send_keys("Coursera")
     time.sleep(3)
     nameTextbox.send_keys(Keys.ENTER)
     time.sleep(6)
     print("PASSED")

finally:

    driver.quit()