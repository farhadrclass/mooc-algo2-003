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
    num_subproblems = 1
    current_set = set([knapsack_size])
    previous_set = set()

    for i in reversed(xrange(1,len(items))):
        for w_current in list(current_set):
            w_previous = items[i][1]
            previous_set.add(w_current)

            if w_current-w_previous >= 0:
                previous_set.add(w_current-w_previous)

        num_subproblems += len(previous_set)
        current_set = previous_set

    return num_subproblems

def get_subproblems_smart(knapsack_size, items):
    """Return dict of subproblems { item # : subproblem list } """
    subproblem_lookup = {(len(items)-1) : [knapsack_size]}
    current_set = set([knapsack_size])
    previous_set = set()

    for i in reversed(xrange(1,len(items))):
        for w_current in list(current_set):
            w_previous = items[i][1]
            previous_set.add(w_current)

            if w_current-w_previous >= 0:
                previous_set.add(w_current-w_previous)

        subproblem_lookup[i-1] = list(previous_set)
        current_set = previous_set
    return subproblem_lookup


def knapsack_smart(knapsack_size, items):
    subproblem_lookup = get_subproblems_smart(knapsack_size, items)
    previous_subproblems = {}

    for i, item in enumerate(items):
        current_subproblems = {}
        [value, weight] = item

        if i == 0:
            for x in subproblem_lookup[i]:
                if x - weight < 0:
                    current_subproblems[ x ] = 0
                else:
                    current_subproblems[ x ] = max(0, 0 + value)
        else:
            for x in subproblem_lookup[i]:
                if x - weight < 0:
                    current_subproblems[ x ] = previous_subproblems[ x ]
                else:
                    current_subproblems[ x ] = max(previous_subproblems[ x ], previous_subproblems[ x - weight ] + value)

        previous_subproblems = current_subproblems
        del current_subproblems

    return previous_subproblems[knapsack_size]
