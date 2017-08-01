'''
Created on 2017. 8. 1.

@author: acorn
'''
"""

"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import csv
import sys, pymysql


print('#' * 30 ,"cursor.execute('select date, name, price, count from stock')")

    ## common connection
try:
    con = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = '11111', db = 'test', charset = 'utf8')
    print(con)  # conn test
    cursor = con.cursor()

    ######## create && insert
#     cursor.execute('create table stock( num int primary key auto_increment, date varchar(30), name varchar(20), price int, count int ) ')
#     cursor.execute("insert into stock(date, name, price, count) values ('2017-03-20', '다음', 84900, 500)")
#     cursor.execute("insert into stock(date, name, price, count) values ('2017-03-20', '넥슨', 1756, 300)")
#     cursor.execute("insert into stock(date, name, price, count) values ('2017-03-20', 'NC', 292000, 200)")
#     cursor.execute("insert into stock(date, name, price, count) values ('2017-03-21', '다음', 86100, 450)")
#     cursor.execute("insert into stock(date, name, price, count) values ('2017-03-21', '넥슨', 1787, 220)")
#     cursor.execute("insert into stock(date, name, price, count) values ('2017-03-21', 'NC', 29500, 320)")
#     con.commit()
#     print('insert completed')
    
    
    ####### select
    cursor.execute('select date, name, price, count from stock')
    data = cursor.fetchall()
    sList = []
    for datum in data:
        sList.append(datum)
    sDF = DataFrame(sList, columns  = ['date', 'name', 'price', 'count'])
    print(sDF)
except:
    con.rollback()
    print('rollback worked', sys.exc_info() )
    
finally:
    con.close()
    print('done works')

## pivot이란 중복된 데이터를 기준으로 요약본을 만들어서 보기쉽게 만들어주는 역할.
print('#' * 30 ,"date, name기준으로 pivot설정.")
print(sDF.pivot('date', 'name'))




