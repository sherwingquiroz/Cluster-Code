#Function XOR

import math
import random
import string

#Show you matrix
def matrix(x, y):
    m = []
    for i in range(x):
        m.append([0.0]*y)
    return m
    
def sigmoid(x):
    return math.tanh(x)
    
def dsigmoid(x):
    return 1.0 - x**2
    
def init_perceptron():
    global nodes_in, nodes_hi, nodes_ex, weights_in, weights_ex
    global act_in, act_hi, act_ex
    random.seed(0)
    
    nodes_in = nodes_in + 1
    
    act_in = [1.0] * nodes_in
    act_hi = [1.0] * nodes_hi
    act_ex = [1.0] * nodes_ex
    
    weights_in = matrix(nodes_in, nodes_hi)
    weights_ex = matrix(nodes_hi, nodes_ex)
    
    for i in range(nodes_in):
        for j in range(nodes_hi):
            weights_in[i][j] = random.uniform(-0.5, 0.5)
            
    for j in range(nodes_hi):
        for k in range(nodes_ex):
            weights_ex[j][k] = random.uniform(-0.5, 0.5)
            
def update_nodes(intake):
    global nodes_in, nodes_hi, nodes_ex, weights_in, weights_ex
    global act_in, act_hi, act_ex

    if len(intake) != nodes_in-1:
        raise ValueError('Number of Entries Nodes Incorrect. ')
        
    for i in range(nodes_in-1):
        act_in[i] = intake[i]
    
    for j in range(nodes_hi):
        sum = 0.0
        for i in range(nodes_in):
            sum = sum + act_in[i] * weights_in[i][j]
        act_hi[j] = sigmoid(sum)
        
    for k in range(nodes_ex):
        sum = 0.0
        for j in range(nodes_hi):
            sum = sum + act_hi[j] * weights_ex[j][k]
        act_ex[k] = sigmoid(sum)
    
    return act_ex[:]
    

