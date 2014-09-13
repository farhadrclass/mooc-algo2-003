#!/usr/bin/env python

"""
    test_q1.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""
from algorithms import knapsack
import unittest





class TestSequenceFunctions(unittest.TestCase):

    def _test_small(self):
        file_name = './data/knapsack_test.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        max_value = knapsack.knapsack_naive(knapsack_size, items)
        print max_value

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



    def test_num_subproblems_smart_small(self):
        file_name = './data/knapsack_test.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        print items
        print sorted(items)
        num_subproblems = knapsack.num_subproblems_smart(knapsack_size, items)
        print num_subproblems

    def _test_num_subproblems_smart_q2(self):
        """# subproblems: 10623872"""
        file_name = './data/knapsack_big.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        num_subproblems = knapsack.num_subproblems_smart(knapsack_size, items)
        print num_subproblems

    def _test_num_subproblems_smart_q2_sorted(self):
        """ # subproblems: 10587432 """
        file_name = './data/knapsack_big.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        items = sorted(items)
        num_subproblems = knapsack.num_subproblems_smart(knapsack_size, items)
        print num_subproblems

    def _test_num_subproblems_smart_q2_sorted_rev(self):
        """ # subproblems: 10673022 """
        file_name = './data/knapsack_big.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        items.sort()
        items.reverse()
        num_subproblems = knapsack.num_subproblems_smart(knapsack_size, items)
        print num_subproblems
