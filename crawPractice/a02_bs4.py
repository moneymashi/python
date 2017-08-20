'''
Created on 2017. 8. 9.

@author: acorn
'''
"""
http://creativeworks.tistory.com/entry/PYTHON-3-Tutorials-24-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%9F%AClike-Google-%EB%A7%8C%EB%93%A4%EA%B8%B0-1-How-to-build-a-web-crawler

http://market.cetizen.com/market.php?q=market&auc_sale=1&escrow_motion=3&sc=1&qs=&auc_wireless=&auc_uid=&stype=&akeyword=&just_one=&just_one_name=&just_one_pcat=&view_type=&m%5B1%5D=1&auc_price1=&auc_price2=&keyword_p=&pno=&pw=&p=1


######
거의완성본@@ 
Aug21, 2017
02:27.
JB

"""
import requests
import numpy as np
from bs4 import BeautifulSoup as BS

def spider(startPage, endPage):
    page = startPage
    while page< endPage+1 :
        print('#' * 30 ,"   page ::", page)
        url = 'http://market.cetizen.com/market.php?q=market&auc_sale=1&escrow_motion=3&sc=1&qs=&auc_wireless=&auc_uid=&stype=&akeyword=&just_one=&just_one_name=&just_one_pcat=&view_type=&m%5B1%5D=1&auc_price1=&auc_price2=&keyword_p=&pno=&pw=&p='+ str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BS(plain_text, 'lxml')  ## lxml은 html.parser보다 월등히빠름.
        
        soldTitles = []
        titles = []
        models = []
        soldLists = []
        prices = []
        deliverFees = []
        sellerNames = []
        sellDates = []
        soupSel01 = soup.select('ul' )  ## 이거 .map function 해도 먹힐거같다?
        
        for uls in soupSel01:
            # find sold items
            sTitles = uls.findAll('span', {'class': 'clr02  pointer'})
            for soldTitle in sTitles:
                soldTitles.append(soldTitle.text)
            # All listed titles
            allTitles = uls.findAll('span', {'style': 'overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block;'})
            for allTitle in allTitles:
                titles.append(allTitle.text) 
            # All listed prices
#             allPrices = uls.findAll('span', {'class': 'b ls-0'})
#             for allPrice in allPrices:
#                 prices.append(allPrice.text)
#             # All Three infos in the last.
#             ## TODO:: filter out last three and last four // 만료/선택/확정/상중하  << analyze
#             allThrees = uls.findAll('span', {'class': 'p11'})
#             for idx in range(3):
#                 for allThree in allThrees:
#                     if idx%3 ==0:
#                         deliverFees.append(allThree.text)
#                     elif idx%3 ==1:
#                         sellerNames.append(allThree.text)
#                     else:
#                         sellDates.append(allThree.text)
            sellInfos = uls.findAll('span', {'class': 'ls-0'})
            for (sellInfo,q) in zip(sellInfos,range(len(sellInfos)) ):
                print(q,' :: ' ,sellInfo.text)
#                 prices = sellInfo[0::4]
#                 deliverFees = sellInfo[1::4]
#                 sellerNames = sellInfo[2::4]
#                 sellDates = sellInfo[3::4]

        if len(soldTitles) != 0:
            soldLists = [titles.index(x) for x in soldTitles] # index number(0 ~) in the list.
            ## TODO:: 한 페이지에 같은 제목 복수개인경우 첫번째 값을 가져온다. 모두 찾기 방법 모색.
        
        soupSel02 = soup.select('ul > li > div > a > span' )  ## 이거 .map function 해도 먹힐거같다?
        for allModel in soupSel02:
            models.append(allModel.text)
            
        print('models :: ',models)    
        print('len(models) :: ', len(models))    
        print('titles :: ',titles)    
        print('len(titles) :: ', len(titles))    
        print('prices :: ',prices)    
        print('len(prices) :: ', len(prices))    
        print('deliverFees :: ',deliverFees)    
        print('len(deliverFees) :: ', len(deliverFees))    
        print('sellerNames :: ',sellerNames)    
        print('len(sellerNames) :: ', len(sellerNames))    
        print('sellDates :: ',sellDates)    
        print('len(sellDates) :: ', len(sellDates))    
        if len(soldTitles) != 0:
            print('soldList :: ',soldLists )    
            print('soldTitle :: ',soldTitles)    
            print('len(soldTitle) :: ', len(soldTitles))
        soldTitles = []
        titles = []
        models = []
        soldLists = []
        prices = []
        deliverFees = []
        sellerNames = []
        sellDates = []
        
        
        
        page+=1



spider(10, 15) ## page start, end.


