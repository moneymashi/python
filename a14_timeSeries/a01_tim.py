'''
Created on 2017. 8. 2.

@author: acorn
'''
"""
시계열 데이터.

금융, 경제, 생태학, 신경과학, 물리학등.. 여러분야에서 사용되는 구조화된 데이터.
시간상의 여러지점을 관측하거나 측정할수 있는 모든것.
고정빈도로 표현, 시간마다.. 특정 규칙에따라 일괄적인 간격


주요 데이터 형태
1. 시간내에서 특정 순간의 타임스탬프
2. 2007년 1월 ~ 2010년 전체에 고정된 기간.
3. 시간의 시작과 끝.

lib -- datetime.datetime - 날짜와 시간정보
1) today()/now() : 현재시간/날짜
2) year/month/day
3) 
4) date: 날짜정보// 그레고리언 달력을 사용날짜(년-월-일)
time : 시간, 분, 초, ms 단위
datetime(YYYY,mm,dd): 날짜/시간
timedelta: 두개의 datetime의 시가느이 차이. (일, 초, ms)

strptime(date_string, format): 문자열 -> datetime.
strftime(format): datetime -> 문자열 
fromtimestamp(timestamp) : timestamp -> datetime
fromordinal(ordinal) : 누적된날짜 ->datetime
Combine(date, time): date+ time -> datetime
weekday() : 0월~ 6일   // isoweekday(): 1월~7일

Date(): datetime -> date
Time(): datetime -> time

%Y(4자리), %y(2자리), %m, %d, %H(24H), %I(12H), %M, %S



"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import sys, pymysql

import time as t
from datetime import datetime, timedelta


print('#' * 30 ,"")
# t.sleep(2) # 10초 경과후 작동.
print(t.time())  ## 1970/01/01부터 누적된시간. -> 변환필요
print(t.gmtime()) # UTC
print(t.localtime()) #현지시간.


print('#' * 30 ,"")
now = datetime.now()
print('now', now)
print(now.year,'-',now.month,'-',now.day, sep = '')

print('#' * 30 ,"")
start = datetime(2017,8,1)
# 해당에서 + timedelta(날짜수)
print('start-timedelta(12)', start-timedelta(12))
delta = now -datetime(2016,8,1)
print('delta', delta)

print('#' * 30 ,"")
#날자 문자열 형식처리
print(str(now))
#now 의 format처리 ==> strftime
print(now.strftime('%Y/%m/%d')) 

print('#' * 30 ,"")


