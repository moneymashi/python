'''
Created on 2017. 8. 9.

@author: acorn
'''
"""
http://creativeworks.tistory.com/entry/PYTHON-3-Tutorials-24-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%9F%AClike-Google-%EB%A7%8C%EB%93%A4%EA%B8%B0-1-How-to-build-a-web-crawler

http://market.cetizen.com/market.php?q=market&auc_sale=1&escrow_motion=3&sc=1&qs=&auc_wireless=&auc_uid=&stype=&akeyword=&just_one=&just_one_name=&just_one_pcat=&view_type=&m%5B1%5D=1&auc_price1=&auc_price2=&keyword_p=&pno=&pw=&p=1




// 문제점:  li > span 이 각 267개나 된다:: 금액, 배송비, 판매자, 날짜(계산) 데이터 추출이 불가능.




"""
import requests
from bs4 import BeautifulSoup as BS

def spider(max_pages):
    page = 1
    listUL = ['> span > s > span > a',   ##sold title
              '> div > a > span ',   ## model num
              '> span > span > a > span'] ## title
    ## sold out + title = 20
    
    while page< max_pages+1 :
        print('#' * 30 ,'   page ::' , page)
        url = 'http://market.cetizen.com/market.php?q=market&auc_sale=1&escrow_motion=3&sc=1&qs=&auc_wireless=&auc_uid=&stype=&akeyword=&just_one=&just_one_name=&just_one_pcat=&view_type=&m%5B1%5D=1&auc_price1=&auc_price2=&keyword_p=&pno=&pw=&p='+ str(page)
        plain_text = requests.get(url).text
        soup = BS(plain_text, 'lxml')  ## lxml은 html.parser보다 월등히빠름.
        
#         for li in range(len(listUL)):
#             soupSel01 = soup.select('ul > li ' + listUL[li] )
#             for s01 in soupSel01:
#                 print(s01.text)
        soldTitle = []
        model = []
        title = []
        for liOrder in range(len(listUL)):
            soupSel01 = soup.select('ul > li ' + listUL[liOrder] )  ## 이거 .map function 해도 먹힐거같다?
            for s01 in soupSel01:
                if liOrder%3 ==0:
                    soldTitle.append(s01.text)
                elif liOrder%3 ==1:
                    model.append(s01.text)
                else:
                    title.append(s01.text)
        print(soldTitle)
        print(page,' :len(sold): ',len(soldTitle))
        print(model)
        print(page,' :len(model): ',len(model))
        print(title)
        print(page,' :len(title): ',len(title))
        sold = []
        model = []
        title = []

        page+=1



spider(5)


