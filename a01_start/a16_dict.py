a = {}
name = 'hong'
scores = [1,2,3]
a[name] = scores
name = 'choi'
scores = [4,5,6]
a[name] = scores
print(a)

print(sum(a['choi']))

## key부르기
for kk in a.keys():
    print(kk, end = '  ')
    print(a[kk], '   sums: ',sum(a[kk]))



