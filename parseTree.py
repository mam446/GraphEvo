
import copy
import random
import matrixOps
import graphOps
import reducerOps
import graphReducerOps
import termNodes
import state
import settings






global label
label =0






reducers = []
nodes = []

reducers.extend(reducerOps.nodes)
reducers.extend(graphReducerOps.nodes)

nodes.extend(matrixOps.nodes)
nodes.extend(graphOps.nodes)


def popNodes(node,a):
    if node.down:
        a.append(node)
    for x in node.down:
        popNodes(x,a)




class parseTree:
    
    def __init__(self,settings):
        self.root = None
        self.depth = 0
        self.size = 0

        global label
        self.name = str(label)
        label+=1


        self.fitness = 0.0
        self.settings = settings

        self.state = state.state(settings)

        self.fit = 0

        self.createRandom()

    def duplicate(self):
        x =copy.deepcopy(self)

        global label
        x.name = str(label)
        label+=1

        x.fitness = 0
        x.update()
        return x

    def createRandom(self,start = None):
        if not start:
            self.reducer = random.choice(reducers)
        size = random.randint(1,self.settings.gpSettings['maxStartNodes'])
        if start ==None:
            start = self.root
        else:
            size = random.randint(1,self.settings.gpSettings['mutateMax'])
            for s in xrange(len(start.down)):
                start.down[s]= None
        for i in xrange(size):
            if not start:
                node = random.choice(nodes)
                start = node(None,self.settings)
                start.randomize()
                continue
            nex = None
            cur = start
            while cur:
                nex = random.choice(cur.down)
                if not nex:
                    break
                cur = nex

            n = random.randrange(0,len(cur.down))
            while cur.down[n]!=nex:
                n = random.randrange(0,len(cur.down))
            node = random.choice(nodes)
            cur.down[n] = node(cur,self.settings)
            cur.down[n].randomize()
        start.fillTerms(self.state.terms)
        if self.root ==None:
            self.root = start
        self.update()
        self.count()
        return

       
    def count(self):
        self.size = self.root.count()
    
    def fillTerms(self):
        self.root.fillTerms(self.state)     


    def evaluate(self):
        for prob in self.settings.probConf:
            self.fit+=(prob['solution']-self.reducer(self.root.evaluate()))**2
            self.update()
            self.settings.nextProbConf() 
        self.fit = self.fit**(.5)+ self.settings.gpSettings['penalty']*self.size
        return self.fit


    def update(self):
        self.state = state.state(self.settings)
        self.depth = self.root.update(0,self.state)

    def toStr(self):
        return str(self.reducer)+str(self.root.toDict())

    def toDict(self):
        return {str(self.reducer):self.root.toDict()}

    def mutate(self):
        x = self.duplicate()
        n = x.randomNode(True)
        
        while n!="reducer" and not n.down:
            n = x.randomNode()
        
        if n=="reducer":
            x.reducer = random.choice(reducers)
            x.update()
            x.count()
            return x
        x.createRandom(n)
        x.update()
        x.count()
        return x

    def mate(self,other):
        x = self.duplicate()
        y = other.duplicate()

        xn = x.randomNode()
        yn = y.randomNode()

        xp = xn.parent
        yp = yn.parent

        if yp is not None:
            if yn==yp.down[0]:
                yp.down[0]=xn
            else:
                yp.down[1] = xn
        else:
            y.root = xn

        if xp is not None:
            if xn ==xp.down[0]:
                xp.down[0] = yn
            else:
                xp.down[1] = yn
        else:
            x.root = yn

        xn.parent = yp
        yn.parent = xp
        x.update()
        y.update()
        x.count()
        y.count()
        return x,y


    def randomNode(self,inc=False):
        z = []
        if inc:
            z.append("reducer")
        popNodes(self.root,z)
        n = random.choice(z)
        return n






    def __gt__(self,other):
        return self.fit>other.fit



