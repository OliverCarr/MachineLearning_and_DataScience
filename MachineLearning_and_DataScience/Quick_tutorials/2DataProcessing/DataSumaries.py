# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 17:34:06 2021

@author: olive
"""

# 7 Ways to summaries a dataset

#1 Peek at data

from pandas import read_csv 

filename = 'pima-indians-diabetes.csv'
names = ['Pregnacies', 'Plasma', 'BloodPress', 'Skin', 'Insulin', 'BMI', 'DPF', 'Age', 'Class']

data = read_csv(filename, names=names)

peek = data.head(20) # the first 20 rows of data
print(peek)

#2 Dimentions of data

shape = data.shape
print(shape)

#3 Data types

type = data.dtypes
print(type)

#4 Class Distributions

'''For class only'''

class_counts = data.groupby('Class').size() #Totak number in each group
print(class_counts)

#5 Data Summary

'''The describe() function - 9 outputs'''
'''Count, Mean, Standard Deviation, Min. Value, (25,50,75, percentile), Max. Value'''

from pandas import set_option

set_option('display.width', 200)
set_option('display.max_columns', 9)
set_option('precision', 3)

description = data.describe()
print(description)

#6 Correlations

'''Correlations are the relationships beween two varriables
 - expressed as correlation coefficients  from -1 to +1
 
 r= (1/(n-1)) * Sum(i=1, n=n, ((xi-x)/sx)*((yi-y)/sy)) #Where n is the number of pairs of data
 
 +1 means directly proportional
 -1 means inversly proportional''' 

correlations  = data.corr(method='pearson')
print(correlations)

#7 Skewness

'''Used to descrive Bell Curves 
    -Normal distribution haveno skew as they have equal on either side of the mean
    -Possitive squew has the tail of the distribution on the possitive side
    -Negative squew has the tail of the distribution on the ngative side''' 
    
skew  = data.skew()
print(skew)

