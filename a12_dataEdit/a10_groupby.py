'''
Created on 2017. 8. 1.

@author: acorn
'''
"""
Groupby
1. DataFrame 이나 Series에서 데이터를 그루핑
2. groupby(키) : 컬럼단위로 묶기.
3. groupby: 메서드  ==> 새로운 instance생성.
4. DataFrameGroupBy: 객체의 SeriesGroupBy함수...
    1) count: na제외 개수.
    2) min, max
    3) sum
    4) mean
    5) median
    6) var, std: 분산, 표준편차
    7) prod: 누적곱셈
    8) first, last: 첫,마지막값
    9) describe:요약.

apply(함수명)
내부함스 사용자정의 함수 모든 원소에 계산처.

"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import csv
import sys, pymysql


print('#' * 30 ,"")
df = DataFrame({
    'key1': ['a','a','b','b','a'], 
    'key2': ['one','two','one','two','one'],
    'data1': np.random.randn(5), 
    'data2': np.random.randn(5) 
    })
print(df)
print('#' * 30 ,"groupby(지정 열 데이터 )")
grp = df['data1'].groupby(df['key1'])
## 그룹만 처리후, 실제 그룹에 해당하는 함수가 적용X
print(grp)
## mean()
print('#' * 30 ,".groupby(df['key1']).mean")
print(grp.mean())

print('#' * 30 ,"df['data1'].groupby([df['key1'], df['key2']]).mean()")
means = df['data1'].groupby([df['key1'], df['key2']]).mean()
print(means)

print('#' * 30 ,"임의 df생성 후 2행 b,c열에 nan주입.")
ppl = DataFrame(np.random.randn(5,5), columns = ['a','b','c','d','e'], index = ['joe', 'wes', 'Stev', 'Travis', 'jhonny'])
ppl.ix[2:3, ['b','c']] = np.nan
print(ppl)

# dit로 그룹설정
print('#' * 30 ,"dict설정, groupby(사용자함수)")
mapping = {'a': 'red', 'b':'red', 'c': 'blue', 'd':'blue', 'e': 'red', 'f': 'orange'}
by_column = ppl.groupby(mapping, axis = 1)
print(by_column.sum() )



## 각 데이터별 건수확인
## 1. mapping한 dict --> Series로 변환
## 2. df.groupby(변경된 mapping).count()
print('#' * 30 ,".groupby(map_series).count()")
map_series = Series(mapping)
print(map_series)
print(ppl.groupby(map_series, axis = 1).count())


# 함수로 묶기.
## 이름의 길이 //len()
print(ppl.groupby(len).sum())












