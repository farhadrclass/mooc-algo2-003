#!/usr/bin/env python

"""
    test_traveling_salesman.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""

from algorithms.traveling_salesman import traveling_salesman
from data_structures import undirected_graph as ug
import math
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test_traveling_salesman_small(self):
        file_name = "./data/a5/tsp_test.txt"
        graph = ug.UndirectedGraph(file_name)
        correct_answer = float(8 * math.sqrt(2))

        answer_error = abs(traveling_salesman(graph) - correct_answer)
        allowable_error = 1e-12

        self.assertTrue(answer_error < allowable_error)

