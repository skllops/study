from selenium import webdriver
import time
driver = webdriver.Chrome("chromedriver")

url = "http://www.naver.com"
driver.get(url)

time.sleep(3)

url = "http://www.daum.net"
driver.get(url)

driver.quit()

