from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://techwithtim.net")

search = driver.find_element(by=By.NAME, value="s")

search.send_keys("text")
search.send_keys(Keys.RETURN)

main = driver.find_element(by=By.ID, value="main")
print(main.text)

time.sleep(10)

driver.quit()