

# cython: profile=True

from random import random,randrange,gauss,choice
import math
import numpy.linalg as lin
import numpy

def multiply(rDown,params={}):
    return rDown[0]*rDown[1]

def inverse(rDown,params={}):
    return lin.inv(rDown[0])i

def transpose(rDown,params={}):
    return numpy.transpose(rDown[0])

def scalarMult(rDown,params={}):
    return params['scalar']['value']*rDown[0]



