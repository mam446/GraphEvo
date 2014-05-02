import sys
import state
import fitnessFunction
import analysis
import pylab
import matplotlib.pyplot as plt


plug1 = __import__(sys.argv[1])
plug2 = __import__(sys.argv[2])






runs = int(sys.argv[3])
size = int(sys.argv[4])

x = range(size)
trend_aveDegree1 = [0 for i in xrange(size)]
trend_edges1 = [0 for i in xrange(size)]
trend_edgecut1 = [0 for i in xrange(size)]
trend_connectivity1 = [0 for i in xrange(size)]
trend_edgecut_edge1 = [0 for i in xrange(size)]
trend_fitness1 = [0 for i in xrange(size)]


trend_aveDegree2 = [0 for i in xrange(size)]
trend_edges2 = [0 for i in xrange(size)]
trend_edgecut2 = [0 for i in xrange(size)]
trend_connectivity2 = [0 for i in xrange(size)]
trend_edgecut_edge2 = [0 for i in xrange(size)]
trend_fitness2 = [0 for i in xrange(size)]

degreeData1= []
degreeData2= []





aveEdgecut1 = 0.0
aveEdgecut2 = 0.0


edges1 = 0.0
edges2 = 0.0
fitness1 = 0.0
fitness2 = 0.0
s1 = None
s2 = None
for i in xrange(runs):
    s1= state.state()
    s2 = state.state()

    for j in xrange(size):
        add1 = plug1.selectNodes(s1)
        s1.addNode(add1)
        add2 = plug2.selectNodes(s2)
        s2.addNode(add2)
        if not j:
            continue
        trend_aveDegree1[j]+=sum(s1.calcDegree())/float(j)
        trend_edges1[j]+=analysis.edges(s1)
        trend_edgecut1[j]+=analysis.edgeCut(s1)
        trend_connectivity1[j]+=analysis.connected(s1)
        trend_edgecut_edge1[j]+=trend_edgecut1[j]/float(trend_edges1[j]+1)
        
        temp = fitnessFunction.funcs[sys.argv[5]](s1)
        if temp>-1000000:
            trend_fitness1[j]+=temp


        trend_aveDegree2[j]+=sum(s2.calcDegree())/float(j)
        trend_edges2[j]+=analysis.edges(s2)
        trend_edgecut2[j]+=analysis.edgeCut(s2)
        trend_connectivity2[j]+=analysis.connected(s2)
        trend_edgecut_edge2[j]+=trend_edgecut2[j]/float(trend_edges2[j]+1)
        
        temp = fitnessFunction.funcs[sys.argv[5]](s2)
        if temp>-1000000:
            trend_fitness2[j]+=temp


    fitness1+=fitnessFunction.funcs[sys.argv[5]](s1)
    degreeData1.extend(s1.calcDegree())
    aveEdgecut1+=analysis.edgeCut(s1)
    edges1+=analysis.edges(s1)
    
    fitness2+=fitnessFunction.funcs[sys.argv[5]](s2)
    degreeData2.extend(s2.calcDegree())
    aveEdgecut2+=analysis.edgeCut(s2)
    edges2+=analysis.edges(s2)


edges1/=float(runs)
fitness1/=float(runs)
aveEdgecut1/=float(runs)
aveDegree1 = sum(degreeData1)/float(len(degreeData1))

edges2/=float(runs)
fitness2/=float(runs)
aveEdgecut2/=float(runs)
aveDegree2 = sum(degreeData2)/float(len(degreeData2))

ave = lambda y: y/float(runs)


trend_aveDegree1 = map(ave,trend_aveDegree1)
trend_edges1 = map(ave,trend_edges1)
trend_edgecut1 = map(ave,trend_edgecut1)
trend_connectivity1 = map(ave,trend_connectivity1)
trend_edgecut_edge1 = map(ave,trend_edgecut_edge1)
trend_fitness1 = map(ave,trend_fitness1)

trend_aveDegree2 = map(ave,trend_aveDegree2)
trend_edges2 = map(ave,trend_edges2)
trend_edgecut2 = map(ave,trend_edgecut2)
trend_connectivity2 = map(ave,trend_connectivity2)
trend_edgecut_edge2 = map(ave,trend_edgecut_edge2)
trend_fitness2 = map(ave,trend_fitness2)

print
print "Nodes:   \t",size,"\t",size
print "Fitness: \t",fitness1,"\t",fitness2
print "Edgecut: \t",aveEdgecut1,'\t',aveEdgecut2
print "Edges:   \t", edges1,'\t',edges2
print "Ave Degree: \t",aveDegree1,'\t',aveDegree2
print
print

fig = plt.figure(1)

fig.subplots_adjust(hspace=.5)

ax1 = plt.subplot(331)
plt.plot(x,trend_aveDegree1,'g',x,trend_aveDegree2,'r')
ax1.set_title('Average Degree')


ax2 = plt.subplot(332)
plt.plot(x,trend_edges1,'g',x,trend_edges2,'r')
ax2.set_title('Edges')

ax3 = plt.subplot(333)
plt.plot(x,trend_edgecut1,'g',x,trend_edgecut2,'r')
ax3.set_title('Edgecut')

ax4 = plt.subplot(334)
plt.plot(x,trend_connectivity1,'g',x,trend_connectivity2,'r')
ax4.set_title('Connectivity Probability')

ax4 = plt.subplot(336)
plt.plot(x,trend_edgecut_edge1,'g',x,trend_edgecut_edge2,'r')
ax4.set_title('Edgecut/Edges')

ax4 = plt.subplot(337)
plt.plot(x,trend_fitness1,'g',x,trend_fitness2,'r')
ax4.set_title('Fitness: '+sys.argv[5])

ax5 = plt.subplot(335)
n1,bins1,patches1 = plt.hist(degreeData1,1+max(degreeData1)-min(degreeData1),histtype='stepfilled')
n2,bins2,patches2 = plt.hist(degreeData2,1+max(degreeData2)-min(degreeData2),histtype='stepfilled')
plt.setp(patches1,'facecolor','g','alpha',0.75)
plt.setp(patches2,'facecolor','r','alpha',0.75)



plt.ylim([0,max([max(n1),max(n2)])])
ax5.set_title('Degree Distribution')
plt.savefig(sys.argv[1][:-4]+sys.argv[2][:-4]+"analysis-"+str(runs)+"-"+str(size)+".png")
plt.show()
































