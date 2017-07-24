'''
Created on 2017. 7. 24.

@author: acorn
'''

class MyException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

try:
    print('print1')
    print('print2')
    raise MyException('user Exception raised')
except MyException as myErr:
    print('except catched ::  {} '.format(myErr))










