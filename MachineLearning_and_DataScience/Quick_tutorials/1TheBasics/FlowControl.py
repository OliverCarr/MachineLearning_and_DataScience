# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 13:12:27 2021

@author: olive
"""
import time

value = 99
if value == 99:
    print ('that is fast')
elif value > 200:
    print ('that is too fast')
else:
    print ('This is safe')
    

t0 = time.time()

for i in range(10):
    print(i)
t1 = time.time()
    
i=0
while i<10:
    print(i)
    i += 1
    
t2  = time.time()

print('for loop:', (t1-t0),'s')
print('while loop:', (t2-t1),'s')