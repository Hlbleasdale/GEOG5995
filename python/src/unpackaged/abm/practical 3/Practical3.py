# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:16:21 2019

@author: gyhlb
"""

# import random
import random 
# import operator 
import operator
# import matplotlib.pyplot 
import matplotlib.pyplot

import time

#start = time.clock()

# Set the random seed to be sure when running again we get the same result
#random.seed(1000)
random.seed(10)

#create agents list
agents = []

# control how many agents there are 
num_of_agents = 10

num_of_iterations = 100

# create a for loop that gives every agent a random int between 0 and 100
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

print(agents)

#for i in range(num_of_iterations):
#    agents.append([random.randint(0,100),random.randint(0,100)])
for j in range(num_of_iterations):
    print('This is iteration',str(j))
# Move all the agents
    for i in range(num_of_agents):
        
        # Move the first cooridnate
        if random.random() < 0.5:
            print("adding to [0]")
            agents[i][0] += 1
        else:
            print("subtracting from [0]")
            agents[i][0] -=1 
        # Move the second cooridnate
        if random.random() < 0.5:
            print("adding to [1]")
            agents[i][1] += 1
        else:
            print("subtracting from [1]")
            agents[i][1] -=1
        print("Agent", str(i),'has been moved.')

#end = time.clock()

#print("time = " + str(end - start))

print(agents)

# run a loop to display multiple agent coordinates
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    print(i)
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

# Move agent.
if random.random() < 0.5:
    agents[i][0] += 1
else:
    agents[i][0] -= 1
# Check if off edge and adjust.
if agents[i][0] < 0:
    agents[i][0] = 0
if agents[i][1] < 0:
    agents[i][0] = 0
if agents[i][0] > 99:
    agents[i][0] = 99
if agents[i][1] > 99:
    agents[i][0] = 99


if random.random() < 0.5:
    agents[i][0] = (agents[i][0] + 1) % 100
else:
    agents[i][0] = (agents[i][0] - 1) % 100 