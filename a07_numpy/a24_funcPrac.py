'''
Created on 2017. 7. 26.

@author: acorn
'''
"""
리스트에서 확정점수 비교해서 높은처리
np.where로 최정점수 list

"""

import numpy as np

ar = np.array([[7,8,9,6],[9,7,7,8]])
s1 = ar[0]
s2 = ar[1]
print(s1)
print(s2)
ckp = s1>=s2
print(ckp)
lp = np.where(ckp, s1, s2)
print(lp)






