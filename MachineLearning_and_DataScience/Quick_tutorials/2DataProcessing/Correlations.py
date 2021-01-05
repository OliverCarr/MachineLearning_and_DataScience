# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 18:38:26 2021

@author: olive
"""


# 7 Ways to summaries a dataset

#1 Peek at data
#2 Dimentions of data
#3 Data types
#4 Class Distributions
#5 Data Summary


#6 Correlations*****


#7 Skewness


'''Correlations are the relationships beween two varriables
 - expressed as correlation coefficients  from -1 to +1
 
 r= (1/(n-1)) * Sum(i=1, n=n, ((xi-x)/sx)*((yi-y)/sy)) #Where n is the number of pairs of data
 
 +1 means directly proportional
 -1 means inversly proportional
 
''' 

from pandas import read_csv 
from pandas import set_option

filename = 'pima-indians-diabetes.csv'
names = ['Pregnacies', 'Plasma', 'BloodPress', 'Skin', 'Insulin', 'BMI', 'DPF', 'Age', 'Class']

data = read_csv(filename, names=names)

set_option('display.width', 200)
set_option('display.max_columns', 9)
set_option('precision', 3)

correlations  = data.corr(method='pearson')
print(correlations)
