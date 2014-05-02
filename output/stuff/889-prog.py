from funcs import *




{'trunc(min degree,num=5)': [{'trunc(min degree,num=36)': ['allNodes']}]}


fitness = 732.0
size = 3


def selectNodes(state):
    x00 = set(range(len(state.nodeList)))
    x0 = trunc([x00],{'opt':{'value':'min'},'num':{'value':36},'data':state.calcDegree(),'val':{'value':'degree'}})
    x = trunc([x0],{'opt':{'value':'min'},'num':{'value':5},'data':state.calcDegree(),'val':{'value':'degree'}})
    return x
    