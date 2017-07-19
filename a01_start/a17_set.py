'''
Created on 2017. 7. 19.

@author: acorn
'''

s1 = set([1,2,3])
s2 = set([3,4,5])
s3 = set('hallow')
## s1.intersection(s2) 과 같은 결과값.
print(s1 & s2) # {3}
print(s1 | s2) # {1, 2, 3, 4, 5}
print(s1- s2) # {1, 2}
print(s3) #{'w', 'l', 'h', 'o', 'a'}

s1.update([4, 5, 6])
print('s1 update   ', s1)


if(''):
    print("python?" )
else:
    print("none")



