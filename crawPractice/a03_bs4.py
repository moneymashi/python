'''
Created on 2017. 8. 9.

@author: acorn
'''
"""

http://market.cetizen.com/market.php?q=market&auc_sale=1&escrow_motion=3&sc=1&qs=&auc_wireless=&auc_uid=&stype=&akeyword=&just_one=&just_one_name=&just_one_pcat=&view_type=&m%5B1%5D=1&auc_price1=&auc_price2=&keyword_p=&pno=&pw=&p=1

@@@@@ 참고
@ 웹 크롤링
http://creativeworks.tistory.com/entry/PYTHON-3-Tutorials-24-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%9F%AClike-Google-%EB%A7%8C%EB%93%A4%EA%B8%B0-1-How-to-build-a-web-crawler
@ DataFrame -> mariaDB 방법.
http://creativeworks.tistory.com/entry/how-to-insert-dataframe-data-into-mysql-database-using-pymysqlpure-python3-library
@ DB배우기.
http://blog.naver.com/PostView.nhn?blogId=hmkuak&logNo=220583392375

######
Aug21, 2017
11:10 in work
JB

Work Done
------- Aug 21, 2017
2. 마지막4개. 분석하는 변수중 하나로 쓸만할듯.        
3. df form.
4. put in mariaDB.


 ## TODO:: 
-------- Aug 22, 2017
00. 가독성증가용 :: 함수/ 클래스화. 제발 ㅜㅜ
1. auc_no따오고 판매자 정보(가입일자 : 2016.05, 6개월간 판매 732 건   (거래완료 598 건   판매취소 1 건   구매취소 72 건   반품 61 건)), 판매자평가, 
2. last4 options>> 설명나누기.
3. 슬슬 데이터 -> matplot사용해서 그래프그리기.
4. word clouding
5. All listed prices 더 좋은방법 모색. <<< if, elif가 필요없다.

??. soldTitles의 경우, 한 페이지에 같은 제목 복수개중 첫번째 값만 가져온다. 모두 찾기 방법 모색.


"""
import requests
import pandas as pd
from pandas import DataFrame, Series
from bs4 import BeautifulSoup as BS
import mysql.connector
from sqlalchemy import create_engine
import pymysql, sys
from datetime import datetime

def spider(startPage, endPage):
    page = startPage
    soldTitles = []
    titles = []
    models = []
    soldLists = []
    prices = []
    deliverFees = []
    sellerNames = []
    sellTimes = []
    options = []
    while page< endPage+1 :
        print('#' * 30 )
        print('#' * 30 ,"   page ::", page)
        print('#' * 30 )
        
        # Web Scrap
        url = 'http://market.cetizen.com/market.php?q=market&auc_sale=1&escrow_motion=3&sc=1&qs=&auc_wireless=&auc_uid=&stype=&akeyword=&just_one=&just_one_name=&just_one_pcat=&view_type=&m%5B1%5D=1&auc_price1=&auc_price2=&keyword_p=&pno=&pw=&p='+ str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BS(plain_text, 'lxml')  ## lxml은 html.parser보다 월등히빠름.
        
        ## 리스트 초기할당
        
        
        
#         soupSel01 = soup.select('ul')  
#         for uls in soupSel01:
#             # find sold items
#             sTitles = uls.findAll('span', {'class': 'clr02', 'style': 'overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block;'})
#             for soldTitle in sTitles:
#                 soldTitles.append(soldTitle.text)
        
        
        # 리스트의 기본 container.
        soupSel01 = soup.select('li')
        test = []
        aucId = []
        phoneId = []
        phoneName = []
        for lis in soupSel01:
            s01 = lis.findAll('div', {'style': 'overflow:hidden;cursor:hand;cursor:pointer;margin-top:2px;margin-left:5px;'})
            for s02 in s01:
                s02 = s02['onmouseover'].strip('OnUserMenuShow(').strip(');').replace("'","") 
                test.append(s02)
        print(test)
        for (te,p) in zip(test, range(len(test))):
            aucId.append(te.split(',')[0]) 
            phoneId.append(te.split(',')[1]) 
            phoneName.append(te.split(',')[2]) 
        print(aucId)
        print(phoneId)
        print(phoneName)
        print(len(aucId))
        print(len(phoneId))
        print(len(phoneName))
        
          




        
        
        
        page+=1
    ### while loop END
        
        
    df = DataFrame(data = {'models':models,
                    'titles': titles,
                    'prices': prices,
                    'deliverFees': deliverFees,
                    'sellerNames': sellerNames,
                    'sellTimes': sellTimes,
                    'options': options })
    # 페이지 넓게 보여줌.
    pd.set_option('expand_frame_repr', False)
#     print(df)
    
    print('#' * 30 ,"  df.describe()  ::")
#     print(df.describe())   
        
        
#     dfToMaria(df)


def dfToMaria(df):
    ###Anaconda prompt:: pip install mysql-connector
    ###Anaconda prompt:: pip install mysql-connector-python-rf
    
    try:
        con = pymysql.connect(host = 'localhost', port = 3306, 
                              user = 'root', passwd = '11111', 
                              db = 'crawl', charset = 'utf8')
        engine = create_engine('mysql+mysqlconnector://root:11111@localhost:3306/crawl', echo=False)
        df.to_sql(name='sample_table3', con=engine, if_exists = 'append', index=False)
        
        con.commit()
        print('-'*30, ' insert df in Maria :: Well done')
    
    except:
        print('-'*30, ' insert df in Maria :: went Wrong ::\n', sys.exc_info())
        
        con.rollback()
    finally:
        print('='*30, ' insert df in Maria :: finally')
        con.close()



s1 = datetime.now()
spider(1, 5) ## page start, end.
s2 = datetime.now()
print('$'*50, 'time elapsed :: ', s2-s1)

