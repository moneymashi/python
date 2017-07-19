'''
Created on 2017. 7. 19.

@author: acorn
'''

count = 100  # 정수
weight = 25.7 # 부동 소수점
name = '홍hong' # string
# print(count," ", weight,'  ',  name)
# print(type(count))

a=2
s =2
s1 = '2'
b=3
#a,b = b,a
#print(a, b)

#print('true' if 'true' else 'false')

#print('??: ', (b,a) if a<b else a,b)
#  
# print( a == 2)
# print( a == '2')
# print( a is 2)
# print( a is '2')
# 
# print(1,2, end = ''); print(3,4)  # x표시가 나타나지만 제대로 역할한다..
# print(1,2, sep = '\t'); print(3,4)
# 
# print(format(4, '10d')) #         4 숫자앞 자리수에도 영향이 온다는걸 알수잇음.
# print(format(43.3, '10.3f')) #    43.300
# print(format('himan', '10s'))

# print('{0} is {1}'.format('python', 'fun'))  #python is fun
# 
# 
# languages = ['python', 'perl', 'c', 'java']
# for lang in languages:
#     print(lang)
#     if lang in ['python', 'perl']:
#         print(lang, 'needs interpreter')   
#     elif lang in ['c', 'java']:
#         print('%10s need compiler' % lang) ##여기서 %의 역할? {}와 10s의 합성. lang이라는 단어를 할당받고 10s라는 크기까지 주어진다. 
#     else:
#         print('error')


# v1 = 1000
# v2 = 0
# if v1:
#     print('1- true?')
#     print(v1)
# if v2:
#     print('0 - false?')
#     print(v2)
# print('bb!!')
# 
# 
# list01 = ['국', '영', '수']
# score = []
# i = len(list01)
# while(i>0):
#     for item in list01:
#         uin = input('%3s 점수? ' % item) 
#         print('%4s is ' %item, uin )
#         score.append(int(uin))
#         i-=1
#     mean = sum(score)/len(score)
#     print(format(mean,'2.1f'))
#     

# # 1~9단. 
# def gugu():
#     i = 1; j = 1;
#     for i in range(1,10):
#         for j in range(1,10):
#             if i==8 and j ==5:
#                 return;
#             elif j ==3:
#                 continue;
#             print(i,'*',j,'=',j*i , sep = ' ', end = '\t')
#         print()
# 
# gugu()

# 입력받고 단위처리
# def healthy():
#     name = input('your name is ')
#     nowWeight = int(input('your weight is '))
#     goalWeight = format(nowWeight* 0.9, '10.1f')
#     print('name: ', name, 
#           'nowWeight: ', nowWeight,
#           'goalWeight: ', goalWeight, sep = '')
# 
# healthy()

# from fractions import Fraction
# a = Fraction(5,7) +Fraction ('2/5')
# print(a)

# from decimal import Decimal
# hap = Decimal(0.0)
# delta = Decimal(0.01)
# for i in range(0,1000):
#     hap += delta;
#     print('hap: ', hap)
 
# a=5
# b=3
# if a==5 & b==3:
#     print('!!')
# else:
#     print(a==5 , b==3,a==5 & b==3)

# def sAndm(a,b):
#     return a+b, a*b;
# 
# (sum01, mul01) = sAndm(1,2);
# print(sum01, mul01)

# ####
# num = input('주민번호: ')
# y = '19' + num[0:2]  ## 0,1번째 자리수 구하기. :2번째자리 이전까지.
# m = num[2:4]
# d = num[4:6]
# g = num[6]
# if g =='1':
#     genderStr ='M'
# elif g =='2':
#     genderStr ='F'
# print('생년월일 {0}년{1}월{2}일'.format(y,m,d))

# print('성별', genderStr)

# int_val = 23
# float_val = 34.93
# print('int_val: %3d, float_val %0.2f' %(int_val,float_val))
# 
# line =  '''
# ddddd
# ccccc
# '''
# print(line)
# print(line[3:8])

# a = 'npython'
# b = ( 'a'+ a[1:len(a)] )
# print(b)

