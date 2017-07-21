'''
Created on 2017. 7. 21.

@author: acorn
'''

class Parent:
    def printData(self):
        pass
class Child1(Parent):
    def printData(self):## method override
        print('child1 called')
class Child2(Parent):
    def printData(self):## method override
        print('child2 called')
        print('부모와 다른내용 override.라고합니다.')
c1 = Child1()
c1.printData()

c2 = Child2()
c2.printData()

print('####polymorphism 처리')
par = Parent()
par = c1 ## polymorphism 다형성처리
par.printData()
par = c2
par.printData()

print('#### 클래스 배열처리')
plist = [c1, c2]
for p in plist:
    p.printData()


