'''
Created on 2017. 7. 28.

@author: acorn
'''
"""
pandas.read_csv("파일",옵션1="", 옵션2="".....)
1. sep : 구분자 설정.. ex) sep="," sep="@"....
2. header : 컬럼이름..행 번호로 기본은 0이면, 없을 때 None

5.skiprows: 파일의 시작부터 읽지않을 row수
6.na_values: NA갑으로 처리할 값들 나열
7.comment: 주석처리로 파싱하지않을 문자들
8.converters: 변호나시 컬럼에 적용할 함수
9.nrows: 파일의 첫일부만.
10 skip_footer: 무시할 파일의 마지막줄수
11.encoding
12. squeeze: row하나. Series객체 반환
13. thousand: 숫자를 천단위로 끊을때.


"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd

items = pd.read_csv('good.csv', header = None, thousands =',', names = ['제품명', '갯수', '가격'])
print(items)
#######
print('#'*30)












