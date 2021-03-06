import networkx as nx
import metis
from random import choice, sample

REALLY_BAD = -99999999999999999.0

def maxMetisEval(state,partitions=2):
    G = state
    if type(G) is not nx.classes.graph.Graph:
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
    return REALLY_BAD

def minMetisEval(state,partitions=2):
    G = state
    if type(G) is not nx.classes.graph.Graph:
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
    return REALLY_BAD

def minEccenEval(state):
    G = state
    if type(G) is not nx.classes.graph.Graph:
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
        return -50 * avgEccen - G.number_of_edges()
    return REALLY_BAD

def maxEccenEval(state):
    G = state
    if type(G) is not nx.classes.graph.Graph:
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
        return 50 * avgEccen - G.number_of_edges()
    return REALLY_BAD

def maxClustEval(state):
    G = state
    if type(G) is not nx.classes.graph.Graph:
        G = nx.Graph()
        for node in xrange(len(state.nodeList)):
            G.add_node(node)
            for edge in state.nodeList[node]:
                G.add_edge(node,edge)
    if nx.is_connected(G):
        return 100000 * nx.average_clustering(G) - G.number_of_edges()
    return REALLY_BAD

def resilNodeEval(state, failureRatio=0.1):
    if type(state) is not nx.classes.graph.Graph:
        G = nx.Graph()
        for node in xrange(len(state.nodeList)):
            G.add_node(node)
            for edge in state.nodeList[node]:
                G.add_edge(node,edge)
    else:
        G = state.copy()
    if nx.is_connected(G):
        numEdges = G.size()
        numFails = int(G.order() * failureRatio)
        G.remove_nodes_from(sample(G.nodes(), numFails))
        possibleEdges = G.order() * (G.order() + 1) / 2
        return (1000.0 * len(nx.connected_components(G)[0]) / G.order()) - (2000.0 * G.size() / possibleEdges)
    return REALLY_BAD

def resilEdgeEval(state, failureRatio=0.1):
    if type(state) is not nx.classes.graph.Graph:
        G = nx.Graph()
        for node in xrange(len(state.nodeList)):
            G.add_node(node)
            for edge in state.nodeList[node]:
                G.add_edge(node,edge)
    else:
        G = state.copy()
    if nx.is_connected(G):
        numEdges = G.size()
        numFails = int(G.size() * failureRatio)
        G.remove_edges_from(sample(G.edges(), numFails))
        possibleEdges = G.order() * (G.order() + 1) / 2
        return (1000.0 * len(nx.connected_components(G)[0]) / G.order()) - (2000.0 * G.size() / possibleEdges)
    return REALLY_BAD


funcs = {}
funcs['minMetis'] = minMetisEval
funcs['maxMetis'] = maxMetisEval
funcs['minEccen'] = minEccenEval
funcs['maxEccen'] = maxEccenEval
funcs['maxClust'] = maxClustEval
funcs['resilNode'] = resilNodeEval
funcs['resilEdge'] = resilEdgeEval


