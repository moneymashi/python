'''
Created on 2017. 7. 31.

@author: acorn
'''
"""
1. 파일로 xml데이터 읽기
    1) 필요한 패키지 import
        import xml.etree.ElementTree as ET
    2) 계층형 객체로 변경...
        doc = ET.parse(파일이름)
    3) root를 지정
                계층형객체.getroot()
2. url xml 데이터 읽기
    1) url을 통해 요청객체 가져오기
        url = 'www. ...  /localhost:6380/web...'
        request = urllib.request.Request(url)
    2)request를 통해 응답객체(결과처리) 가져오기
        response = urllib .request.urlopen( request)
    3) 계층형으로 변경..
        tree = ET.parse(response)
    4) root접근하기
        Root = tree.getroot()
    
"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import csv
import sys, pymysql

## url로 처리
# 1. 패키지 호출..
import requests
import xml.etree.ElementTree as ET
import urllib.request

# 2. 외부주소. .url
url = 'https://apis.daum.net/local/v1/search/keyword.xml?apikey=465b06fae32febacbc59502598dd7685&code=AT4&location=37.6510085,127.02983770000003&radius=3000&query=%EC%88%98%EC%84%A0'

# 3. response가져오기(url -> request -> response)
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)

# 4. 계층형으로 변경
tree = ET.parse(response)
# 5. 최상위 객체지정
root = tree.getroot()
# 6. 실제 데이터를 찾기위함 item
items = root.findall('item')  ## findall 스펠링조심, 여기는 .//item이 아니다.

# 7. 전체 데이터를 담기위한 list객체 선언.
ar = []
## 배열[].append(단위객체)

# 8. 하나 데이터를 list의 속성값을 '지정'해서 할당.
## list['속성'] = find('xml명')

for imsi in items:
    item = {}
    item['title'] = imsi.find('title').text
    item['latitude'] = imsi.find('latitude').text
    item['longitude'] = imsi.find('longitude').text
    
    # 위의 item 객체를 할당후, 배열에 append()로 할당.
    ar.append(item)
print(ar)

# 9. DataFrame 할당..
df = DataFrame(ar, columns = ['title', 'latitude', 'longitude'])
### 주의: ar이 dict형태일땐 columns의 이름을 매핑해서 가져오므로, 이름이 같아야만한다.
print(df)





