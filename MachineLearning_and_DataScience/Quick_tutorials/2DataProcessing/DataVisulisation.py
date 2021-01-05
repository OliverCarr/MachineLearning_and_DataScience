# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:16:47 2021

@author: olive
"""

'''Univariate Plots 
- one variable'''

from matplotlib import pyplot
from pandas import read_csv 
import numpy
from pandas.plotting import scatter_matrix

#Histograms - Useful for seeing if data is guassian or is skewed 



filename = 'pima-indians-diabetes.csv'
names = ['Pregnacies', 'Plasma', 'BloodPress', 'Skin', 'Insulin', 'BMI', 'DPF', 'Age', 'Class']

data = read_csv(filename, names=names)

data.hist()



#Density Plots - very simular to histogram but with a curve plotted

data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)

#Box and whisker plot

data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)



'''Mulitvariable Plots'''

#Correlation Matrix Plot


correlations  = data.corr()

fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1,vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)

pyplot.show()

#Scatter Plot Matrix  -2D scatter plot of two varriables plotted against each other 


scatter_matrix(data)




















