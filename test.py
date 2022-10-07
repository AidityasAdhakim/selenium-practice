from multiprocessing.sharedctypes import Value
from this import d
from typing import final
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://techwithtim.net")

search = driver.find_element(by=By.NAME, value="s")

search.send_keys("text")
search.send_keys(Keys.RETURN)
date_list =[]
try:
    for i in range(5):    
        main = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.ID, "main")))
        articles = main.find_elements(by=By.TAG_NAME,value="article")

        for article in articles:
            date = article.find_element(by=By.CLASS_NAME, value="entry-meta")
            header = date.find_element(by=By.TAG_NAME,value="a")
            date_list.append(header.text)
        
        page_div = main.find_element(by=By.CLASS_NAME, value="paging-navigation")
        page_button = page_div.find_element(by=By.CLASS_NAME, value="next")
        page_button.click()
    
    print(date_list[0])
    print(date_list[-1])

finally:
    driver.quit()
