#Function OR

def target(k, weights, t):
    z = -t
    
    for i in range(len(k)):
        z = z+(k[i] * weights[i])
    
    if z >= 0:
        return 1
    else:
        return 0
        
def train_perceptron(data_in, weights, t, l):
    errors = True
    while errors:
        errors = False
        
        #train perceptron
        for k,y in data_in.items():
            z = target(k, weights, t)
            if z != y:
                errors = True
                #Errors
                e = (y - z)
                
                #Tune up
                delta_t = -(l*e)
                t = t+delta_t
                
                for i in range(len(k)):
                    delta_w = l*e*k[i]
                    weights[i] = weights[i]+delta_w
                    
    return weights, t
    
def clasify(intake, weights, t):
    return target(intake, weights, t)
    
#Just Dance
