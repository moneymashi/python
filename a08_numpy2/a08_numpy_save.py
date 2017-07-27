'''
Created on 2017. 7. 27.

@author: acorn
'''
"""
numpy에서 저장과 열기
1. numpy.save(파일경로, 데이터):
    raw데이터의 형태로 저장, 확장자는 .npy 자동삽입.
2. 읽을떄: laod(파일경로)
3. dict형태(K,V)로 저장.
    numpy.savez('파일명', k1 =data1, k2 =data2) 저장확장자.npz
4. 데이터를 읽을때, ㅇ
    데이터명['k1']
5.구분자로 csv형식 파일읽기
    loadtxt('파일경로', delimiter = '구분자' )  csv형식의 파일읽기.

"""

import numpy as np
ar = [100,200,300]
np.save('z10_data01', ar)
## 파일의 데이터 가져오기
br = np.load('z10_data01.npy')
print('파일에서 온 데이터: ', br)

cr = ar+br
## dict형식저장.. savez(), *.npz
## 마찬가지로 byte로 저장하는거라 꺠져잇을것이다.
np.savez('dict', a = ar, b = br, c = cr)
## 불러오기 load
loadFromNpz = np.load('dict.npz')
print('ar(기존 list)+br(from npz): ', loadFromNpz['c'])



########### PRAC
'''3명 급여데이터
1월급여 300,400,500 -> 저장
2월급여 15%인센티브. 1월급여 로딩받고 보너스 추가. 저장.
다시 로딩해서 3번쨰사람의 급여를 출력.'''

sal = np.array([300,400,500])
np.save('z11_salData01.npy', sal)
sal2 = np.load('z11_salData01.npy')
print('load salData(dict X)', sal2)

incentives =np.round(sal * 0.15)
np.savez('salData', jan = sal, ic = incentives, tot = sal + incentives )
loadFromSalData = np.load('salData.npz')
print('load salData(dict["ic"]): ', loadFromSalData['ic'])
print('마지막사람 2월급여(+15%): ', loadFromSalData['tot'][len(loadFromSalData['tot'])-1])









