"""
    bellman_ford.py
    ~~~~~~~~~~~~
    Contains Bellman-Ford algorithm for computing the single source shortest paths of a graph in O( E log V ) time.
"""

import copy

def bellman_ford_naive(graph=None, source_node=1):
    """ """
    if graph is None:
        graph = copy.deepcopy(self.graph)
    source_node = int(source_node)

    # setup dicts for keeping track of current and previous iterations of
    # bellman-ford algorithm
    previous_iteration = {}
    for head_node in graph.keys():
        previous_iteration[head_node] = float("inf")
        for tail_node in graph[head_node].keys():
            previous_iteration[tail_node] = float("inf")
    previous_iteration[source_node] = 0
    current_iteration = copy.deepcopy(previous_iteration)
    newly_added_nodes = [source_node]

    # main body of bellman-ford algorithm
    for i in xrange(len(graph) - 1):
        for head_node in graph:
            for tail_node in graph[head_node]:
                head_node_length = previous_iteration[head_node]
                tail_node_length = previous_iteration[tail_node]
                edge_length = graph[head_node][tail_node]
                # print head_node, tail_node, edge_length, head_node_length
                if head_node_length + edge_length < tail_node_length:
                    current_iteration[
                        tail_node] = head_node_length + edge_length
        previous_iteration = copy.deepcopy(current_iteration)

    return current_iteration
def bellman_ford_smart(graph=None, source_node=1):
    """ Implementation of bellman-ford algorithm
        Why it's smart:
            It keeps track of which nodes were added in the last iteration and only checks those nodes' outgoing edges, avoiding double-checking edges
    """
    if graph is None:
        return None

    # setup dicts for keeping track of current and previous iterations of
    # bellman-ford algorithm
    previous_iteration = {}
    for node in graph.nodes():
        previous_iteration[node] = float("inf")
    previous_iteration[source_node] = 0

    current_iteration = copy.deepcopy(previous_iteration)
    newly_added_nodes = [source_node]

    # main body of bellman-ford algorithm
    for i in xrange(len(graph) - 1):
        for head_node in newly_added_nodes:
            for tail_node in graph[head_node]:
                head_node_length = current_iteration[head_node]
                tail_node_length = current_iteration[tail_node]
                edge_length = graph[head_node][tail_node]
                if head_node_length + edge_length < tail_node_length:
                    current_iteration[
                        tail_node] = head_node_length + edge_length

        # compute the set of newly added nodes, so that we don't double-check edges
        previous_nodes = set([node for node in previous_iteration if previous_iteration[node] < float("inf")])
        current_nodes = set([node for node in current_iteration if current_iteration[node] < float("inf")])
        newly_added_nodes = current_nodes - previous_nodes
        previous_iteration = copy.deepcopy(current_iteration)

    return current_iteration
