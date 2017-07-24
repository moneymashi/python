'''
Created on 2017. 7. 24.

@author: acorn
'''

class Book:
    price = 3000;
    
    @classmethod
    def showBookPrice(cls):
        print(cls.price, '원')
    
    @staticmethod
    def showBookName():
        name = '파이써어어언!'
        print('도서명 ', name)
        









