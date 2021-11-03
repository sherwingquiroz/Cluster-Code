#Test for Flights DFS_Iter
from Flights_DFS_Iter import Flights_DFS_Iter

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
    node_init = Node(init_state)
    node = Flights_DFS_Iter(node_init, target)
    
    #Show result
    if node != None:
        result = []
        while node.get_ancestor() != None:
            result.append(node.get_data())
            node = node.get_ancestor()
            
        result.append(init_state)
        result.reverse()
        print(result)
        
    else:
        print("No solution foun")
