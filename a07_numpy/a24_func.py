'''
Created on 2017. 7. 26.

@author: acorn
'''
"""
abs :: 절대값
sqrt() :: 제곱근
square()  :: 원소의 제곱값
modf():: 정수와 소수점 구분 2개 배열반환
sign() :: 열원소 부호판별함수 1(+), 0(neutral), -1(-)

is.nan(): not a number 포함여부
isfinite() 유한수포함여부
isinf() 무한수 포함여부
logical_not() ::조건 불만족시 T



"""

import numpy as np
b = np.array([10,1,2,3,4])
print(np.logical_not(b<=2))
print(b[np.logical_not(b<=2)])

ar = np.array([1,2,3,4])
br = np.array([5,6,7,8])
print('ar+br', ar+br)
cond = [True, False, False, True]
### np.where(조건, 배열1(T일떄), 배열2(F일떄) )
print(np.where(cond,ar, br))





