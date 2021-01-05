# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 20:47:41 2021

@author: olive
"""

#python list to numpy array
import numpy 
mylist = [[1,2,3], [3,4,5]]

myarray = numpy.array(mylist)

print(myarray)
print(myarray.shape)

print("First row: %s:" % myarray[0])
print("Last row: %s:" % myarray[-1])


print("Specific row and col: %s" % myarray[0,2])
print("Whole col: %s" % myarray[:,2])


#arrithmetic
 
myarray1 = numpy.array([2,2,2])
myarray2 = numpy.array([3,3,3])

print("Addition: %s" % (myarray1+myarray2))
print("Multiplication: %s" % (myarray1*myarray2))