#!/usr/bin/env python

"""
    test_bellman_ford.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""
from algorithms.bellman_ford import bellman_ford
from data_structures.directed_graph import DirectedGraph
import unittest


class TestSequenceFunctions(unittest.TestCase):

    def test_bellman_ford_small(self):
        file_name = './data/a4/bellman_ford_small.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")

        shortest_path_lengths = bellman_ford(graph=directed_graph, source_node=1)
        correct_answer = {1: 0, 2: 2, 3: 3, 4: 4, 5: 6}
        self.assertTrue(shortest_path_lengths == correct_answer)
