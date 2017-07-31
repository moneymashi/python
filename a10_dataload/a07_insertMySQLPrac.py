'''
Created on 2017. 7. 31.

@author: acorn
'''
"""

"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import csv
import sys, pymysql
 

try:
    con = pymysql.connect(host = 'localhost',port = 3306, user = 'root',  passwd ='11111', db = 'test', charset = 'utf8' )
    cursor = con.cursor()
    #cursor.execute("create table dept(empno int primary key auto_increment, name varchar(100), deptno int)")
    cursor.execute("insert into dept (name, deptno) values('kimbley', 30)")
    con.commit()
    print('insert worked')
except:
    con.rollback()
    
    print('rollback worked\n', sys.exc_info())
finally:
    con.close()
    print('work done')












