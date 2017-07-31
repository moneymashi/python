'''
Created on 2017. 7. 31.

@author: acorn
'''

"""
HTML데이터 가져오기. apis를 쓰면 보이긴하니깐..
1. tag형식을 트리형식으로 변환
    lxml.html.parse( io.StringIO(문자열) )
2. 핵심 데이터의 root객체 가져오기.. : 트리객체.getRoot()
3. 태그에 해당하는 데이터를 Element의 list로 가져오기.
    루트객체.finall(".//태그명")
    ex) tables[0].finall('.//th') 타이틀..
    ex) tables[0].finall('.//td') 테이블셀..

4. 데이터 찾기..
    루트객체.find('from') : 루트객체 태그 하위에 from과 일차하는 첫번쨰 데이터 return, 없다면 None
    특정한 데이터를 첫번째 데이터를 찾고싶다.. ==? 루트객체.findtext('from')
    ==>  첫번쨰 텍스트의 값을 return
5. 속성찾기..
    Elements의 get('속성'): 속성값 가져오기 <td class = "##" >
6. 태그의 내용 가져오기..
    Elements의 text_content()

http://finance.daum.net/quote/kospi_yyyymmdd.daum

"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import csv
import sys, pymysql
import requests
from lxml.html import parse ## 태그형식 계층으로 변환
from io import StringIO

## 사용 주소
url = 'http://finance.daum.net/quote/kospi_yyyymmdd.daum'
## 응답받을 response객체만들기
data = requests.get(url)
## tag를 계층형으로 변견처리.
doc = parse(StringIO(data.text))
## 최상의 root()를받기...
root = doc.getroot()
## 핵심 데이터가 table안에 잇어서 ...
cols = []
vals = []

tables = root.findall('.//table') ## 테이블접근
titles = tables[0].findall('.//th')  ##컬럼접근
for title in titles:
    print(title.text_content())
    cols.append(title.text_content())
    
contents = tables[0].findall('.//td') ## 테이블셀접근
for val in contents:
    if val.text_content() != '':
        print(val.text_content())
        vals.append(val.text_content())
print(cols)
print(vals)  ## 이상없음.

####
# 나열된 데이터를 9개 단위변경
# 1) np.array()처리  ##### 중요!!!!
# 2) .reshape()처리.

ar= np.array(vals).reshape(10,9)
print(ar)
vals = DataFrame(ar, columns = cols, index = ['데이터1',2,3,4,5,6,7,8,9,10])
print(vals)


############ Prac
# localhost:6380/auction/main.do에서 데이터를 가져와봐라.





