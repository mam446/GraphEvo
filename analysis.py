import networkx as nx
import metis
from random import choice


def edgeCut(state,partitions=2):
    G = state
    if type(G) is not nx.classes.graph.Graph:
        G = nx.Graph()
        for node in xrange(len(state.nodeList)):
            G.add_node(node)
            for edge in state.nodeList[node]:
                G.add_edge(node,edge)

    (edgecuts,parts) = metis.part_graph(G,partitions)
    return edgecuts

def edges(state):
    G = state
    if type(G) is not nx.classes.graph.Graph:
        G = nx.Graph()
        for node in xrange(len(state.nodeList)):
            G.add_node(node)
            for edge in state.nodeList[node]:
                G.add_edge(node,edge)
    return G.number_of_edges() 



def connected(state):
    G = nx.Graph()
    for node in xrange(len(state.nodeList)):
        G.add_node(node)
        for edge in state.nodeList[node]:
            G.add_edge(node,edge)
    return nx.is_connected(G)

def resilNode(state, failureRatio=0.1):
    """ Returns percentage (0-1) of nodes in largest connected component after (n * failureRatio) nodes are removed randomly """
    if type(state) is not nx.classes.graph.Graph:
        G = nx.Graph()
        for node in xrange(len(state.nodeList)):
            G.add_node(node)
            for edge in state.nodeList[node]:
                G.add_edge(node,edge)
    else:
        G = state.copy()
    numFails = int(G.order() * failureRatio)
    for _ in xrange(numFails):
        G.remove_node(choice(G.nodes()))
    return float(len(nx.connected_components(G)[0])) / G.order()

def resilEdge(state, failureRatio=0.1):
    """ Returns percentage (0-1) of nodes in largest connected component after (m * failureRatio) edges are removed randomly """
    if type(state) is not nx.classes.graph.Graph:
        G = nx.Graph()
        for node in xrange(len(state.nodeList)):
            G.add_node(node)
            for edge in state.nodeList[node]:
                G.add_edge(node,edge)
    else:
        G = state.copy()
    numFails = int(G.size() * failureRatio)
    for _ in xrange(numFails):
        G.remove_edge(*choice(G.edges()))
    return float(len(nx.connected_components(G)[0])) / G.order()

def eccentricity(state):
    G = nx.Graph()
    for node in xrange(len(state.nodeList)):
        G.add_node(node)
        for edge in state.nodeList[node]:
            G.add_edge(node,edge)
    if nx.is_connected(G):
        avgEccen = 0.0
        nodeEccentricities = nx.eccentricity(G)
        for node in nodeEccentricities:
            avgEccen += nodeEccentricities[node]
        avgEccen /= G.number_of_edges()
        return avgEccen 
    else:
        return 0











