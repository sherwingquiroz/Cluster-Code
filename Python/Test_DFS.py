#Test for DFS
from DFS import DFS

if __name__ == "__main__":
    init_state = [4, 2, 3, 1]
    target = [1, 2, 3, 4]
    node_target = DFS(init_state, target)
    
    #Show result
    result = []
    node = node_target
    
    while node.get_ancestor() != None:
        result.append(node.get_data())
        node = node.get_ancestor()
        
    result.append(init_state)
    result.reverse()
    print(result)
