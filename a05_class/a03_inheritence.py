'''
Created on 2017. 7. 21.

@author: acorn
'''

class Person:
    say = 'sup :) '
    age = 25;
    def __init__(self, age):
        print('=' * 10)
        print('const caller')
        self.age = age;
        print('new const age: ', self.age)
    def printInfo(self):
        print('나이 : {}, 말하기:: {}'.format(self.age, self.say))
    def sayGB(self):
        print('Byebi! ')
    
    
class Employee(Person): 
    say = 'employee'   
    subject = '근로자'
    
    
    def __init__(self):
        print('=' * 10)
        print('Emp const')
        
    def ePrintInfo(self):
        self.printInfo()
        print(self.say, self.subject)
        self.sayGB()
    
class Worker(Person):
    def __init__(self, age):
        print('=' * 10)
        print('worker const')
        super.__init__(age)
    def wPrintInfo(self):
        self.printInfo()
    
        
p = Person(28)
print(Person.say)
print(p.sayGB())

e = Employee()
print(e.say, e.age)
e.ePrintInfo()

w = Worker(29)
print(w.wPrintInfo())







