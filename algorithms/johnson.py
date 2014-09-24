"""
    johnson.py
    ~~~~~~~~~~~~
    Contains Johnson algorithm for computing the all-pairs shortest paths of a graph.
"""
import copy
from collections import defaultdict
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
from heap import Heap


def shortest_shortest_path(all_pairs_shortest_paths):
    shortest_path = float("inf")
    for node in all_pairs_shortest_paths:
        shortest_path = min([shortest_path] + all_pairs_shortest_paths[node].values())
    return shortest_path

def reweight(graph=None):
    """ Reweight graph to have non-negative edge lengths while preserving shortest-path relations"""

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
        u, v, w = edge
        reweighted_graph[u][v] = w + node_weights[u] - node_weights[v]

    return reweighted_graph, node_weights


def johnson(directed_graph=None):
    if directed_graph is None:
        return None
    else:
        results = reweight(directed_graph)
        if not results:
            return False
        else:
            reweighted_graph, node_weights = results

    all_pairs_shortest_paths = defaultdict(dict)

    for u in reweighted_graph.nodes():
        shortest_paths = dijkstra(graph=reweighted_graph, source_node=u)
        for v in shortest_paths:
            shortest_paths[v] += (-node_weights[u] + node_weights[v])
        all_pairs_shortest_paths[u] = shortest_paths

    return all_pairs_shortest_paths

