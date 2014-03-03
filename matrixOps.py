import random
import genNode
import funcs
import copy


class multiply(genNode.node):

    def __init__(self,parent,settings):
        super(multiply,self).__init__(parent,settings,funcs.mutate,"multiply",2,{})

    def toDict(self):
        return {"multiply":[self.down[0].toDict(),self.down[1].toDict()]}

class inverse(genNode.node):
    def __init__(self,parent,settings):
        super(inverse,self).__init__(parent,settings,funcs.mutate,"inverse",1,{})

    def toDict(self):
        return {"inverse":[self.down[0].toDict()]}

class transpose(genNode.node):
    def __init__(self,parent,settings):
        super(transpose,self).__init__(parent,settings,funcs.mutate,"transpose",1,{})

    def toDict(self):
        return {"transpose":[self.down[0].toDict()]}

class scalarMult(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['scalarMult'])
        super(scalarMult,self).__init__(parent,settings,funcs.mutate,"scalarMult",1,p)

    def toDict(self):
        return {"scalarMult":[self.down[0].toDict()]}




nodes = [multiply,inverse,transpose,scalarMult]


