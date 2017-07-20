a = {}
name = 'hong'
scores = [1,2,3]
a[name] = scores
scores.append(sum(scores))
name = 'choi'
scores = [4,5,6]
scores.append(sum(scores))
a[name] = scores
print(a)

print(sum(a['choi']))

## key부르기
for kk in a.keys():
    print(kk, end = '  ')
    print(a[kk], ' allover  sums: ',sum(a[kk]))
    print(kk, a.get(kk) ) 

 

