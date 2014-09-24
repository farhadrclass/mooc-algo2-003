"""
    traveling_salesman.py
    ~~~~~~~~~~~~
    Contains dynamic programming algorithm for computing the shortest route visiting all nodes in a completed graph.
    Runs in O ( n^2 2^n ) time, compared to O(n!) for brute force search.
"""

import copy
from collections import defaultdict
from itertools import combinations

def traveling_salesman(graph=None, initial_node=1):
    """ Return the shortest possible route between nodes in the undirected graph """

    previous_subproblems = defaultdict(dict)
    current_subproblems = defaultdict(dict)

    #populate initial set of subproblems
    for v in graph.nodes():
        previous_subproblems[str(set([v]))][initial_node] = float("inf")
        previous_subproblems[str(set([initial_node]))][initial_node] = 0

    # m is the subproblem size
    for m in xrange(2,len(graph)+1):
        for vertex_list in combinations((set(graph.nodes()) - set([initial_node])), m-1):
            vertex_set = set(vertex_list)
            vertex_set = vertex_set.union(set([initial_node]))  # add the initial node back in

            for j in vertex_set - set([initial_node]):
                subproblems = []
                for k in vertex_set - set([j]):
                    try:
                        previous_subproblems[str(vertex_set - set([j]))][k]
                    except KeyError:
                        previous_subproblems[str(vertex_set - set([j]))][k] = float("inf")
                    finally:
                        subproblems.append(previous_subproblems[str(vertex_set - set([j]))][k] + graph[j][k] )
                current_subproblems[str(vertex_set)][j] = min(subproblems)

        previous_subproblems = copy.deepcopy(current_subproblems)
        del current_subproblems
        current_subproblems = defaultdict(dict)


    return min([previous_subproblems[ str(set(graph.nodes())) ][ j ] + graph[j][initial_node] for j in xrange(2, len(graph)+1)])
