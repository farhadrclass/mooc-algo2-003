#!/usr/bin/python

import math
import numpy
import random
import unittest
from collections import defaultdict


class Node(object):

    def __init__(self, key=None, name=None):
        self._pos = float("inf")
        self._key = key
        self._name = name

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __repr__(self):
        return self.key

    def __str__(self):
        return "Name: {}, Key: {}".format(self.name, self.key)

    def __lt__(self, other):
        return self.key < other.key

    def __eq__(self, other):
        return [self.var == other.var for var in vars(self)]

class Heap(object):

    def __init__(self, array=[], mode='min', named=True):
        self._node_array = [Node(node[0], node[1])
                            for node in array]  # contains Nodes
        self._node_lookup = {}  # enable node position lookup
        self.mode = mode
        self.named = named

        self.heapify()

    @property
    def node_array(self):
        return self._node_array

    @node_array.setter
    def node_array(self, value):
        self._node_array = value

    @property
    def node_lookup(self):
        return self._node_lookup

    @node_lookup.setter
    def node_lookup(self, value):
        self._node_lookup = value

    def __repr__(self):
        if self.named:
            return str([(node.key, node.name) for node in self.node_array])
        else:
            return str([node.key for node in self.node_array])
        return

    def __getitem__(self, key):
        return self.node_array[self._node_lookup[key]]

    def __len__(self):
        return len(self.array)

    # def get_pos(self, name):
        # lookup_table = self._node_lookup

    def heapify(self):
        self.node_array = sorted(self.node_array, key=lambda node: node.key)
        self.node_array = reversed(self.node_array) if self.mode == 'max'

        for index, node in enumerate(self.node_array):
            node.pos = index
            self.node_array[index] = node
            self.node_lookup[node.name] = node.pos

    def insert(self, node):
        node.pos = len(self.node_array)
        self.node_array.append(node)
        self.bubble_up()
        pass

    def delete(self, node):
        self.swap_nodes
        pass

    def swap_nodes(self, node1, node2):
        node1.pos, node2.pos = node2.pos, node1.pos
        self.node_array[node1.pos], self.node_array[node2.pos] = node1, node2
        self.node_lookup[node1.name], self.node_lookup[node2.name] = node1.pos, node2.pos

    def bubble_up(self, child_pos=None):
        if child_pos is None:
            child_pos = len(self.node_array) - 1
        while child_pos > 0:
            parent_pos = (child_pos) // 2
            child_node = self.node_array[child_pos]
            parent_node = self.node_array[parent_pos]

            if child_node < parent_node:
                self.swap_nodes(child_node, parent_node)
                child_pos = parent_pos
                continue
            else:
                break

    def bubble_down(self, parent_pos=0):
        max_num_parents = self.max_num_parents()
        while parent_pos < max_num_parents:
            parent_node = self.node_array[parent_pos]
            left_child_node, right_child_node = self.get_children(parent_node)

            if (parent_node < left_child_node) and (parent_node < right_child_node):
                break
            else:
                if left_child_node < right_child_node:
                    self.swap_nodes(parent_node, left_child_node)
                else:
                    self.swap_nodes(parent_node, right_child_node)
                parent_pos = parent_node.pos
                continue

    def delete(self):
        pass

    def return_min(self):
        pass

    def max_num_parents(self):
        return int(math.pow(2, math.floor(math.log(len(self.node_array), 2))) - 1)

    def get_children(self, parent_node):
        parent_pos = parent_node.pos
        left_child_pos = (parent_pos + 1) * 2 - 1
        right_child_pos = (parent_pos + 1) * 2

        children_nodes = []
        for pos in [left_child_pos, right_child_pos]:
            try:
                children_nodes.append(self.node_array[pos])
            except IndexError:
                pass

        return children_nodes

    def is_heap_property_satisfied(self):
        for parent_pos in xrange(0, self.max_num_parents()):
            parent_node = self.node_array[parent_pos]
            children_nodes = self.get_children(parent_node)
            if self.mode == 'min':
                for child_node in children_nodes:
                    if parent_node > child_node:
                        return False
        else:
            return True


"""
Question 3 - Prim's Minimum Spanning Tree Algorithm
"""


def load_data(file_name, skiprows=1):
    with open(file_name, 'r') as f:
        num_nodes, num_edges = [int(n) for n in f.readline().strip().split()]

    node_matrix = numpy.loadtxt(file_name, skiprows=skiprows)

    return num_nodes, num_edges, node_matrix


def generate_graph(node_matrix):
    """
    Takes as input a matrix where rows are edges and columns are [node1 node2 weight]
    """
    graph = defaultdict(dict)
    for item in node_matrix:
        node1, node2, weight = [int(n) for n in item]
        graph[node1][node2] = weight
        graph[node2][node1] = weight

    return graph


def prim(graph):
    """ If only there were a heapdict... """

    all_vertices = set(graph.keys())
    new_graph = defaultdict(dict)

#     crossing_edges = {}

#     next_vertex = random.choice(list(all_vertices))
#     crossing_edges
#     print graph[initial_node]
#     while (all_vertices - set(new_graph.keys())):
#         new_crossing_nodes = set(graph[new_node].keys()) - set(new_graph.keys())
#         for vertex in :
#             next_vertex
#         crossing_edges[]
#         break

#     return new_graph
#     pass


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.file_name = 'edges.txt'
        self.num_nodes, self.num_edges, self.node_matrix = load_data(
            self.file_name)
        self.graph = generate_graph(self.node_matrix)

    def tearDown(self):
        pass

    def test_Node(self):
        node = Node(name="name", key="key")
        node.pos = 0
        self.assertTrue(
            all((node.name == "name", node.key == "key", node.pos == 0)))

    def test_Node_cmp(self):
        node1 = Node(20, "node1")
        node2 = Node(1, "node2")
        self.assertTrue(node2 < node1)

    def test_Heap(self):
        node1 = (20, "node1")
        node2 = (1, "node2")
        heap = Heap([node1, node2], named=True)
        self.assertTrue(heap["node1"].pos == 1 and heap["node2"].pos == 0)

    def test_Heap_bubble_up(self):
        heap = Heap([(int(x), str(x))
                     for x in random.sample(xrange(10, 100), 10)])
        node = Node(1, "1")
        node.pos = len(heap.node_array)
        heap.node_array.append(node)

        self.assertFalse(heap.is_heap_property_satisfied())
        heap.bubble_up()
        self.assertTrue(heap.is_heap_property_satisfied())

    def test_Heap_bubble_down(self):
        heap = Heap([(int(x), str(x))
                     for x in random.sample(xrange(0, 90), 10)])
        node = Node(100, "100")
        node.pos = 0
        heap.node_array[0] = node

        self.assertFalse(heap.is_heap_property_satisfied())
        heap.bubble_down()
        self.assertTrue(heap.is_heap_property_satisfied())

    def test_Heap_getitem(self):
        heap = Heap([(int(x), str(x))
                     for x in random.sample(xrange(0, 100), 10)])
        node = random.choice(heap.node_array)
        # self.assertTrue(heap[node.name] == node)
        print
        print node.pos
        print vars(node)



if __name__ == '__main__':
    unittest.main()
