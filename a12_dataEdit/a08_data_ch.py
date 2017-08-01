'''
Created on 2017. 8. 1.

@author: acorn
'''
"""
데이터 가공
1. duplicated()
    데이터의 중복을 boolena Series객체로 return
2. drop_duplicates()
    1) 매개변수X: 모든 컬럼의 값이 동일한 경우 제거
    2) 매개변수(컬럼의 리스트): 해당 컬럼의 값이 일치하는데이터 제거, 중복데이터 는 첫번쨰값만.
    3) kepp 옵션last 설정하면 마지막 데이터의 값을 보존함.
3. map()
    함수이름이나 dict을 대입해, 함수를 수행한 결과나 핑되는 dict값 리턴.


"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import csv
import sys, pymysql


print('#' * 30 ,"")

def func(s):
    if len(s)< 5:
        return s
    else:
        return s[0:3]+ '...'

loc = {'한국': 'korea','중국': 'china','일본': 'japan' }
df =DataFrame([['안녕하세요', '니하오', '곤니찌와', '안녕하세요'],['한국', '중국', '일본', '한국']])
df = df.T
print(df)

print('#' * 30 ,"df.drop_duplicates()")
df.columns = ['인사말', '국가']
df = df.drop_duplicates()
print(df)

print('#' * 30 ,"map(dict)적용후")
df['nation'] = df['국가'].map(loc)
print(df)

print('#' * 30 ,"func 적용후")
df['인사말'] = df['인사말'].map(func)
print(df)














