#!/usr/bin/env python

"""
    test_q1.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford_smart as bellman_ford
from algorithms.directed_graph import DirectedGraph
import unittest





class TestSequenceFunctions(unittest.TestCase):


    def test_dijkstra_small(self):
        file_name = './data/dijkstraData_small.txt'
        directed_graph  = DirectedGraph(file_name=file_name, file_format="adjacency list")
        shortest_path_lengths = dijkstra(graph=directed_graph, source_node=1)
        correct_answer = {1: 0, 2: 1, 3: 3, 4: 6}

        self.assertTrue(shortest_path_lengths == correct_answer)

    def test_dijkstra(self):
        file_name = './data/dijkstraData.txt'
        directed_graph  = DirectedGraph(file_name=file_name, file_format="adjacency list")
        shortest_path_lengths = dijkstra(graph=directed_graph, source_node=1)

        nodes_of_interest = [7,37,59,82,99,115,133,165,188,197]
        correct_answer = [2599,2610,2947,2052,2367,2399,2029,2442,2505,3068]
        calculated_answer =  [shortest_path_lengths[node] for node in nodes_of_interest]

        self.assertTrue(calculated_answer==correct_answer)

    def test_bellman_ford_small(self):
        file_name = './data/bellman_ford_small.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")

        shortest_path_lengths = bellman_ford(graph=directed_graph, source_node=1)
        correct_answer = {1: 0, 2: 2, 3: 3, 4: 4, 5: 6}
        self.assertTrue(shortest_path_lengths == correct_answer)

    def test_reweighting(self):
        file_name = './data/reweight_small.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")
        reweighted_graph  = directed_graph.reweight()
        print reweighted_graph

    def _test_johnson(self):
        file_name = './data/reweight_small.txt'
        directed_graph = dg.DirectedGraph(file_name=file_name, file_format="edge list")
        directed_graph.johnson()

