'''
Created on 2017. 7. 26.

@author: acorn
'''
"""
unique()  중복제거
intersect1d() 교집합
union1d() 합집합
in1d() 데이터 존재여부 boolean
setdiff1d() 차집합
setxor1d() 한쪽만 있는 데이터 집합.

"""

import numpy as np

ar = np.array([9,4,3,7.8,3])
print('중복제거: ', np.unique(ar))
br = np.array([3,4.5,7.6,9])
print('ar',ar)
print('br',br)

print('중복만', np.intersect1d(ar,br)) # intersection
print('합집합', np.union1d(ar,br)) # union
print('데이터 존재여부: ', np.in1d(ar,br)) # in ?
print('차집합: ', np.setdiff1d(ar,br)) # ar - br
print('xor: ', np.setxor1d(ar,br)) # union - intersection









