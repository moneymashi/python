'''
Created on 2017. 7. 21.

@author: acorn
'''

class Father:
    weight = 70
    def play(self):
        print('운동 굳!')
    def sing(self):
        print('노래 굳!')
        

class Mother:
    height = 170;
    def study(self):
        print('공부 잘햇다고 알려짐')
    def sing(self):
        print('노래는 별루라하더라...')

class Son1(Father, Mother):
    def play(self):
        super().play()
        print('공을 잘 잃어버림')
    def both(self):
        super().sing()
        print('???')

class Daughter1(Father,Mother):
    def study(self):
        super().study()
        print('설대 합격!')
    def both(self):
        super().sing()
        print('버터페이스...')

li = [Father, Mother, Son1, Daughter1 ]
for mem in li:
    print('--- who? ', mem)
    if mem == '__main__.Father' or mem == 'Son1':
        mem.play()
    elif mem == 'Father':
        mem.sing()
    elif mem == 'Mother' or mem == 'Daughter1':
        mem.study()
    elif mem == 'Son1' or mem == 'Daughter1' :
        mem.both()
