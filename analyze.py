import sys
import state
import fitnessFunction
import analysis
import pylab
import matplotlib.pyplot as plt


plug = __import__(sys.argv[1])







runs = int(sys.argv[2])
size = int(sys.argv[3])

x = range(size)
trend_aveDegree = [0 for i in xrange(size)]
trend_edges = [0 for i in xrange(size)]
trend_edgecut = [0 for i in xrange(size)]
trend_connectivity = [0 for i in xrange(size)]


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
        if not j:
            continue
        trend_aveDegree[j]+=sum(s.calcDegree())/float(j)
        trend_edges[j]+=analysis.edges(s)
        trend_edgecut[j]+=analysis.edgeCut(s)
        trend_connectivity[j]+=analysis.connected(s)
    fitness+=fitnessFunction.funcs[sys.argv[4]](s)
    degreeData .extend(s.calcDegree())
    aveEdgecut+=analysis.edgeCut(s)
    edges+=analysis.edges(s)

edges/=runs    
fitness/=runs
aveEdgecut/=runs
aveDegree = sum(degreeData)/float(len(degreeData))

ave = lambda y: y/float(runs)

trend_aveDegree = map(ave,trend_aveDegree)
trend_edges = map(ave,trend_edges)
trend_edgecut = map(ave,trend_edgecut)
trend_connectivity = map(ave,trend_connectivity)

print
print "Nodes: ",size
print "Fitness: ",fitness
print "Edgecut: ",aveEdgecut
print "Edges: ", edges
print "Ave Degree: ",aveDegree
print
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
plt.show()
































