'''
Created on 2017. 7. 20.

@author: acorn
'''

a = 10
b = eval('a+5')
print(b)

print(round(1.2), round(1.7))
import math
print(math.ceil(1.2), math.ceil(1.6))

b_list = [True, 1, False]
print(all(b_list))
print(any(b_list))

b_list2 = [1,2,3,6,5,6,7]

re = all(d<5 for d in b_list2)
print('모두 t? ', re)

re01 = any(d>3 for d in b_list2)
print('하나라도 t? ', re01)

## zip()복구개 리스트로 듀플작성
x = [10,20,30]
y = ['a', 'b']
for i in zip(x,y):
    print(i)

subj = ['kor', 'eng', 'mat', 'soc', 'sci']
score = [98, 69, 70, 80 ,100]
print(sum(score))
for i in zip(subj, score):
    print(i, end = '  ')
print()    

prize = 0;
msg = """ ===  아빠의 메세지 ===\n"""
if any(i == 100 for i in score) :
    prize += 5000
    msg += "올.. 100점 맞앗네...? 잘햇어\n"
if all(s >= 70 for s in score) :
    prize += 3000
    msg += "올.. 전부 70점이상 맞앗네...? 잘햇어\n"
if sum(score) >= 80 : 
    prize += 4000
    msg += "올.. 평균 80점이상 맞앗네...? 잘햇어\n"
msg += """ ===  아빠의 메세지 === """
print('현실적인 총상금 ', prize)
print(msg)






