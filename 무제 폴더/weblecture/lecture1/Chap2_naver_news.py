import requests
from bs4 import BeautifulSoup

raw = requests.get("https://search.naver.com/search.naver?where=news&query=딥러닝")
html = BeautifulSoup(raw.text, "html.parser")



articles = html.select("ul.list_news > li") # 뉴스기사 요소 덩어리를 가져와줘야함. (li)

title = articles[0].select_one("a.news_tit").text
source = articles[0].select_one("div.dsc_wrap").select("a")[0].text 
# ※ class이름을 띄어쓰기로 해놓아서 Fake 거는 경우가 있다. 선택자에는 띄어쓰기가 자식 요소로 판별됨

print(title)
print(source)

