'''
Created on 2017. 7. 26.

@author: acorn
'''

"""
1. 형식:
배열[조건-boolean]
    1) boolean값 :: == != ~(==) & |
        ex) ar[br=='A'] :
        br 배열에 A인경우에 T 아니면 F
        T인 경우에만 slice(할당)처리
    2) boolean 값, index
        boolean값이 T경우에, 해당 행/열dml idx.
        .두가지 조건을 다 만족하는경우
        ex) ar[br == 'A', 2] 'A' 인경우 행,열 인경우, idx 열/행 경우만 slice.
    3) boolean값, idx시작: idx마지막
        ex) ar[br == 'A', 0:2] : 열의 0에서 2까지
                    
"""
import numpy as np
ar = np.arange(20).reshape(5,4)
print(ar)

br = np.array(['AC','BB','AC','AD','DE'])
print(br)
## br에 문자열이 A인 대한 여부를 boolean처리
print(br[br=='B'*2])
## ar배열에 [] 안에 위에있는 ckr을 입력하면 
## 동일한 해당 배열의 값중 T값에 slicing.
ckr = br== 'AC'
print(ckr)
print('ckr조건의 ar :: \n', ar[br =='AC'])
## 설명: 조건문의 T, F를 찾고 ar[boolean]일떄 조건문에 맞는 해당위치의 행을 가져오고, 열처리를 한다.





