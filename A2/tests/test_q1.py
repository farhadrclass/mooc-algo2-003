#!/usr/bin/env python

"""
    test_q1.py
    ~~~~~~~~~~~~

"""

from collections import defaultdict
import numpy
import unittest


def load_data(file_name, skiprows=1):
    """ Returns matrix of  node and edges from .txt file"""
    return numpy.loadtxt(file_name, skiprows=skiprows)


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
        self.node_matrix = load_data('./data/clustering1.txt')
        self.graph = generate_graph(self.node_matrix)
        pass

    def _test(self):
        pass
