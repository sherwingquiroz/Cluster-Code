#Breadth First Search
from Node import Node

def BFS(init_state, target):
    targeting = False
    nodes_visited = []
    nodes_border = []

    nodeInit = Node(init_state)
    nodes_border.append(nodeInit)
    
    while (not targeting) and len(nodes_border) != 0:
        node = nodes_border.pop(0)
        #Extract node and append to visited
        nodes_visited.append(node)
        if node.get_data() == target:
            #targeting finded
            targeting = True
            return node
        else:
            #Expand nodes inheritance
            data_node = node.get_data()
            
            #left bracket
            inheritance = [data_node[1], data_node[0], data_node[2], data_node[3]]
            inheritance_left = Node(inheritance)
            if not inheritance_left.in_list(nodes_visited) and not inheritance_left.in_list(nodes_border):
                nodes_border.append(inheritance_left)
                
            #center bracket
            inheritance = [data_node[0], data_node[2], data_node[1], data_node[3]]
            inheritance_center = Node(inheritance)
            if not inheritance_center.in_list(nodes_visited) and not inheritance_center.in_list(nodes_border):
                nodes_border.append(inheritance_center)
                
            #right bracket
            inheritance = [data_node[0], data_node[1], data_node[3], data_node[2]]
            inheritance_right = Node(inheritance)
            if not inheritance_right.in_list(nodes_visited) and not             inheritance_right.in_list(nodes_border):
                nodes_border.append(inheritance_right)
                
            node.set_inheritance([inheritance_left, inheritance_center, inheritance_right])
            

#Happy ending
            
