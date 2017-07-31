'''
Created on 2017. 7. 28.

@author: acorn
'''

'''
csv 파일저장
df.to_csv(  ~~)  ## df데이터는 DataFrame형태여야 수월.
1.Series , DataFrame 객체. to_csv
2.sep : 구분자 설정.
3. na_rep: Nan값을 원하는 형식으로 replace
4. index, header값을 false 대입해서 idx,col출력 안되게.
5. cols  필요한 컬럼이름지정.


'''

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd

items = {'사과':{'count':10, 'price':1500},
        '바나나':{'count':5, 'price':15000},
        '멜론':{'count':7, 'price':100},
        '키위':{'count':20, 'price':500},
        '망고':{'count':20, 'price':1500},
        '오렌지':{'count':4, 'price':700}}
data = DataFrame(items)
data = data.T
print(data)

data.to_csv('z01_fruit.csv', index = False, header = False) # 왼쪽컬럼, 위컬럼명 없어짐.
data.to_csv('z01_fruit.csv') # 그나마 table같은데 읽기 힘들듯?



