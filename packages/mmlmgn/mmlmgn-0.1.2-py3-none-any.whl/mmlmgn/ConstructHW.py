from . import HypergraphConstructKNN
from . import HypergraphConstructKmeans


def constructHW_knn(X, K_neigs, is_probH):
    """incidence matrix"""
    H = HypergraphConstructKNN.construct_H_with_KNN(X, K_neigs, is_probH)

    G = HypergraphConstructKNN._generate_G_from_H(H)

    return G


def constructHW_kmean(X, clusters):
    """incidence matrix"""
    H = HypergraphConstructKmeans.construct_H_with_Kmeans(X, clusters)

    G = HypergraphConstructKmeans._generate_G_from_H(H)

    return G
