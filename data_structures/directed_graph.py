#!/usr/bin/env python

"""
    directed_graph.py
    ~~~~~~~~~~~~
    Contains object for represeting directed graphs.

"""

from collections import defaultdict


class DirectedGraph(object):

    @property
    def graph(self):
        return self._graph

    @graph.setter
    def graph(self, value):
        self._graph = value

    def __init__(self, file_name=None, load_function=None, file_format="adjacency list"):
        if load_function is None:
            if file_name is not None:
                if file_format == "adjacency list":
                    self.graph = self.load_adjacency_list(file_name)
                elif file_format == "edge list":
                    self.num_nodes, self.num_edges, self.graph = self.load_edge_list(file_name)
            else:
                return
        else:
            self.graph = load_function(file_name)

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
        return str(self.graph)\


    def head_nodes(self):
        """ iterator that yields all head nodes in graph """
        for head_node in self.graph:
            yield head_node

    def tail_nodes(self):
        """ iterator that yields all tail nodes in graph """
        for head_node in self.graph:
            for tail_node in self.graph[head_node]:
                yield tail_node

    def nodes(self, graph=None):
        """ iterator that yields all nodes in graph """
        node_list = []
        if graph is None:
            graph = self.graph
        for head_node in self.graph:
            node_list.append(head_node)
            for tail_node in self.graph[head_node]:
                node_list.append(tail_node)
        for node in set(node_list):
            yield node

    def edges(self, graph=None):
        """ iterator that yields all edges in graph as (head, tail, weight) tuples """
        for head_node in self.graph:
            for tail_node in self.graph[head_node]:
                if type(self.graph[head_node] == 'list'):
                    yield head_node, tail_node
                else:
                    yield head_node, tail_node, self.graph[head_node][tail_node]

    def reversed(self):
        default = self.graph.default_factory
        if default == type({}):
            graph_rev = defaultdict(dict)
        elif default == type([]):
            graph_rev = defaultdict(list)
            for head_node in self.graph:
                for tail_node in self.graph[head_node]:
                    graph_rev[tail_node].append(head_node)
        return graph_rev



        return graph_rev
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
            num_nodes, num_edges = [int(x) for x in f.readline().strip().split()]
            for line in f:
                head_node, tail_node, weight = [
                    int(x) for x in line.strip().split()]
                graph[head_node][tail_node] = weight
        return num_nodes, num_edges, graph

