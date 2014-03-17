import networkx as nx
from networkx.algorithms.approximation import max_clique


def largestComp(rDown, params={}):
    # Returns matrix for (one of) the largest connected component(s) of rDown
    G = nx.from_numpy_matrix(rDown[0])
    biggest = nx.connected_components(G)[0]
    for u, v in G.edges():
        if u not in biggest or v not in biggest:
            G.remove_edge(u, v)
    return nx.to_numpy_matrix(G)

def maxClique(rDown, params={}):
    # Reduces graph to maximal clique
    G = nx.from_numpy_matrix(rDown[0])
    clique = max_clique(G)
    for u, v in G.edges():
        if u not in clique or v not in clique:
            G.remove_edge(u, v)
    return nx.to_numpy_matrix(G)

def minSpanTree(rDown, params={}):
    # Reduces graph to minimum spanning tree
    G = nx.from_numpy_matrix(rDown[0])
    H = nx.Graph()
    H.add_nodes_from(G)
    for u, v, attr in nx.minimum_spanning_edges(G):
        H.add_edge(u, v, attr)
    return nx.to_numpy_matrix(H)

def complement(rDown, params={}):
    # Returns graph complement (Note: weight information is lost)
    return nx.to_numpy_matrix(nx.complement(nx.from_numpy_matrix(rDown[0])))

def reverse(rDown, params={}):
    # Returns reverse of directed graph
    return nx.to_numpy_matrix(nx.reverse(nx.from_numpy_matrix(rDown[0], create_using=nx.DiGraph())))

def compose(rDown, params={}):
    # Returns composition of two graphs
    G = nx.from_numpy_matrix(rDown[0])
    H = nx.from_numpy_matrix(rDown[1])
    return nx.to_numpy_matrix(nx.compose(G, H))