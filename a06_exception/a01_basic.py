'''
Created on 2017. 7. 24.

@author: acorn
'''

def func(y):
    x = input('numeric pliz :: ')
    return int(x)**y

#print(func(3))
## 예외를 강제적으로 문자열을 입력함으로 발생.

try: 
    print(func(4))
except: ## 예외 발생시, 처리블록.
    print('예외 발생!!')
else:  ## 정상처리시.
    print('정상처리됨.')   










