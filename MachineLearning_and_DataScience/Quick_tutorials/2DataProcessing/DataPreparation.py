# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 13:28:06 2021

@author: olive
"""

'''The data must be prepared 
    -To give the machine learning algorithms a better chance 
    -Different algorithms make different assumptions 
'''

#Data Transformation

#We must not try to fit linear regresions to exponential data
#One tranfermation might be to take the log of the data in the y axis
#(for example)

'''
Work flow

1. Load the dataset

2. Split the dataset into inputs and outputs

3. Apply a pre-processing transformation

4. Summarise the data to show the change
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

'''In this data:    Varriables 1-8 are input 
                    Variable 9 is output'''
                    
'''The scikit-learn library has two transformation'''

#1. Fit and Multiple Transormation --- RECOMENDED
'''Call the fit(), then the transform() functions 
to perepare the parameters and then to prapare for modeling'''

#2. Combined Fit-And-Transform
'''Convienient for one off jobs'''

'''There are 4 recipes for data pre-processing'''




from pandas import read_csv 
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Binarizer



filename = 'pima-indians-diabetes.csv'
names = ['Pregnacies', 'Plasma', 'BloodPress', 'Skin', 'Insulin', 'BMI', 'DPF', 'Age', 'Class']

data = read_csv(filename, names=names)
array = data.values #THIS MAKES A PANDA BACK INTO A NORMAL 2D ARRAY

X = array[:,0:8]    #inputs
Y = array[:,8]      #outputs

# 1. Rescale data 
#       - minmaxscaler class to a range between 0 and 1


scaler1 = MinMaxScaler(feature_range=(0,1))
rescaledX1 = scaler1.fit_transform(X)

set_printoptions(precision=3)
print('Rescaled',rescaledX1[0:5,:])

# 2. Standardise data 
#       -StandardScaler class  mean = 0, SD = 1

'''z= (x-x_)/s  -- number of SDs awayfrom the mean'''

#We standadise to a normal (gaussian) distribution with mean=0, SD=1
#Mostsuitable for:
#   -linear regression, 
#   -logistic regression, and 
#   -linear discriminate analysis

scaler2 = StandardScaler().fit(X)
rescaledX2 = scaler2.transform(X)

set_printoptions(precision=3)
print('Standaised',rescaledX2[0:5,:])


# 3. Normalise data
#       -Normalizer class
#       -Adjustig values to a common scale
#       -Possibly relative to some siz variable

'''Find min and max value, lable them A and B respectivel
    if our desired range is 1 to 10 then lable them a and b
    Normalised vaule of x with
    
    Value = a +((x-A)(b-a))/(B-A)
    
    Useful for spase datasets'''
    
scaler3 = Normalizer().fit(X)
NormalisedX = scaler3.transform(X)

set_printoptions(precision=3)
print('Normalised',NormalisedX[0:5,:])



# 4. Binarise data
#       -Binarizer class
#       -Choose a value and if the data is above it return 1, 
#           below or equal to it retuen 0


binarizer = Binarizer(threshold=0).fit(X)
binaryX = binarizer.transform(X)

set_printoptions(precision=3)
print('Binarized',binaryX[0:5,:])

























