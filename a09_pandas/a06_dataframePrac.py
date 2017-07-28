'''
Created on 2017. 7. 27.

@author: acorn
'''
"""

"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd

items = {
    '1': {'name': 'apple', 'manufacture': 'korea', 'price': 15000},
    '2': {'name': 'waterMelon', 'manufacture': 'korea', 'price': 11000},
    '3': {'name': 'banana', 'manufacture': 'korea', 'price': 1000},
    '4': {'name': 'lemon', 'manufacture': 'brazil', 'price': 13000},
    '5': {'name': 'pineApple', 'manufacture': 'pillipine', 'price': 7000},
    '6': {'name': 'aplesin', 'manufacture': 'sweden', 'price': 9000}
    }
# data =DataFrame(items)
# print(data)
# data01 = data.T
# print(data01)
# print(data01[0:3])
# # print(data01.price> 1000)
# print(data01[data01.price> 1000])

###### PRAC
dataKBO = {
    'id':  [1,2,3,4,5,6,7,8],
    'rank':[1,2,3,4,5,6,7,8],
    'name':['kia', 'NC','Doosan', 'Nexen', 'LG', 'SK', 'Lotte', 'Samsung'],
    'win': [61,54,49,49, 46,49,46,38],
    'lose':[32,37,40,44, 42,46,45,53],
    'draw':[0,1,1,1, 1,1,2,4]
    }

#default data given.
data02 = DataFrame(data= dataKBO)
data02['ratio'] = round(data02['win']/(data02['win']+ data02['lose']+data02['draw']), 2 )
print('##### default data given.\n', data02)

# show rows except row3.
data03 = data02[data02.index != 3]  ##?? 0:2& 3:8
print('##### show rows except row3.\n',data03)

# drop the row of index 5
data04 = data02.drop(5) ## data02.index ==5 이러면 왜 안될까?
print('##### drop the row of index 5\n', data04)

# drop last two of DataFrame
# data05 = data02.drop( len(data02)-1)
# data05 = data05.drop( len(data05)-1)
data05 = data02.drop( [len(data02)-1, len(data02)-2])
print('##### drop last two of DataFrame\n', data05)

# slice only rows 0:4, col = name , ratio
data06 = DataFrame(data = data02, index = range(4), columns = ['name', 'ratio'])
print('##### slice only rows 0:4, col = name , ratio\n',data06)

# slice only the rank 1~3
data061 = data02[ data02['rank'] <=3 ]
print('##### slice only the rank 1~3\n',data061)
# slice rank between 3 and 5
data062 = data02[ (data02['rank'] <=5) & (data02['rank'] >=3) ]
# print('between' in dir(data02['rank']))
data062 = data02[ data02['rank'].between(3,5, inclusive = True) ] ## inclusive default = False 
print('##### slice rank between 3 and 5\n',data062)


# ratio > 53%
data07 = data02[data02.ratio > 0.53]
print('##### ratio > 53%\n',data07)

### upto a08_dataframe Prac done.

