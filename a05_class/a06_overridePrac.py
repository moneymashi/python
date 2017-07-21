'''
Created on 2017. 7. 21.

@author: acorn
'''

class Write():
    def wrSomething(self):
        print('writing something?')
        
class Pen(Write):
    def wrSomething(self):
        print('write w/ a pen ');

class Pencil(Write):
    def wrSomething(self):
        print('write w/ a pencil ');

print('### override ')
p1 = Pen();
p1.wrSomething()
p2 = Pencil();
p2.wrSomething()

print('### poly')
w = Write()
w = p1
w.wrSomething()
w = p2
w.wrSomething()






