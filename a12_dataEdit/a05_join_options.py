'''
Created on 2017. 8. 1.

@author: acorn
'''
"""
cont'

6. merge() 옵션: how를 통해 outer join.
1) right: 오른 우선
2) left: 왼쪽우선
3) outer: 완전 외부.

2.suffixes
듀플로 컬럼이름을 2개 대입하면 양쪽에 동일한 이름의 컬럼이 존재하는경우
컬럼이름 뒤에 튜플의 값을 추가해 주는데, 기본값 _x, _y

3. index로 조인
left_index,right_index에 T/F (default = T)

4. sort
key 기준으로 정렬.
    
"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import csv
import sys, pymysql


stock1 = { 'name' : ['다음', 'KT', '넥슨'] ,
        '2017-07-28': [84900,1756, 292000],
        '2017-07-31': [86100,1734, 295000]
        }
stock2 = { 'name' : ['다음', '네이버', 'NC'],
        '2017-08-01': [90820,738000,1723 ],
        '2017-08-02': [90300,723000,1711 ]
        }
df1 = DataFrame(stock1, columns = ['2017-07-28','2017-07-31','name' ])
df2 = DataFrame(stock2, columns = ['2017-08-01','2017-08-02','name' ])

result = df1.merge(df2, on = 'name')
print('#' * 30 ,'df1.merge(df2, on = "name")')
print(result)

result = df1.merge(df2, on = 'name', how = 'outer').fillna(' - ')
print('#' * 30 ,"df1.merge(df2, on = 'name', how = 'outer')")
print(result)

df1.index = df1['name']
df3= df1.drop('name', axis = 1)
df2.index = df2['name']
df4 = df2.drop('name', axis = 1)
result1 = pd.concat([df3, df4], axis=1).fillna('-')
print('#' * 30 ,".concat([df1, df2], join = 'outer'")  ## index asc자동 정렬됨.
print(result1)


print('#' * 30 ,"df.index = result['name'] && df.drop('name', axis = 1)")
result.index = result['name']
print(result.drop('name', axis = 1))

