#!/usr/bin/env python

"""
    test_q1.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
from algorithms.johnson import reweight, johnson, shortest_shortest_path
from algorithms.directed_graph import DirectedGraph
import unittest


class TestSequenceFunctions(unittest.TestCase):

    def _test_dijkstra_small(self):
        file_name = './data/dijkstraData_small.txt'
        directed_graph = DirectedGraph(
            file_name=file_name, file_format="adjacency list")
        shortest_path_lengths = dijkstra(graph=directed_graph, source_node=1)
        correct_answer = {1: 0, 2: 1, 3: 3, 4: 6}

        self.assertTrue(shortest_path_lengths == correct_answer)

    def _test_dijkstra(self):
        file_name = './data/dijkstraData.txt'
        directed_graph = DirectedGraph(
            file_name=file_name, file_format="adjacency list")
        shortest_path_lengths = dijkstra(graph=directed_graph, source_node=1)

        nodes_of_interest = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
        correct_answer = [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]
        calculated_answer = [shortest_path_lengths[node]
                             for node in nodes_of_interest]

        self.assertTrue(calculated_answer == correct_answer)

    def _test_bellman_ford_small_naive(self):
        file_name = './data/bellman_ford_small.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")

        shortest_path_lengths = bellman_ford_naive(graph=directed_graph, source_node=1)
        correct_answer = {1: 0, 2: 2, 3: 3, 4: 4, 5: 6}
        self.assertTrue(shortest_path_lengths == correct_answer)

    def _test_bellman_ford_small_smart(self):
        file_name = './data/bellman_ford_small.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")

        shortest_path_lengths = bellman_ford_smart(graph=directed_graph, source_node=1)
        correct_answer = {1: 0, 2: 2, 3: 3, 4: 4, 5: 6}
        self.assertTrue(shortest_path_lengths == correct_answer)

    def _test_reweighting(self):
        file_name = './data/reweight_small.txt'
        directed_graph = DirectedGraph(
            file_name=file_name, file_format="edge list")
        reweighted_graph = reweight(directed_graph)
        correct_answer = {1: {2: 0}, 2: {3: 0}, 3: {1: 1, 4: 0, 5: 0}, 6: {4: 2, 5: 2}}
        for node in correct_answer:
            self.assertTrue(reweighted_graph[node] == correct_answer[node])

    def _test_johnson_small(self):
        file_name = './data/reweight_small.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")
        all_pairs_shortest_paths = johnson(directed_graph)

    def _test_negative_weight_cycle(self):
        file_name = './data/negative_weight_cycle.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")
        all_pairs_shortest_paths = johnson(directed_graph)
        self.assertFalse(all_pairs_shortest_paths)

    def testcase_1(self):
        file_name = './data/testcase_1.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")
        all_pairs_shortest_paths = johnson(directed_graph)
        shortest_path = shortest_shortest_path(all_pairs_shortest_paths)

        self.assertEquals(shortest_path, -2)
    def _test_g1(self):
        file_name = './data/g1.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")
        all_pairs_shortest_paths = johnson(directed_graph)
        self.assertFalse(all_pairs_shortest_paths)
    def _test_g2(self):
        file_name = './data/g2.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")
        all_pairs_shortest_paths = johnson(directed_graph)
        self.assertFalse(all_pairs_shortest_paths)
    def _test_g3(self):
        file_name = './data/g3.txt'
        directed_graph = DirectedGraph(file_name=file_name, file_format="edge list")
        all_pairs_shortest_paths = johnson(directed_graph)
        shortest_path = shortest_shortest_path(all_pairs_shortest_paths)
        self.assertEquals(shortest_path, -19)
