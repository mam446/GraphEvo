from funcs import *




{'union': [{'relRandSubset(relNum=47)': [{'trunc(max degree,num=33)': [{'kTourn(max degree,k=9,num=36)': [{'relTrunc(min degree,relNum=39)': [{'relTrunc(min degree,relNum=40)': [{'intersection': ['allNodes', 'allNodes']}]}]}]}]}]}, {'symDifference': [{'symDifference': [{'union': [{'intersection': ['allNodes', 'allNodes']}, {'intersection': ['allNodes', 'allNodes']}]}, 'allNodes']}, {'relKTourn(max degree,relK=28,relNum=5)': ['allNodes']}]}]}


fitness = -76766.45
size = 21


def selectNodes(state):
    x0000000 = set(range(len(state.nodeList)))
    x0000001 = set(range(len(state.nodeList)))
    x000000 = intersection([x0000000,x0000001])
    x00000 = relTrunc([x000000],{'opt':{'value':'min'},'relNum':{'value':40},'data':state.calcDegree(),'val':{'value':'degree'}})
    x0000 = relTrunc([x00000],{'opt':{'value':'min'},'relNum':{'value':39},'data':state.calcDegree(),'val':{'value':'degree'}})
    x000 = kTourn([x0000],{'opt':{'value':'max'},'k':{'value':9},'num':{'value':36},'data':state.calcDegree(),'val':{'value':'degree'}})
    x00 = trunc([x000],{'opt':{'value':'max'},'num':{'value':33},'data':state.calcDegree(),'val':{'value':'degree'}})
    x0 = relRandSubset([x00],{'relNum':{'value':47},'data':state.calcDegree()})
    x10000 = set(range(len(state.nodeList)))
    x10001 = set(range(len(state.nodeList)))
    x1000 = intersection([x10000,x10001])
    x10010 = set(range(len(state.nodeList)))
    x10011 = set(range(len(state.nodeList)))
    x1001 = intersection([x10010,x10011])
    x100 = union([x1000,x1001])
    x101 = set(range(len(state.nodeList)))
    x10 = symDifference([x100,x101])
    x110 = set(range(len(state.nodeList)))
    x11 = relKTourn([x110],{'relK':{'value':28},'relNum':{'value':5},'opt':{'value':'max'},'data':state.calcDegree(),'val':{'value':'degree'}})
    x1 = symDifference([x10,x11])
    x = union([x0,x1])
    return x
    