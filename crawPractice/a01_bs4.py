'''
Created on 2017. 8. 9.

@author: acorn
'''
"""
http://creativeworks.tistory.com/entry/PYTHON-3-Tutorials-24-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%9F%AClike-Google-%EB%A7%8C%EB%93%A4%EA%B8%B0-1-How-to-build-a-web-crawler

http://market.cetizen.com/market.php?q=market&auc_sale=1&escrow_motion=3&sc=1&qs=&auc_wireless=&auc_uid=&stype=&akeyword=&just_one=&just_one_name=&just_one_pcat=&view_type=&m%5B1%5D=1&auc_price1=&auc_price2=&keyword_p=&pno=&pw=&p=1




// 문제점:  li > span 이 각 267개나 된다:: 금액, 배송비, 판매자, 날짜(계산) 데이터 추출이 불가능.

20미만 sold 데이터  뽑아내기



"""
import requests
from bs4 import BeautifulSoup as BS

def spider(max_pages):
    page = 1
    listUL = ['> span > s > span > a']
    while page< max_pages+1 :
        url = 'http://market.cetizen.com/market.php?q=market&auc_sale=1&escrow_motion=3&sc=1&qs=&auc_wireless=&auc_uid=&stype=&akeyword=&just_one=&just_one_name=&just_one_pcat=&view_type=&m%5B1%5D=1&auc_price1=&auc_price2=&keyword_p=&pno=&pw=&p='+ str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BS(plain_text, 'lxml')  ## lxml은 html.parser보다 월등히빠름.
        
#         for li in range(len(listUL)):
#             soupSel01 = soup.select('ul > li ' + listUL[li] )
#             for s01 in soupSel01:
#                 print(s01.text)
        sold = []
        price = []
        deliveryFee = []
        seller = []
        p = q =0
        
        for liOrder in range(len(listUL)):
            soupSel01 = soup.select('ul > li ' + listUL[liOrder] )
            print(soupSel01)
            for (s01,p) in zip(soupSel01, range(len(soupSel01)) ):
                sold.append(s01.text)
                print('s01.text',s01.text)
                if s01.text != '':
                    infos = soup.findAll('span', {'class': 'b ls-0'})
                    print('liOrder',liOrder)
                    print('infos',infos)
        print(sold)
        print(page,' :len(sold): ',len(sold))
        

        b = soup.findAll('span', {'class': 'ls-0'})
        
        if len(sold) != 0 :
            for (j,q) in zip(b,range(len(b)) ):
                if q>5:
        #             print(q,' :: ' ,j.text)
                    if q%3 ==0:
                        price.append(j.text)
                    elif q%3 ==1:
                        deliveryFee.append(j.text)
                    else:
                        seller.append(j.text)
#             print(price[p])
#             print(page,' :len(price): ', len(price))
#             print(deliveryFee[p])
#             print(page,' :len(deliveryFee): ', len(deliveryFee))
#             print(seller[p])
#             print(page,' :len(seller): ', len(seller))

        
        sold = []
        price = []
        deliveryFee = []
        seller = []
        
        page+=1



print('#' * 30 ,"")
spider(7)


