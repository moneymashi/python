'''
파이썬에서  삽입, 삭제, 갱신..
1. 연결 객체인 pymysql.connect()에 있는 cursor() 메서드를 통해
실제 sql(insert into...) 명령으로 처리.
2. execute( sql명령어
3. commit;

try:
    연결 , sql처리, commit()
except:
    예외발생시 rollback;
finally:
    정상처리/ 예외처리후 프린트. con.close();

'''
from pandas import Series, DataFrame
import numpy as np
import pandas as np
import sys, pymysql

try:
    con = pymysql.connect(host = 'localhost', port = 3306, 
                          user = 'root', passwd = '11111', db = 'test', charset = 'utf8')
    print(con)
    cursor = con.cursor()
    cursor.execute('insert into contact(name, phone) values ("paypal", "0112304548")')
    con.commit()
    print('insert completed')
except:
    con.rollback()
    print('rollback worked')
finally:
    con.close()
    print('done works')












