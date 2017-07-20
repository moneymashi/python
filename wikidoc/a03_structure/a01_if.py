'''
Created on 2017. 7. 20.

@author: acorn
'''
########
# if

price = int(3000)
user = 'customer'
if user == 'customer' and price >= 2000:
    print('{0} takes taxi paying with {1}Won'.format(user, price) )
else: print('BMW dude.');


list = [1,2,3]
if 1 in list: print('int in list !!')

list = ['1','2','3']
if 1 in list: print('in list !!')
else: print('str not in list')

print('i' in 'python')


################
#while
i = 0
while i <10:
    i +=1
    print('나무 찍음 ', i)
    if(i ==10):
        print('나무 넘어감')
print('i result: ', i)

pmt = '''
1. add
2. del
3. list
4. quit

Enter number: '''

# num = 0
# while num != 4 : 
#     print(pmt)
#     num = int(input(' '))

# cof = 4
# while True:
#     money = int(input('money!: '))
#     if cof <= 0:
#         print('커피가 떨어졋대..')
#         break;
#     if money >= 300:
#         money -=300
#         print('커피 나옵니다. 아. 거스름돈 가져가: %d ' %money)
#         cof -=1
#         print('cof', cof)
#     elif money < 300:
#         print('커피값도 없냐.. 잘 찾아봐')
#     else: print('??')
#     
#######
#for
a = [1,2,3,4]
list = [num * 3 for num in a]
print(list)
list = [num * 3 for num in a if num % 2 ==1]
print(list)

gugu = [x*y for x in range(1,10) 
        for y in range(1,10) ]
print(gugu)


