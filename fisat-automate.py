from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
try:
     driver.get("https://fisat.ac.in/")
     nameTextbox = driver.find_element(By.ID,"menu-item-dropdown-4054")
     nameTextbox.click()
     time.sleep(1)
     nameTextbox = driver.find_element(By.ID,"menu-item-dropdown-4055")
     nameTextbox.click()
     time.sleep(1)
     nameTextbox = driver.find_element(By.ID,"menu-item-dropdown-4057")
     nameTextbox.click()
     time.sleep(6)

     actualTitle = driver.title
     if actualTitle == "UG Programs | FISAT | Federal Institute of Science And Technology":
        print("Passed")
     else:
        print("Failed")

finally:

    driver.quit()