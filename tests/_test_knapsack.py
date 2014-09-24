#!/usr/bin/env python

"""
    test_knapsack.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""
from algorithms import knapsack
import unittest


class TestSequenceFunctions(unittest.TestCase):

    def test_small_naive(self):
        file_name = './data/a3/knapsack_test.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        max_value = knapsack.knapsack_naive(knapsack_size, items)
        correct_answer = 8
        self.assertEquals(max_value, correct_answer)

    def test_small_smart(self):
        file_name = './data/a3/knapsack_test.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        max_value = knapsack.knapsack_smart(knapsack_size, items)
        correct_answer = 8
        self.assertEquals(max_value, correct_answer)

    def _test_num_subproblems_smart_small(self):
        file_name = './data/a3/knapsack_test.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        num_subproblems = knapsack.num_subproblems_smart(knapsack_size, items)
        print num_subproblems

    def _test_num_subproblems_smart_q2(self):
        """ # subproblems: 10623872.
            max # subproblems for w = 0...capacity : 5421
            sorting the items doesn't change the number of subproblems, as expected.
        """
        file_name = './data/a3/knapsack_big.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        num_subproblems = knapsack.num_subproblems_smart(knapsack_size, items)
        print num_subproblems

    def _test_get_subproblems_smart_small(self):
        file_name = './data/a3/knapsack_test.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        num_subproblems = knapsack.get_subproblems_smart(knapsack_size, items)
        print num_subproblems

    def _test_get_subproblems_smart_big(self):
        file_name = './data/a3/knapsack_big.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        num_subproblems = knapsack.get_subproblems_smart(knapsack_size, items)
        print num_subproblems

