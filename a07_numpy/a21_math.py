'''
Created on 2017. 7. 26.

@author: acorn
'''
"""

"""

import numpy as np

# b = np.arange(1,5)
# print('sum(1:4)', np.sum(b))
# print('mul(1:4)',np.prod(b))
# c = np.arange(1,5).reshape(2,2)
# print('c:\n', c)

## 만약 array가 행렬형식일떄..
# #axis = 0이면 col연산, 1이면 row연산
# print( np.sum(c, axis =0) ) # ## 1+3 2+4 
# print( np.prod(c, axis =1) ) # ## 1*2 3*4

#############Prac

guest = np.array(['aa', 'bb', 'cc'])
price= np.array([[5000,3], [4000,2],[13000,1]])
print(price)
pp = (np.prod(price, axis = 1))
print(pp)
print(np.sum(pp))





