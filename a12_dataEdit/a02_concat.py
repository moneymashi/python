'''
Created on 2017. 7. 31.

@author: acorn
'''
"""
cf)  a01_concat부분포함.


concat()
    1. 축(x,y)을 이용해서 데이터를 붙이는 함수
        세로로 데이터를 이어주는 경우, 1차 -->2차원( axis=1 )
        axis=1 옵션은 컬럼 단위로 이어 붙이는 DataFrame을 만들어 준다.
    2. join옵션 : 두개의 데이터를 어떻게 연결할 것인가?
        1) inner : 양쪽에 존재하는 인덱스가 동일할 경우만 만들어 준다.
        2) outer : 한쪽에만 있더라도 데이터를 만들어줌.
        3) join_axes : 참여한 인덱스를 직접 설정


1. 초기에 데이터를 컬럼을 매핑처리..
    변수01 ={'컬럼명':[...,....,...]}
2. 결측치(NaN)값에 대한 처리.. 
    .fillna("결측치NaN발생시, 대체할 문자열")
3. 데이터 프레임간 연결    
    pd.concat([프레임1, 프레임2], axis=1)   axis = 1 열(col)붙이기


"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import csv
import sys, pymysql

# 1. 날짜별, = 다음,네이버, 넥슨, NC
stock1 = { '2017-07-28': [84900,818000,1756, 292000],
        '2017-07-31': [86100,872000,1734, 295000] }
stock2 = { '2017-08-01': [90820,738000,1723],
        '2017-08-02': [90300,723000,1711] }

# 2. df 만들기, 상단 cols ='데이터 있는 데이터 매핑' 왼쪽 idx = 각회사명
df1 = pd.DataFrame(stock1, columns = ['2017-07-28','2017-07-31'], index = ['다음', '네이버','넥슨', 'NC'])
df2 = pd.DataFrame(stock2, columns = ['2017-08-01','2017-08-02'], index = ['다음', '네이버','넥슨'])

# 3. concat()을 이용한 데이터 연결 2차원, axis = 1
# 결측치 처리 -> fillna('-')
print('최종결과처리(df+ df)',pd.concat([df1,df2], axis = 1).fillna(' - '))

# 4. join_axis = [지정index] 해당 index로 join처리..
print('최종결과처리(join axes) - df1.index\n', pd.concat([df1, df2], axis = 1, join_axes = [df1.index]).fillna(' - ') )
print('최종결과처리(join axes) - df2.index\n', pd.concat([df1, df2], axis = 1, join_axes = [df2.index]) )



##############PRAC
# 아버지가 이상해
# KBS2
# 32.4%
# 미운 우리 새끼 2부
# SBS
# 15.9%
# 당신은 너무합니다
# MBC
# 14.7%
# 전국노래자랑
# KBS1
# 14.4%

NilsonKorea = {'아버지가 이상해': ['KBS2', 31.0], '미운 우리 새끼 2부': ['SBS', 16.1], '당신은 너무합니다': ['MBC', 15.2], '전국노래자랑':['KBS1', 13.1] }
TNMS = {'아버지가 이상해': ['KBS2', 32.4], '미운 우리 새끼 2부': ['SBS', 15.9], '당신은 너무합니다': ['MBC', 14.7], '전국노래자랑':['KBS1', 14.4] }
NilsonKorea = pd.DataFrame(NilsonKorea, columns = ['아버지가 이상해', '미운 우리 새끼 2부','당신은 너무합니다','전국노래자랑'], index = ['NilsonKorea-방송사', '시청률(%)']).T
TNMS = pd.DataFrame(TNMS, columns = ['아버지가 이상해', '미운 우리 새끼 2부','당신은 너무합니다','전국노래자랑'], index = ['TNMS-방송사', '시청률(%)']).T

print(pd.concat([NilsonKorea,TNMS] , axis = 1).fillna(' - '))




