#Script template copied by @sherwingquiroz from "Inteligencia Artificial" by Alberto Garcia Serrano
#Node

class Node:

    def __init__(self, data, inheritance=None):
        self.data = data
        self.inheritance = None
        self.ancestor = None
        self.cost = None
        self.set_inheritance(inheritance)
        
    def set_inheritance(self, inheritance):
        self.inheritance = inheritance
        if self.inheritance != None:
            for h in self.inheritance:
                h.ancestor = self
                
    def get_inheritance(self):
        return self.inheritance
        
    def get_ancestor(self):
        return self.ancestor
        
    def set_ancestor(self, ancestor):
        self.ancestor = ancestor
        
    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data
        
    def set_cost(self, cost):
        self.cost = cost
        
    def get_cost(self):
        return self.cost
        
    def equal(self, node):
        if self.get_data() == node.get_data():
            return True
        else:
            return False
            
    def in_list(self, list_node):
        listed = False
        for n in list_node:
            if self.equal(n):
                listed = True
        return listed
        
    def __str__(self):
        return str(self.get_data())
        
#End of File?
