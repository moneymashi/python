'''
Created on 2017. 7. 25.

@author: acorn
'''
####a02_arr01

import numpy as np
nparr =np.array(np.arange(12)).reshape(4,3)
dict = {}
dict['nparr'] = nparr
# print(dict['nparr'])  # 뻘짓

ar = np.arange(12).reshape(3,4)
print(ar)
print(type(ar))
print(ar.shape)
print(ar[0] ,'\n', ar[0][0],'\n',ar[1],'\n',ar[2])


######### a04_arr02내용

### 덧셈의 미학.
list01 = [1,2,3]
list02 = [1,2,3]
list03 = list01+ list02
print('list03 ', list03)

set01 = (1,2,3)
set02 = (1,2,3)
set03 = set01 + set02
print('set03 ', set03)


nparr01 = np.array(list01)
nparr02 = np.array(list02)
nparr03 = nparr01+ nparr02
print('nparr03 = ', nparr03)

#### 본수업

# linspace(시작값, 마지막값, return갯수, endpoint = False) : 마지막값포함/불포함
ar = np.linspace(0,1,6) # default endpoint = True
print(ar)
# linspace(시작값, 마지막값, return갯수, endpoint = False) : 마지막값포함/불포함
ar = np.linspace(0,1,6, endpoint = False)
print(ar)

## 매트릭스형태만들기
ar = np.arange(1,13).reshape(3,4)
print('reshape ar:: ', '\n',ar)





