# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 17:35:08 2021

@author: olive
"""

#CSV, comma separated values
#No Fonts or colors or boxes or arrows --- Just text
#this is to make it easy for 3rd party systems to read

#File Headers - first row
#Comments - denoted with a # (crazy... right!)
#Delimiter - the C in CSV, commas seperate... values
#Quotes -   "abc" double quotes are standard, used to indicate spaces 


#DataSet being used is about diabetes in te Pima-Indian population
'''
# 1. Number of times pregnant
# 2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test
# 3. Diastolic blood pressure (mm Hg)
# 4. Triceps skin fold thickness (mm)
# 5. 2-Hour serum insulin (mu U/ml)
# 6. Body mass index (weight in kg/(height in m)^2)
# 7. Diabetes pedigree function
# 8. Age (years)
# 9. Class variable (0 or 1)
'''
#First load the csv file

#Then there are three methods to analyse the data
#Python standard library, NumPy, Pandas


'''load CSV using standard python library'''
#Use the reader() funcion

import csv
import numpy as np

filename = 'pima-indians-diabetes.csv'
raw_data = open(filename, 'rt')     #only 'rt' for text
reader = csv.reader(raw_data, delimiter= ',', quoting = csv.QUOTE_NONE)
x = list(reader)

data1 = np.array(x).astype('float')
print(data1.shape)

#From a URL
#url = 'https://some_stuff'
#raw_data = urlopen(url)




'''load CSV using NumPy library'''

from numpy import loadtxt
filename = 'pima-indians-diabetes.csv'
raw_data = open(filename, 'rt')     #for 'rt' or 'rb' - text or binary

data2 = loadtxt(raw_data, delimiter= ',')
print(data2.shape)


'''load CSV using Panda library''' #RECOMENDED

from pandas import read_csv 

filename = 'pima-indians-diabetes.csv'
names = ['Pregnacies', 'Plasma', 'BloodPress', 'Skin', 'Insulin', 'BMI', 'DPF', 'Age', 'Class']

data3 = read_csv(filename, names=names) #for URL replace filename
print(data3.shape)

for i in range(767):
    sli = data3.loc[i, 'BMI']
    if sli == 0:
        print(data3.loc[i, :])





