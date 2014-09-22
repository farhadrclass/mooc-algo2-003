"""
    bellman_ford.py
    ~~~~~~~~~~~~
    Contains Bellman-Ford algorithm for computing the single source shortest paths of a graph in O( |V| |E| ) time.
"""

import copy

def bellman_ford(graph=None, source_node=1):
    """ """
    if graph is None:
        return None
    # setup dicts for keeping track of current and previous iterations of bellman-ford algorithm
    previous_iteration = {node: float("inf") for node in graph.nodes()}
    previous_iteration[source_node] = 0

    current_iteration = copy.deepcopy(previous_iteration)

    # main body of bellman-ford algorithm
    for i in xrange(len(graph) - 1):
        for edge in graph.edges():
            u, v, w = edge
            if previous_iteration[u] + w < previous_iteration[v]:
                current_iteration[v] = previous_iteration[u] + w
        if current_iteration == previous_iteration:
            break
        previous_iteration = copy.deepcopy(current_iteration)

    # check for negative weight cycles
    for edge in graph.edges():
        u, v, w = edge
        if previous_iteration[u] + w < previous_iteration[v]:
            return False

    return current_iteration
