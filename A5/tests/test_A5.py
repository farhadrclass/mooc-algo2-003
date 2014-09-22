#!/usr/bin/env python

"""
    test_A5.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""

from algorithms.traveling_salesman import traveling_salesman
from algorithms.undirected_graph import UndirectedGraph
import unittest


class TestSequenceFunctions(unittest.TestCase):

    def test(self):
        file_name = "./data/tsp_test.txt"
        graph = UndirectedGraph(file_name)
        print traveling_salesman(graph)
        pass

    def test_A5(self):
        """ Runtime: 279.133m, yuck."""
        file_name = "./data/tsp.txt"
        graph = UndirectedGraph(file_name)
        print traveling_salesman(graph)
        pass
