#!/usr/bin/env python

"""
    test_q1.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""

import unittest

def load_data(file_name):
    items = []
    with open(file_name) as f:
        knapsack_size = int(f.readline().strip().split()[0])
        for line in f:
            items.append([int(n) for n in line.strip().split()])

    return items, knapsack_size


class TestSequenceFunctions(unittest.TestCase):

    def test_q1(self):
        file_name = './data/knapsack1.txt'
        items, knapsack_size = load_data(file_name)
        print items

