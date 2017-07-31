'''
Created on 2017. 7. 31.

@author: acorn
'''
"""

"""

import cx_Oracle as co
from pandas import Series, DataFrame
import numpy as np
import sys

empList= []
try:
    db = co.connect("scott/tiger@localhost/xe")
    print("Connected to the Oracle " + db.version + " database.")
    cursor = db.cursor()
    cursor.execute('select * from emp')
    for row in cursor:
        print(row)
        empList.append(row)
    empList = DataFrame(empList, columns = ['empno', 'ename', 'position', 'mgr', 'hiredate','sal', 'incentives', 'deptno'])
    print(empList)
except co.DatabaseError as e:
    error = e.args
    print('error.code',error.code)
    print('error.msg', error.message)
    print('raised error \n',sys.exc_info())
finally:
    print('work done')


