# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 17:58:54 2021

@author: olive
"""


# 7 Ways to summaries a dataset

#1 Peek at data
#2 Dimentions of data
#3 Data types
#4 Class Distributions


#5 Data Summary*****


#6 Correlations
#7 Skewness


'''The describe() function - 9 outputs'''
'''Count, Mean, Standard Deviation, Min. Value, (25,50,75, percentile), Max. Value'''

from pandas import read_csv 
from pandas import set_option

filename = 'pima-indians-diabetes.csv'
names = ['Pregnacies', 'Plasma', 'BloodPress', 'Skin', 'Insulin', 'BMI', 'DPF', 'Age', 'Class']

data = read_csv(filename, names=names)

set_option('display.width', 200)
set_option('display.max_columns', 9)
set_option('precision', 3)

description = data.describe()

print(description)


