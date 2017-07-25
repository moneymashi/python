'''
Created on 2017. 7. 25.

@author: acorn
'''
from numpy import *

ar  = arange(5,21)
ar.astype(string_)
print('ar.dtype:: ', ar.dtype)
print('ar:: ',ar)
# ar = np.array([3.2,'4'], dtype = np.int32)
ar = array(ar, dtype = int32)
print('숫자형', ar)
sum = 0
for data in ar:
    sum+= data
print(sum)

import numpy as np

list03 =['1','2','3','4','5']
st = np.array(list03)
print(st)












