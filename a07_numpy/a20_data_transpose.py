'''
Created on 2017. 7. 26.

@author: acorn
'''
"""
## 행렬 변환
T라는 속성으로 기본행과 열이 변환되어 처리됨
eX) ar = 배열..
ar.T    (행과열이 변경된 내용확인.)
2) transpose()


"""

import numpy as np
ar = np.random.uniform(80,100,15).reshape(3,5)
print('ar\n',ar)
print('ar.T\n',ar.T)
print('ar.transpose(0,1)\n',ar.transpose(0,1))
print('ar.transpose(1,0)\n',ar.transpose(1,0))








