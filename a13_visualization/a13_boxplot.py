'''
Created on 2017. 8. 2.

@author: acorn
'''
"""
boxplot: 평균값을 기준으로 50%의 데이터가 출현하는 범위를 출력하는 차트. outlier표시 등.



"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import sys, pymysql

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name= font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)

df =pd.read_csv('student.csv', encoding ='ms949')
data = [df['국어'],df['영어'],df['수학']]
plt.boxplot(data,  labels = ('국', '영', '수') )
print('min',data[0].min())
print('mean',data[0].mean())
print('median',data[0].median())
print('max',data[0].max())
plt.title('student_ boxplot')
plt.legend()
plt.show()
print('#' * 30 ,"")




