'''
Created on 2017. 8. 1.

@author: acorn
'''
"""
막대그래프
1. 비교대상이 있을떄, 강조해야하는 경우
2.bar()함수로 출력
3.barh() : 수평막대그래프
4. 너비: width
5. 막대그래프를 2개 출력 width: 0.5이하, x축이동.


"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import sys, pymysql

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name= font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)

print('#' * 30 ,"")
df = pd.read_csv('student.csv', encoding = 'ms949')
print(df)
plt.figure()
plt.bar(df.index, df['국어'], width = 1.0, color = 'r', label = '국어')
plt.bar(df.index, df['영어'], width = 1.0, color = 'g', label = '영어', bottom = df['국어'])
plt.bar(df.index, df['수학'], width = 1.0, color = 'b', label = '수학', bottom = df['국어'] + df['영어'])
plt.xticks(range(0, len(df.index), 1), df['이름'], rotation = 'vertical')
plt.yticks(range(0,300,20))
plt.title('학생별 국영수 점수!')
plt.legend()
plt.show()



