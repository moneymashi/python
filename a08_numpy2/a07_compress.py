'''
Created on 2017. 7. 27.

@author: acorn
'''
"""
zip 파일 압축 모듈  - zipfile 모듈가져오기.
1. ZipFile함수로 압축객체 생성, write()함수를 이용해 하나씩압축
2. 압축해제 ZipFile을 만든후, extreactall()처리

cf) w대신 a를쓰면 zip에 파일을 추가할수잇다.

참고사이트:   http://pwnbit.kr/23
"""

import numpy as np
import zipfile
fileList = ['movie.txt','proverb.txt','z04_test.txt']

with zipfile.ZipFile('z06_test.zip', 'w', compression = zipfile.ZIP_BZIP2) as myzip:
    for temp in fileList:
        myzip.write(temp)
## extractall('경로설정')
zipfile.ZipFile('z06_test.zip').extractall('./a01')


"""
tar 파일압축은 tarfile모듈.
1. open함수를 압축객체 생성, add함수를 통해 파일추가.
2. 압축해제 extractall('풀기위치') 호출
"""
import tarfile
filelist = ['a01_file.py', 'a02_file_read.py', 'a02_filePrac.py']
with tarfile.open('z07_test.tar.gz', 'w:gz') as mytar:
    for temp in filelist:
        mytar.add(temp)
tarfile.open('z07_test.tar.gz').extractall('./a2')


