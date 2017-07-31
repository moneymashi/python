'''
Created on 2017. 7. 28.

@author: acorn
'''
"""
CSV 파일 읽기.
1. pd.read_csv('경로/파일이름'), pd.read_table('경로/파일이름') ## df객체 생성하고 리턴.
2. read_csv :: 기본구분자','
    read_table 기본구분자 table탭 사용.
3. 컬럼명은 default로 첫번쨰 행 데이터

CSV 파일 옵션.
pandas.read_csv("파일",옵션1="", 옵션2="".....)
 1. sep: 구분자 설정 ex) sep="," sep="|"....
 2. header: 컬럼이름
 3. index_col = 위치 / 이름   :: index이름을 대체할수잇음.. ex) index_col = 0 , index_col = 'ID'
 4. names: 컬럼이름으로 사용할 번호나 이름 또는 리스트
 5. skiprows: 읽지 않을 행의 숫자
 6. na_values: NA갑으로 처리할 값들 나열    :: ex) na_values = ['null']
 7. comment: 주석으로 분류되어 파싱하지 않을 문자
 8. converters: 변환 시 컬럼에 적용할 함수 지정
 9. norws: 파일의 일부분만 읽어올 때
 10. skip_footer: 무시할 마지막 줄 수
 12. squeeze: 로우가 하나뿐. Series 객체 반환
 13. thousands: 숫자를 천단위로 끊을 때
"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd

items = pd.read_csv('good.csv', header = None, thousands =',', names = ['제품명', '갯수', '가격'], na_values = 0)
print(items)
#######
print('#'*30)

