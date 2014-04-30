import sys
import state
import fitnessFunction
import analysis
import pylab
plug = __import__(sys.argv[1])







runs = int(sys.argv[2])
size = int(sys.argv[3])

degreeData= []

aveEdgecut = 0.0


edges = 0.0
fitness = 0.0
s = None
for i in xrange(runs):
    s = state.state()

    for j in xrange(size):
        add = plug.selectNodes(s)
        s.addNode(add)
    fitness+=fitnessFunction.funcs[sys.argv[4]](s)
    degreeData .extend(s.calcDegree())
    aveEdgecut+=analysis.edgeCut(s)
    edges+=analysis.edges(s)

edges/=runs    
fitness/=runs
aveEdgecut/=runs
aveDegree = sum(degreeData)/float(len(degreeData))


print
print "Nodes: ",size
print "Fitness: ",fitness
print "Edgecut: ",aveEdgecut
print "Edges: ", edges
print "Ave Degree: ",aveDegree
print
print
n,bins,patches = pylab.hist(degreeData,1+max(degreeData)-min(degreeData),histtype='stepfilled')
pylab.setp(patches,'facecolor','g','alpha',0.75)
pylab.ylim([0,max(n)])
pylab.show()
































