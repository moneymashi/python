'''
Created on 2017. 7. 27.

@author: acorn
'''
"""
객체를 파일로 저장할떄,
PROS
1) 파일에 특정 데이터를 로딩하지않고도, 객체단위로 바로 활용,.

파이선에 객체를 파일로 저장할떄, 사용되는 모듈.
1) 피클링 모듈, DBM관련모듈
2) [피클링 모듈]은 임의의 파이선 객체를 저장하는 가장 일반화된 모듈

피클링을 통한 저장처리..
1) pickle.dump(출력할 객체, 파일객체)

피클링을 통해 읽어오기..
1) pickle.load(파일객체) : 객체를 1개씩 읽기
2) pickle.loads(파일객체) : 객체전체를 바이트단위로 읽기.

"""

import numpy as np
class Dto:
    def setNum(self , num):
        self.num = num
    def setName(self, name):
        self.name = name
    def getNum(self, num):
        return self.num
    def getName(self, name):
        return self.name
    def toString(self):
        return '{번호: ' +str(self.num) + ', 이름: '+ self.name + '}'
        
data01 = Dto();
data01.setNum(7777)
data01.setName('himan')
data02 = Dto();
data02.setNum(1234)
data02.setName('chicken')
# print(data01.toString())
# print(data02.toString())
li = []
li.append(data01)
li.append(data02)
# print(li)

import pickle
# 반복을 통해 여러객체를 한파일에 할당할떄
# with opne('fileName') as 파일객체명
#     pickle.dum(리스트데이터, 파일객체명)
with open('z04_test.txt', 'wb') as f:
    pickle.dump(li,f)

with open('z04_test.txt', 'rb') as f:
    result = pickle.load(f)  ## 로딩처리.
    for temp in result:
        print(temp.toString())  ## 반복문을 통해 해당객체 메서드

#######PRAC
class Person:
    def __init__(self):
        pass
    
    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def toPrint(self):
        return '{이름: ' +str(self.name) + ', 나이: '+ self.age + '}'
    
p1 = Person()
p1.setName('hong')
p1.setAge(29)
p2 = Person()
p2.setName('gill')
p2.setAge(27)

pList = []

file = open('z05_test.txt', 'wb')
with file:
    pickle.dump(pList, file)

file2 =open('z05_test.txt', 'rb')
with file2:
    result = pickle.load(file2)
    for temp in result:
        print(temp.toPrint())
