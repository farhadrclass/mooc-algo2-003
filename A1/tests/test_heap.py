#!/usr/bin/env python

from heap.heap import Node, Heap
import random
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass
        # self.file_name = 'edges.txt'
        # self.num_nodes, self.num_edges, self.node_matrix = load_data(
        #     self.file_name)
        # self.graph = generate_graph(self.node_matrix)

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
        self.assertTrue(heap[node.name] == node)

if __name__ == '__main__':
    unittest.main()
