'''
Created on 2017. 7. 26.

@author: acorn
'''
"""

"""

# file = open('mod1.txt', 'r', encoding= 'utf-8') #FileNotFoundError
a = [1,2,3]
# print(a[4]) #IndexError

'''
try:
    ...
except [발생 오류[as 오류 메시지 변수]]:
    ...
'''
try:
    k = 4/0
    a = [1,2,3]
    print(a[4])
except (ZeroDivisionError, IndexError) as e:
    #print(e)
    pass  ## 오류를 회피한다고해서 else에 결과값을 보여주지않음.
else:
    a = int(k)
    print(a)
finally:
    print('exception done')


#################

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass
    def fly(self):
        print('FAST!!!')
eagle = Eagle()
eagle.fly()  # NotImplementedError  >> 왜? Eagle에서 Bird의 fly를 재정의 안해줘서.

#################

class UserError(Exception):
    def __init__(self):
        self.msg = 'userMsg raised'
        print(self.msg)
#     pass
    def __str__(self):
        return 'not allowed string'

def say_nick(nick):
    if nick =='babo':
        raise UserError()
    else :
        print(nick)
    print(nick)

try:
    say_nick('babo')
    say_nick('booo')
except UserError as ue:
    print(ue)




