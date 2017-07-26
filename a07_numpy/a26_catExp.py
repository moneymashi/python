'''
Created on 2017. 7. 26.

@author: acorn
'''
"""
1-1 홍길동 김길동
1-2 이길도 마길도
2-1 이영순 최정아
2-2 오연지 신혜영
3-1 이수아 조정연
3-1 신혜라 이정석

위 데이터를 2차원배열로 만드기.
1. 학년별 편성을 처리하기.
2. 반별로 반편성을 
  ex) 1-1, 2-1, 3-1
"""

import numpy as np

ar = np.array([[['홍길','김길'],['이길','마길']], 
               [['이영','최정'],['오연','신혜']], 
               [['서리','팔하'],['고석','도민']]])
listSt = []
listGrade = []
for i in range(3):
    for j in range(2):
        listSt.append(np.array(ar[i])[j])
        print('{}-{}반 : '.format(i+1, j+1), listSt[j], end = '\t')
        
    print()
    listGrade.append(np.concatenate(np.array(ar[i])))
    print('{}학년 전체 : '.format(i+1),listGrade[i])
    
print('1반 전체: ', np.concatenate(np.array(listSt)[::2]))
print('2반 전체: ',np.concatenate(np.array(listSt)[+1::2]))



