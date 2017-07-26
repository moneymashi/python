'''
Created on 2017. 7. 26.

@author: acorn
'''
"""
abs(x)
all(x)
any(x)
chr(x) :: ASCII -> character
dir(list/dict format) ## 객체가 가지고있는 '변수'나 '함수'를 보여줌.
    ex) dir([{'1':'a'}])  ##['clear', 'copy', 'get', 'has_key', 'items', 'keys',...]
divmod(a,b)  몫, 나머지...
enumerate : 리스트 열거.
    ex) for i, name in enumerate(['a','b','c'])
    ## 0 a \n 1 b \n 2 c ...
eval(expression) : 문자를 받고 연산할수잇음.
filter 조건식 필터링  :: True값만 반환
    print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))
hex(x) :: 정수 -> hex
id(object) :: 객체의 고유주소값. dict 에서 copy는 다른주소. =는 갖은주소를 갖게됨
input('msg') :: 받는건 왜 항상 str뿐일까..
int(x , 진수) ->int로 형변환       ##ex) int('11',2) # 3
str(x)  ->str형변환.
isinstance(object, class) # 인스턴스인지 boolean.
lambda 인수1, 인수2, ... : 인수를 이용한 표현식
    ex) lesser = lambda x: x+2;
    lesser(3) # 5
list()  -> list형변환. ex) list((1,2,3)) #[1,2,3]
map(func, iterable) iterable리스트형태에 각각 함수를 적용해서 return.
min/max() # 참고로 문자형도 ASCII로 최대최소구할수잇음.
open('fileName', 모드)    ##모드: w- 쓰기, r-읽기, a-추가, b-바이너리 
ord(x)   str -> ASCII   # chr의 반대형.
pow(a,b)  ## a**b
range(start, stop, step) start... end-1까지만. step은 단계수.
sorted  # sort후 return
zip() # 동일한 개수로 이루어진 자료형을 묶어줌.
    ex) list(zip([1, 2, 3], [4, 5, 6]))  ##[(1, 4), (2, 5), (3, 6)]

"""

import numpy as np

a = {'0', 13}
b = a
c = a.copy()
# print('id_a: ', id(a))
# print('id_b: ', id(b))
# print('id_c: ', id(c))

lesser = lambda x: x<2
print(lesser(3))

print(list(map(lesser, [1,2,3,4]))) #[True, False, False, False]

list = [5,3,33,5,2]
print(sorted(list))

