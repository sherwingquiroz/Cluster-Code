#Test Uniform Cost Search
from UCS import UCS

if __name__ == "__main__":
    linkeden = {
        'Malaga':{'Granada': 125, 'Madrid': 513},
        'Sevilla':{'Madrid': 514},
        'Granada':{'Malaga': 125, 'Madrid': 423, 'Valencia': 491},
        'Valencia':{'Granada': 491, 'Madrid': 356, 'Zaragoza': 309, 'Barcelona': 346},
        'Madrid':{'Salamanca': 203, 'Sevilla': 514, 'Malaga': 513, 'Granada': 423, 'Barcelona': 603, 'Santander': 437, 'Valencia': 356, 'Zaragoza': 313, 'Santander': 437, 'Santiago': 599},
        'Salamanca':{'Santiago': 390, 'Madrid': 203},
        'Santiago':{'Salamanca': 390, 'Madrid':599},
        'Santander':{'Madrid': 437, 'Zaragoza': 394},
        'Zaragoza':{'Barcelona': 296, 'Valencia': 309, 'Madrid': 313},
        'Barcelona':{'Zaragoza': 296, 'Madrid': 603, 'Valencia': 346}
         }
         
    init_state = 'Malaga'
    target = 'Santiago'
    node_target = UCS(linkedin, init_state, target)
    
    #Show result
    result = []
    node = node_target
     while node.get_ancestor() != None:
        result.append(node.get_data())
        node = node.get_ancestor()
        
    result.append(init_state)
    result.reverse()
    print(result)
    print('Cost:' + str(node_target.get_cost()))
    
