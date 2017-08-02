'''
Created on 2017. 8. 2.

@author: acorn
'''
"""
PIE
1. 전체적으로 데이터 비율/기여도 확인.
2. plt.pie()
3. thrtjd:
1) labels : 데이터 레이블 출력
2) colors : 각 데이터별 색상
3) explode : 조각분할.
4) autopct : 백분율 표시




"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import sys, pymysql

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name= font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family = font_name)

df= pd.read_csv('student.csv', encoding = 'ms949')
# print(df)
plt.figure()
explode1 = np.arange(0,0.5,0.5/len(df.index))
plt.pie(df['국어']+df['영어']+df['수학'], labels = df['이름'], 
        explode = explode1, autopct = '%1.1f%%')
plt.title('학생 기여도')
plt.legend(loc =4)
plt.show()
print('#' * 30 ,"")




