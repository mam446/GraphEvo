# cython: profile=True
import numpy as np
import copy
import genNode


class allNodes(genNode.node):
    def __init__(self,parent,settings):
        super(allNodes,self).__init__(parent,settings,None,"allNodes",0,{})

    def evaluate(self):
        return set(range(len(self.state.nodeList)))

    
    def update(self,depth,state):
        self.depth = depth
        self.height = 0
        self.state = state
        return self.height

    def randomize(self):
        return 
    
    def toDict(self):
        return "allNodes"

class empty(genNode.node):
    def __init__(self,parent,settings):
        super(empty,self).__init__(parent,settings,None,"empty",0,{})

    def evaluate(self):
        return set()

    
    def update(self,depth,state):
        self.depth = depth
        self.height = 0
        self.state = state
        return self.height

    def randomize(self):
        return 
    
    def toDict(self):
        return "empty"

nodes = [allNodes,empty]
