'''
Created on 2017. 7. 25.

@author: acorn
'''

import numpy as np
# 2차 배열 접근방법
# [[1,2],[3,4]]
# [첫번쨰idx, 두번쨰 내부배열idx]
# [0,0] ==> 1
# [1,0] ==> 2

print('='*15,'ex1)')
list01 = np.arange(4)
ar = np.array(list01)
print(list01)
print('ar[0] ', ar[0])
print('ar[-1] ', ar[-1])

print('='*15,'ex2)')
ar2 = np.arange(12).reshape(4,3)
print(ar2)
print('ar2[0][0]', ar2[0][0])
print('ar2[-1][-1]', ar2[-1][-1])
print('ar2[-1][-3]', ar2[-1][-3])
print('ar2[3][0]', ar2[3][0])






