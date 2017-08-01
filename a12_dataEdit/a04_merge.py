'''
Created on 2017. 8. 1.

@author: acorn
'''
"""
merge()
1. DataFrame 이나 Series.
    1) 첫,두번째의 입력데이터를 합침.
    ex) merge(df1, df2)

2. 하나 이상의 key / id 존재

3. db join연산 유사함.
    key나 on옵션에 명시된 컬럼이름 기준으로 join.

4. on옵션에 컬럼이름 명시. : join기준.
    ex_ on = 'name' : 동일 데이터가 있는 기준컬럼(name)으로 조인.

5. 양쪽 데이터가 다른경우 left_on / right_on 프레임의 컬럼이름 대입.
    db의 outer와 유사.
    컬럼명 다른경우 alias이름 활용.
    
    
    
"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import csv
import sys, pymysql
print("#"*30 , 'concat Review')

stock1 = { '2017-07-28': [84900,818000,1756, 292000],
        '2017-07-31': [86100,872000,1734, 295000],
        'name' : ['다음', '네이버', '넥슨', 'NC'] }
stock2 = { '2017-08-01': [90820,738000,1723, 366500],
        '2017-08-02': [90300,723000,1711, 130252],
        'name' : ['다음', '네이버', '넥슨', 'NC'] }
df1 = DataFrame(stock1, columns = ['2017-07-28','2017-07-31','name' ], index = ['다음', '네이버', '넥슨', 'NC'])
df2 = DataFrame(stock2, columns = ['2017-08-01','2017-08-02','name' ], index = ['다음', '네이버', '넥슨', 'NC'])

print(pd.concat([df1, df2], axis =1).fillna(' - '))

print("#"*30 , 'Merge on name')

print(pd.merge(df1, df2))

