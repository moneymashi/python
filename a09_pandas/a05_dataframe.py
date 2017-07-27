'''
Created on 2017. 7. 27.

@author: acorn
'''
"""

"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd

dataKBO = {
    'id':  [1,2,3,4],
    'rank':[1,2,3,4],
    'name':['kia', 'NC','Doosan', 'Nexen'],
    'win': [61,54,49,49],
    'lose':[32,37,40,44],
    'draw':[0,1,1,1]
    }

data01 = DataFrame(data= dataKBO)
print(data01)
data01['ratio'] = round(data01['win']/(data01['win']+ data01['lose']+data01['draw']), 2 )
data02 = data01['ratio'] > 1.5
print(data01['name'][data02.values ==True])
# print(dir(data01['ratio']))
print(data01.T)
print(data01.reindex([2,3,0,1]) )
# reindex 과정에서 생긴 결측값 채우기
print('ffill?? limit??: \n',data01.reindex([2,3,0,1], fill_value = 0) )
print(list(data01.ix[0]) ) # 길게 보기싫어서 list형변환.



##########
data03 = data01.T
data03= data03.drop('rank') ## .drop('rank')작업은 .T작업이 선행필수다.
print(data03)



