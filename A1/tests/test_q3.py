#!/usr/bin/env python

from heap.heap import Heap
from collections import defaultdict
import numpy
import random
import unittest

def load_data(file_name, skiprows=1):
    """ Returns matrix of  node and edges from edges.txt"""
    with open(file_name, 'r') as f:
        num_nodes, num_edges = [int(n) for n in f.readline().strip().split()]

    node_matrix = numpy.loadtxt(file_name, skiprows=skiprows)

    return num_nodes, num_edges, node_matrix


def generate_graph(node_matrix):
    """Takes as input a matrix where rows are edges and columns are [node1 node2 weight]"""
    graph = defaultdict(dict)

    for item in node_matrix:
        node1, node2, weight = [int(n) for n in item]
        graph[node1][node2] = weight
        graph[node2][node1] = weight

    return graph


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):

        self.file_name = './data/edges.txt'
        self.num_nodes, self.num_edges, self.node_matrix = load_data(
            self.file_name)
        self.graph = generate_graph(self.node_matrix)

    def tearDown(self):
        pass

    def test_q3(self):
        print self.graph


if __name__ == '__main__':
    unittest.main()
