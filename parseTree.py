
import copy
import random
import matrixOps
import termNodes
import state
import settings






global label
label =0







nodes = []

nodes.extend(matrixOps.nodes)





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


        self.createRandom()



    def createRandom(self,start = None):

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
        return self.root.evaluate()


    def update(self):
        self.depth = self.root.update(0,self.state)

    def toDict(self):
        return self.root.toDict()





















