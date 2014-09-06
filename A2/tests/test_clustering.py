#!/usr/bin/env python

"""
    test_clustering.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""
from clustering.clustering import UnionFind
from collections import defaultdict
from clustering.prim import prim
import numpy
import random
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
        self.union_find = UnionFind(range(0,10))
        pass

    def test_find(self):
        nodes = range(0,10)
        union_find = UnionFind(nodes)
        node = random.choice(nodes)
        leader = union_find.find(node)
        self.assertTrue(node == leader)

    def test_union(self):
        nodes = range(0,10)
        union_find = UnionFind(nodes)
        leader1, leader2 = random.sample(nodes, 2)
        union_find.union(leader1, leader2)
        self.assertTrue(union_find.set_lookup[leader1] == [leader1, leader2])

    def test_kruskal_against_prim(self):
        graph = generate_graph(load_data('../A1/data/edges.txt'))
        prim_mst = prim.prim(graph)
        prim_total_cost = prim.get_mst_total_weight(prim_mst)
        self.assertTrue(prim_total_cost == -3612829)
        # print "Total cost of minimum spanning tree built with Prim's MST algorithm: {}".format(prim_total_cost)


