from funcs import *




{'trunc(max degree,num=6)': [{'trunc(min degree,num=41)': ['allNodes']}]}


fitness = 726.0
size = 3


def selectNodes(state):
    x00 = set(range(len(state.nodeList)))
    x0 = trunc([x00],{'opt':{'value':'min'},'num':{'value':41},'data':state.calcDegree(),'val':{'value':'degree'}})
    x = trunc([x0],{'opt':{'value':'max'},'num':{'value':6},'data':state.calcDegree(),'val':{'value':'degree'}})
    return x
    