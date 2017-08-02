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

df= pd.read_csv('student.csv', encoding = 'ms949')
# print(df)
plt.figure()
plt.barh(df.index, df['국어'], color = 'r', label = '국어')
## 영어점수도 나타나게하는데. 국어랑 반대방향으로 표시.
plt.barh(df.index, -df['영어'], color = 'g', label = '영어')
plt.title('학생별 국영 barh그래프')

# 해당내용에 이름처리
plt.yticks(range(0, len(df.index)), df['이름'])
# 해당내용에 x처리 :: 실제구간, 보여질 구간정의.
plt.xticks([-100,-50,0,50,100],(100,50,0,50,100))
#범례처리
plt.legend()
plt.show()



print('#' * 30 ,"")




