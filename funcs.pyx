

# cython: profile=True

from random import random,randrange,gauss,choice,sample
import math
import numpy.linalg as lin
import numpy

def pSelect(rDown,params={}):
    cdef int i
    ret = set()
    cur = rDown[0]
    for i in xrange(len(cur)):
        if random()<params['p']['value']:
            ret.add(cur.pop())
        else:
            cur.pop()
    return ret

def union(rDown,params={}):
    return rDown[0].union(rDown[1])

def intersection(rDown,params={}):
    return rDown[0].intersection(rDown[1])


def difference(rDown,params={}):
    return rDown[0].difference(rDown[1])

def symDifference(rDown,params={}):
    return rDown[0].symmetric_difference(rDown[1])

def kTourn(rDown,params={}):
    cdef int i,n,c
    data = {}
    cur = rDown[0]
    ret = set()
    if params['val']['value']=='degree':
        for c in xrange(len(params['data'])):
            data[c]=params['data'][c]
    if not cur:
        return ret
    x = list(cur)
    for n in xrange(params['num']['value']):
        best = None
        for i in xrange(params['k']['value']):
            obj = choice(x)
            if params['opt']['value']=='min':
                if not best or data[obj]<data[best]:
                    best = obj
            if params['opt']['value']=='max':
                if not best or data[obj]>data[best]:
                    best = obj
        ret.add(best)
    return ret


def relKTourn(rDown,params={}):
    cdef int i,n,c

    size = len(params['data'])

    sel = size/params['relNum']['value']
    if sel==0:
        return set()

    sk= size/params['relNum']['value']
    if sk==0:
        sk=1


    data = {}
    cur = rDown[0]
    ret = set()
    if params['val']['value']=='degree':
        for c in xrange(len(params['data'])):
            data[c]=params['data'][c]
    if not cur:
        return ret
    x = list(cur)

    for n in xrange(sel):
        best = None
        for i in xrange(sk):
            obj = choice(x)
            if params['opt']['value']=='min':
                if not best or data[obj]<data[best]:
                    best = obj
            if params['opt']['value']=='max':
                if not best or data[obj]>data[best]:
                    best = obj
        ret.add(best)
    return ret





def randSubset(rDown,params={}):
    if params['num']['value']>len(rDown[0]):
        return rDown[0]
    x = sample(list(rDown[0]),params['num']['value'])
    return set(x)

def relRandSubset(rDown,params={}):
    size = len(params['data']) 
    
    sel = size/params['relNum']['value']
    if sel==0:
        return set()
    
    if sel>len(rDown[0]):
        return rDown[0]
    x = sample(list(rDown[0]),sel)
    return set(x)



def trunc(rDown,params={}):
    cdef int i,n,c
    data = {}
    cur = rDown[0]
    ret = set()
    if params['val']['value']=='degree':
        for c in xrange(len(params['data'])):
            if c in cur:
                data[c]=params['data'][c]
    rev = False
    if params['opt']['value']=='max':
        rev=True 
    L = sorted(data.items(),key=lambda e:e[1],reverse=rev)
    return set(map(lambda e:e[0],L)[:params['num']['value']])


def relTrunc(rDown,params={}):
    cdef int i,n,c

    size = len(params['data'])
    sel = size/params['relNum']['value']
    if sel==0:
        return set()


    data = {}
    cur = rDown[0]
    ret = set()
    if params['val']['value']=='degree':
        for c in xrange(len(params['data'])):
            if c in cur:
                data[c]=params['data'][c]
    rev = False
    if params['opt']['value']=='max':
        rev=True 
    L = sorted(data.items(),key=lambda e:e[1],reverse=rev)
    return set(map(lambda e:e[0],L)[:sel])

