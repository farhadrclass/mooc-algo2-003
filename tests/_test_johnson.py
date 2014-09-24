#!/usr/bin/env python

"""
    test_johnson.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""
from algorithms.johnson import reweight, johnson, shortest_shortest_path
from data_structures.directed_graph import DirectedGraph
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test_reweighting(self):
        file_name = './data/a4/reweight_small.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")
        reweighted_graph, node_weights = reweight(directed_graph)
        correct_answer = {1: {2: 0}, 2: {3: 0}, 3: {1: 1, 4: 0, 5: 0}, 6: {4: 2, 5: 2}}
        for node in correct_answer:
            self.assertTrue(reweighted_graph[node] == correct_answer[node])

    def test_negative_weight_cycle(self):
        file_name = './data/a4/negative_weight_cycle.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")
        all_pairs_shortest_paths = johnson(directed_graph)
        self.assertFalse(all_pairs_shortest_paths)

    def test_shortest_shortest_paths(self):
        file_name = './data/a4/testcase_1.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")
        all_pairs_shortest_paths = johnson(directed_graph)
        shortest_path = shortest_shortest_path(all_pairs_shortest_paths)
        self.assertEquals(shortest_path, -2)

    def test_johnson_small(self):
        file_name = './data/a4/reweight_small.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")
        all_pairs_shortest_paths = johnson(directed_graph)
