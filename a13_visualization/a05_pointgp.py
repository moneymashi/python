'''
Created on 2017. 8. 1.

@author: acorn
'''
"""
# 산포도
1. 자료의 분포를 표시,
2. 생성: scatter
3. 색상변화 줄 항목: c
4. colorbar() idx 색상출력

# 차트에 표시해야하는 문자에 한글잇으면?
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname = '글꼴파일이름').get_name()
rc('font', family = font_name)

"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import sys, pymysql  ## mariaDB
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name= font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

df = pd.read_csv('korea.csv', encoding = 'ms949')
print(df)

# 색상분포내용표시
colormap = df.index
plt.figure()
plt.scatter(x = df.index, y = df['점수'], marker = '2', c= colormap)
plt.xticks(range(0,len(df['점수']), 1 ), df['이름'], rotation = 'vertical' )
plt.title('학생별 국어점수 산포도')
plt.show()


