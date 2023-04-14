import requests
from bs4 import BeautifulSoup
url = "http://www.naver.com"
result = requests.get(url)

html = result.text

# print(html)

soup = BeautifulSoup(html,"html.parser")

print(soup)