'''
Created on 2017. 7. 27.

@author: acorn
'''
"""
pandas 지원하는 결측값 관련 함수
1. isnull(Series객체) 데이터가 없는 경우 True
2. isnotnull(Series객체) 데이터가 있는경우 True

pandas의 비교데이터 처리(결측치관련)
1. None: 데이터가없음
2. 결측치가 있는 두개의 배열에서 연산처리.
"""

from pandas import Series, DataFrame
import numpy as np
import pandas as pd

glist1 = [500,3500,None, 2000]
good1 = Series(glist1)
glistIdx1 = ['apple', 'mellon', 'orange', 'kiwi']
good1.index = glistIdx1
glist2 = [500,3500,5800, 2000]
good2 = Series(glist2, glistIdx1 )
print(pd.isnull(glist1))
print(pd.isnull(good1))

## np.array처럼 각 해당셀끼리 map으로 연산한다.
print(good1 + good2)
# print(good1.values[pd.isnull(good1)=='True'])






