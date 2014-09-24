#!/usr/bin/env python

"""
    test_a2.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

    running time:
    real    0m23.838s
    user    0m23.761s
    sys 0m0.071s

"""

from algorithms import kruskal
import array
import numpy
import string
import sys
import unittest


def load_data(file_name, skiprows=1):
    """ Returns matrix of  node and edges from .txt file"""
    return numpy.loadtxt(file_name, skiprows=skiprows)


def generate_edge_list(file_name):
    node_list = set()
    edge_list = []
    with open(file_name) as f:
        num_nodes = int(f.readline().strip().split()[0])
        for line in f:
            node1, node2, weight = [int(n) for n in line.strip().split()]
            node_list.add(node1)
            node_list.add(node2)
            edge_list.append((weight, node1, node2))
    return node_list, edge_list


def load_hamming(file_name):
    node_array = array.array('I')
    with open(file_name) as f:
        num_nodes, node_length = [int(n) for n in f.readline().strip().split()]
        for line in f:
            node = int(string.join(line.strip().split(), ''), 2)
            node_array.append(node)
    return node_array, node_length


class TestSequenceFunctions(unittest.TestCase):

    def test_q1(self):
        """ time:
        real    0m0.740s
        user    0m0.702s
        sys     0m0.035s
        """

        file_name = './data/a2/clustering1.txt'
        node_list, edge_list = generate_edge_list(file_name)
        maximum_spacing = kruskal.maximum_spacing(node_list, edge_list, 4)
        correct_answer = 106
        self.assertEquals(maximum_spacing, correct_answer)

    def test_q2_small1(self):
        file_name = './data/a2/clustering_small1.txt'
        node_array, node_length = load_hamming(file_name)
        max_k = kruskal.maximum_k(node_array, node_length=node_length)
        self.assertTrue(max_k, 1)

    def test_q2_small2(self):
        file_name = './data/a2/clustering_small2.txt'
        node_array, node_length = load_hamming(file_name)
        max_k = kruskal.maximum_k(node_array, node_length=node_length)
        self.assertTrue(max_k, 3)

    def test_q2(self):
        """ time:
        real    0m24.678s
        user   0m24.584s
        sys     0m0.077s
        """

        file_name = './data/a2/clustering_big.txt'
        node_array, node_length = load_hamming(file_name)
        max_k = kruskal.maximum_k(node_array, node_length=node_length, maximum_spacing=3)
        correct_answer = 6118
        self.assertEquals(max_k, correct_answer)
