'''
Created on 2017. 7. 20.

@author: acorn
'''

##########
def question():
    num01 = 3
    num02 = 5
    print( num01, '+', num02, ' = ?')
    answ = input('answer ?')
    if (answ) == str(num01+ num02):
        print('zz')
    else :
        print('너무 졸리다')
    
# question()


### 지역, 전역변수
player = 'rec player'
def FuncSoccer():
    name = 'hong gil'
    player = 'local player'
    print(name, player, sep = '\t')
# FuncSoccer()

#global : 전역변수의 내용을 명시적으로 처리하기위해 사용되는 키워드
a = 10; b=20; c=5;
def Foo():
    a = 30
    def Bar():
        global a
        a = 3
        c = 40
        print('L:{}, E:{}, G:{}'.format(c,a,b))
    Bar()
    print('Bar a : ', a)  # Foo의 지역변수인 a=30을 부른다.
    a = 50
    print('a =50 allocated : ', a)  # a=50. 당연.
#Foo()
#print('after Foo: ', a) # 맨처음 global인 a=10을 엎엇다 global a=3으로 변경됨.


v1 = 1
def varTest(v1):
    v1 = v1+1
    print('지역: ', v1) # 지역에서 +1은 먹히지만...
varTest(v1)
print('전역: ', v1)  # 지역변수의 +1은 전역에 영향이 오기않는다.

defLam = lambda x,y:x*y
kbs = lambda a, su=10 : a+su
print(kbs(5))
print(kbs(5,6))
print(defLam(5,6))

### 
defProd = lambda b,c: b*c
qlist = ['물건명', '가격', '갯수', '총계']
dic ={}
name = input('%s 를 입력하세요. ' %qlist[0])
while name != 'quit' : 
    alist = []
    for i in range(1,len(qlist)-1):
        a = input(qlist[i])
        alist.append(a)
        print(a, alist)
    alist.append( defProd(int(alist[0]), int(alist[1])) )
    print(alist)
    dic[name] = alist
    print(dic)
    name = input('%s 를 입력하세요. 끝내려면 quit. ' %qlist[0])
print(qlist[:], sep = '\t')
for item in dic.keys():
    print(item, dic.get(item))





