'''
Created on 2017. 7. 25.

@author: acorn
'''

import numpy as np
# np.random.normal():: 데이터 1개를 랜덤생성.
print(int(np.random.normal()))

# np.random.normal():: 데이터 size= 데이터건수.
print(np.random.normal(100))

# 매트릭스도 생성가능 size =(행,렬)
print(np.random.normal(size = (2,3) ))

# 시드를 설정해주면 한번 랜덤설정후 고정값 된다.
np.random.seed(seed = 100)
print((np.random.normal(5)))
print((np.random.normal(5)))













