#!/usr/bin/env python

from heap.heap import Heap
import random
import unittest


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):

        self.file_name = 'edges.txt'
        self.num_nodes, self.num_edges, self.node_matrix = load_data(
            self.file_name)
        self.graph = generate_graph(self.node_matrix)

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
