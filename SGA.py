# cython: profile=True
import sys
import time
import random
import settings
import parseTree
import copy
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--settings', default='', metavar='settingsFile.pyx', help='specifies the settings file')
parser.add_argument('-o', '--outdir', default='', metavar='path/to/output', help='directory in which to place output files')

args = parser.parse_args()

def ktourn(pop,k):

    best = None

    for i in xrange(k):
        obj = random.choice(pop)
        if not best or obj>best:
            best = obj
    return best


s = None
if args.settings != '':
    s = settings.runSettings(args.settings)
else:
    s = settings.runSettings()
outdir = args.outdir
if outdir != '':
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    if not outdir.endswith('/'):
        outdir += '/'
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
pop.sort(reverse=True)
for p in pop:
    print p.fit

maxEvals = 5000
cur = mu
children = 50
sk = 5
pop[0].report(outdir=outdir)
while cur<maxEvals:
    
    c = 0
    childs = []
    while c<children:    
        choice = random.choice([0,1,2])
        rate = random.random()
        
        if c+1!=children and rate<.35:
            mom = ktourn(pop,k)
            dad = ktourn(pop,k)
            x,y = mom.mate(dad)
            x.evaluate()
            childs.append(x)
            c+=1
            y.evaluate()
            childs.append(y)
            c+=1
        elif rate<.70:
            x=ktourn(pop,k).mutate()
            x.evaluate()
            childs.append(x)
            c+=1
        else:
            x = ktourn(pop,k).altMutate()
            x.evaluate()
            childs.append(x)
            c+=1
    pop.extend(childs)
    x = []
    for i in xrange(mu):
        x.append(ktourn(pop,sk))
    pop = x
    pop.sort(reverse=True)
    cur+=children
    #pop = pop[:mu]

    ave = 0
    for p in pop:
        ave+=p.fit
    ave/=len(pop)


    print cur,pop[0].fit,ave
    print pop[0].toDict()
    pop[0].report(outdir=outdir)
    pop[0].makeProg(outdir=outdir)
pop[0].report(True, outdir=outdir)
pop[0].makeProg(outdir=outdir)
print
print
print "Best"
print pop[0].toDict()


























