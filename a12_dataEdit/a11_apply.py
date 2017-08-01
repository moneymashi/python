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


print('#' * 30 ,"")
s = Series(np.random.randn(6))
print(s)

print('#' * 30 ,"")
s[::2] = np.nan  ## [::2]는 %2 ==0을 의미한다.
print(s)

print('#' * 30 ,"")
## 누락된값을 평균값으로 대처하고, 데이터처리.
s = s.fillna(s.mean())
print(s.mean())
print(s)


print('#' * 30 ,"")
states = ['OH', 'NY', 'VM', 'FL', 'OR','NV', 'CA', 'ID']
group_key = ['East']*4 +['West']*4
## 데이터를 임의로 만들되, index를 주, 도시이름으로.
data = Series(np.random.randn(8), index = states)
print(data)
# 특정 주를 결측치 처리.
data[['VM', 'FL', 'ID']] = np.nan
print(data.groupby(group_key).mean())
# print(data)

print('#' * 30 ,"")
# 람다함수 선언후, apply에 적용.
fill_mean = lambda g:g.fillna(g.mean())
print(data.groupby(group_key).mean())
print(data.groupby(group_key).apply(fill_mean))


