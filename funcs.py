

# cython: profile=True

from random import random,randrange,gauss,choice
import math
import numpy.linalg as lin
import numpy

def multiply(rDown,params={}):
    d = numpy.dot(rDown[0],rDown[1])
    return d

def add(rDown,params={}):
    
    d =  rDown[0]+rDown[1]
    return d

def inverse(rDown,params={}):
    return lin.inv(rDown[0])

def transpose(rDown,params={}):
    return numpy.transpose(rDown[0])

def scalarMult(rDown,params={}):
    return params['scalar']['value']*rDown[0]



