'''
Created on 2017. 7. 31.

@author: acorn
'''
"""
JSON
1. 속성-값 쌍으로 이루어진 데이터 객체 전달을 위한 개방형 표준형태
eX) {'name':'홍길동', 'age':25}
2. 인터넷에서 자룔를 주고받을떄, 표현방법중 하나
3. jscript 구문형식의 언어 독립형 데이터포맷
4. 언어나 플랫폼os독립적이고, 쉽게이용.
5. 파이선에선 json.loads('json형식 문자열의 파일 또는 url')
 ->파싱된 결과 return
6. 표현방법
    배열: [], 객체{속성1:값1, ... } 배열+ 객체: [{속성1:값1},{속성1:값1}]




"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import csv
import sys, pymysql

# 1.json패키지
import json
import requests

# 2.url로 get방식호출.
url = 'https://apis.daum.net/local/v1/search/keyword.json?apikey=465b06fae32febacbc59502598dd7685&code=AT4&location=37.6510085,127.02983770000003&radius=3000&query=%EC%88%98%EC%84%A0'
data = requests.get(url)

# 3. json으로 데이터파일 loading
result = json.loads(data.text)
# print(result)

# 4. 결과에 대한 최상위값 가져옴
channel = result['channel']

# 5. 핵심 데이터key값 가져오기
item = channel['item']
print('channel["item"]', item)

# 6. 데이터 프레임에 처리.
# DataFrame(핵심데이터, columns = [컬럼명지정])
df = DataFrame(item, columns = ['title', 'phone', 'address'])
print(df)




