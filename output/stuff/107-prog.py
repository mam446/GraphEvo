from funcs import *




{'kTourn(min degree,k=40,num=40)': [{'pSelect(p=0.646334889855)': [{'union': [{'relKTourn(max degree,relK=27,relNum=16)': ['allNodes']}, {'relTrunc(min degree,relNum=43)': ['allNodes']}]}]}]}


fitness = -2421.55
size = 7


def selectNodes(state):
    x0000 = set(range(len(state.nodeList)))
    x000 = relKTourn([x0000],{'relK':{'value':27},'relNum':{'value':16},'opt':{'value':'max'},'data':state.calcDegree(),'val':{'value':'degree'}})
    x0010 = set(range(len(state.nodeList)))
    x001 = relTrunc([x0010],{'opt':{'value':'min'},'relNum':{'value':43},'data':state.calcDegree(),'val':{'value':'degree'}})
    x00 = union([x000,x001])
    x0 = pSelect([x00],{'p':{'value':0.646334889855}})
    x = kTourn([x0],{'opt':{'value':'min'},'k':{'value':40},'num':{'value':40},'data':state.calcDegree(),'val':{'value':'degree'}})
    return x
    