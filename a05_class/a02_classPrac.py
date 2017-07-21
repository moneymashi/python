'''
Created on 2017. 7. 21.

@author: acorn
'''

class CoffeeShop():
    kind = ''
    price = 0
    orderNumber = 0
    totPrice =0
    
    def __init__(self, kind):
        self.kind = kind;
    def order(self, price, orderNumber):
        self.price = price;
        self.orderNumber = orderNumber;
    def calc(self):
        self.totalPrice = self.price * self.orderNumber;
        print('가격: ', self.price,
              '\n주문커피종: ', self.kind,
              '\n주문수량: ', self.orderNumber,
            '\n주문결제: ', self.totalPrice);

cs01 = CoffeeShop('luwak');
cs01.order(500, 30);
cs01.calc()







