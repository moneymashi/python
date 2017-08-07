'''
Created on 2017. 8. 3.

@author: acorn
'''
"""

"""

from pandas import Series, DataFrame
import numpy as np 
import pandas as pd
import sys, pymysql
#crawling 
import requests
from io import StringIO # 데이터 받아오기
from lxml.html import parse # 태그형식 계층변환

url = "http://market.cetizen.com/market.php?q=market&auc_sale=1&escrow_motion=3&sc=1&qs=&auc_wireless=&auc_uid=&stype=&akeyword=&just_one=&just_one_name=&just_one_pcat=&view_type=&m%5B1%5D=1&auc_price1=&auc_price2=&keyword_p=&pno=&pw="

data = requests.get(url)
## 최상의 root()받기
doc = parse(StringIO(data.text))
root =doc.getroot()
cols = []
vals = []

form = root.findall('.//form', {'name': 'AucListForm'}) # div접근
print('len(form):: ', len(form))
for whatIs in form:
    print(whatIs)
print(dir(form))
for divs in form:
    print('len(divs)::',len(divs))
    for div in divs:
        if len(divs)==3 and len(div) ==22:
            print('len(div)::',len(div))
            for ul in div:
                print(ul )
                for li in ul:
                    for span1 in li:
                        for span2 in span1:
                            print(span2)
                            print('len a span2',len(span2))
                            for ahref in span2:
                                print('len a href',len(ahref))
#                                 print(ahref[0].findall('span').text_content())

span = root.findall('.//span', {"class": "clr02"})
print(len(span))
for sp in span:
    print(sp.text_content())
                    
                    

#     for span in div:
#         print(span.text_content() )

## check div contents
# data = requests.get(url)
# print(data)
# print(data.text)
# file = open('data_text1.txt','w',encoding = 'utf-8')
# file.write(''.join(data.text))
# file.writelines(data.text)

 
# uls = divs[0].findall('.//ul')
# print('len(uls)::',len(uls))
# lis = uls[0].findall('.//li')
# print('len(lis)::',len(lis))
# for div in divs:
#     for ul in uls:
#         for li in lis:
#             print('li.text_content', li.text_content() )


#  for ultag in soup.find_all('ul', {'class': 'my_class'}):
# ...     for litag in ultag.find_all('li'):
# ...             print litag.text









print('#' * 30 ,"")




