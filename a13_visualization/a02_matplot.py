'''
Created on 2017. 8. 1.

@author: acorn
'''
"""
산포도 그래프
1. 자료의 분포를 표시할때,
2. 생성: scatter
3. 색상변화 줄 항목: c
4. colorbar() 인덱스에 해당하는 색상출력

# 차트에 표시해야하는 문자에 한글잇을떈
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname = '글꼴파일이름').get_name()
rc('font', family = font_name)
"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import sys, pymysql


print('#' * 30 ,"")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import font_manager, rc
font_name= font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


## matplotlib.image의 imread('이미지경로/파일명')
img = mpimg.imread('wordscloud.jpg')
## pyplot.imshow(이미지객체)
imgplot = plt.imshow(img)
plt.show()





