
class Car:
    handle = 1
    speed = 0
    kind = 'kind'
    airBag = 0
    speed = 0
    
    
    
    # 생성자 초기화
    def __init__(self, airBag, kind):
        self.airBag = airBag;
        self.kind = kind
    """def __init__(self):
        print('초기생성자');
        self.kind = 'Graduer'
        print(self.kind)
    """    
    def setSpeed(self, speed):
        self.speed = speed
    def getSpeed(self):
        return self.speed
    
    #소멸자 : del을 하게될때 소멸하기 직전에 프린트후에 자원해제한다.
    def __del__(self):
        print('lease the resources')
    
    
    
car01 = Car(True,'Gradeur')
print(car01.kind)
car01.setSpeed(5)
print('The speed : ', car01.getSpeed())

del car01


