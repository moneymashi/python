'''
Created on 2017. 8. 2.

@author: acorn
'''
"""
1. 누락된 데이터를 삽입/삭제
-resample()
2. date_range
1) 범위지정: start: , end:
2) freq 빈도수지정.
B: business day
MS: 월의 시작 month start
M: 월의 마지막날짜
M,T,S: 매시간, 분, 초
BM, BMS: 일을하는 월의 마지막과 시작날짜
W-Mon: 요일
Wom-1Mon: 월의 첫번째 월요일 - 응용.


"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import sys, pymysql

## visualization
#import matplotlib.pyplot as plt
#from matplotlib import font_manager, rc
#font_name= font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
#rc('font', family = font_name)

## timeseries
from datetime import datetime

#날짜범위지정: date_range()
print(pd.date_range('2017-8-1', '2017-8-31'))

# 시작에서 날짜수 지정
print(pd.date_range(start = '2017-8-1', periods = 10))



print('#' * 30 ,"")




