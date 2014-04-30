
# cython: profile=True
import random


class node(object):

    def __init__(self,parent,settings,func,name,children=0,params={}):
        self.depth = 0
        self.height = 0


        self.settings = settings
    
        self.function = func
        self.name = name
    
        self.params = params

        self.parent = parent
        if parent:
            self.depth = self.parent.depth+1
        self.down = [None for i in xrange(children)]
        
        self.state = None
        if parent:
            self.state = self.parent.state
    
    
    def evaluate(self):
        rDown = []
        for d in self.down:
            rDown.append(d.evaluate())
        return self.function(rDown,self.params)
    
    def update(self,depth,state):
        d = [i.update(depth+1,state) for i in self.down]
        d.append(-1)
        self.depth = depth
        self.height = max(d)+1
        self.state = state
        return self.height

    def randomize(self):
        for p in self.params:
            if p=='data':
                continue
            if self.params[p]['type'] == 'int':
                self.params[p]['value'] =  random.randint(self.params[p]['range'][0],self.params[p]['range'][1])
            elif self.params[p]['type'] == 'float':
                self.params[p]['value'] = random.random()*(self.params[p]['range'][1]-self.params[p]['range'][0])+self.params[p]['range'][0]
            elif self.params[p]['type']== 'choice':
                self.params[p]['value'] = random.choice(self.params[p]['range'])
            else:
                raise "Error: No type"

    def toStr(self):
        s = self.name+"\\n"
        for p in self.params:
            if p=='data':
                continue
            s+=p+": "+str(self.params[p]['value'])+"\\n"
        return s


    def fillTerms(self,terms):
        for i in xrange(len(self.down)):
            if self.down[i]:
                self.down[i].fillTerms(terms)
            else:
                self.down[i] = random.choice(terms)(self,self.settings)
                self.down[i].randomize()

    def count(self):
        t = 1 
        for d in self.down:
            t+=d.count()
        return t


    def makeProg(self,numTab,var):
        tab = "    "
        indent = ""
        for i in xrange(numTab):
            indent+=tab
        prog = ""
        dList = "["
        for d in xrange(len(self.down)):
            prog+=self.down[d].makeProg(numTab,var+str(d))
            dList+="x"+var+str(d)+","
        if self.name!="randInd":
            dList = dList[:-1]+"]"
        else:
            dList = '[],sol'
        pList = "{"
        for p in self.params:
            if p=='weight':
                continue
            if p=='data':
                pList+="\'data\':state.calcDegree(),"
                continue
            if self.params[p]['type']=='choice':
                pList+="\'"+p+"\':{'value':\'"+self.params[p]['value']+"\'},"
                continue
            pList+="\'"+p+"\':{'value':"+str(self.params[p]['value'])+"},"
        if pList!="{":
            pList = pList[:-1]+"}"
            prog+="x"+var+" = "+self.name+"("+dList+","+pList+")\n"+indent
        else:
            prog+="x"+var+" = "+self.name+"("+dList+")\n"+indent
        return prog
