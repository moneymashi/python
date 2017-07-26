'''
Created on 2017. 7. 26.

@author: acorn
'''
"""
연습예제
영화
가격
영화
가격
...


>> output:::
영화       가격
@@@   @@@
@@@   @@@
...
=========
합계 : @@@

"""

import numpy as np

file = open('movie.txt', 'w', encoding = 'utf-8')
mList = ['아이언맨', "5000", '식스맨', "7000", '관상', "6000"]
file.write('\n'.join(mList))
file.close()

file = open('movie.txt', 'r', encoding = 'utf-8')
content = file.readlines()
title = []
price = []
for i in range(len(content)):
    if i%2 ==0:
        title.append(content[i].rstrip()) 
    elif i%2 ==1:
        price.append(content[i].rstrip())
    else : print('error') 

print(title)
print(price)
    

print('영화이름 \t 가격')
print('='*20)
for j in range(len(title)):
    print(title[j],'\t',price[j], end= '\t')
    print()

file.close()




