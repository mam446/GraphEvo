import parseTree
import settings


s = settings.runSettings()


x = parseTree.parseTree(s)


print x.toDict()


print x.evaluate()


