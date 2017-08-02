'''
Created on 2017. 8. 2.

@author: acorn
'''
"""
pandas 시계열 자료
테이블 형태자료는 index포함.
시계열자료 DatetimeIndex(타임스탭프) 포함

DatetimeIndex
1. 특정순간에 기록된 시계열 자료를위한 인덱스: 단일스탬프
2. 일정간격은 자룔를 조건으로 하지않음
3. 인덱스 생성.
pd.to_datetime() 함수
pd.date_range()

"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import sys, pymysql

## timeseries
from datetime import datetime

date_array = ["2017/8/9","2017/8/16","2017/8/23","2017/8/30","2017/9/6"]
idx = pd.to_datetime(date_array)
print(idx)

# 다음실행시도, 동일한 랜덤내용이 출력.
np.random.seed(0)
s = pd.Series(np.random.randn(5), index = idx)
print('pd.Series(np.random.randn(5), index = idx):: \n', s)



print('#' * 30 ,"")




