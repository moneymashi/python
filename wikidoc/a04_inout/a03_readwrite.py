'''
Created on 2017. 7. 21.

@author: acorn
'''

# 파일 생성하기
# f = open('C:/Users/acorn/Desktop/tester.txt', 'w')
# f.close()

# f = open('C:/Users/acorn/Desktop/tester2.txt', 'w')
# for i in range(1,10):
#     data = '%d 번쨰 라인입니다 \n' %i
#     print(data, end = '')
#     f.write(data)
# f.close()


# f = open('C:/Users/acorn/Desktop/tester2.txt', 'r')
# while True:
#     line = f.readline()
#     if not line: break;  ## 라인이 null일땐 while문 break.
#     print(line, end = '')
# f.close

print('~')

# f = open('C:/Users/acorn/Desktop/tester2.txt', 'r')
# data = f.read()
# print(data)
# f.close()



# f = open('C:/Users/acorn/Desktop/tester2.txt', 'a')
# for i in range(10, 21):
#     data ='%d 번째 줄입니다만...\n' %i
#     f.write(data)
# f.close()


# f = open('C:/Users/acorn/Desktop/tester2.txt', 'w')
# f.write('beautiful Life~ 난 너의 곁에 있을게~')
# f.close()

with open('C:/Users/acorn/Desktop/tester2.txt', 'a') as f:
    f.write('beautiful Life~ 난 너의 곁에 있을게~~~~~~\n' )
    ## 주의. w(with)는 이전의 데이터를 모두 날린다. add는 a....


f = open('C:/Users/acorn/Desktop/tester2.txt', 'r')
data = f.read()
print(data)
f.close()