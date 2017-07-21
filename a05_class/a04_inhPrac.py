'''
Created on 2017. 7. 21.

@author: acorn
'''

# 상속처리
# 
# 탈것Vehicle
# 속성: kind, riderNum
# 생성자 통해서 종류가 할당
# 1) 탑승자수 할당
# 2) def gogo()
# @@@을 @@@명이 타고갑니다
# 
# 
# 상속class Car
# 속성: Speed 
# const: 탑승자수, speed를 할당
#    상위 생성자 호출.
#    def drive()
#     상위 gogo()호출
#     시속 @@@로 달리다

class Vehicle():
    kind = ''
    riderNum = 0
    
    def __init__(self, kind):
        self.kind = kind;
    def setRiderNum(self, riderNum):
        self.riderNum = riderNum;
    def getRiderNum(self):
        return self.riderNum;
    def gogo(self):
        print('{}을 {}명이 타고갑니다'.format(self.kind, self.riderNum) )

class Car():
    speed = 0
    
    def __init__(self, riderNum, speed):
        super().__init__()
        super().setRiderNum(riderNum)
        self.setSpeed(speed)
        print('this speed ', self.speed)
    def setSpeed(self, speed):
        self.speed = speed;
    def drive(self):
        super().gogo()
        print('the speed : {}'.format(self.speed ) )




v01 = Vehicle('Zip')
v01.setRiderNum(4)
v01.gogo()

c01 = Car(200)
c01.drive()