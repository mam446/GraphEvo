import networkx as nx

def numComponents(mat):
    # Returns the number of connected components
    return nx.number_connected_components(nx.from_numpy_matrix(mat))

def numBicomponents(mat):
    # Returns the number of bicomponents
    return len(nx.biconnected_components(nx.from_numpy_matrix(mat)))

def avgClustering(mat):
    # Returns average clustering of graph
    return nx.average_clustering(nx.from_numpy_matrix(mat))



nodes = [numComponents, numBicomponents, avgClustering]