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

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name= font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)

print('#' * 30 ,"plt.bar(range(0,len(data),1), data) ")
df = pd.read_csv('lovefruits.csv', encoding = 'ms949')
data = df['선호과일'].value_counts(sort=False)
print(data.index)
plt.bar(range(0,len(data),1), data)  ## 핵심 hist그래프.
plt.xticks(range(0,len(data), 1), data.index)
plt.title('과일선호')
plt.show()


print('#' * 30 ,"plt.hist(data, bins=10, label = ('국', '영', '수'))")

############################### a11_hist_student
df = pd.read_csv('student.csv', encoding = 'ms949')
# data = pd.concat([df['국어'],df['영어'],df['수학']])
# plt.xticks(range(0,100,40),['하','중','상'])   ## 0~40, 40~80, 80~100
data = (df['국어'],df['영어'],df['수학'])
plt.hist(data, bins=10, label = ('국', '영', '수'))  ##bins의 역할이 뭘까???
plt.title('점수별 구간')
plt.legend()
plt.show()


print('#' * 30 ,"plt.hist(data, stacked = True, label = ('국', '영', '수'))")
############################### a12_histAdv
df = pd.read_csv('student.csv', encoding = 'ms949')
data = [df['국어'],df['영어'],df['수학']]
plt.hist(data, stacked = True, label = ('국', '영', '수') )
plt.title('점수빈도 stacked = T')
plt.legend()
plt.show()






