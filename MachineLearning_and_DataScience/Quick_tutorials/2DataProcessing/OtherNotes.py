# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 21:35:51 2021

@author: olive
"""

'''

Pandas data structures are not simply arrays, 
slicing is not as straightforward as or numpy arrays

the [x,y] notation is simalar but requires specifc comands




For searching a dataset, I found this setup to work well for the purposes of cleaning data 
'''

from pandas import read_csv 

filename = 'pima-indians-diabetes.csv'
names = ['Pregnacies', 'Plasma', 'BloodPress', 'Skin', 'Insulin', 'BMI', 'DPF', 'Age', 'Class']
data = read_csv(filename, names=names) #for URL replace filename

for i in range(767):
    sli = data.loc[i, 'BMI']
    if sli == 0:
        print(data.loc[i, :])
        
'''
This code is designed to identify people with 0 BMI as outlier.
 Simalar Techniches are possible with minimal varriation. 



The comand .loc[] comand is useful here

the .iloc[] command is for integers only

strings are used in place of column values, as described by the 'names' variable 

'''
#array = data.values #THIS MAKES A PANDA BACK INTO A NORMAL 2D ARRAY
