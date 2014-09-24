"""
    test_kruskal.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

    running time:
    real    0m0.885s
    user    0m0.845s
    sys 0m0.035s

"""

from collections import defaultdict
from algorithms import prim, kruskal
from data_structures import union_find as uf
import numpy
import random
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


def generate_graph(file_name):
    """Takes as input a matrix where rows are edges and columns are [node1 node2 weight]"""

    node_matrix = numpy.loadtxt(file_name, skiprows=1)
    graph = defaultdict(dict)
    for item in node_matrix:
        node1, node2, weight = [int(n) for n in item]
        graph[node1][node2] = weight
        graph[node2][node1] = weight

    return graph


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.union_find = uf.UnionFind(range(0, 10))
        pass

    def test_find(self):
        nodes = range(0, 10)
        union_find = uf.UnionFind(nodes)
        node = random.choice(nodes)
        leader = union_find.find(node)
        self.assertTrue(node == leader)

    def test_union(self):
        nodes = range(0, 10)
        union_find = uf.UnionFind(nodes)
        leader1, leader2 = random.sample(nodes, 2)
        union_find.union(leader1, leader2)
        self.assertTrue(union_find.set_lookup[leader1] == [leader1, leader2])

    def test_kruskal_against_prim(self):
        file_name = './data/a1/edges.txt'

        #prim
        graph = generate_graph(file_name)
        prim_mst = prim.prim(graph)
        prim_total_cost = prim.get_mst_total_weight(prim_mst)
        self.assertTrue(prim_total_cost == -3612829)

        #kruskal
        node_list, edge_list = generate_edge_list(file_name)
        kruskal_mst = kruskal.kruskal(node_list=node_list, edge_list=edge_list)
        kruskal_total_cost = prim.get_mst_total_weight(kruskal_mst)
        self.assertEquals(prim_total_cost, kruskal_total_cost)

