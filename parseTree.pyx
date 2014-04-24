import pylab
import copy
import random
import selectionNodes
import setNodes
import termNodes
import state
import settings
import numpy
import metis
import networkx as nx
import pygraphviz as pgv


global label
label =0






nodes = []


nodes.extend(selectionNodes.nodes)
nodes.extend(setNodes.nodes)


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

    def createER(self):
        self.root = selectionNodes.pSelect(None,self.settings)
        self.root.down = [termNodes.allNodes(self.root,self.settings)]
        self.root.params['p']['value'] = .001
        self.update()
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

    def eval2(self):
        data = []
        for i in xrange(self.settings.gpSettings['runs']):
            self.state.bigGraph(self.settings.gpSettings['maxSize'])
            for j in xrange(self.settings.gpSettings['maxSize']):
                add = self.root.evaluate()
                self.state.add2Node(add,j)
            self.fit+=self.metisEval()
            data.extend(self.state.calcDegree())
            self.state.reset()
        
        self.fit/=self.settings.gpSettings['runs']
        self.fit-=self.size*self.settings.gpSettings['penalty']
        return self.fit

    def evaluate(self):
        cdef int i,j
        self.fit = 0
        data = []
        for i in xrange(self.settings.gpSettings['runs']):
            for j in xrange(self.settings.gpSettings['maxSize']):
                add = self.root.evaluate()
                self.state.addNode(add)
            self.fit+=self.metisEval()
            data.extend(self.state.calcDegree())
            self.state.reset()
        
        self.fit/=self.settings.gpSettings['runs']
        self.fit-=self.size*self.settings.gpSettings['penalty']
        
        return self.fit


    def metisEval(self):
        G = nx.Graph()
        for node in xrange(len(self.state.nodeList)):
            G.add_node(node)
            for edge in self.state.nodeList[node]:
                G.add_edge(node,edge)
        (edgecuts, parts) = metis.part_graph(G,self.settings.solSettings['parts'])
        mod = 0
        if nx.is_connected(G):
            mod = 1
            return float(edgecuts)-G.number_of_edges()
        return -99999999999999999


    def report(self,plot=False):
        self.fit = 0
        data = []
        for i in xrange(self.settings.gpSettings['runs']):
            self.state.reset()
            for j in xrange(self.settings.gpSettings['maxSize']):
                add = self.root.evaluate()
                self.state.addNode(add)
            data.extend(self.state.calcDegree())
        self.fit=numpy.std(data) 
        
        n,bins,patches = pylab.hist(data,1+max(data)-min(data),histtype='stepfilled')
        pylab.setp(patches,'facecolor','g','alpha',0.75)
        print n
        print bins
        print patches
        pylab.ylim([0,max(n)])
        G = nx.Graph()
        for node in xrange(len(self.state.nodeList)):
            G.add_node(node)
            for edge in self.state.nodeList[node]:
                G.add_edge(node,edge)
        nx.write_dot(G,self.name+".dot")
        X = pgv.AGraph(self.name+".dot") 
        X.layout(prog='neato',args="-Goverlap=false -Gscale=.01")
        X.draw(self.name+".png") 
        if plot:
            pylab.show()
        return self.fit


    def makeProg(self):
        tab = "    "
        indent = tab*1

        prog = "\n\n"
        prog+= "def selectNodes(state):\n"+indent
        prog+=self.root.makeProg(1,"")
        prog+="return x\n"+indent
        f = open(self.name+"-prog.py",'w+')
        f.write(prog)
        f.close()

    def update(self):
        self.state = state.state(self.settings)
        self.depth = self.root.update(0,self.state)

    def toStr(self):
        return str(self.root.toDict())

    def toDict(self):
        return self.root.toDict()

    def mutate(self):
        x = self.duplicate()
        n = x.randomNode(True)
        
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
        popNodes(self.root,z)
        n = random.choice(z)
        return n






    def __gt__(self,other):
        return self.fit>other.fit


    def altMutate(self):
        x = self.duplicate()
        t = None
        i = 0
        while not t:
            n =x.randomNode(True)
            t = n.params
            i+=1
            if i> self.size:
                n = self.root
                break
        n.randomize()
        
        return x

