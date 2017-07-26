'''
Created on 2017. 7. 26.

@author: acorn
'''
"""
concatenate :: 이항함수  - 배열2개 가지고 작업.
여러개의 배열을 한개로 합침
2차 이상인 경우, x축, y축으로 합치는 경우 2가지
axis = 0 : y축
axis = 1 : x축

"""

import numpy as np
ar = np.array([[7,8,9,6],[9,7,7,8]])
arr1 = ar[0]
arr2 = ar[1]
print('np.concatenate( (arr1, arr2)) \n', np.concatenate( (arr1, arr2)) )

print('in case of Matrix :: two 2 X 2')
ar = np.array([[1,2],[3,4]])
br = np.array([[5,6],[2,1]])
print('axis = 0 \n',np.concatenate((ar,br), axis = 0))
print('axis = 1 \n',np.concatenate((ar,br), axis = 1))




