#!/usr/bin/env python

"""
    graph.py
    ~~~~~~~~~~~~
    Contains graph algorithms for computing the all-pairs shortest path of a directed graph.

"""

import copy
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
            elif file_format == "edge list":
                self.num_nodes, self.num_edges, self.graph = self.load_edge_list(file_name=file_name)

    def __getitem__(self, key):
        return self.graph[key]

    def __iter__(self):
        for head_node in self.graph:
            yield head_node

    def __len__(self):
        return len([x for x in self.nodes()])

    def nodes(self, graph=None):
        node_list = []
        if graph is None:
            graph = copy.deepcopy(self.graph)
        for head_node in self.graph:
            node_list.append(head_node)
            for tail_node in self.graph[head_node]:
                node_list.append(tail_node)
        for node in set(node_list):
            yield node

    def edges(self, graph=None):
        if graph is None:
            graph = copy.deepcopy(self.graph)
        for head_node in self.graph:
            for tail_node in self.graph[head_node]:
                yield head_node, tail_node, self.graph[head_node][tail_node]

    def load_adjacency_list(self, file_name):
        graph = defaultdict(dict)
        with open(file_name) as f:
            for line in f:
                line = line.strip().split()
                head_node = int(line[0])
                graph[head_node] = {}
                for item in line[1:]:
                    tail_node, weight = [int(x) for x in item.split(',')]
                    graph[head_node][tail_node] = weight
        return graph

    def load_edge_list(self, file_name):
        graph = defaultdict(dict)
        with open(file_name) as f:
            num_nodes, num_edges = [int(x)
                                    for x in f.readline().strip().split()]
            for line in f:
                head_node, tail_node, weight = [
                    int(x) for x in line.strip().split()]
                graph[head_node][tail_node] = weight
        return num_nodes, num_edges, graph







    def reweight(self, graph=None):
        """ Reweights graph to have non-negative edge lengths while preserving shortest-path relations"""
        if graph is None:
            graph = copy.deepcopy(self.graph)

        # insert psuedo-node with distance 0 to every node in graph
        graph[0] = {node: 0 for node in self.nodes(graph)}

        # get reweight values for each node with bellman ford algorithm
        node_weights = self.bellman_ford_smart(graph=graph, source_node=0)

        # delete pseudo-node
        del graph[0]

        # reweight nodes
        reweighted_graph = defaultdict(dict)

        for edge in self.edges(graph):
            head_node, tail_node, weight = edge
            reweighted_graph[head_node][tail_node] = weight + node_weights[head_node] - node_weights[tail_node]

        reweighted_graph = DirectedGraph()

        return reweighted_graph


