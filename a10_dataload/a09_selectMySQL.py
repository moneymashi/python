'''
Created on 2017. 7. 31.

@author: acorn
'''
"""
파이선에서 데이터 검색
1. 연결객체의 cursor()메서드 호출, sql실행 객체를 가져옴
2. cursor.execute()
3. cursor객체를 가지고, fetchone(): 첫번쨰 데이터/ fetchall():전체데이터//
메서드 호출하면, 듀플(K,V)로 return됨.

4. list형태로 전환
    1) list 선언.
    2) 각 데이터를 append()
        for item in data:
            list.append(item)
5. DataFrame으로 전환.
    3) list를 첫번쨰 parameter할당
        DataFrame(list)
    4) columns = [컬럼명1, 2, 3...]
        DataFrame(list, columns = ['번호', '이름'....] )


"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import csv
import sys, pymysql

con = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = '11111', db = 'test', charset ='utf8')
try:
    cursor = con.cursor()
    cursor.execute('select * from good') ## 만약 utf8 charset이없을땐 한글대신 ?? 가뜬다.
#     data = cursor.fetchone() # 듀플로 한개만 가져옴
    data = cursor.fetchall() # 듀플로 모두 가져옴
    lists = []
    for item in data:
        print(item)
        lists.append(item)
    print('########')
    print('##### convert from tuples to DataFrames')
    lists = DataFrame(lists, columns = ['id', 'name', 'su', 'dan'])
    print(type(lists))
    print(lists)
    print('#####select done')
except:
    print('exception occured\n', sys.exc_info())
    con.rollback()
    print('#####rollback done')
finally:
    con.close()
    pass






