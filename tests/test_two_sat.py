#!/usr/bin/env python

"""
    test_two_sat.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""
import unittest
from collections import defaultdict, Counter
import algorithms.two_sat as ts
import data_structures.directed_graph as dg


def load_edge_list(file_name):
        graph = defaultdict(list)
        with open(file_name) as f:
            for line in f:
                head_node, tail_node = [ int(x) for x in line.strip().split() ]
                graph[head_node].append(tail_node)
        return graph

class TestSequenceFunctions(unittest.TestCase):
    def _test_depth_first_search(self):
        file_name = "./data/a6/SCC.txt"
        pass
    def test_kosaraju(self):
        """correct answer: 434821,968,459,313,211"""
        file_name = "./data/a6/SCC.txt"
        directed_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list)
        leaders = ts.kosaraju(directed_graph)
        print Counter(leaders.values()).most_common(5)

    def test_kosaraju_simple(self):
        """ correct_answer: 3, 3, 3"""
        file_name = "./data/a6/SCC_simple.txt"
        directed_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list)
        leaders = ts.kosaraju(directed_graph)
        print Counter(leaders.values()).most_common(5)

    def _test_two_sat(self):
        pass
