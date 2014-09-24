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

    def test_two_sat_1(self):
        file_name = "./data/a6/2sat1.txt"
        implication_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list_sat)
        are_conditions_satisfiable = ts.two_sat_scc(implication_graph)
        correct_answer  = True
        self.assertEquals(are_conditions_satisfiable, correct_answer)

    def test_two_sat_2(self):
        file_name = "./data/a6/2sat2.txt"
        implication_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list_sat)
        are_conditions_satisfiable = ts.two_sat_scc(implication_graph)
        correct_answer  = False
        self.assertEquals(are_conditions_satisfiable, correct_answer)

    def test_two_sat_3(self):
        file_name = "./data/a6/2sat3.txt"
        implication_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list_sat)
        are_conditions_satisfiable = ts.two_sat_scc(implication_graph)
        correct_answer  = True
        self.assertEquals(are_conditions_satisfiable, correct_answer)

    def test_two_sat_4(self):
        file_name = "./data/a6/2sat4.txt"
        implication_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list_sat)
        are_conditions_satisfiable = ts.two_sat_scc(implication_graph)
        correct_answer  = True
        self.assertEquals(are_conditions_satisfiable, correct_answer)

    def test_two_sat_5(self):
        file_name = "./data/a6/2sat5.txt"
        implication_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list_sat)
        are_conditions_satisfiable = ts.two_sat_scc(implication_graph)
        correct_answer  = False
        self.assertEquals(are_conditions_satisfiable, correct_answer)

    def test_two_sat_6(self):
        file_name = "./data/a6/2sat6.txt"
        implication_graph = dg.DirectedGraph(file_name=file_name, load_function=load_edge_list_sat)
        are_conditions_satisfiable = ts.two_sat_scc(implication_graph)
        correct_answer  = False
        self.assertEquals(are_conditions_satisfiable, correct_answer)
