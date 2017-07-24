'''
Created on 2017. 7. 24.

@author: acorn
'''

try:
    print('print1')
    print('print2')
    text = input('input numeric! : ')
    if text.isdigit() == False:
        raise Exception('예외 발생 raise ')
except Exception as err:
    print('예외 발생!! except :: {}'.format(err) )
    







