'''
Created on 2017. 7. 24.

@author: acorn
'''

#모듈이란 함수나 변수 또는 클래스 들을 모아 놓은 파일

import mod1
# print(mod1.sum(3,4))


# print(mod1.safe_sum(4,5))
# print(mod1.safe_sum(4,'5')) # None은 return 에 의해서 주어짐.


from mod1 import * # mod1의 모든 메서드를 사용하고플때.
# print(safe_sum(3,4))


from mod2 import *
a = Math()
# print(a.solv(2))


import sys
sys.path.append('c:/Python/Mymodules')
print(sys.path)



