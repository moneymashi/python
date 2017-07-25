'''
Created on 2017. 7. 25.

@author: acorn
'''

# 데이터 해당차원에 0이나 1로 채워 넣은 함수.
# ones(크기)  ::해당 크기의 배열에 1로 데이터를 채움.

import numpy as np
b1 = np.ones(10)
print(b1)
# 자매품 zeros
# shape = (5,2)는 reshape와 같은 형식. 생략가능. 괄호는 반드시 잇어야함.
b1 = np.zeros( (5,2) )
print(b1)

# eye(행렬갯수, dtype = 데이터 형식 int, float, str...)
## eye 라는건 행렬의 I(identity)를 말함.
ar = np.eye(5, dtype = str)
print(ar)
# k = 올릴행수, 값들의 '행'을 k만큼 올림. 올려진 행들은 0처리.
ar = np.eye(5, k = 2, dtype = int)
print(ar)
ar = np.eye(5, k = -1,  dtype = int)
print(ar)


# diag(배열) :: 대각선값만 빼내오기, 마찬가지로 k는 행올림처리. 
ar = np.arange(25).reshape((5,5))
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]
print(ar)
br = np.diag(ar) #[ 0  6 12 18 24]
print(br)
br = np.diag(ar, k=2)  #[ 2  8 14]
print(br)
br = np.diag(ar, k=-1) #[ 5 11 17 23]
print(br)
















