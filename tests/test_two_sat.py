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

def load_edge_list_sat(file_name):
        graph = defaultdict(set)
        with open(file_name) as f:
            f.next()
            for line in f:
                u, v = [ int(x) for x in line.strip().split() ]
                graph[-u].add(v)
                graph[-v].add(u)
        return graph


class TestSequenceFunctions(unittest.TestCase):

    def _test_kosaraju(self):
        """correct answer: 434821,968,459,313,211"""
        file_name = "./data/a6/SCC.txt"
        directed_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list)
        leaders = ts.kosaraju(directed_graph)

    def test_kosaraju_simple(self):
        file_name = "./data/a6/SCC_simple.txt"
        directed_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list)
        leaders = ts.kosaraju(directed_graph)
        self.assertEquals(leaders, {1: 9, 2: 3, 3: 6, 4: 9, 5: 3, 6: 6, 7: 9, 8: 3, 9: 6})

    def test_condensation(self):
        file_name = "./data/a6/SCC_simple.txt"
        directed_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list)
        leaders = ts.kosaraju(directed_graph)
        condensed_graph = dg.DirectedGraph(graph=ts.condense(directed_graph, leaders))
        self.assertEquals(set([node for node in condensed_graph.nodes()]), set([3,6,9]))

    def test_two_sat_1(self):
        file_name = "./data/a6/2sat1.txt"
        implication_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list_sat)
        two_sat = ts.two_sat_scc(implication_graph)
        print two_sat

    def test_two_sat_2(self):
        file_name = "./data/a6/2sat2.txt"
        implication_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list_sat)
        two_sat = ts.two_sat_scc(implication_graph)
        print two_sat

    def test_two_sat_3(self):
        file_name = "./data/a6/2sat3.txt"
        implication_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list_sat)
        two_sat = ts.two_sat_scc(implication_graph)
        print two_sat

    def test_two_sat_4(self):
        file_name = "./data/a6/2sat4.txt"
        implication_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list_sat)
        two_sat = ts.two_sat_scc(implication_graph)
        print two_sat

    def test_two_sat_5(self):
        file_name = "./data/a6/2sat5.txt"
        implication_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list_sat)
        two_sat = ts.two_sat_scc(implication_graph)
        print two_sat

    def test_two_sat_6(self):
        file_name = "./data/a6/2sat6.txt"
        implication_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list_sat)
        two_sat = ts.two_sat_scc(implication_graph)
        print two_sat
