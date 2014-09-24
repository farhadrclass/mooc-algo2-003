#!/usr/bin/env python

"""
    test_two_sat.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""

from collections import defaultdict, Counter
import unittest
import algorithms.two_sat as ts
import data_structures.directed_graph as dg


def load_edge_list(file_name):
        graph = defaultdict(set)
        with open(file_name) as f:
            for line in f:
                head_node, tail_node = [ int(x) for x in line.strip().split() ]
                graph[head_node].add(tail_node)
        return graph

class TestSequenceFunctions(unittest.TestCase):

    def test_kosaraju(self):
        """correct answer: 434821,968,459,313,211"""
        file_name = "./data/a6/SCC.txt"
        directed_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list)
        leaders = ts.kosaraju(directed_graph)
        c = Counter(leaders.values()).most_common(5)
        five_most_frequent_leaders = sorted([pair[1] for pair in c])
        correct_answer = sorted([434821,968,459,313,211])
        self.assertEquals(five_most_frequent_leaders, correct_answer)

    def test_kosaraju_simple(self):
        file_name = "./data/a6/SCC_simple.txt"
        directed_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list)
        leaders = ts.kosaraju(directed_graph)
        correct_answer = {1: 9, 2: 3, 3: 6, 4: 9, 5: 3, 6: 6, 7: 9, 8: 3, 9: 6}
        self.assertEquals(leaders, correct_answer)
