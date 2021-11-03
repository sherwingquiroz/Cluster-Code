#Test for XORF
from XORF import *

if __name__ == "__main__":
    data_in = [[[0,0], [0]], [[0,1], [1]], [[1,0], [1]], [[1,1], [0]]]
    
    nodes_in = 2 #neurons intake
    nodes_hi = 2 #neurons hide
    nodes_ex = 1 #neurons outing
    l = 0.5
    init_perceptron()
    train_perceptron(data_in, l)
    clasify(data_in)
