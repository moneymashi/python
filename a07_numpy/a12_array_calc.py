'''
Created on 2017. 7. 25.

@author: acorn
'''
# ndarray 산술연
# 1. 배열과 숫자 데이터의 연산은 배열의 ** 각 요소* 에 연산결과를 return함.
#     ex) list01 = np.array([1,2,3])
#     ex) list02 = np.array([3,4,5])
#         list03 = list01 * 2  << 각요소에 2를 곱함.
#         list04 = list02 + 3  << 각요소에 3를 더함.
# 2. 동일크기를 갖는 배열은 ** 동일한 위치의 요소데이터끼리 연산수행

# 3. 비교연산도 동일한 위치의 데이터를 비교
#  boollist = np.equal(list01, list02)
 ## [False,False,False]
 ## np.not_equal(a,b) np.greater(a,b) np.greater_equal(a,b) np.less(a,b) np.less_equal(a,b)
 
 
import numpy as np
list01 = list(range(1,4))
list02 = list(range(4,7))
ar = np.array(list01)
br = np.array(list02)
cr = np.array([[6,7,8],
               [10,20,30]])

# print('ar', ar)
# print('br', br)
# print('cr', cr)
# result = ar*2 # 배열의 모든요소 2곱함
# print('ar*2', result)
# result = ar + br # 배열의 요소한 덧셈 : ** 동일한 위치간 덧셈..
# print('ar + br', result)
# 
# br = np.array([4,2,6])
# # equal 각요소의 데이터 동일한지 여부를 boolean return
# print('equal ', np.equal(ar,br) )


######### Prac

import numpy as np

names = np.array(['a','b','c'])
s01list = [50,80,70]
s02list = [80,80,80]
s03list = [50,80,60]
sub01 =np.array(s01list) #java
sub02 =np.array(s02list) #jscript
sub03 =np.array(s03list) #python
avgs = (sub01+sub02+sub03)/3

# print(avgs)
# isPass = np.greater_equal(avgs, 70)
# sub01Pass = np.greater_equal(sub01, 70)
# sub02Pass = np.greater_equal(sub02, 70)
# sub03Pass = np.greater_equal(sub03, 70)
# print('names \t\t', names)
# print('isPass\t:: ', isPass)
# print('sub01Pass:: ',sub01Pass)
# print('sub02Pass:: ',sub02Pass)
# print('sub03Pass:: ',sub03Pass)




################################## 개인연습

subList = ['oracle','spring', 'jquery']
names = ['aa','bb','cc', 'dd']
stuA = [90, 80, 40]
stuB = [100, 80, 70]
stuC = [60, 70, 30]
stuD = [70,80,90]
print(np.mean(stuA))
 
import math
 
# stuAscore = np.array(stuA)
# stuBscore = np.array(stuB)
# stuCscore = np.array(stuC)
stuScores = [stuA,stuB,stuC, stuD]
 
stuSub = []
for (name, stuS) in zip(names, stuScores) : 
    for sub, int in zip(subList, range(len(stuS)))  :
        stuSub.append((name, sub , stuS[int]))
 
for list in stuSub: 
    print(list) 

############################

a = np.array([10,20,30])
b = np.arange(12)

# print('a', a)
# print('b', b)
# # b배열에 각 열마다 a배열에 같은열 위치의 데이터값 연산.
# #print('a+b', (a+b))
# a = np.array([10,20,30]).reshape(3,1)
# b = np.arange(12).reshape(3,4)
# print('a', a)
# print('b', b)
# print('a+b', (a+b))













