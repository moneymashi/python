# a03_module(패키지명).a01_callme(파일명)
# mypi = 3.14
# def area(r):
#     return mypi*r*r
# 
# print('local 에서 부르는', area(2))

from a03_module import a01_callme as a


print(a.mypi)
print('import 에서 부르는', a.area(5))




