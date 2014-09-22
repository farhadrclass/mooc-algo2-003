#!/usr/bin/env python

"""
    test_directed_graph.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""
import unittest
from collections import defaultdict
from data_structures import directed_graph as dg


def load_edge_list(file_name):
        graph = defaultdict(list)
        with open(file_name) as f:
            for line in f:
                u, v = [ int(x) for x in line.strip().split() ]
                graph[u].append(v)
        return graph
def load_edge_list_rev(file_name):
        graph = defaultdict(list)
        with open(file_name) as f:
            for line in f:
                u, v = [ int(x) for x in line.strip().split() ]
                graph[v].append(u)
        return graph

class TestSequenceFunctions(unittest.TestCase):
    def test_rev(self):
        file_name = "./data/a6/SCC_simple.txt"
        directed_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list)
        directed_graph_rev= dg.DirectedGraph(file_name=file_name, load_function=load_edge_list_rev)
        self.assertEquals(directed_graph.reversed(), directed_graph_rev.graph)
