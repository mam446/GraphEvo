from funcs import *




{'kTourn(min degree,k=1,num=14)': [{'trunc(min degree,num=2)': [{'trunc(min degree,num=36)': ['allNodes']}]}]}


fitness = 443.0
size = 4


def selectNodes(state):
    x000 = set(range(len(state.nodeList)))
    x00 = trunc([x000],{'opt':{'value':'min'},'num':{'value':36},'data':state.calcDegree(),'val':{'value':'degree'}})
    x0 = trunc([x00],{'opt':{'value':'min'},'num':{'value':2},'data':state.calcDegree(),'val':{'value':'degree'}})
    x = kTourn([x0],{'opt':{'value':'min'},'k':{'value':1},'num':{'value':14},'data':state.calcDegree(),'val':{'value':'degree'}})
    return x
    