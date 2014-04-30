import networkx as nx
import metis


def edgeCut(state,partitions=2):
    G = nx.Graph()
    for node in xrange(len(state.nodeList)):
        G.add_node(node)
        for edge in state.nodeList[node]:
            G.add_edge(node,edge)

    (edgecuts,parts) = metis.part_graph(G,partitions)
    return edgecuts

def edges(state):
    G = nx.Graph()
    for node in xrange(len(state.nodeList)):
        G.add_node(node)
        for edge in state.nodeList[node]:
            G.add_edge(node,edge)
    return G.number_of_edges() 


















