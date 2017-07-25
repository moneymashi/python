'''
Created on 2017. 7. 25.

@author: acorn
'''

import numpy as np
games = np.array(['S', 'R', 'P'])
# random_integers(최소, 최대, 갯수)
idx1 = np.random.random_integers(0,2,1)
print(games[idx1])
idx2 = np.random.random_integers(0,2,1)
print(games[idx1],games[idx2])









