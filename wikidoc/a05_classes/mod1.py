'''
Created on 2017. 7. 24.

@author: acorn
'''

def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print('뭐가지고 더하려는거냐...')
        return
    else:
        result = sum(a,b)
        return result









