'''
Created on 2017. 7. 28.

@author: acorn
'''

'''
csv 파일저장
1.Series , DataFrame 객체. to_csv



'''

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd

items = {'사과':{'count':10, 'price':1500},
        '바나나':{'count':5, 'price':15000},
        '멜론':{'count':7, 'price':100},
        '키위':{'count':20, 'price':500},
        '망고':{'count':20, 'price':1500},
        '오렌지':{'count':4, 'price':700}}
data = DataFrame(items)
data = data.T
print(data)

data.to_csv('z01_fruit.csv', index = False, header = False) # 왼쪽컬럼, 위컬럼명 없어짐.
data.to_csv('z01_fruit.csv') # 그나마 table같은데 읽기 힘들듯?



