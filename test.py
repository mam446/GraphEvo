import parseTree
import settings


s = settings.runSettings()


x = parseTree.parseTree(s)
x.createER()
print x.toDict()


print x.evaluate()
#print x.eval2()
x.makeProg()
x.report()
x.makeGraph()
