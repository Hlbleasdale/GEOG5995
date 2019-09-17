# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:02:14 2019

@author: gyhlb
"""

# import random
import random 
# import operator 
import operator
# import matplotlib.pyplot 
import matplotlib.pyplot


#create agents list
agents = []
## Append two random coordinates to the agents list

num_of_agents = 10
# Create num_of_agents
#for i in range(0, num_of_agents,2):
#for i in range(0, num_of_agents):
for i in range(num_of_agents):
    print(i)
    agents.append([random.randint(0,99),random.randint(0,99)])
print(agents)


#y0 = random.randint(0,99)
#x0 = random.randint(0,99)


print(agents)
# find the largest coordinate
print(max(agents)) # this only takes in account the first y, not x
# to find the largest x coordinate (the furthest east)
print(max(agents, key=operator.itemgetter(1)))
#print (y0)

#matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
#matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
#max_dot = max(agents, key=operator.itemgetter(1))
#matplotlib.pyplot.scatter(max_dot[1],max_dot[0], color='red')
#matplotlib.pyplot.show()


matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

for i in range(num_of_agents):
    print(i)
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
max_dot = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(max_dot[1],max_dot[0], color='red')    

#matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
#max_dot = max(agents, key=operator.itemgetter(1))
#matplotlib.pyplot.scatter(max_dot[1],max_dot[0], color='red')
matplotlib.pyplot.show()



## Move y0 randomly
#if random.random() < 0.5:
#    y0 = y0 + 1
#else:
#    y0 = y0 - 1
##print (y0)
##print (x0)
## Move x0 randomly
#if random.random() < 0.5:
#    x0 = x0 + 1
#else:
#    x0 = x0 - 1
##print (x0)
#
## Move y0 and x0 randomly a second time
#    
#if random.random() < 0.5:
#    y0 = y0 + 1
#else:
#    y0 = y0 - 1
#if random.random() < 0.5:
#    x0 = x0 + 1
#else:
#    x0 = x0 - 1
#
## Make y1 and x1 = 50
#y1 = 50
#x1 = 50
##print (y1)
## Move y1 randomly
#if random.random() < 0.5:
#    y1 = y1 + 1
#else:
#    y1 = y1 - 1
##print (y1)
##print (x1)
#    
#    
## Move x1 randomly
#if random.random() < 0.5:
#    x1 = x1 + 1
#else:
#    x1 = x1 - 1
##print (x1)
#
## Move y1 and x1 randomly a second time
#    
#if random.random() < 0.5:
#    y1 = y1 + 1
#else:
#    y1 = y1 - 1
#    
#if random.random() < 0.5:
#    x1 = x1 + 1
#else:
#    x1 = x1 - 1
#
##y0 = 0 
##x0 = 0 
##y1 = 4
##x1 = 3
## answer = Pythagorian distance between y0,x0 and y1,x1
#y_diff = (y0 - y1)
#y_diffsq = y_diff * y_diff 
#x_diff = (x0 - x1)
#x_diffsq = x_diff * x_diff
#sum = y_diffsq + x_diffsq
#answer = sum**0.5
## print answer
##print(answer)
#
## Randomly start the coordinates at different locations within a 100x100 grid
## with the coordinates being integer values between and including 0 and 99
#y0 = random.randint(0, 99)
#x0 = random.randint(0, 99)
##print(y0)
##print(x0)
#
#
