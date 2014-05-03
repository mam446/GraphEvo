import sys
import state
import fitnessFunction
import analysis
import pylab
import networkx as nx
import argparse
from random import choice

parser = argparse.ArgumentParser()
parser.add_argument('program', metavar='path/to/programName', help='name of the program to evaluate')
parser.add_argument('runs', default=30, help='number of runs to perform', type=int)
parser.add_argument('size', default=300, help='number of nodes in generated graphs', type=int)
parser.add_argument('evaluator', default='minMetis', help='name of fitness evaluation method')
parser.add_argument('-c', '--compare', default='gnm', metavar='randomGraphName', help='compare to specified random graph')
args = parser.parse_args()

if args.program.find('/') != -1:
    sys.path.append(args.program[:args.program.rfind('/')+1])
plug = __import__(args.program[args.program.rfind('/')+1:])

degreeData= []
compDegreeData = []

aveEdgeCut = 0.0
compAveEdgeCut = 0.0

edges = 0.0
compEdges = 0.0

fitness = 0.0
compFitness = 0.0

s = None
for i in xrange(args.runs):
    s = state.state()

    for j in xrange(args.size):
        add = plug.selectNodes(s)
        s.addNode(add)
    fitness+=fitnessFunction.funcs[args.evaluator](s)
    degreeData .extend(s.calcDegree())
    aveEdgeCut+=analysis.edgeCut(s)
    numEdges = analysis.edges(s)
    edges+=numEdges

    # Compare to random graph model
    if args.compare:
        if args.compare == 'gnm':
            randomGraph = nx.gnm_random_graph(args.size, numEdges)
        else: # Stay tuned for more!
            randomGraph = nx.gnm_random_graph(args.size, numEdges)
        while not nx.is_connected(randomGraph): # Have to add edges to connect the graph
            components = nx.connected_components(randomGraph)
            randomGraph.add_edge(choice(components[0]), choice(components[1]))
        compFitness += fitnessFunction.funcs[args.evaluator](randomGraph)
        compDegreeData.extend(nx.degree(randomGraph).values())
        compAveEdgeCut += analysis.edgeCut(randomGraph)
        compEdges += numEdges

edges/=args.runs
fitness/=args.runs
aveEdgeCut/=args.runs
aveDegree = sum(degreeData)/float(len(degreeData))

print "Evolved Program"
print "Nodes: ",args.size
print "Fitness: ",fitness
print "EdgeCut: ",aveEdgeCut
print "Edges: ", edges
print "Ave Degree: ",aveDegree
print
n,bins,patches = pylab.hist(degreeData,1+max(degreeData)-min(degreeData),histtype='stepfilled')
pylab.setp(patches,'facecolor','g','alpha',0.75)
pylab.ylim([0,max(n)])
pylab.show()

if args.compare:
    compEdges /= args.runs
    compFitness /= args.runs
    compAveEdgeCut /= args.runs
    compAveDegree = sum(compDegreeData)/float(len(compDegreeData))

    print "Random Graph Comparison"
    print "Nodes: ",args.size
    print "Fitness: ",compFitness
    print "EdgeCut: ",compAveEdgeCut
    print "Edges: ", compEdges
    print "Ave Degree: ",compAveDegree
    print
    n,bins,patches = pylab.hist(compDegreeData,1+max(compDegreeData)-min(compDegreeData),histtype='stepfilled')
    pylab.setp(patches,'facecolor','g','alpha',0.75)
    pylab.ylim([0,max(n)])
    pylab.show()

