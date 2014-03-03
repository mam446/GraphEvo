# cython: profile=True
import numpy as np


class adjacency(genNode.node):
    def __init__(self,parent,settings):
        super(termNode,self).__init__(parent,settings,None,"Adj",0,{})

    def evaluate(self):
        return state.adj


    def update(self,depth,state):
        self.depth = depth
        self.height = 0
        self.state = state
        return self.height


    def randomize(self,state):
        return 

    def toDict(self):
        return "Adj"


class degree(genNode.node):
    def __init__(self,parent,settings):
        super(termNode,self).__init__(parent,settings,None,"Deg",0,{})

    def evaluate(self):
        return state.deg


    def update(self,depth,state):
        self.depth = depth
        self.height = 0
        self.state = state
        return self.height


    def randomize(self,state):
        return 

    def toDict(self):
        return "Deg"



class identity(genNode.node):
    def __init__(self,parent,settings):
        super(termNode,self).__init__(parent,settings,None,"I",0,{})

    def evaluate(self):
        return np.identity(self.state.numNodes)


    def update(self,depth,state):
        self.depth = depth
        self.height = 0
        self.state = state
        return self.height


    def randomize(self,state):
        return 

    def toDict(self):
        return "I"

nodes = [adjacency,degree,identity]
