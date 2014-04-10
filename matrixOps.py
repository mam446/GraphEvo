
import random
import genNode
import funcs
import copy

class add(genNode.node):

    def __init__(self,parent,settings):
        super(add,self).__init__(parent,settings,funcs.add,"add",2,{})

    def toDict(self):
        return {"add":[self.down[0].toDict(),self.down[1].toDict()]}

class multiply(genNode.node):

    def __init__(self,parent,settings):
        super(multiply,self).__init__(parent,settings,funcs.multiply,"multiply",2,{})

    def toDict(self):
        return {"multiply":[self.down[0].toDict(),self.down[1].toDict()]}

class inverse(genNode.node):
    def __init__(self,parent,settings):
        super(inverse,self).__init__(parent,settings,funcs.inverse,"inverse",1,{})

    def evaluate(self):
        d = self.down[0].evaluate()
        try:
            super(inverse,self).evaluate(d)
        except :
            return d

    def toDict(self):
        return {"inverse":[self.down[0].toDict()]}

class transpose(genNode.node):
    def __init__(self,parent,settings):
        super(transpose,self).__init__(parent,settings,funcs.transpose,"transpose",1,{})

    def toDict(self):
        return {"transpose":[self.down[0].toDict()]}

class scalarMult(genNode.node):
    def __init__(self,parent,settings):
        p = copy.deepcopy(settings.nodeSettings['scalarMult'])
        super(scalarMult,self).__init__(parent,settings,funcs.scalarMult,"scalarMult",1,p)

    def toDict(self):
        return {"scalarMult(scalar="+str(self.params['scalar']['value'])+")":[self.down[0].toDict()]}




nodes = [multiply,inverse,transpose,scalarMult,add]


