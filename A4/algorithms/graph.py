#!/usr/bin/env python

"""
    graph.py
    ~~~~~~~~~~~~
    Contains graph algorithms for computing the all-pairs shortest path of a directed graph.

"""

from heap import Heap

def load_data(file_name):
    pass

def dijkstra(directed_graph, source_node):
    """ Return shortest path computed by Dijkstra's algorithm. """
    shortest_path_lengths = {}
    crossing_cuts = Heap([((float("inf"), float("inf")), int(node)) for node in graph.keys() if node != source_node])

    for node in directed_graph[source_node].keys():
        new_key = (directed_graph[source_node][node], source_node)

    pass

def bellman_ford(graph):
    pass

def johnson(graph):
    pass
