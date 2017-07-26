'''
Created on 2017. 7. 26.

@author: acorn
'''
"""
슬라이싱 처리
1. 복제X
2. 복제가 필요할땐 copy()
3. 형태: [시작위치: 마지막위치]
    2차원이상 >> [행, 열]
"""
# 설정바꾸기
# pythonexp오른클릭 -> property -> interpreter/grammar_ Interpreter:: Anaconda로  설정바꿔줄것(??)

import numpy as np
ar = np.array([1,2,3,4,5])
br = ar[0:3]
# print('Slicing br: ', br)
cr = br.copy()
# print('Slicing Copy of br: ', cr)
ar[0] = 10
# print('edited ar ', ar)

br = ar[-2:]
# 배열명[idx:] :: 해당 idx이후 마지막까지 내용처리.
# print('idx -2(마지막에서 2번째)부터 ', br)
br = ar[1:len(ar):2]
# print('ar ', ar)
# print('2번째 element부터 2단꼐씩. ', br)