# family  = ['sk','sj','dnfl','rkwhr']
# family.insert(0, 'ss')
# family.append('aa')
# family.extend('bb')
# family.extend(['삼촌', '조카'])
# print(family)
# print(family.index('sj'))
# print('sj' in family)

list01 = ['a','b']
# list01.upper()

# item02 = '   dccd    '
# print(item02)
# print(item02.strip())
# print(item02.lstrip())
# print(item02.rstrip())
# print(item02.replace('cc','ee'))
# print(item02.split(' '))
# item03 = 'sj, sk, li'
# list02 = item03.split(',')
# print(list02)

# list04 =['a','b','c','d','e']
# list04[0] = 'namer'
# print(list04[0][:3])
# list04.sort(reverse = True)
# print(list04)


# a = [1, 2, 3, ['a', 'b', 'c']]
# list01 = [0,1,2,3]
# list02 = [10,11,12,13]
# list03 = [20,21,22,23]
# 
# a = [list01, list02, list03]
# for i in range(0,len(list01)):
#     print( i, list02[i] )
#       
#       
# for i in range(0,len(list01)) :
#     for j in range(0,len(list01)) :
#         print(i,j, end = ' ')
#         print(a[i][j])


# chars = []
# sentence = '대한민국 kor'
# for k in sentence:
#     chars.append(k)
# print(chars)

# name01 = 'hong'
# name02 = name01
# print(name01, name02) 
# print(id(name01), id(name02)) #6496576 6496576
# name01 = 'sss'  #####
# print(id(name01), id(name02)) #6496896 6496576   !=
# 
# name03 = [1,2,3,4]
# name04 = name03
# print(name03, name04) 
# print(id(name03), id(name04)) #31762352 31762352
# name03[0] = 5  #####
# print(id(name03), id(name04)) #31762352 31762352 ==
# 
# #### 해결방법
# import copy
# name05 = copy.deepcopy(name03) # 새로운 객체생성
# print(name03)
# name05[0]= 8
# print(name03, name04, name05)
# print(id(name03), id(name04), id(name05)) #31172528 31172528 41017392


# ## LIFO , stack
# sbs = [10,20,30]
# sbs.append(40); print(sbs)
# sbs.pop(len(sbs) -1 ); print(sbs)
# sbs.pop(2); print(sbs)
# 
# ## FIFO , queue
# sbs = [10,20,30]
# sbs.append(40); print(sbs)
# sbs.pop(0); print(sbs)
# sbs.pop(0); print(sbs)
# 
# 
# sbs = [10,20,30]
# sbs.sort(reverse = True)
# print(sbs)
# sbs.reverse()
# print(sbs)


list01 = [1,2,3,4]
list02 = [3,4,5,6]
list00 = []
list00.append(list01)
list00.append(list02)
del list02[:]
print(list00)

# 
# ########## 개인연습
# slist = []
# clist = []
# head = ['이름', 'kor', 'eng', 'mat']
# id =0
# while(id < 4):
#     for item01 in range(0, len(head)) :
#         print(id, item01)
#         score = input('%s 적어라: ' %head[item01] )
#         clist.append(score)
#         print(clist)
#     slist.append(clist)
#     del clist[:]
# #        slist.append(input( '%s 을 기입: ' %head[item01]  ))
#     id+=1
#          
# print(slist)



#### mean, sum받아내기. 만들다 만것.
# def getScore(listAll):
#     for ss in listAll:
#         sscore = sum(listAll[ss][1:len(listAll)])
#         mscore = sscore / len(listAll)  # 과목합산 / 학생수
#     return sscore, mscore;
# 
# head = ['이름', 'kor', 'eng', 'mat']
# numStudents = 4
# stuList = [[0]*len(head) for i in range(numStudents)]
# stu=0; scores=0
# ran = range(len(head))
# for stu in ran:
#     for scores in ran:
#         score = input('%s 적어라: ' %head[scores] )
#         stuList[stu][scores] = score
#         print(stu, scores, stuList[stu][scores])
# print(stuList)
# getScore(stuList);
# 
# print(sum(stuList[1][1:len(stuList)]))





