'''
Created on 2017. 8. 2.

@author: acorn
'''
"""

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
import datetime as t
import time
dt = t.datetime.now()
print('dt.date(), dt.time()::', dt.date(), dt.time())

d =t.date(2017,9,5) ## day
# print('datetime.date(2017,9,5)::', d)
t01 = t.time(18,30,1) ## time
print(t01)
print('datetime.combine(d,t01):: ',datetime.combine(d,t01))

dt1 = t.datetime.combine(d,t01)
dt2 = t.datetime(2017,9,7,19,30,5)
td = dt2 - dt1
print('dt2 - dt1::', td)
print('td.days, td.seconds, td.microseconds::',td.days, td.seconds, td.microseconds)

print('#' * 30 ,"")

## time.sleep expriment!
print('start')
print(t.datetime.now())
time.sleep(4)
print(t.datetime.now())
print('the end')

print('#' * 30 ,"")

from dateutil.parser import parse
print(parse('2017-08-02') )  ## parse():: 문자열 -> datetime.datetime형변환.
print(type(parse('2017-08-02')) )





