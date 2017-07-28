'''
Created on 2017. 7. 28.

@author: acorn
'''
"""
데이터 파일만들기
emp.csv 사번 이름 부서번호 급여  - 데이터 5개정도


컬럼명설정
시작row를 두번쨰부터
마지막 2개 데이터 생략.
"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd

emp = pd.read_csv('emp.csv', header =None, names = ['사번', '이름', '급여', '부서번호'])

print('#'* 30,' whole EMP')
print(emp)

print('#'* 30, 'EMP index from 2nd row')
# print(emp[1:])
emp01 = pd.read_csv('emp.csv', header =None, names = ['사번', '이름', '급여', '부서번호'], skiprows = 1)
print(emp01)

print('#'* 30, 'EMP omit last two rows')
# print(emp[0:len(emp)-2])
emp02 = pd.read_csv('emp.csv', header =None, names = ['사번', '이름', '급여', '부서번호'], skip_footer = 2)
print(emp02)




