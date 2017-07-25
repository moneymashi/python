'''
Created on 2017. 7. 25.

@author: acorn
'''

import numpy as np
if __name__ == '__main__':
    points = np.array([7,8,10])
    tot = 0
    for point in points:
        tot+=point
    avg = tot/len(points)
    print('{}\t{}\t{}\t{}\t{}'.format(points[0],points[1],points[2],tot, int(avg)) )








