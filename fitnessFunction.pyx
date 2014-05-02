import networkx as nx
import metis





def maxMetisEval(state,partitions=2):
    G = nx.Graph()
    for node in xrange(len(state.nodeList)):
        G.add_node(node)
        for edge in state.nodeList[node]:
            G.add_edge(node,edge)
    (edgecuts, parts) = metis.part_graph(G,partitions)
    mod = 0
    if nx.is_connected(G):
        mod = 1
        return float(edgecuts)-2*G.number_of_edges()#nx.radius(G)
    return -99999999999999999








def minMetisEval(state,partitions=2):
    G = nx.Graph()
    for node in xrange(len(state.nodeList)):
        G.add_node(node)
        for edge in state.nodeList[node]:
            G.add_edge(node,edge)
    (edgecuts, parts) = metis.part_graph(G,partitions)
    mod = 0
    if nx.is_connected(G):
        mod = 1
        return -50*float(edgecuts)+G.number_of_edges()#nx.radius(G)
    return -99999999999999999


funcs = {}
funcs['minMetis'] = minMetisEval
funcs['maxMetis'] = maxMetisEval


