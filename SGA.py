# cython: profile=True
import sys
import time
import random
import settings
import parseTree
import copy

def ktourn(pop,k):

    best = None

    for i in xrange(k):
        obj = random.choice(pop)
        if not best or obj>best:
            best = obj
    return best


s = None
if len(sys.argv)>1:
    s = settings.runSettings(sys.argv[1])
else:
    s = settings.runSettings()
s.seed =time.time()
random.seed(s.seed)
mu = 100 
k = 8

pop = []
i = 0
while i<mu:
    x = parseTree.parseTree(copy.deepcopy(s))
    x.evaluate()
    pop.append(x)
    print x.fit
    i+=1
pop.sort()
for p in pop:
    print p.fit

maxEvals = 5000
cur = mu
children = 40

while cur<maxEvals:
    
    c = 0
    childs = []
    while c<children:    
        choice = random.choice([0,1,2])
        rate = random.random()
        
        if c+1!=children and rate<.3:
            mom = ktourn(pop,k)
            dad = ktourn(pop,k)
            x,y = mom.mate(dad)
            x.evaluate()
            childs.append(x)
            c+=1
            y.evaluate()
            childs.append(y)
            c+=1
        else:
            x=ktourn(pop,k).mutate()
            x.evaluate()
            childs.append(x)
            c+=1

    pop.extend(childs)
    pop.sort()
    pop = pop[:mu]
    cur+=children

    print cur,pop[0].fit
    print pop[0].toDict()

print
print
print "Best"
print pop[0].toDict()

























