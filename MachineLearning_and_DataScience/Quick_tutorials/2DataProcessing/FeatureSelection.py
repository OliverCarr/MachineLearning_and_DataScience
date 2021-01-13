# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:14:33 2021

@author: olive
"""

'''Feature selection'''

#Example
#Lear Granting Problem
#   - a model for bankers to tell if they should give out loans or not

#Features should be kept to a minimum to save computational power

#Especially when using linear and logistical regression algorithms

'''Automatic Feature Selection Techniques'''

#1. Univariate Selection

#Statistical tests can find the features withe the 
#strongest relationship with the output varriable

#Use thescikit-learn library - SelectKBest class 

#This example uses chi-squared statistical test for the 
# non-negative features to select 4 of the best features from the data

'''Chi-Squared  X^2 = Sum((o-e)^2/e)
o - observed frequency
e - expected frequency

X^2 should be as close to 0 as possible == 0 in  perfect, theoretical world

must know the degrees of freedom n 
n = number of possible occerances - 1 
'''

#Feature Extraction with Univarriable Statistical tests

from pandas import read_csv
from numpy import set_printoptions

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

#load data

filename = 'pima-indians-diabetes.csv'
names = ['Pregnacies', 'Plasma', 'BloodPress', 'Skin', 'Insulin', 'BMI', 'DPF', 'Age', 'Class']

data = read_csv(filename, names = names)

array = data.values

X = array[:,0:8]
Y = array[:,8]

#feature extraction

test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X,Y)

#summarise scores


set_printoptions(precision=3)
print(fit.scores_)

features = fit.transform(X)

#Summarise selected features

print(features[0:5,:])

#The 4 selected featureswere plasma, insulin, BMI, age

'''Recursive Feature Elimination - RFE
    -Remove the least imortant field 
    -Repeats until the number of features specified is reached
    -Uses logistic regression '''

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(solver = 'liblinear')
rfe  = RFE(model, n_features_to_select=3)
fit = rfe.fit(X,Y)
n_features_to_select=3

print("Num Feature: %d" % fit.n_features_)
print("Selected Features: %s" % fit.support_)
print("Feature Ranking: %s" % fit.ranking_)



'''Principal Component Analysis - PCA
    -uses linear algebra to compress a dataset
    -data reduction technique
    -dimention reduction technique
    -PCA class in scikit-learn
'''

from sklearn.decomposition import PCA

#feature extraction

pca = PCA(n_components=3)
fit = pca.fit(X)

#Summaries components

print("Explain Variance: %s" % fit.explained_variance_ratio_)
print(fit.components_)

'''Feature Importance
    -Decision tree to estimate the importance of features
    -ExtraTreesClassifier in the example
    '''

from sklearn.ensemble import ExtraTreesClassifier

#Featureextraction

model = ExtraTreesClassifier(n_estimators=100)
model.fit(X,Y)

print(model.feature_importances_)










