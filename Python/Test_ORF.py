#Test for ORF
from ORF import *

if __name__ == "__main__":
    data_in = {(0,0):0, (0,1):1, (1,0):1, (1,1):1}
    weights = [0.2, -0.5]
    t = 0.4
    l = 0.2
    weights, t = train_perceptron(data_in, weights, t, l)
    print (clasify((0,1), weights, t))
