'''
Created on 2017. 7. 26.

@author: acorn
'''
"""

"""

import numpy as np
ar =np.array([9,4,3,7.5])
## 데이터 상위 소속데이터, 하위소속된 데이터..
print(ar)
ar.sort()
print(len(ar))
print('크기에서 중간? ', int(0.5*len(ar)))

#idx 범위데이터 접근.. ㅇ배열[시작:마지막]
print('1~2번쨰: ', ar[0:2])
print('1~2번쨰: ', ar[[0,1]])

# 하위 50%
print('하위 50%: ', ar[0:int(len(ar)*0.5)])
print('상위 50%: ', ar[int(len(ar)*-0.5):])




