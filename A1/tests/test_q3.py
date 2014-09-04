#!/usr/bin/env python

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

    return num_nodes, num_edges, node_matrix


def generate_graph(node_matrix):
    """Takes as input a matrix where rows are edges and columns are [node1 node2 weight]"""
    graph = defaultdict(dict)

    for item in node_matrix:
        node1, node2, weight = [int(n) for n in item]
        graph[node1][node2] = weight
        graph[node2][node1] = weight

    return graph

def prim(graph):
    minimum_spanning_tree = defaultdict(dict)
    initial_node = random.choice(graph.keys())

    crossing_cuts = Heap([((float("inf"), float("inf")), int(node)) for node in graph.keys() if node != initial_node])
    for node_name in graph[initial_node].keys():
        new_key = (graph[initial_node][node_name], initial_node)

        crossing_cuts.update_key(node_name, new_key)
    print crossing_cuts
    return minimum_spanning_tree
    # print crossing_cuts
    # while crossing_cuts:
    #     smallest_node = crossing_cuts.pop()
    #     (node_out, (weight, node_in)) = smallest_node.name, smallest_node.key
    #     minimum_spanning_tree[node_in][node_out] = weight
    #     minimum_spanning_tree[node_out][node_in] = weight

    #     for node_name in (set(graph[node_out].keys()) - set(minimum_spanning_tree.keys())):
    #         new_key = (graph[node_out][node_name], node_out)
    #         if node_name in crossing_cuts.node_names():
    #             old_key =   crossing_cuts[node_name].key
    #             if new_key < old_key:
    #                 crossing_cuts.update_key(node_name, new_key)
    #         else:
    #             crossing_cuts.insert(Node(name=node_name, key=new_key))
    #     break
    # return minimum_spanning_tree



class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):

        self.file_name = './data/edges.txt'
        self.num_nodes, self.num_edges, self.node_matrix = load_data(
            self.file_name)
        self.graph = generate_graph(self.node_matrix)

    def tearDown(self):
        pass

    def _test_crossing_cut_initialization(self):
        crossing_cuts = Heap([   (float("inf"), int(node)) for node in self.graph.keys()    ])
        initial_node = random.choice(self.graph.keys())
        for node_name in self.graph[initial_node].keys():
            crossing_cuts.update_key(node_name, self.graph[initial_node][node_name])

        self.assertTrue(crossing_cuts.is_heap_property_satisfied())
    def test_prim(self):
        minimum_spanning_tree = prim(self.graph)

    def _test_q3(self):
        pass


if __name__ == '__main__':
    unittest.main()
