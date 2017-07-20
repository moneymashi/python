'''
Created on 2017. 7. 19.

@author: acorn
'''

# s1 = set([1,2,3])
# s2 = set([3,4,5])
# s3 = set('hallow')
# ## s1.intersection(s2) 과 같은 결과값.
# print(s1 & s2) # {3}
# print(s1 | s2) # {1, 2, 3, 4, 5}
# print(s1- s2) # {1, 2}
# print(s3) #{'w', 'l', 'h', 'o', 'a'}
# 
# s1.update([4, 5, 6])
# print('s1 update   ', s1)


# if(''):
#     print("python?" )
# else:
#     print("none")


# ##########
# # hastset = set();
# hastset = ();
# hashset = {1,2,3}
# print('hashset: ',hashset)
# 
# hashset = ((1,2,3),(3,2,1))
# print('hashset: ',hashset)
# 
# hashset = ([1,2,3])
# print('hashset: ',hashset)


## 추가 add , update([데이터나열])
# 복사 copy()
# 전체제거 clear()
# 한개제거 discard()  #없다면 pass
# 한개제거 remove() # 없다면 예외
# pop(): 1개제거, (앞, 뒤에 내용제거)

# a = {1,2,3,1}
# print('count', len(a))
# b = {3,4,5}
# print(a.union(b))
# print(a.difference(b))
# print(a-b, a|b, a&b)
# 
# b.add(6)
# print(b)
# b.update([7,8])
# print(b)
# b.update({7,8})
# print(b)
# b.update((7,8))
# print(b)
# b.discard(6)
# print(b)
# b.remove(5)
# print(b)
# b.pop()
# print(b)
# print(b.pop())
# 
# print('tuple: ', tuple(a))
# print('list: ', list(a))


cart = ({'a','v','b','c','d','a'})
cart = list(cart)
print(cart)
cart = set(cart)
print(len(cart))

#########
p01 = (3,5,2,3,5)
p02 = (1,2,6)
p01 = set(p01)
p02 = set(p02)
p01.intersection(p02)
p03 = list(p01.union(p02))
print('중복제거 계획', p03)
print('마지막계획', p03[len(p03)-1])

