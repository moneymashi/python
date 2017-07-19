import sys
sys.getrefcount(4);

a = b = 'python'
print(a,b)

del a,b
# print(a,b)

a = ['a', 2,3]
b = a
print(a is b) # T

from copy import copy  ## copy method 사용.
b = copy(a)
print(a is b) # F




