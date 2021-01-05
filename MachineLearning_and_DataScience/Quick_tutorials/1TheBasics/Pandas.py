# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 17:13:06 2021

@author: olive
"""

'''Pandas'''

#Provide data structure to analyse and maipulate data
#Series data structure - One dimentional array, labeled rows/columns

import numpy as np
import pandas as pd

myarray =np.array([1,2,3])
rownames = ['a','b','c']

myseries = pd.Series(myarray, index=rownames)

print (myseries)  #'''seems a lot a dictionary to me '''


#DataFrame data structure - Multi-dimentional array, labeled rows/columns


myarray1 = np.array([[1,2,3],[4,5,6]])
rownames1 = ['a','b']
columnnames1 = ['one','two', 'three']

mydataframe = pd.DataFrame(myarray1, index=rownames1, columns=columnnames1)
print(mydataframe)

print('Method 1:')
print('one column: %s' % mydataframe['one'])

print('Method 2:')
print('one column: %s' % mydataframe.one)