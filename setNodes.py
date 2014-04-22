import random
import genNode
import funcs
import copy



class union(genNode.node):
    def __init__(self,parent,settings):
        super(union,self).__init__(parent,settings,funcs.union,"union",2,{})

    def toDict(self):
        return {"union":[self.down[0].toDict(),self.down[1].toDict()]}

class intersection(genNode.node):
    def __init__(self,parent,settings):
        super(intersection,self).__init__(parent,settings,funcs.intersection,"intersection",2,{})

    def toDict(self):
        return {"intersection":[self.down[0].toDict(),self.down[1].toDict()]}

class difference(genNode.node):
    def __init__(self,parent,settings):
        super(difference,self).__init__(parent,settings,funcs.difference,"difference",2,{})

    def toDict(self):
        return {"difference":[self.down[0].toDict(),self.down[1].toDict()]}

nodes = [union,intersection,difference]






