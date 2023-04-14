import requests
from bs4 import BeautifulSoup
url="http://kin.naver.com/search/list.nhn?query=파이썬"
response = requests.get(url)


if response.status_code == 200:
    html = response.text
    soup =  BeautifulSoup(html,'html.parser')

    #ul 자식태그에는 li태그가 10개?
    #각 li태그 안에는 dl -> dt -> a 태그안에  제목이 들어있다
    #li > dl > dt > a 는 자식 선택자를 이용한 것
    ul = soup.select_one('ul.basic1')
    titles = ul.select('li > dl > dt >a')
    print(titles)
    for title in titles:
        print(title.get_text())

    #     #select_one 하나의 html d요소를 찾는 함수
    # title = soup.select_one('#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(5) > a')

    # print(title)
else:
    print(response.status_code)