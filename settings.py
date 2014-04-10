# cython: profile=True
import numpy as np





class runSettings:
    def __init__(self,filename = None):

        self.gpSettings = {}

        self.seed = None

        self.nodeSettings = {}
        
        self.solSettings = {}
        
        self.probConf = []


        self.gpSettings['maxStartNodes'] = 15            
        self.gpSettings['maxDepth'] = 5
        self.gpSettings['mutateMax'] = 5
        self.gpSettings['runs'] = 5
        self.gpSettings['penalty'] = .001
        #variation node
        self.nodeSettings['scalarMult'] = {'scalar':{'value':0.0,'range':(-50.0,50.0),'type':'float'}}

        
        if filename:
            f = open(filename)
            d = eval(f.read())
            for key in d['nodeSettings']:
                self.nodeSettings[key] = d['nodeSettings'][key]
            for key in d['gpSettings']:            
                self.gpSettings[key] = d['gpSettings'][key]

            self.probConf = d['problems']
        else:
            self.probConf.append({'adj':np.matrix([[0,1,1],[1,0,0],[1,0,0]]),'deg':np.matrix([[2,0,0],[0,1,0],[0,0,1]]),'solution':5})



        self.solSettings = self.probConf[0]

    def nextProbConf(self):
        x = self.probConf[0]
        self.probConf = self.probConf[1:]
        self.probConf.append(x)
        self.solSettings = self.probConf[0]
        

    def getAdj(self):
        return self.solSettings['adj']


    def getDeg(self):
        return self.solSettings['deg']




