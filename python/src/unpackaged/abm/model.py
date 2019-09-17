# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:42:02 2019

@author: gyhlb
"""
import random 
y0 = 50
x0 = 50
print (y0)
if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print (y0)
print (x0)
if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print (x0)


y1 = 50
x1 = 50
print (y1)

if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
print (y1)
print (x1)
if random.random() < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print (x1)
y0 = 0 
x0 = 0 
y1 = 4
x1 = 3
y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff 
x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff
sum = y_diffsq + x_diffsq
answer = sum**0.5
print(answer)

y = random.randint(0, 99)
x = random.randint(0, 99)
print(y)
print(x)

# Practical 2

