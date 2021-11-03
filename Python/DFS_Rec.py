#Depth First Search Recursive
from Node import Node

def DFS_Rec(node_init, target, visited):
    visited.append(node_init.get_data())
    if node_init.get_data() == target:
        return node_init
        
    else:
        #expand nodes_inheritance
        data_node = node_init.get_data()
        inheritance = [data_node[1], data_node[0], data_node[2], data_node[3]]
        inheritance_left = Node(inheritance)
        inheritance = [data_node[0], data_node[2], data_node[1], data_node[3]]
        inheritance_center = Node(inheritance)
        inheritance = [data_node[0],data_node[1], data_node[3], data_node[2]]
        inheritance_right = Node(inheritance)
        node_init.set_inheritance([inheritance_left, inheritance_center, inheritance_right])
        
        for node_inheritance in node_init.get_inheritance():
            if not node_inheritance.get_data() in visited:
                #call recursive
                tgt = DFS_Rec(node_inheritance, target, visited)
                if tgt != None:
                    return tgt
                    
        return None
