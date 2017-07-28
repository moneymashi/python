'''
Created on 2017. 7. 28.

@author: acorn
'''
"""

"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import csv

li = [50300, 51100, 32000, 4000, 50300,50800,35000,6500,50800, 50700,37000,8000,51800, 50500,37500,8200]
ar = np.array(li)
ar = ar.reshape(4,4)
print(ar)

stocks = DataFrame(ar, index =["다음","네이버","넥슨","NC"], 
                   columns =[["7월","7월","8월","8월"],
                             ["28일","31일","1일","2일"]])
print(stocks)
print('#'*30)
stocks.columns.names = ['월','일']
print(stocks)

print('#'*30)
print(stocks.sum(level = '월', axis = 1)) ## 월별합계
print('#'*30)
print(stocks.sum(level = '일', axis = 1)) ## 월별합계






