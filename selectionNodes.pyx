
import random
import genNode
import funcs
import copy


class pSelect(genNode.node):
    def __init__(self,parent,settings):
        p= copy.deepcopy(settings.nodeSettings['pSelect'])
        super(pSelect,self).__init__(parent,settings,funcs.pSelect,"pSelect",1,p)

    def toDict(self):
        return {"pSelect(p="+str(self.params['p']['value'])+")":[self.down[0].toDict()]}

class kTourn(genNode.node):
    def __init__(self,parent,settings):
        p= copy.deepcopy(settings.nodeSettings['kTourn'])
        super(kTourn,self).__init__(parent,settings,funcs.kTourn,"kTourn",1,p)

    def evaluate(self):
        
        self.params['data'] = self.state.calcDegree()
        return super(kTourn,self).evaluate()

    def toDict(self):
        return {"kTourn("+self.params['opt']['value']+" "+self.params['val']['value']+",k="+str(self.params['k']['value'])+",num="+str(self.params['num']['value'])+")":[self.down[0].toDict()]}


class relKTourn(genNode.node):
    def __init__(self,parent,settings):
        p= copy.deepcopy(settings.nodeSettings['relKTourn'])
        super(relKTourn,self).__init__(parent,settings,funcs.relKTourn,"relKTourn",1,p)

    def evaluate(self):
        
        self.params['data'] = self.state.calcDegree()
        return super(relKTourn,self).evaluate()

    def toDict(self):
        return {"relKTourn("+self.params['opt']['value']+" "+self.params['val']['value']+",relK="+str(self.params['relK']['value'])+",relNum="+str(self.params['relNum']['value'])+")":[self.down[0].toDict()]}




class randSubset(genNode.node):
    def __init__(self,parent,settings):
        p= copy.deepcopy(settings.nodeSettings['randSubset'])
        super(randSubset,self).__init__(parent,settings,funcs.randSubset,"randSubset",1,p)

    def toDict(self):
        return {"randSubset(num="+str(self.params['num']['value'])+")":[self.down[0].toDict()]}


class relRandSubset(genNode.node):
    def __init__(self,parent,settings):
        p= copy.deepcopy(settings.nodeSettings['relRandSubset'])
        super(relRandSubset,self).__init__(parent,settings,funcs.relRandSubset,"relRandSubset",1,p)

    def evaluate(self):
        
        self.params['data'] = self.state.calcDegree()
        return super(relRandSubset,self).evaluate()
    
    
    def toDict(self):
        return {"relRandSubset(relNum="+str(self.params['relNum']['value'])+")":[self.down[0].toDict()]}




class trunc(genNode.node):
    def __init__(self,parent,settings):
        p= copy.deepcopy(settings.nodeSettings['trunc'])
        super(trunc,self).__init__(parent,settings,funcs.trunc,"trunc",1,p)

    def evaluate(self):
        self.params['data'] = self.state.calcDegree()
        return super(trunc,self).evaluate()

    def toDict(self):
        return {"trunc("+self.params['opt']['value']+" "+self.params['val']['value']+",num="+str(self.params['num']['value'])+")":[self.down[0].toDict()]}



class relTrunc(genNode.node):
    def __init__(self,parent,settings):
        p= copy.deepcopy(settings.nodeSettings['relTrunc'])
        super(relTrunc,self).__init__(parent,settings,funcs.relTrunc,"relTrunc",1,p)

    def evaluate(self):
        self.params['data'] = self.state.calcDegree()
        return super(relTrunc,self).evaluate()

    def toDict(self):
        return {"relTrunc("+self.params['opt']['value']+" "+self.params['val']['value']+",relNum="+str(self.params['relNum']['value'])+")":[self.down[0].toDict()]}



nodes = [pSelect,kTourn,randSubset,trunc,relKTourn,relRandSubset,relTrunc]


