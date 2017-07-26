'''
Created on 2017. 7. 26.

@author: acorn
'''
"""

"""

import numpy as np
## open('파일명', 'w-쓰기옵션', 'encoding방식')
file = open ('proverb01.txt','w', encoding = 'utf-8')
print(file)
file.write('hello world!!')
file.write('\n\n')
lines = ['안녕하세요', '반값습니다', '파이썬하고잇네']
# write('데이터 단위구분자  \n'.join(데이터배열))
file.write('\n'.join(lines))
file.writelines(lines)
# file자원해제
file.close()
