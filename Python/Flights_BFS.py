#Flights Breadth First Search
from Node import Node

def Flights_BFS(linkedin, init_state, target):
    targeting = False
    nodes_visited = []
    nodes_border = []
    
    nodeInit = Node(init_state)
    nodes_border.append(nodeInit)
    
    while (not targeting) and len(nodes_border) != 0:
        node = nodes_border[0]
        #Extract nodes and append to visited
        nodes_visited.append(nodes_border.pop(0))
        if node.get_data() == target:
            #targeting finded
            targeting = True
            return node
            
        else:
            #expand nodes_inheritance
            data_node = node.get_data()
            list_inheritance = []
            for a_inheritance in linkedin[data_node]:
                inheritance = Node(a_inheritance)
                list_inheritance.append(inheritance)
                
                if not inheritance.in_list(nodes_visited) and not inheritance.in_list(nodes_border):
                    nodes_border.append(inheritance)
                    
            node.set_inheritance(list_inheritance)
                    
