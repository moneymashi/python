'''
Created on 2017. 7. 24.

@author: acorn
'''

class Student:
    num = 10
    @classmethod
    def cmethod(cls):
        print('class 메서드')
        print(cls)
        
    @classmethod
    def cadd(cls, x,y):
        return x+y
    
        
    ## static 메서드 선언
    @staticmethod
    def smethod():
        print('static 메서드')
    
    @staticmethod
    def sadd(x,y):
        return  x+y


stu01 = Student()
stu01.cmethod()
stu01.smethod()

print('class x+y = ', stu01.sadd(15,25) )
print('static x+y = ', stu01.cadd(10,20) )








