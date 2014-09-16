#!/usr/bin/env python

"""
    graph.py
    ~~~~~~~~~~~~
    Contains graph algorithms for computing the all-pairs shortest path of a directed graph.

"""

from heap import Heap
from collections import defaultdict

class DirectedGraph(object):

    @property
    def graph(self):
        return self._graph
    @graph.setter
    def graph(self, value):
        self._graph = value

    def __init__(self, file_name=None, file_format="adjacency list"):
        if file_name is not None:
            if file_format == "adjacency list":
                self.graph = self.load_adjacency_list(file_name)

    def load_adjacency_list(self, file_name):
        graph = defaultdict(dict)
        with open(file_name) as f:
            for line in f:
                line= line.strip().split()
                head_node = int(line[0])
                graph[head_node] = {}
                for item in line[1:]:
                    tail_node, weight = [ int(x) for x in item.split(',') ]
                    graph[head_node][tail_node] = weight
        return graph

    def dijkstra(self, source_node=1):
        """ Return shortest path computed by Dijkstra's algorithm. """
        source_node = int(source_node)
        shortest_path_lengths = {}

        # Heap object to keep track of crossing cuts
        crossing_cuts = Heap([(float("inf"), int(node)) for node in self.graph.keys()])
        crossing_cuts.update_key(source_node, 0)

        while crossing_cuts:
            shortest_cut = crossing_cuts.pop()

            head_node, path_length = shortest_cut.name, shortest_cut.key
            shortest_path_lengths[head_node] = path_length
            #update heap
            for tail_node in set(self.graph[head_node].keys()) - set(shortest_path_lengths.keys()):
                old_key = crossing_cuts[tail_node].key
                new_key = shortest_path_lengths[head_node] + self.graph[head_node][tail_node]
                if new_key < old_key:
                    crossing_cuts.update_key(tail_node, new_key)
        return shortest_path_lengths


    def bellman_ford(self):
        pass

    def johnson(self):
        pass
