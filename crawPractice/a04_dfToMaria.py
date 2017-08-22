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
12:48 workDone upto debug #2

JB

 ## TODO:: 
4. put in mariaDB.
   


"""
import requests
import numpy as np
from pandas import DataFrame, Series
from bs4 import BeautifulSoup as BS
from datetime import datetime
list1 = ['a','b','c','d','e']
list2 = np.arange(5)
np.random.seed(seed = 100)
list3 = np.random.randint(1,10,5)

df = DataFrame(data = {
    'list1': list1,
    'list2': list2,
    'list3': list3
    
    })
print(df)
print(df.describe())


import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

import pymysql, sys
###Anaconda prompt:: pip install mysql-connector
###Anaconda prompt:: pip install mysql-connector-python-rf

try:
    con = pymysql.connect(host = 'localhost', port = 3306, 
                          user = 'root', passwd = '11111', 
                          db = 'crawl', charset = 'utf8')
    cursor = con.cursor()
#     cursor.execute('create table tester( list1, list2, list3 )')
    
    
    engine = create_engine('mysql+mysqlconnector://root:11111@localhost:3306/crawl', echo=False)
    df.to_sql(name='sample_table2', con=engine, if_exists = 'append', index=False)
    
    con.commit()
    print('Well done')

except:
    print('went Wrong ::', sys.exc_info())
    
    con.rollback()
finally:
    print('final')
    con.close()









