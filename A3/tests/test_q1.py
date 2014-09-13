#!/usr/bin/env python

"""
    test_q1.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""
from algorithms import knapsack
import unittest





class TestSequenceFunctions(unittest.TestCase):

    def _test_q1(self):
        file_name = './data/knapsack1.txt'
        knapsack_size, items = lknapsack.oad_data(file_name)
        max_value = knapsack.knapsack_naive(knapsack_size, items)
        print max_value

    def _test_q2(self):
        file_name = './data/knapsack_big.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        max_value = knapsack.knapsack_naive(knapsack_size, items)
        print max_value

    def test_small(self):
        file_name = './data/knapsack_test.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        max_value = knapsack.knapsack_naive(knapsack_size, items)
        print max_value
