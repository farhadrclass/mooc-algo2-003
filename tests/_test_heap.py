#!/usr/bin/env python

"""
    test_heap.py
    ~~~~~~~~~~~~
    Tests for heap.py to ensure it implements insert, delete, pop operations correctly while maintaining the heap invariant that all parent nodes < children nodes.

    runtime:
    real    0m0.221s
    user    0m0.189s
    sys 0m0.028s

"""

from data_structures.heap import Node, Heap
import random
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.heap = Heap([(int(x), str(x))
                          for x in random.sample(xrange(10, 90), 10)])

    def test_Node_init(self):
        node = Node(name="name", key="key")
        node.pos = 0
        self.assertTrue(
            all((node.name == "name", node.key == "key", node.pos == 0)))

    def test_Node_cmp(self):
        node1 = Node(20, "node1")
        node2 = Node(1, "node2")
        self.assertTrue(node2 < node1)

    def test_Heap_init(self):
        node1 = (20, "node1")
        node2 = (1, "node2")
        self.heap = Heap([node1, node2], named=True)
        self.assertTrue(
            self.heap["node1"].pos == 1 and self.heap["node2"].pos == 0)

    def test_Heap_bubble_up(self):
        node = Node(1, "1")
        node.pos = len(self.heap.node_array)
        self.heap.node_array.append(node)
        self.heap.node_lookup[node.name] = node.pos

        self.assertFalse(self.heap.is_heap_property_satisfied())
        self.heap.bubble_up()
        self.assertTrue(self.heap.is_heap_property_satisfied())

    def test_Heap_bubble_down(self):
        node = Node(100, "100")
        node.pos = 0
        self.heap.node_array[0] = node

        self.assertFalse(self.heap.is_heap_property_satisfied())
        self.heap.bubble_down()
        self.assertTrue(self.heap.is_heap_property_satisfied())

    def test_Heap_getitem(self):
        node = random.choice(self.heap.node_array)
        self.assertTrue(self.heap[node.name] == node)

    def test_Heap_insert(self):
        node = Node(1000, "1000")
        self.assertTrue(self.heap.is_heap_property_satisfied())
        self.heap.insert(node)
        self.assertTrue(self.heap.is_heap_property_satisfied())

    def test_Heap_delete_first(self):
        node = random.choice(self.heap.node_array)
        node = self.heap.node_array[0]
        self.assertTrue(self.heap.is_heap_property_satisfied())
        self.heap.delete(node)
        self.assertTrue(self.heap.is_heap_property_satisfied())

    def test_Heap_delete_last(self):
        node = self.heap.node_array[-1]
        self.assertTrue(self.heap.is_heap_property_satisfied())
        self.heap.delete(node)
        self.assertTrue(self.heap.is_heap_property_satisfied())

    def test_Heap_delete_random(self):
        node = random.choice(self.heap.node_array)
        self.assertTrue(self.heap.is_heap_property_satisfied())
        self.heap.delete(node)
        self.assertTrue(self.heap.is_heap_property_satisfied())

    def test_Heap_pop(self):
        min_node = self.heap.node_array[0]
        popped_node = self.heap.pop()
        self.assertTrue(self.heap.is_heap_property_satisfied())
        self.assertTrue(popped_node == min_node)

    def test_Heap_update_key(self):
        node = random.choice(self.heap.node_array)
        node_name = node.name
        new_key = random.choice(xrange(0, 1000))
        self.heap.update_key(node_name, new_key)
        self.assertTrue(self.heap.is_heap_property_satisfied())

