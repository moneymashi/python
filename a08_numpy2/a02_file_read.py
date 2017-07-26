'''
Created on 2017. 7. 26.

@author: acorn
'''
"""

"""

import numpy as np
file = open('proverb.txt', 'r', encoding = 'utf-8')
print(file) # 파일상태창...
#content = file.read()
#print(content) # 내용 출력
#file.close()

##content = file.read() 신기하게 이게 위에서 쓰이면 두번 쓰이지는 않는가보다.
for line in file:
    print(line)
file.close()

print('readlines 활용')
file = open('proverb.txt', 'r', encoding = 'utf-8')
lines = file.readlines()
print(type(lines))
print('라인별 배열할당', lines)
file.close()






