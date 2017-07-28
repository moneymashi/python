'''
Created on 2017. 7. 28.

@author: acorn
'''
"""

"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd

## chunksize ::로딩할떄 , 한번에 읽어 올 데이터건수.
parser = pd.read_csv('good.csv', header = None, chunksize = 3)  ##chunksize 나누기갯수.
print(parser ,' read_csv// chunksize = 3')

# 반복문을 통해 데이터 가져오기
for piece in parser:
    print(piece.sort_values(by = 0, ascending = True)) # 몇번깨 col을 기준으로 asc/desc할것인지?
    ## 0번째 컬럼으로 내림차순 정렬.
    print('#' * 30)


import csv
items = pd.read_csv('fruit.csv', header =None)
print(items)
## csv 객체를 통한 reaade호라용 -ㅇ파일릭기, delimiter지원
lines = list( csv.reader(open('fruit.csv'), delimiter = '|'))  ##import csv  ,, |는 or단자.
print(lines)

#list 데이터 프레임에 넣기.. column지정.
frame = DataFrame(lines, columns = ['name', 'count', 'price'])
print(frame)








