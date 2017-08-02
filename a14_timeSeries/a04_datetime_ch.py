'''
Created on 2017. 8. 2.

@author: acorn
'''
"""
1. 기본적인 시계열 종류
1) 파이썬 문자열.
2) Series: datetime객체/타임스탬프 index
3) indexing은 Series와 동일
4) 날짜 --> 문자열, 연도나 월까지만도 가능.
5) 슬라이싱은 Series와 동일
6) truncate(): before, after
7) 날짜중복 > 기술통꼐수행 ::groupby대입

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
dates =[datetime(2017,8,2),datetime(2017,8,9),datetime(2017,8,16),
        datetime(2017,8,23),datetime(2017,8,30),datetime(2017,9,6)]
ts = Series(np.random.randn(len(dates)), index = dates)
print('###########Series(np.random.randn(len(dates)), index = dates)\n',ts)

print('#' * 30 ,"데이터 출력")
print('3번쨰 데이터출력 ', ts[ts.index[2] ]) # 0.822094741645 ==np.random.randn(len(dates)
print("문자열로 찾기  ts['2017/8/9']", ts['2017/8/9']) # 0.404042580835
print("문자열로 찾기  ts['20170816']", ts['20170816']) # 0.822094741645

##truncate처리. before/ after
print('truncate 처리::before 0816 \n', ts.truncate(before = '2017-08-16'))

print('truncate 처리::after 0816 \n', ts.truncate(after = '2017-08-16'))






