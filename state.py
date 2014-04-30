import termNodes

class state:
    def __init__(self,settings=None):
        self.terms = termNodes.nodes
        self.settings = settings
        self.nodeList = []

        self.degreeList = []

    def addNode(self,nodes):
        self.nodeList.append(list(nodes))
        for n in nodes:
            self.nodeList[n].append(len(self.nodeList)-1)
    
    def add2Node(self,nodes,j):
        self.nodeList[j] = nodes 

    def bigGraph(self,size):
        self.nodeList=[[] for i in xrange(size)]
    

    def calcDegree(self):
        x = map(len,self.nodeList)
        self.degreeList = x
        return x


    def reset(self):
        self.nodeList = []


