'''
Created on 2017. 7. 25.

@author: acorn
'''

import numpy as np

#print(np.random.rand(4,4))

## gabage값을 갖는 10행 5열의 배열생성..
# ar = np.empty((10,5))   ## dummy arr[10][5]
ar = np.zeros((10,5), dtype = int)
# ar = np.arange(50).reshape(10,5)
# print(ar)
for idx1 in range(10):
    for idx2 in range(5):
        ar[idx1][idx2] = idx1+ idx2*2
print('ar', ar)

## 1,3,5,7 행만선택
br = ar[[1,3,5,7]]
print('br', br)

## 선택
cr = ar[[1,3],[2,3]]
print('cr', cr)








