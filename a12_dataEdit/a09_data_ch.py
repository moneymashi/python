'''
Created on 2017. 8. 1.

@author: acorn
'''
"""
replace(매개변수1, 매개변수2)
1. 데이터의 값변경
2. 매개변수1 -> 매개변수2로 대체.
3. list일떄 치환처리
4. dict(K,V) 치환가능

rename()
1. idx, columns이름변경
2. idx = 함수
    columns = 함수
    함수의 결과를 이요해 변경가능. a08_data_ch참고.
3. dict(K,V) : K -> V치환처리가능.

조건처리..
1. DataFrame[컬럼 =데이터값] = 대입데이터..
    해당 컬럼에 데이터값이 있으면 대입데이터로 할당.
2. Series의 데이터 순서 임의변경
    np.random.permutation()


"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import csv
import sys, pymysql


print('#' * 30 ,"")
stock = {
    '2017-08-01': [84900,1756,292000],
    '2017-03-21': [86100, np.nan, 29500]
    }
df = pd.DataFrame(stock, index = ['다음', '넥슨', 'NC'])
# index -> df처리
df = df.rename(index = {'다음':'Daum', '넥슨': 'Nexon', 'NC':'NCsoft'})
print(df.replace({np.nan:'-'}))



