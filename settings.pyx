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
        self.gpSettings['runs'] = 20 
        self.gpSettings['penalty'] = 1
        self.gpSettings['maxSize'] = 300
        self.gpSettings['fitness'] = 'maxEccen'
        #variation node
        self.nodeSettings['randSubset'] = {'num':{'value':0,'range':(1,50),'type':'int'}}

        self.nodeSettings['pSelect'] = {'p':{'value':0.0,'range':(0,1),'type':'float'}}
        self.nodeSettings['kTourn'] = {'k':{'value':0,'range':(1,50),'type':'int'},'num':{'value':0,'range':(1,50),'type':'int'},'opt':{'value':"",'range':['max','min'],'type':'choice'},'val':{'value':"",'range':['degree'],'type':'choice'}}

        self.nodeSettings['trunc'] = {'num':{'value':0,'range':(1,50),'type':'int'},'opt':{'value':"",'range':['max','min'],'type':'choice'},'val':{'value':"",'range':['degree'],'type':'choice'}}
       
        self.nodeSettings['relRandSubset'] = {'relNum':{'value':0,'range':(1,50),'type':'int'}}

        self.nodeSettings['relKTourn'] = {'relK':{'value':0,'range':(1,50),'type':'int'},'relNum':{'value':0,'range':(1,50),'type':'int'},'opt':{'value':"",'range':['max','min'],'type':'choice'},'val':{'value':"",'range':['degree'],'type':'choice'}}
        
        self.nodeSettings['relTrunc'] = {'relNum':{'value':0,'range':(1,50),'type':'int'},'opt':{'value':"",'range':['max','min'],'type':'choice'},'val':{'value':"",'range':['degree'],'type':'choice'}}
        
        if filename:
            f = open(filename)
            d = eval(f.read())
            for key in d['nodeSettings']:
                self.nodeSettings[key] = d['nodeSettings'][key]
            for key in d['gpSettings']:            
                self.gpSettings[key] = d['gpSettings'][key]

            self.probConf = d['problems']
        else:
            self.probConf.append({'parts':2})



        self.solSettings = self.probConf[0]

    def nextProbConf(self):
        x = self.probConf[0]
        self.probConf = self.probConf[1:]
        self.probConf.append(x)
        self.solSettings = self.probConf[0]
        





