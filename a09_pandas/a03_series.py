'''
Created on 2017. 7. 27.

@author: acorn
'''
"""

"""

from pandas import Series, DataFrame
import numpy as np
import pandas as pd

good = Series([4000,3000,3500,2000])
index = ['apple', 'mellon', 'orange', 'kiwi']
good2 = good[good >3000]
print(good2)

good3 = good + 100
print(good3)
buyall =np.sum(good)
print('sum ::', buyall)

#### Series만들기
# 1. keys 데이터 배열형식
# 2. values 데이터 배열형식
# 3. dic형태로 설정.. dic(zip(K, V))
# 4. Series에 할당. Series(dic)
keys = ['중식','한식','일식','간식']
values = [5000, 6000, 8000, 4000]
dic = dict(zip(keys, values))
print('dic', dic)
foods= Series(dic)
print(foods)





