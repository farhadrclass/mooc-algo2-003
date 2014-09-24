#!/usr/bin/env python

"""
    test_dijkstra.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""
from algorithms.dijkstra import dijkstra
from data_structures.directed_graph import DirectedGraph
import unittest


class TestSequenceFunctions(unittest.TestCase):

    def test_dijkstra_small(self):
        file_name = './data/a4/dijkstraData_small.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="adjacency list")
        shortest_path_lengths = dijkstra(graph=directed_graph, source_node=1)
        correct_answer = {1: 0, 2: 1, 3: 3, 4: 6}

        self.assertTrue(shortest_path_lengths == correct_answer)

    def test_dijkstra(self):
        file_name = './data/a4/dijkstraData.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="adjacency list")
        shortest_path_lengths = dijkstra(graph=directed_graph, source_node=1)

        nodes_of_interest = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
        correct_answer = [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]
        calculated_answer = [shortest_path_lengths[node]
                             for node in nodes_of_interest]

        self.assertTrue(calculated_answer == correct_answer)
