# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 17:02:13 2021

@author: olive
"""

#MatplotLib

import matplotlib.pyplot as plt
import numpy

myarray = numpy.array([1,2,3])
plt.plot(myarray)

plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()

myarray1 = numpy.array([1,2,3]) #x
myarray2 = numpy.array([3,2,3]) #y


plt.scatter(myarray1, myarray2)

plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()