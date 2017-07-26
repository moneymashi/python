'''
Created on 2017. 7. 26.

@author: acorn
'''
"""
Fancy indexing
정수배열을 indexer로 사용해 다차원 배열.

1. 기본접근방식..
배열명[[행][열]]
ex) 첫번행과 두번쨰행 선택
배열명::    [[0,1]]
뒤에서 2개:: [[-1,-2]]

행은 0,2,4 선택 & 열 0,2선택
[[0,2,4]] [:,[0,2]] 
== [ np.ix_([0,2,4],[0,2]) ]
"""

import numpy as np
ar = np.arange(20).reshape(5,4)
print(ar)
print('ar[1,2]', ar[1,2])
print('ar[[1,2]]\n', ar[[1,2]])
print('ar[[-1,-2]]\n', ar[[-1,-2]])
print('ar[[1,2]] [:,[0,2]] \n', ar[[1,2]] [:,[0,2]] )
print('#'* 10, 'np.ix_가 가독성이 더 좋다.//' )
print('ar[np.ix_([1,2],[0,2])] \n', ar[np.ix_([1,2],[0,2])] )








