'''
Created on 2017. 8. 1.

@author: acorn
'''
"""

"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import sys, pymysql
import pytagcloud
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

print('#' * 30 ,"")
foods = list()
foods.extend(['불고기' for t in range(8)])
foods.extend(['비빔밥' for t in range(7)])
foods.extend(['김치찌개' for t in range(6)])
foods.extend(['돈까스' for t in range(6)])
foods.extend(['순두부백반' for t in range(6)])
foods.extend(['짬뽕' for t in range(5)])
foods.extend(['짜장면' for t in range(9)])
foods.extend(['삼겹살' for t in range(4)])
foods.extend(['초밥' for t in range(1)])
foods.extend(['우동' for t in range(3)])

# 데이터 건수
count= Counter(foods)
print('count', count)
tag2 = count.most_common(100)
taglist = pytagcloud.make_tags(tag2, maxsize = 50)
print(taglist)
pytagcloud.create_tag_image(taglist,'wordscloud.jpg', size = (900,600), 
                            fontname = 'Korean', rectangular = False)

 
## matplotlib.image의 imread('이미지경로/파일명')
img = mpimg.imread('wordscloud.jpg')
## pyplot.imshow(이미지객체)
imgplot = plt.imshow(img)
plt.show()

