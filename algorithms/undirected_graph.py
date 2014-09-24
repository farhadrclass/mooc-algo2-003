#!/usr/bin/env python

"""
    undirected_graph.py
    ~~~~~~~~~~~~
    Contains object for represeting undirected graphs.

"""

from itertools import combinations
from collections import defaultdict
from math import sqrt


class UndirectedGraph(object):

    @property
    def graph(self):
        return self._graph

    @graph.setter
    def graph(self, value):
        self._graph = value

    def __init__(self, file_name=None, file_format="coordinates"):
        if file_name is not None:
            if file_format == "coordinates":
                self.graph = self.load_coordinates(file_name)

    def __getitem__(self, key):
        return self.graph[key]

    def __setitem__(self, key, item):
        self.graph[key] = item

    def __delitem__(self, key):
        del self.graph[key]

    def __iter__(self):
        for head_node in self.graph:
            yield head_node

    def __len__(self):
        """ Return number of all head/tail nodes in directed graph"""
        return len([x for x in self.nodes()])

    def __str__(self):
        return str(self.graph)

    def nodes(self):
        """ iterator that yields all nodes in graph """
        node_list = []
        for head_node in self.graph:
            node_list.append(head_node)
            for tail_node in self.graph[head_node]:
                node_list.append(tail_node)
        for node in set(node_list):
            yield node

    def edges(self):
        """ iterator that yields all edges in graph as (head, tail, weight) tuples """
        for head_node in self.graph:
            for tail_node in self.graph[head_node]:
                yield head_node, tail_node, self.graph[head_node][tail_node]

    def load_coordinates(self, file_name):
        graph = defaultdict(dict)
        coordinates = {}
        with open(file_name) as f:
            f.next()
            for i, line in enumerate(f):
                x, y = [float(n) for n in line.strip().split()]
                coordinates[i+1] = (x,y)
            for v1, v2 in combinations(coordinates, 2):
                x1, y1 = coordinates[v1]
                x2, y2 = coordinates[v2]
                euclidean_distance = sqrt(pow((x1-x2),2) + pow((y1-y2),2))
                graph[v1][v2] = euclidean_distance
                graph[v2][v1] = euclidean_distance
        return graph
