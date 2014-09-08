#!/usr/bin/env python

"""
    test_q1.py
    ~~~~~~~~~~~~

"""

from clustering import kruskal
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
        file_name = './data/clustering1.txt'
        node_list, edge_list = generate_edge_list(file_name)
        maximum_spacing = kruskal.maximum_spacing(node_list, edge_list, 4)
        print maximum_spacing

    def test_q2_small1(self):
        file_name = './data/clustering_small1.txt'
        node_array, node_length = load_hamming(file_name)
        max_k = kruskal.maximum_k(node_array, node_length=node_length)
        self.assertTrue(max_k, 1)

    def test_q2_small2(self):
        file_name = './data/clustering_small2.txt'
        node_array, node_length = load_hamming(file_name)
        max_k = kruskal.maximum_k(node_array, node_length=node_length)
        self.assertTrue(max_k, 3)

    def _test_q2(self):
        """ Run 1: 167.636s"""
        file_name = './data/clustering_big.txt'
        node_array, node_length = load_hamming(file_name)
        max_k = kruskal.maximum_k(
            node_array, node_length=node_length, max_spacing=3)
        self.assertTrue(max_k, 6118)
