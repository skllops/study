

import requests
from bs4 import BeautifulSoup
import pandas as pd

page_list = []
for i in range(1,4002,10):
    page_list.append(str(i))
print(page_list)



# raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EB%94%A5%EB%9F%AC%EB%8B%9D&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=46&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=page")
# html = BeautifulSoup(raw.text, "html.parser")

# articles = html.select("ul.list_news > li") 
# # 뉴스기사 요소 덩어리를 가져와줘야함. (li)

title_list = []         
#제목 담을 리스트
content_list =[]
#내용 담을 리스트

for page in page_list:
    raw =requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EB%94%A5%EB%9F%AC%EB%8B%9D&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=46&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={page}")
    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("ul.list_news > li") 

    for i in range(len(articles)):
    
        title = articles[i].select_one("a.news_tit").text      
# # #list_news 안에 li들이 여러개가 있는데 그중 처번째 liㄴ안쪽에 a가 여러개가 이는데 news_tit라는 a 호출

        content = articles[i].select_one("div.dsc_wrap").text
#     #뉴스 overview 내용 가져오기
        title_list.append(title)            
#     #제목 불러올때마다 붙이기
        content_list.append(content)
#     #내용 불러올때마다 붙이기


sdict = {'첫번째 컬럼':title_list,              #뉴스제목에 list를 제목의 컬럼에 값으로 넣기
         '두번재 컬럼':content_list}            #뉴스내용에 list를 제목의 컬럼에 값으로 넣기

title_content = pd.DataFrame(sdict)
title_content.to_csv("./naver_news_crawling_result.csv", index=False)


# title_content.to_csv("/result.csv", index=False)



