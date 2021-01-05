# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 20:15:20 2021

@author: olive
"""

def mysum(x,y):
    return x+y

result = mysum(1,3)
print(result)



#Tuples - Read only collections of items ()
a = (1,2,3)
print(a)

#Lists - uses array notation[]
mylist= [1,2,3]

print("Zeroth Value: %d" % mylist[0])

mylist.append(4)

print("List length: %d" % len(mylist))

for value in mylist:
    print(value)
    

#Dictionaries - mapping names to values {} first are the keys

mydict = {'a':1,'b':2, 'c':3}

print("A Value: %d" % mydict['a'])

mydict['a'] = 11

print("A Value: %d" % mydict['a'])      #%d - decimal

print("Keys: %s" % mydict.keys() )      #%s - string

print("Values: %s" % mydict.values() ) 

for key in mydict.keys():
    print(mydict[key])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    