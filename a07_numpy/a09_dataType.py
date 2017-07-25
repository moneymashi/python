'''
Created on 2017. 7. 25.

@author: acorn
'''

# ndaarray의 자료형
# dtype를 통해 데이터의 형태를 casting, promote 변경 및 설정가능.
# 또는 해당 데이터의 type을 확인가능.
# astype함수를 이용해 타입을 변경함.
# 
# 정수형:: int8, int16... uint8
# 실수형: float16, float32
# 복소수: complex64, complex128
# boolean: bool
# 객체: object
# ###문자열: string_
# 유니코드: unicode

import numpy as np
ar = np.array([1,2,3])
print(ar.dtype)
ar = np.array(['1','2','3'])
print(ar.dtype)
ar = np.array(["a","b","c"])
print(ar.dtype)
ar = np.array([1,2,"c"])
print(ar.dtype)
ar = np.array([1,2,"5"], dtype = np.int32)
print(ar.dtype) #int32
ar = np.array([1,2,"c"], dtype = np.string_)
print(ar.dtype) # |S1 :: 한글자 고정 string












