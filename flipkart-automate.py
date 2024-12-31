from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
try:
    driver.get("https://www.flipkart.com/")
    a = driver.find_element(By.NAME,"q")
    a.send_keys("Bluetooth Speakers")
    time.sleep(2)
    a.send_keys(Keys.ENTER)
    time.sleep(3)
    print("Passed")

finally:
    driver.quit()
