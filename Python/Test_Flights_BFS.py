#Test for Flights BFS
from Flights_BFS import Flights_BFS

if __name__ == "__main__":
    linkedin = {
        'Malaga':{'Salamanca', 'Madrid', 'Barcelona'},
        'Sevilla':{'Santiago', 'Madrid'},
        'Granada':{'Valencia'},
        'Valencia':{'Barcelona'},
        'Madrid':{'Salamanca', 'Sevilla', 'Malaga', 'Barcelona', 'Santander'},
        'Salamanca':{'Malaga', 'Madrid'},
        'Santiago':{'Sevilla', 'Santander', 'Barcelona'},
        'Santander':{'Santiago', 'Madrid'},
        'Zaragoza':{'Barcelona'},
        'Barcelona':{'Zaragoza', 'Santiago', 'Madrid', 'Malaga', 'Valencia'}
        }
        
    init_state = 'Malaga'
    target = 'Santiago'
    node_target = Flights_BFS(linkedin, init_state, target)
    
    #Show result
    result = []
    node = node_target
    
    while node.get_ancestor() != None:
        result.append(node.get_data())
        node = node.get_ancestor()
        
    result.append(init_state)
    result.reverse()
    print(result)
