'''
Created on 2017. 7. 27.

@author: acorn
'''
"""
pandas -효과적인 데이터분석을 위한 자료와 tool제공.

1차원 데이터: Series를 통해 효과적으로 처리
2차원 데이터: Dataframe.

Series : 리스트 형태의 구조..
1) 정수 인덱스 + 값
2) values: 데이터값이 return
3) index: 데이터 값에 매핑된 idx
4) 데이터 접근: 변수명[index]

"""

from pandas import Series, DataFrame
import numpy as np

print('##### from pandas packages!!!! #######')
price = Series([4000,3000,3500,2000])
print('Series\n', price)
# price1 = np.array([4000,3000,3500,2000])
# print(price1)
# price2 = list([4000,3000,3500,2000])
# print(price2)
print(price.index)
print(price.values)

good = Series([4000,3000,3500,2000])
good.index = ['apple', 'mellon', 'orange', 'kiwi']
print('good:: \n', good)
print('good[0]:: ',good[0])
print('good["apple"]', good['apple'])

print('#'*30,'PRAC')
############### PRAC

clist = ['010-7777-8888','010-7777-8889','010-7777-8890']
cell = Series(clist)
cell.index = ['hong', 'gill','dong']
print(cell)


evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)









