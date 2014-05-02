

def selectNodes(state):
    x000 = set()
    x001 = set(range(len(state.nodeList)))
    x00 = union([x000,x001])
    x0 = kTourn([x00],{'opt':{'value':'max'},'k':{'value':19},'num':{'value':2},'data':{state.calcDegree()},'val':{'value':'degree'}})
    x = kTourn([x0],{'opt':{'value':'max'},'k':{'value':49},'num':{'value':4},'data':{state.calcDegree()},'val':{'value':'degree'}})
    return x
    