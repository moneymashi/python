'''
Created on 2017. 7. 24.

@author: acorn
'''

class Student:
    def start(self):
        print('안녕하세요')
    def printName(self, name):
        print('이름은 {}'.format(name))
    def call(self):
        self.start()  ##내부 메서드 콜
    def __init__(self,name = 'noname'):  ## 2번 매개값이 없으면 default값 지정.
        self.start()  

#Student.start() 언바운스 호출
st01 = Student()
st01.start() # 바운스 호출
st01.printName('ee')

######## 회부 클래스 호출      :: from 패키지.파일명 import 클래스명







