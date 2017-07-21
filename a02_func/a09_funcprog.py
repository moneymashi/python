'''
Created on 2017. 7. 21.

@author: acorn
'''
def f(x):
    return x**x

li = [1,2,3,4]
for i in li:
    print(f(i), end = ' '  )
print()
result = list(map(f, li))
print(result);

print('lambda list: ', list(map(lambda x:x**x, li)) )


lis = []
allowed = set((1,2,3,4,5,6,7,8,9,0))
while True:
    ui = input('zzz: ')
    if allowed.issuperset(int(ui)):
        break;
    else:
        lis.append( int(ui) )
        print(lis)
#     if type(int(lis[len(lis)-1]) ) != int:
#         break;

lamFunc = lambda *x: x*3

print('tester: ',list(map(lamFunc, lis)) )


####

while True:
    message = input("Enter num: ")

    if message and allowed.issuperset(message):
        # do whatever
        break
    print("Invalid characters entered!")