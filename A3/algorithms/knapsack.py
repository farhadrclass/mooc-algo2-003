#!/usr/bin/env python

"""
    knapsack.py
    ~~~~~~~~~~~~

"""

def load_data(file_name):
    items = []
    with open(file_name) as f:
        knapsack_size = int(f.readline().strip().split()[0])
        for line in f:
            items.append([int(n) for n in line.strip().split()])

    return knapsack_size, items

def knapsack_naive(knapsack_size, items):
    subproblems = [[0 for x in xrange(knapsack_size)] for i in xrange(len(items))]

    for i in xrange(1, len(items)):
        for x in xrange(knapsack_size):
            [value, weight] = items[i]
            if x - weight < 0:
                subproblems[ i ][ x ] = subproblems[ i - 1 ][ x ]
            else:
                subproblems[ i ][ x ] = max(subproblems[ i - 1 ][ x ], subproblems[ i -1 ][ x - weight ] + value)

    return subproblems[-1][-1]

def num_subproblems_naive(knapsack_size, items):
    return knapsack_size * len(items)

def num_subproblems_smart(knapsack_size, items):
    current_set = set(knapsack_size)
    previous_set = set()

    for i in xrange(len(items)):

        current_set = previous_set



def knapsack_smart(knapsack_size, items):
    subproblems = [[0 for x in xrange(knapsack_size)] for i in xrange(len(items))]

    for i in xrange(1, len(items)):
        for x in xrange(knapsack_size):
            [value, weight] = items[i]
            if x - weight < 0:
                subproblems[ i ][ x ] = subproblems[ i - 1 ][ x ]
            else:
                subproblems[ i ][ x ] = max(subproblems[ i - 1 ][ x ], subproblems[ i -1 ][ x - weight ] + value)

    return subproblems[-1][-1]
