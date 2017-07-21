'''
Created on 2017. 7. 21.

@author: acorn
'''



class AddClass:
    def __init__(self,s):
        self.s = s;
    def __add__(self,b):
        return '더하기결과: ' + str(self.s + b)
    
c = AddClass(5)
print(c+5)
c2 = AddClass('kbs')
print(c2 + 'sbs')


class Gstring:
    def __init__(self, iniData):
        self.content = iniData
    ## 해당객체에 - 연산자를 뒤에 붙을때 처리될내용
    def __sub__(self, ss):
        for i in ss : 
            self.content = self.content.replace(i, '')
        return Gstring(self.content)





