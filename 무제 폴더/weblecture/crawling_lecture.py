import requests
from bs4 import BeautifulSoup
url="http://kin.naver.com/search/list.nhn?query=파이썬"
response = requests.get(url)


if response.status_code == 200:
    html = response.text
    soup =  BeautifulSoup(html,'html.parser')
    print(soup)

        #select_one 하나의 html d요소를 찾는 함수
    title = soup.select_one('#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(5) > a')

    print(title)
else:
    print(response.status_code)