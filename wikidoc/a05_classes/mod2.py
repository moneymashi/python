'''
Created on 2017. 7. 24.

@author: acorn
'''

pi = 3.14

class Math:
    def solv(self, r):
        return pi* r * r
    
def sum(a,b):
    return a+b
if __name__ == '__main__':  
    ## 여기서 compile하게되면 모두 프린트하게된다.
    ## 만약, import를 하게되면 main에서 쓰는게 아니므로 불러지지않는다.
    print(pi)
    a = Math()
    print(a.solv(2))
    print(sum(pi, 4.4))









