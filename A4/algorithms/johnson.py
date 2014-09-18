"""
    johnson.py
    ~~~~~~~~~~~~
    Contains Johnson algorithm for computing the all-pairs shortest paths of a reweighted_graph.
"""
import copy
from collections import defaultdict
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford_naive as bellman_ford
from heap import Heap


def reweight(graph=None):
    """ Reweights reweighted_graph to have non-negative edge lengths while preserving shortest-path relations"""

    if graph is None:
        return None
    else:
        # so that we don't alter the input graph
        reweighted_graph = copy.deepcopy(graph)

    # insert psuedo-node with distance 0 to every node in reweighted_graph
    reweighted_graph[0] = {node: 0 for node in reweighted_graph.nodes()}

    # get reweight values for each node with bellman ford algorithm
    node_weights = bellman_ford(graph=reweighted_graph, source_node=0)

    if not node_weights:
        return False

    # delete pseudo-node
    del reweighted_graph[0]

    # reweight nodes
    for edge in reweighted_graph.edges():
        head_node, tail_node, weight = edge
        reweighted_graph[head_node][tail_node] = weight + node_weights[head_node] - node_weights[tail_node]

    return reweighted_graph


def johnson(directed_graph=None):
    if directed_graph is None:
        return None
    else:
        reweighted_graph = reweight(directed_graph)
        if not reweighted_graph:
            return False
        all_pairs_shortest_paths = defaultdict(dict)

    for node in reweighted_graph.nodes():
        shortest_paths = dijkstra(graph=reweighted_graph, source_node=node)
        all_pairs_shortest_paths[node] = shortest_paths

    return all_pairs_shortest_paths
