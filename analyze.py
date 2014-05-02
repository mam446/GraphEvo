import sys
import state
import fitnessFunction
import analysis
import pylab
import matplotlib.pyplot as plt
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

x = range(args.size)
trend_aveDegree = [0 for i in xrange(args.size)]
trend_edges = [0 for i in xrange(args.size)]
trend_edgecut = [0 for i in xrange(args.size)]
trend_connectivity = [0 for i in xrange(args.size)]


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
        if not j:
            continue
        trend_aveDegree[j]+=sum(s.calcDegree())/float(j)
        trend_edges[j]+=analysis.edges(s)
        trend_edgecut[j]+=analysis.edgeCut(s)
        trend_connectivity[j]+=analysis.connected(s)
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

ave = lambda y: y/float(args.runs)

trend_aveDegree = map(ave,trend_aveDegree)
trend_edges = map(ave,trend_edges)
trend_edgecut = map(ave,trend_edgecut)
trend_connectivity = map(ave,trend_connectivity)


ad = open(sys.argv[1][:-4]+"aveDeg.dat",'w')
ed = open(sys.argv[1][:-4]+"edge.dat",'w')
ec = open(sys.argv[1][:-4]+"edgecut.dat",'w')
con = open(sys.argv[1][:-4]+"connect.dat",'w')

for i in xrange(args.size):
    ad.write(str(i)+","+str(trend_aveDegree[i])+"\n")
    ed.write(str(i)+","+str(trend_edges[i])+"\n")
    ec.write(str(i)+","+str(trend_edgecut[i])+"\n")
    con.write(str(i)+","+str(trend_connectivity[i])+"\n")

ad.close()
ed.close()
ec.close()
con.close()






print
print "Evolved Program"
print "Nodes: ",args.size
print "Fitness: ",fitness
print "EdgeCut: ",aveEdgeCut
print "Edges: ", edges
print "Ave Degree: ",aveDegree
print

fig = plt.figure(1)

fig.subplots_adjust(hspace=.5)

ax1 = plt.subplot(321)
plt.plot(x,trend_aveDegree,'k')
ax1.set_title('Average Degree')


ax2 = plt.subplot(322)
plt.plot(x,trend_edges,'k')
ax2.set_title('Edges')

ax3 = plt.subplot(323)
plt.plot(x,trend_edgecut,'k')
ax3.set_title('Edgecut')

ax4 = plt.subplot(324)
plt.plot(x,trend_connectivity,'k')
ax4.set_title('Connectivity Probability')


ax5 = plt.subplot(325)
n,bins,patches = plt.hist(degreeData,1+max(degreeData)-min(degreeData),histtype='stepfilled')
plt.setp(patches,'facecolor','g','alpha',0.75)
plt.ylim([0,max(n)])
ax5.set_title('Degree Distribution')
plt.savefig(sys.argv[1][:-4]+"analysis.png")
plt.show()

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

