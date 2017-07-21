'''
Created on 2017. 7. 21.

@author: acorn
'''

from abc import *
class AbstractClass(metaclass = ABCMeta): ## 추상클래스
    ## 추상메서드 선언...
    @abstractclassmethod
    
    def absMethod(self):
        pass
    def normalMethod(self):
        print('추상클래스 내에 일반 메서드')

### b d= AbstactClass() 추상클래스 단독 객체생성할수 없다.
class Chil1(AbstractClass):
    def absMethod(self):
        print('추상메서드를 오버라이딩함.')


c1 = Chil1()
c1.absMethod()
c1.normalMethod()

print('##' * 25)
class Friend(metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name
    def hobbu(self):
        pass
    def printName(self):
        print('name' + self.name)
class Tom(Friend):
    def __init__(self, name, addr):
        Friend.__init__(self,name)
        self.addr = addr
    def hobby(self):
        print(self.addr + '거리를 걸어다녀')
    def printAddr(self):
        print('주소;;;' + self.addr)
class James(Friend):
    def __init__(self, name, addr):
        Friend.__init__(self,name)
        self.addr = addr
    def hobby(self):
        print(self.addr + '거리를 뛰어다녀')
    def printAddr(self):
        print('배송지;;;' + self.addr)

tom = Tom('톰', '강남')
tom.printName()
tom.printAddr()
tom.hobby()








