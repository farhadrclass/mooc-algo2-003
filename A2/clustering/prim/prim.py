#!/usr/bin/env python

"""
    prim.py
    ~~~~~~~~~~~~
    Prim's MST algorithmf from assignment 1

"""

from heap import Node, Heap
from collections import defaultdict
import numpy
import random
import unittest



def prim(graph):
    """
    Implements Prim's Minimum Spanning Tree Algorithm in O(VlogE) time with a min heap.
    """
    mst = defaultdict(dict)
    initial_node = random.choice(graph.keys())

    # Initialize minimum heap to contain the nodes of the graph, whose keys
    # are the edge values
    crossing_cuts = Heap([((float("inf"), float("inf")), int(node))
                          for node in graph.keys() if node != initial_node])

    # Populate min heap with initial node's crossing cuts
    for node_name in graph[initial_node].keys():
        new_key = (graph[initial_node][node_name], initial_node)
        crossing_cuts.update_key(node_name, new_key)

    # Pop nodes from minimum heap until minimum spanning tree is formed
    while crossing_cuts:
        smallest_node = crossing_cuts.pop()
        (node_out, (weight, node_in)) = smallest_node.name, smallest_node.key
        mst[node_in][node_out] = weight
        mst[node_out][node_in] = weight

        for node_name in (set(graph[node_out].keys()) - set(mst.keys())):
            new_key = (graph[node_out][node_name], node_out)
            if node_name in crossing_cuts.node_names():
                old_key = crossing_cuts[node_name].key
                if new_key[0] < old_key[0]:
                    crossing_cuts.update_key(node_name, new_key)

    return mst

def get_mst_total_weight(graph):
    total_cost = 0
    for node in graph.keys():
        total_cost += sum(graph[node].values())
    total_cost /= 2
    return total_cost
