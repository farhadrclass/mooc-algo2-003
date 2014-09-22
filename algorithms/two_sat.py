"""
    two_sat.py
    ~~~~~~~~~~~~
    Contains algorithm for computing whether a set of two-valued constraints can be satisified, leveraging Kosaraju's two-pass algorithm for computing strongly connected components.
"""
import copy
from collections import defaultdict
import Queue

def depth_first_search(directed_graph):
    """ Returns finishing times for a depth first search on graph."""
    visited_nodes = set()
    finishing_time = 0
    finishing_times = {}
    leaders = {}


    unvisited_queue = [node for node in sorted(directed_graph.nodes())]
    backtrack_queue = []

    #first DFS iteration

    while unvisited_queue:
        u = unvisited_queue.pop()
        if u in visited_nodes:
            continue
        else:
            leader = u
            while True:
                if u not in visited_nodes:
                    visited_nodes.add(u)
                    leaders[u] = leader

                try:
                    v = directed_graph[u].pop()
                except:
                    finishing_time += 1
                    finishing_times[u] = finishing_time
                    try:
                        u = backtrack_queue.pop()
                        continue
                    except:
                        break

                if v in visited_nodes:
                    continue
                else:
                    backtrack_queue.append(u)
                    u = v

    return finishing_times, leaders

def kosaraju(directed_graph=None):
    directed_graph_rev = copy.deepcopy(directed_graph)
    directed_graph_rev.graph  = directed_graph.reversed()
    finishing_times, _ = depth_first_search(directed_graph_rev)

    directed_graph_mapped = copy.deepcopy(directed_graph)
    remapped_graph = defaultdict(list)

    for u in directed_graph.graph:
        remapped_graph[finishing_times[u]] = [finishing_times[v] for v in directed_graph.graph[u]]

    directed_graph_mapped.graph = remapped_graph

    _, leaders = depth_first_search(directed_graph_mapped)

    return leaders

def two_sat_scc(graph):
    pass
