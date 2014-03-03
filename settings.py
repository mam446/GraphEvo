# cython: profile=True






class runSettings:
    def __init__(self,filename = None):

        self.bbsaSettings = {}

        self.seed = None

        self.nodeSettings = {}
        
        self.solSettings = {}
        
        self.probConf = []


        self.bbsaSettings['maxStartNodes'] = 15            
        self.bbsaSettings['maxDepth'] = 5
        self.bbsaSettings['mutateMax'] = 5
        self.bbsaSettings['runs'] = 5
        self.bbsaSettings['penalty'] = .001
        #variation node
        self.nodeSettings['scalarMult'] = {'scalar':{'value':0.0,'range':(0.0,50.0),'type':'float'}}

        
        if filename:
            f = open(filename)
            d = eval(f.read())
            for key in d['nodeSettings']:
                self.nodeSettings[key] = d['nodeSettings'][key]
            for key in d['bbsaSettings']:            
                self.bbsaSettings[key] = d['bbsaSettings'][key]

            self.probConf = d['problems']


        self.solSettings = self.probConf[0]

    def nextProbConf(self):
        x = self.probConf[0]
        self.probConf = self.probConf[1:]
        self.probConf.append(x)
        self.solSettings = self.probConf[0]
        
