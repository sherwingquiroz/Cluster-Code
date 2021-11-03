#Test for DFS_Rec
from DFS_Rec impot DFS_Rec

if __name__ == "__main__":
    init_state = [4, 2, 3, 1]
    target = [1, 2, 3, 4]
    visited = []
    node_init = Node(init_state)
    node = DFS_Rec(node_init, target, visited)
    
    #Show result
    result = []
    while node.get_ancestor() != None:
        result.append(node.get_data())
        node = node.get_ancestor()
        
    result.append(init_state)
    result.reverse()
    print(result)
