'''
Created on 2017. 7. 26.

@author: acorn
'''
"""
split
배열을 여러개의 크기로 나눠주는 함수
기준에따라 axis의 속성으로 x,y축에 0,1값 할당.
"""

import numpy as np
ar =np.arange(1,17).reshape(4,4)
print(ar)
print(np.split(ar,2, axis=0))
print(np.split(ar,2, axis=1))

#### 2번쨰 앞까지 나누고 3번쨰 앞까지 나누고 나머지..
ss = np.split(ar, [1,3], axis =1)
print('ss[0]::\n',ss[0],'\nss[1]::\n',ss[1],'\nss[2]::\n',ss[2])







