'''
Created on 2017. 7. 21.

@author: acorn
'''

class Tiger:
    data = '동물판'
    def cry(self):
        print('호랑이 ...?')
    def eat(self):
        print('당연한듯  동물원에서 취침.')
    
class Lion:
    def cry(self):
        print('사자 ...?')
    def hobby(self):
        print('당연한듯 22시간 취침.1111')

## multi inherit
class Liger01(Tiger, Lion):
    pass

class Liger02(Tiger, Lion):
    def play(self):
        print('라이거 출현!! 기사거리...')
        super().hobby()
        
    def showHobby(self):
        print('self hobby', end = ' ')
        self.hobby()
        print('super hobby', end = ' ')
        super().hobby()
        print(self.data + ', ' + super().data )


l01 = Liger01()
l01.cry()
l01.eat()
l01.hobby()

print('######## multi inh')
l02 = Liger02()
l02.cry() # 우선순위가 먼저인것을 부르고 나머지 cry는 씹는듯...
l02.eat()
l02.hobby()
l02.showHobby()





