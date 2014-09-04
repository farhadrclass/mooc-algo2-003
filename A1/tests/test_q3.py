#!/usr/bin/env python

"""
    test_q3.py
    ~~~~~~~~~~~~
    For Programming Assignment #1, Algorithms: Design and Analysis Part 2 (https://class.coursera.org/algo2-003)

    Implements Prim's Spanning Tree Algorithm in O(VlogE) time (V: # vertices, E: # edges) in a graph using a minimum heap.
"""

from heap.heap import Node, Heap
from collections import defaultdict
import numpy
import random
import unittest


def load_data(file_name, skiprows=1):
    """ Returns matrix of  node and edges from edges.txt"""
    with open(file_name, 'r') as f:
        num_nodes, num_edges = [int(n) for n in f.readline().strip().split()]

    node_matrix = numpy.loadtxt(file_name, skiprows=skiprows)

    return node_matrix


def generate_graph(node_matrix):
    """Takes as input a matrix where rows are edges and columns are [node1 node2 weight]"""
    graph = defaultdict(dict)

    for item in node_matrix:
        node1, node2, weight = [int(n) for n in item]
        graph[node1][node2] = weight
        graph[node2][node1] = weight

    return graph


def prim(graph):
    """
    Implements Prim's Minimum Spanning Tree Algorithm in O(VlogE) time with a min heap.
    """
    minimum_spanning_tree = defaultdict(dict)
    initial_node = random.choice(graph.keys())

    # Initialize minimum heap to contain the nodes of the graph, whose keys
    # are the edge values
    crossing_cuts = Heap([((float("inf"), float("inf")), int(node))
                          for node in graph.keys() if node != initial_node])

    # Populate min heap with initial node's crossing cuts
    for node_name in graph[initial_node].keys():
        new_key = (graph[initial_node][node_name], initial_node)
        crossing_cuts.update_key(node_name, new_key)

    # Pop nodes from minimum heap until minimum spanning tree is formed
    while crossing_cuts:
        smallest_node = crossing_cuts.pop()
        (node_out, (weight, node_in)) = smallest_node.name, smallest_node.key
        minimum_spanning_tree[node_in][node_out] = weight
        minimum_spanning_tree[node_out][node_in] = weight

        for node_name in (set(graph[node_out].keys()) - set(minimum_spanning_tree.keys())):
            new_key = (graph[node_out][node_name], node_out)
            if node_name in crossing_cuts.node_names():
                old_key = crossing_cuts[node_name].key
                if new_key[0] < old_key[0]:
                    crossing_cuts.update_key(node_name, new_key)

    return minimum_spanning_tree


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.node_matrix = load_data('./data/edges.txt')
        self.graph = generate_graph(self.node_matrix)

    def test_q3(self):
        minimum_spanning_tree = prim(self.graph)
        total_cost = 0
        for node in minimum_spanning_tree.keys():
            total_cost += sum(minimum_spanning_tree[node].values())

        # Divide total by 2 so that we don't double count
        total_cost = total_cost / 2
        print "Total cost of minimum spanning tree built with Prim's MST algorithm: {}".format(total_cost)
