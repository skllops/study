import requests
from bs4 import BeautifulSoup

# openpyxl은 파이썬에서 엑셀을 다루는 것을 쉽게 해주는 도구
from openpyxl import Workbook

# 네이버 파이낸셜 사이트
url = 'https://finance.naver.com/'

# url 요청
response = requests.get(url)

# 해당 url의 정보 모두 텍스트 형태로 가져옴
html = response.text 

# HTML의 요소별로 파싱시켜줌
soup = BeautifulSoup(html, 'html.parser')

# 인기검색종목의 테이블 안의 요소를 가져옴
# #container > div.aside > div > div.aside_area.aside_popular > table > tbody
tbody = soup.select_one('#container > div.aside > div > div.aside_area.aside_popular > table > tbody')

# print(tbody)

price_list = tbody.select("td")

slist = tbody.select("a")

count = 0

for i in range(0,len(price_list),2):
    temp = slist[count]

    print ("종목이름:", temp.text, "종목코드:",  str(temp)[str(temp).find("code=")+5:  (str(temp).find("code=")+5 ) +6] , "현재가:", price_list[i].text, "전일대비:", price_list[i+1].text)

   
    # temp = price_list[count]

    # print(    str(temp)[str(temp).find("code=")+5:  (str(temp).find("code=")+5 ) +6] )     #종목코드 위 치 가져오기 [] 인덱스로 만들기?
    
    #print(i.text)
    count +=1

# for i in slist:
#     print(    str(i)[str(i).find("code=")+5:  (str(i).find("code=")+5 ) +6] )     #종목코드 위 치 가져오기 [] 인덱스로 만들기?
#     print(i.text)