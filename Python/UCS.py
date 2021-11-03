#Uniform Cost Search
from Node import Node

def contrast (x, y):
            return x.get_cost() - y.get_cost()
            
def UCS(linkedin, init_state, target):
    targeting = False
    nodes_visited = []
    nodes_border = []
    node_init = Node(init_state)
    node_init.set_cost(0)
    nodes_border.append(node_init)
    
    while (not targeting) and len(nodes_border) != 0:
        #Command the list nodes_border
        nodes_border = sorted(nodes_border, cmp = contrast)
        node = nodes_border[0]
        
        #Extract node and add in visited
        nodes_visited.append(nodes_border.pop(0))
        if node.get_data() == target:
            #Find answer
            targeting = True
            return node
            
        else:
            #Expand nodes_inheritance
            data_node = node.get_data()
            list_inheritance = []
            for a_inheritance in linkedin[data_node]:
                inheritance = Node(a_inheritance)
                cost = linkedin[data_node][a_inheritance]
                inheritance.set_cost(node.get_cost() + cost)
                list_inheritance.append(inheritance)
                if not inheritance.in_list(nodes_visited):
                    #
                    #
                    if inheritance.in_list(nodes_border):
                        for n in nodes_border:
                            if n.equal(inheritance) and n.get_cost() > inheritance.get_cost():
                                nodes_border.remove(n)
                                nodes_border.appnd(inheritance)
                                
                    else:
                        nodes_border.append(inheritance)
                        node.set_inheritance(list_inheritance)
                        
