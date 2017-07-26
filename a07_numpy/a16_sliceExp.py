'''
Created on 2017. 7. 26.

@author: acorn
'''
"""
예제)
학생 5명의 과목별(3)점수처리
배열만들고 과목명을 문자배열만들고
1)첫번쨰 과목점수 2) 세번쨰 과목점수
3) 80이상 과목점수
4) 두번쨰 과목의 2번쨰 학생의 점수
"""

import numpy as np
nparr = np.random.uniform(80,100,15).reshape(3,5)
subList = np.array(['kor', 'mat','eng'])
print('nparr::\n', nparr)
print('1) ',nparr[ subList == 'kor'])
print('3) ',nparr[ nparr >= 80 ])
print('2) ',nparr[ subList == subList[1], 1 ])




