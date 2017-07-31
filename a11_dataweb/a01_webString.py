'''
Created on 2017. 7. 31.

@author: acorn
'''
"""

"""

import requests

url = 'http://www.naver.com'
# url = 'http://localhost:6080/springweb/start.do'  ## localhost도 가능하다는걸 보여주기만..
data = requests.get(url)
print(data)
print(data.text)

file = open('data_text.txt','w',encoding = 'utf-8')
file.write(''.join(data.text))
file.writelines(data.text)

