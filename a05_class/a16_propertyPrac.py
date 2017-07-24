'''
Created on 2017. 7. 24.

@author: acorn
'''
# property와 private선언
# 
# Member라는 클래스 선언.
# id, pass는 private
# 
# set/getLoginId()
# set/getLoginPass()
# 
# 메서드::
# login()
# validate01()을 통해 현재 저장된 id와 pass가 맞ㄴ느지 여부로 인증/비인증으로 처리


### 내가한 방법..(틀림..)
# class Member:
#     def __init__(self, id="", pass01 = ''):
#         print('id::{} , pass01:: {}'.format(id, pass01) )
#         self.setLoginId(id)
#         self.setLoginPass(pass01)
#     
#     def setLoginId(self, id):
#         self.__id = id
#         goid = id
#     def getLoginId(self):
#         return self.__id
#     def setLoginPass(self, pass01):
#         self.__pass01 = pass01
#         gopass01 = pass01
#     def getLoginPass(self):
#         return self.__pass01
#     
# #     def login(self,id, pass01):
#     
# #     login = property(setLoginId, getLoginId)
#     def login(self, id, pass01):
#         if id == self.__id and pass01 == self.__pass01 :
#             print('환영!')
#         else:
#             print('누구냐 너..')
#             
# m01 = Member('money', '1111')
# m01.setLoginId('money01')  ## set이 두번 적용된다면 마지막set을 overwrite하게됨.
# m01.setLoginPass('1234')
# print( m01.getLoginId() )
# print( m01.getLoginPass() )
# m01.login('money01', '1234')
# m01.login('money', '1111')

###############################

class Member:
    def __init__(self):
        self.__id__ = 'pass 저장x'
        self.__pass__ = 'pass 저장x'
    def getLoginId(self):
        return self.__id__
    def setLoginId(self, id):
        self.__id__ = id
    def getLoginPass(self):
        return self.__pass__
    def setLoginPass(self, pass01):
        self.__pass__ = pass01
    goId = property(getLoginId, setLoginId)
    goPass = property(getLoginPass, setLoginPass)
    
    def login(self, id, pass01):
        isValid = '미인증'
        if self.__id__ == id and self.__pass__ == pass01:
            isValid ='인증'
        return isValid;
    
p01 = Member();
p01.goId = 'future'
p01.goPass = '7777'
print(p01.getLoginId(),' // ', p01.getLoginPass() )
print('인증될것::', p01.login('future', '7777'))
print('미인증될것::', p01.login('future', '7778'))






