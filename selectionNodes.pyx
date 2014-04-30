
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

class randSubset(genNode.node):
    def __init__(self,parent,settings):
        p= copy.deepcopy(settings.nodeSettings['randSubset'])
        super(randSubset,self).__init__(parent,settings,funcs.randSubset,"randSubset",1,p)

    def toDict(self):
        return {"randSubset(num="+str(self.params['num']['value'])+")":[self.down[0].toDict()]}


class trunc(genNode.node):
    def __init__(self,parent,settings):
        p= copy.deepcopy(settings.nodeSettings['trunc'])
        super(trunc,self).__init__(parent,settings,funcs.trunc,"trunc",1,p)

    def evaluate(self):
        
        self.params['data'] = self.state.calcDegree()
        return super(trunc,self).evaluate()

    def toDict(self):
        return {"trunc("+self.params['opt']['value']+" "+self.params['val']['value']+",num="+str(self.params['num']['value'])+")":[self.down[0].toDict()]}






nodes = [pSelect,kTourn,randSubset,trunc]


