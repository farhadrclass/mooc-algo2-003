"""
    dijkstra.py
    ~~~~~~~~~~~~
    Contains Dijkstra algorithm for computing the single source shortest paths of a graph.
"""

from heap import Heap

def dijkstra(graph=None, source_node=1):
        """ Return shortest path lengths computed by Dijkstra's algorithm. """
        if graph is None:
            return None

        shortest_path_lengths = {}  #dict for keeping track of shortest path legnths

        # min heap to keep track of crossing cuts
        crossing_cuts = Heap([(float("inf"), int(node)) for node in graph.nodes()])
        crossing_cuts.update_key(source_node, 0)

        # main algorithm body
        while crossing_cuts:
            # get smallest crossing cut cut
            shortest_cut = crossing_cuts.pop()
            head_node, path_length = shortest_cut.name, shortest_cut.key
            shortest_path_lengths[head_node] = path_length
            # update heap
            unadded_tail_nodes = set(graph[head_node]) - set(shortest_path_lengths)
            for tail_node in unadded_tail_nodes:
                old_key = crossing_cuts[tail_node].key
                new_key = shortest_path_lengths[head_node] + graph[head_node][tail_node]
                if new_key < old_key:
                    crossing_cuts.update_key(tail_node, new_key)

        return shortest_path_lengths
