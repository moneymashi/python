print('~')

# li = [1,2,3,4,5]
# result = list(filter(lambda x: x%2 ==0, li))
# print(result);



kor = [60,70,80]
eng = [90,100,70]
mat = [50,60,70]

li = [kor, eng, mat]
# 
# for l in li:
#     print(list(filter(lambda x: x>=70 , l )) )
# 
# def mean(x):
#     return format(sum(x)/len(x) , '0.2f');
#  
# for l in li:
#     print(mean(l) )
#      
#      
#      
# for l in li:
#     print(list(filter(lambda x: mean(x)>=70 ), l) )


####
# 내껄로 다시 만들어보기.
#####
#  성생님답안.
def avg(k,e,m):
    return (k+e+m)/3
avglist = list(map(avg, kor, eng, mat))
print('avglist: ', avglist)
result = list(filter( lambda x: x>=70, avglist) )
print('result: ',result)







