#Flights Depth First Search Iterative
from Node import Node

def Flights_DFS_Iter(node, target):
    for limit in range(0, 100):
        visited = []
        tgt = DFS_Rec(node, target, vidited, limit)
        if tgt != None:
            return tgt
            
def DFS_Rec(node, target, visited, limit):
    if limit > 0:
        visited.append(node)
        if node.get_data() == target:
            return node
            
        else:
        #Expand nodes_inheritance
        data_node = node.get_data()
        list_inheritance = []
        for a_inheritance in linkedin[data_node]:
            inheritance = Node(a_inheritance)
            if not inheritance.in_list(visited):
                list_inheritance.append(inheritance)
                
        node.set_inheritance(list_inheritance)
        
        for node_inheritance in node.get_inheritance():
            if not node_inheritance.get_data() in visited:
                #Call recursive
                tgt = DFS_Rec(node_inheritance, target, visited, limit-1)
                if tgt != None:
                    return tgt
                    
        return None
