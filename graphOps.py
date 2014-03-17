import genNode
import graphFuncs

class largestComp(genNode.node):
    # Find the largest connected component of a graph
    def __init__(self, parent, settings):
        super(largestComp, self).__init__(parent, settings, graphFuncs.largestComp, 'largestComp', 1, {})

    def toDict(self):
        return {'largestComp': [self.down[0].toDict()]}


class maxClique(genNode.node):
    # Find the max clique of a graph
    def __init__(self, parent, settings):
        super(maxClique, self).__init__(parent, settings, graphFuncs.maxClique, 'maxClique', 1, {})

    def toDict(self):
        return {'maxClique': [self.down[0].toDict()]}


class minSpanTree(genNode.node):
    # Find the minimum spanning tree of a graph
    def __init__(self, parent, settings):
        super(minSpanTree, self).__init__(parent, settings, graphFuncs.minSpanTree, 'maxSpanTree', 1, {})

    def toDict(self):
        return {'minSpanTree': [self.down[0].toDict()]}


class complement(genNode.node):
    # Find the complement of a graph
    def __init__(self, parent, settings):
        super(complement, self).__init__(parent, settings, graphFuncs.complement, 'complement', 1, {})

    def toDict(self):
        return {'complement': [self.down[0].toDict()]}


class reverse(genNode.node):
    # Find the reverse of a directed graph
    def __init__(self, parent, settings):
        super(reverse, self).__init__(parent, settings, graphFuncs.reverse, 'reverse', 1, {})

    def toDict(self):
        return {'reverse': [self.down[0].toDict()]}


class compose(genNode.node):
    # Find the composition of two graphs
    def __init__(self, parent, settings):
        super(compose, self).__init__(parent, settings, graphFuncs.compose, 'compose', 2, {})

    def toDict(self):
        return {'compose': [self.down[0].toDict()]}


nodes = [largestComp, maxClique, minSpanTree, complement, reverse, compose]