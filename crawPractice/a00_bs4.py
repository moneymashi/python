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
    listUL = ['> div > a', '> span > span > a > span']
    while page< max_pages:
        url = 'http://market.cetizen.com/market.php?q=market&auc_sale=1&escrow_motion=3&sc=1&qs=&auc_wireless=&auc_uid=&stype=&akeyword=&just_one=&just_one_name=&just_one_pcat=&view_type=&m%5B1%5D=1&auc_price1=&auc_price2=&keyword_p=&pno=&pw=&p='+ str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BS(plain_text, 'lxml')  ## lxml은 html.parser보다 월등히빠름.
        
#         for li in range(len(listUL)):
#             soupSel01 = soup.select('ul > li ' + listUL[li] )
#             for s01 in soupSel01:
#                 print(s01.text)
        model = []
        title = []
        for liOrder in range(len(listUL)):
            soupSel01 = soup.select('ul > li ' + listUL[liOrder] )
            for (s01,p) in zip(soupSel01, range(len(soupSel01)) ):
#             print(s01.text)
                if p%2 ==0:
                    model.append(s01.text)
                else:
                    title.append(s01.text)
        print(model)
        print(page,' :: ',len(model))
        print(title)
        print(page,' :: ',len(title))
        model = []
        title = []
        
        b = soup.findAll('span', {'class': 'ls-0'})
        price = []
        deliveryFee = []
        seller = []
        for (j,q) in zip(b,range(len(b)) ):
            if q>5:
    #             print(q,' :: ' ,j.text)
                if q%3 ==0:
                    price.append(j.text)
                elif q%3 ==1:
                    deliveryFee.append(j.text)
                else:
                    seller.append(j.text)
        print(price)
        print('len(price):: ', len(price))
        print(deliveryFee)
        print('len(deliveryFee):: ', len(deliveryFee))
        print(seller)
        print('len(seller):: ', len(seller))
        price = []
        deliveryFee = []
        seller = []
        
        page+=1


# def soupEach(soup, which, page):
#     model = []
#     title = []
#     soupSel01 = soup.select('ul > li ' + which )
#     for (s01,p) in zip(soupSel01, range(len(soupSel01)) ):
# #             print(s01.text)
#         if p%2 ==0:
#             model.append(s01.text)
#         else:
#             title.append(s01.text)
#     print(model)
#     print(page,' :: ',len(model))
#     print(title)
#     print(page,' :: ',len(title))
#     model = []
#     title = []






print('#' * 30 ,"")
spider(10)


