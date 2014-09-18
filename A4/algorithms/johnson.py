"""
    johnson.py
    ~~~~~~~~~~~~
    Contains Johnson algorithm for computing the all-pairs shortest paths of a reweighted_graph.
"""
import copy
from algorithms.bellman_ford import bellman_ford_smart as bellman_ford
from heap import Heap


def reweight(graph=None):
    """ Reweights reweighted_graph to have non-negative edge lengths while preserving shortest-path relations"""

    if graph is None:
        return None
    else:
        # so that we don't alter the input reweighted_graph
        reweighted_graph = copy.deepcopy(graph)

    # insert psuedo-node with distance 0 to every node in reweighted_graph
    reweighted_graph[0] = {node: 0 for node in reweighted_graph.nodes()}

    # get reweight values for each node with bellman ford algorithm
    node_weights = bellman_ford(graph=reweighted_graph, source_node=0)

    # delete pseudo-node
    del reweighted_graph[0]

    # reweight nodes
    # reweighted_reweighted_graph = defaultdict(dict)

    for edge in reweighted_graph.edges():
        head_node, tail_node, weight = edge
        reweighted_graph[head_node][tail_node] = weight + \
            node_weights[head_node] - node_weights[tail_node]

    return reweighted_graph


def johnson(reweighted_graph=None):
    if reweighted_graph is None:
        return None
