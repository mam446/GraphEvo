import termNodes

class state:
    def __init__(self,settings):
        self.terms = termNodes.nodes
        self.settings = settings
        self.adj = settings.getAdj()
        self.deg = settings.getDeg()

        self.numNodes = len(self.deg)
