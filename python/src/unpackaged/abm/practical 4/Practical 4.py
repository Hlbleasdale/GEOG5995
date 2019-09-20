# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:44:07 2019

@author: gyhlb
"""

import random
import operator
import matplotlib.pyplot
import time

start = time.clock()

def distance_between(agents_row_a, agents_row_b):
    return ((agents_row_a[0] - agents_row_b[0])**2 + (agents_row_a[1] - agents_row_b[1])**2)**0.5
    
num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

'''
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)
'''

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

distance = distance_between(agents[0], agents[1])
print(distance)

#distance_all=[]
for agents_row_a in agents:
    distance=[]
    for agents_row_b in agents:
        distance.append (distance_between(agents_row_a, agents_row_b))
    print(distance)
#    distance_all.append(distance)
#print(distance_all)

print(max(distance))
print(min(distance))

end = time.clock()

print("time = " + str(end - start))
