#!/usr/bin/env python

"""
    test_a5.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""

from algorithms.traveling_salesman import traveling_salesman
from data_structures import undirected_graph as ug
import math
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test_a5(self):
        """ Runtime: 279.133m, yuck."""
        file_name = "./data/a5/tsp.txt"
        graph = ug.UndirectedGraph(file_name)
        correct_answer = float(26442)
        self.assertEquals(math.floor(traveling_salesman(graph), correct_answer))

