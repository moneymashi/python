'''
Created on 2017. 7. 24.

@author: acorn
'''
    


### 간단 메서드
result = 0
def adder(num):
    global result  ## 전역변수로 등극.
    result +=num
    return result
# print(adder(3))
# print(adder(4))


## 계산기 클래스
class Calculator:
    def __init__(self):
        self.result = 0
        print('계산기 동작!')
    def adder(self, num):
        self.result += num
        return self.result
    
# c01 = Calculator()
# print(c01.adder(3) )
# print(c01.adder(4) )
# 
# c02 = Calculator()
# print(c02.adder(1) )
# print(c02.adder(3) )


## 서비스클래스_ self에 객체 넣어서도 메서드 활용가능.
class Src:
    secret = 'gggg?'
    def __init__(self, name):
        self.name = name
    def sum(self,a,b):
        result = a+b
        return '%s님 :: %d + %d = %d' %(self.name, a,b,result)
sc01 = Src('hongGilDong')
sc01.secret = 'ssssssss?'
# print(sc01.secret)
# 
# print(Src.sum(sc01, 1,2))
# # == 위아래 결과값이 같음.
# print(sc01.sum(1,2) )


######## 클래스 초기값 설정하기

class HousePark:
    famName = 'Park'
    def __init__(self, name):
        self.fullName = self.famName + name
    def travel(self, where):
        self.where = where
        print('%s님은 %s로 여행하시러 가셨습니다.'%(self.fullName, self.where))

    def __add__(self, other):
        print('%s, %s 결혼!!! '%(self.fullName, other.fullName))
        
    def __sub__(self,other):
        print('%s, %s 졸혼!!!!! '%(self.fullName, other.fullName))
        
# h01 = HousePark('사람')
# h01.travel('Pusan')

######## 클래스  상속

class HouseKim(HousePark): ## class HousePark을 상속받음.
    famName = 'Kim'
    def travel(self, where):
        self.where = where
        print('%s님은 %s로 여행하실 예정입니다.'%(self.fullName, self.where))
    
# 
# jul = HouseKim('Dong')
# jul.travel('PC')


#### 연산자 오버로딩  ::연산자 오버로딩(Overloading)이란 연산자(+, -, *, /,,, )를 객체끼리 사용할 수 있게 하는 기법

pey = HousePark(' er')
jul = HouseKim(' lee')
print(pey+ jul)
print(pey - jul)





















