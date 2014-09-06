#!/usr/bin/env python

"""
    test_clustering.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""
from clustering.clustering import UnionFind
import random
import unittest

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
        print leader1, leader2
        print union_find.set_lookup
        self.assertTrue
