# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 20:00:42 2021

@author: olive
"""


# 7 Ways to summaries a dataset

#1 Peek at data
#2 Dimentions of data
#3 Data types
#4 Class Distributions
#5 Data Summary
#6 Correlations


#7 Skewness*****


'''Used to descrive Bell Curves 
    -Normal distribution haveno skew as they have equal on either side of the mean
    -Possitive squew has the tail of the distribution on the possitive side
    -Negative squew has the tail of the distribution on the ngative side
 
''' 

from pandas import read_csv 

filename = 'pima-indians-diabetes.csv'
names = ['Pregnacies', 'Plasma', 'BloodPress', 'Skin', 'Insulin', 'BMI', 'DPF', 'Age', 'Class']

data = read_csv(filename, names=names)

skew  = data.skew()

print(skew)


