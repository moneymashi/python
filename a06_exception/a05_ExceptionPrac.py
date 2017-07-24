'''
Created on 2017. 7. 24.

@author: acorn
'''

# 범위숫자 사용자범위 예외처리
# 1~10 숫자처리
# 그외는 예외.

print(  )


class NumException(Exception):
    def __init__(self, num):
        super().__init__(num)
        print('user Exception raised:: ', num)
        
class ValException(ValueError):
    def __init__(self, num):
        super().__init__(num)
        print('user ValueError raised:: ', num)
        
        
try:
    print('print1')
    uin = input('num 1~10  pliz ::')
    if type(int(uin)) != int:
        raise ValException(uin)
    else: 
        if int(uin) in range(1,11):
            print("int(uin):: ",int(uin))
        else: 
            raise NumException(uin)
        
except NumException as nerr:
    print('numeric error:: {} '.format(nerr))
except ValueError as verr:
    print('ValueError error:: {} '.format(verr))
finally:
    print('work done')








