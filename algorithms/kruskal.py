#!/usr/bin/env python

"""
    kruskal.py
    ~~~~~~~~~~~~

"""

from collections import defaultdict
from data_structures.union_find import UnionFind
from itertools import combinations
import string


def kruskal(node_list, edge_list):
    edge_list.sort()
    mst = defaultdict(dict)  # minimum spanning tree
    union_find = UnionFind(nodes=node_list)
    for edge in edge_list:
        weight, node1, node2 = edge
        if union_find.find(node1) != union_find.find(node2):
            union_find.union(node1, node2)
            mst[node1][node2] = weight
            mst[node2][node1] = weight
        else:
            continue

    return mst


def maximum_spacing(node_list=[], edge_list=[], k=0):
    """ Returns maximum spacing between k clusters"""
    edge_order = []
    # mst = defaultdict(dict)
    union_find = UnionFind(nodes=node_list)

    edge_list.sort()

    for edge in edge_list:
        weight, node1, node2 = edge
        if union_find.find(node1) != union_find.find(node2):
            union_find.union(node1, node2)
            # mst[node1][node2] = weight
            # mst[node2][node1] = weight
            edge_order.append(edge)
        else:
            continue

    return edge_order[-(k - 1)][0]


def get_bitmasks(length=24):
    swap = {'0': '1', '1': '0'}
    bitmasks = {}

    for pos in xrange(length):
        mask = ['0' for i in xrange(length)]
        mask[pos] = swap[mask[pos]]
        bitmasks[pos] = int(string.join(mask, ''), 2)

    return bitmasks


def maximum_k(node_list=[], node_length=24, maximum_spacing=3):
    """ Input:
            list of nodes (edges defined implictly by Hamming distances between nodes)
        Output:
            max number of clusters with specified maximum spacing
        Method:
            BRUTE FORCE
            For each node iterate through all permuations of possible n-bit differences  from 1 up to max_spacing - 1.
                For example, for max_spacing = 3, node length 24 bits, the number of permutations is (24 C 1) + (24 C 2) = 300.
    """

    node_set = set(node_list)
    node_list = list(node_set)
    union_find = UnionFind(nodes=node_list)
    bitmasks = get_bitmasks(node_length)

    for node1 in node_list:
        for i in xrange(1, maximum_spacing):
            for permutation in combinations(xrange(node_length), i):
                node2 = node1
                for pos in permutation:
                    node2 ^= bitmasks[pos]
                if node2 in node_set:
                    if union_find.find(node1) != union_find.find(node2):
                        union_find.union(node1, node2)

    return len(set(union_find.leader_lookup.values()))
