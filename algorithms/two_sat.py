"""
    two_sat.py
    ~~~~~~~~~~~~
    Contains algorithm for computing whether a set of two-valued constraints can be satisified, leveraging Kosaraju's two-pass algorithm for computing strongly connected components.
    E is the number of edges, V the number of vertices in a graph.
"""

from collections import defaultdict
import data_structures.directed_graph as dg


def depth_first_search(directed_graph):
    """ Returns:
            finishign times and leader vertices for each vertex after having traversing the full directed graph
        Complexity:
            O( E + V )
    """
    visited_nodes = set()
    finishing_time = 0
    finishing_times = {}
    leaders = {}
    unvisited_queue = [node for node in sorted(directed_graph.nodes())]
    backtrack_queue = []

    # while there are still unvisited nodes, after a branch has been fully explored, get the next leader.
    while unvisited_queue:
        u = unvisited_queue.pop()
        if u in visited_nodes:
            continue
        else:
            leader = u

            # while the branch hasn't been fully explored, get the next tail node v from head node u.
            while True:
                # mark node as visited.
                if u not in visited_nodes:
                    visited_nodes.add(u)
                    leaders[u] = leader

                # while u still has unexplored nodes, get the next node to explore as v.
                try:
                    v = directed_graph[u].pop()

                # when u has no more unexplored nodes left, mark it as finished and backtrack.
                except:
                    finishing_time += 1
                    finishing_times[u] = finishing_time
                    try:
                        u = backtrack_queue.pop()
                        continue
                    except:
                        break

                # if v's been visited, try again.
                if v in visited_nodes:
                    continue
                else:
                    backtrack_queue.append(u)
                    u = v

    return finishing_times, leaders

def kosaraju(directed_graph=None):
    """ Returns:
            the strongly connected component membership of each node in directed_graph
        Complexity:
            O( E + V )
    """

    # reverse graph for first pass of depth first search
    directed_graph_rev = dg.DirectedGraph(graph=directed_graph.reversed())
    # first pass of depth first search
    finishing_times, _ = depth_first_search(directed_graph_rev)

    # remap graph based on finishing times from first pass of depth first search
    remapped_graph = defaultdict(set)
    for u in directed_graph.graph:
        remapped_graph[finishing_times[u]] = set([finishing_times[v] for v in directed_graph.graph[u]])

    directed_graph_remapped = dg.DirectedGraph(graph=remapped_graph)

    # second pass of depth first search
    _, leaders = depth_first_search(directed_graph_remapped)

    # reverse remapping to get back leaders of original graph
    finishing_times_rev = {finishing_times[u]: u for u in finishing_times}
    leaders_rev = {finishing_times_rev[u]: leaders[u] for u in leaders}

    return leaders_rev

def scc_has_contradictions(leaders):
    """ Returns:
            True if a node and its complement are in the same strongly connected component.
        Complexity:
            O( V )
    """
    for node in leaders:
        try:
            if leaders[node] == leaders[-node]:
                return True
        except:
            pass
    else:
        return False


def two_sat_scc(implication_graph=None):
    """ Returns:
            True if the implication graph built from a set of two-valued constraints are satisfiable.
        Complexity:
            O( E + V )"""
    ig = implication_graph
    leaders = kosaraju(ig)
    if scc_has_contradictions(leaders):
        return False
    else:
        return True
