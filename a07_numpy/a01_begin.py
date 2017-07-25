'''
Created on 2017. 7. 25.

@author: acorn
'''

# numpy 는 install 해줘야한다.
# 방식은 
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
# numpy‑1.13.1+mkl‑cp36‑cp36m‑win32.whl 다운
# c:\python\lib 로 copy
# 
# python -m pip install [whl 파일의 경로]
# python -m pip install  c:\python\lib\numpy-1.13.1+mkl-cp36-cp36m-win32.whl

## 참고사이트 : http://www.w3ii.com/ko/numpy/numpy_data_types.html


import numpy as np
import datetime
li = range (1,1000000)
s =datetime.datetime.now(); print(s)

for cnt in li:
    cnt = cnt*10
s =datetime.datetime.now(); print(s)

### ndarray로 처리시간 비교.
ar = np.arange(1,1000000)
s =datetime.datetime.now(); print(s)
ar = ar*10
s =datetime.datetime.now(); print(s)
#### 왜 시간이 안걸릴까???













