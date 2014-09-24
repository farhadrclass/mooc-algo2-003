#!/usr/bin/env python

"""
    test_a4.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
from algorithms.johnson import reweight, johnson, shortest_shortest_path
from data_structures.directed_graph import DirectedGraph
import unittest


class TestSequenceFunctions(unittest.TestCase):

    def test_g1(self):
        file_name = './data/a4/g1.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")
        all_pairs_shortest_paths = johnson(directed_graph)
        self.assertFalse(all_pairs_shortest_paths)

    def test_g2(self):
        file_name = './data/a4/g2.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")
        all_pairs_shortest_paths = johnson(directed_graph)
        self.assertFalse(all_pairs_shortest_paths)

    def test_g3(self):
        file_name = './data/a4/g3.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")
        all_pairs_shortest_paths = johnson(directed_graph)
        shortest_path = shortest_shortest_path(all_pairs_shortest_paths)
        self.assertEquals(shortest_path, -19)
