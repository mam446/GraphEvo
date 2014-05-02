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
import math
import subprocess
import fitnessFunction

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

        self.fit = 0.0
        self.settings = settings

        self.state = state.state(settings)


        self.createRandom()

    def duplicate(self):
        x =copy.deepcopy(self)

        global label
        x.name = str(label)
        label+=1

        x.fit = 0.0
        x.update()
        return x

    def createER(self):
        self.root = selectionNodes.pSelect(None,self.settings)
        self.root.down = [termNodes.allNodes(self.root,self.settings)]
        self.root.params['p']['value'] = .01
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
        self.fit = 0.0
        data = []
        for i in xrange(self.settings.gpSettings['runs']):
            for j in xrange(self.settings.gpSettings['maxSize']):
                add = self.root.evaluate()
                self.state.addNode(add)
            #self.fit+=self.assortativityEval()
            self.fit+=fitnessFunction.funcs[self.settings.gpSettings['fitness']](self.state)
            data.extend(self.state.calcDegree())
            self.state.reset()
        
        self.fit/=self.settings.gpSettings['runs']
        self.fit-=self.size*self.settings.gpSettings['penalty']
        
        return self.fit

    def assortativityEval(self):
        G = nx.Graph()
        for node in xrange(len(self.state.nodeList)):
            G.add_node(node)
            for edge in self.state.nodeList[node]:
                G.add_edge(node,edge)
        if nx.is_biconnected(G):
          
            r = nx.degree_assortativity_coefficient(G)
            if not math.isnan(r):
                return 5*abs(r)
        if nx.is_connected(G):
            r = nx.degree_assortativity_coefficient(G)
            if not math.isnan(r):
                return abs(r)

        return -99999999999999999


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
            return -50*float(edgecuts)+G.number_of_edges()#nx.radius(G)
        return -99999999999999999


    def report(self,plot=False):
        data = []
        for i in xrange(self.settings.gpSettings['runs']):
            self.state.reset()
            for j in xrange(self.settings.gpSettings['maxSize']):
                add = self.root.evaluate()
                self.state.addNode(add)
            data.extend(self.state.calcDegree())
        
        G = nx.Graph()
        for node in xrange(len(self.state.nodeList)):
            G.add_node(node)
            for edge in self.state.nodeList[node]:
                G.add_edge(node,edge)
        nx.write_dot(G,self.name+".dot")
        X = pgv.AGraph(self.name+".dot") 
        X.node_attr.update(color='gray')
        X.layout(prog='neato',args="-Goverlap=false -Gscale=.01")
        X.draw(self.name+".svg") 
        if plot:
            n,bins,patches = pylab.hist(data,1+max(data)-min(data),histtype='stepfilled')
            pylab.setp(patches,'facecolor','g','alpha',0.75)
            print n
            print bins
            print patches
            pylab.ylim([0,max(n)])
            pylab.show()
        self.makeGraph()
        return self.fit


    def makeProg(self):
        tab = "    "
        indent = tab*1

        prog = "from funcs import *\n\n"
        prog+="\n\n\n"+str(self.toDict())+"\n\n\n"
        prog+="fitness = "+str(self.fit)+"\n"
        prog+="size = "+str(self.size)+"\n\n\n"
        
        
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
        n = x.randomNode()
        
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
            print "root"
            y.root = xn

        if xp is not None:
            if xn ==xp.down[0]:
                xp.down[0] = yn
            else:
                xp.down[1] = yn
        else:
            print "root"
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
        p = {}
        i = 0
        if not inc:
            n = random.choice(z)
            return n 
        
        while not p:
            n = random.choice(z)
            p = n.params
            if i> len(z):
                return None
            i+=1 
        return n






    def __gt__(self,other):
        return self.fit>other.fit


    def altMutate(self):
        x = self.duplicate()
        t = None
        i = 0
        while not t:
            n =x.randomNode(True)
            if not n:
                return None
            t = n.params
            i+=1
            if i> self.size:
                return None 
        n.randomize()
        x.update()        
        return x


    def makeGraph(self):
        val = 'x'
        s = 'strict digraph { \n ordering=out; node[label=\"\\N\"];\n '
        s+=getEdge(self.root,val)
        s+="\n}"
        f = open(self.name+'.dot','w')
        f.write(s)
        f.close()
        subprocess.call(['dot','-Tpng',self.name+'.dot','-o',self.name+'.png'])

        return


def getEdge(node,val):
    s = ""
    if not node.parent:
        s+= val+"  [color=goldenrod2,\n label = \""+node.toStr()+"\",\n style=filled];"

    for i in xrange(len(node.down)):
        s+= val+str(i+1)+"   [color=goldenrod2,\n  label =\""+node.down[i].toStr()+"\",\n style=filled];\n"
        s+="  "+val+" -> "+val+str(i+1)+';\n'
        s+=getEdge(node.down[i],val+str(i+1))
    return s









