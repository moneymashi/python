'''
Created on 2017. 7. 24.

@author: acorn
'''



def try_convert(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            try:
                return str(s)
            except ValueError:
                return s

print(type(try_convert('11')))
print(type(try_convert(11)))

print(type('11'))
print(type(11))

str = input('numbers: ')
print(type(try_convert(str)))



