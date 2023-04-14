from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("chromedriver")
driver.get("https://www.google.com/")

elem = driver.find_element(By.CSS_SELECTOR,"#APjFqb")
elem.send_keys("코로나")            #검색어
elem.send_keys(Keys.RETURN)         #엔터

time.sleep(3)