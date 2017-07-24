'''
Created on 2017. 7. 24.

@author: acorn
'''

class Person:
    def __init__(self, sec = 'secret!'):
        print('person caller')
        self.__sec =sec
        print('접근 제어 private 변수:: ', self.__sec , '(객체할당 확인용.)')
        
        ## 클래스 ㅁ내부에서 사용될 member변수 필요할떄
        ## __member :: 변수명

##        
    def setPosition(self, sec):
        self.__sec = sec
    def getPosition(self):
        return self.__sec
    ## position이라는 이름으로 실제는 set, get을 통해 
    ## 받아들일수잇다.
    position = property(getPosition, setPosition)      
        
p01 = Person()
# print('Name1: ', p01.name)
p01.age = 25;
print('age1: ', p01.age)

p02 = Person('비밀요원01')
# print('Name2: ', p02.name)
## 해당변수는 접근 불가..
## print('신분: ', p02.__sec)        

## 정상 접근방법: p01.getPosition()
print('getPosition: ',  p01.getPosition() )
print('getPosition: ',  p02.getPosition() )

print('position property - set,get::', p01.position)
print('position property - set,get::', p02.position)









