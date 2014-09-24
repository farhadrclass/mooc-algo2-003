#!/usr/bin/env python

"""
    test_a3.py
    ~~~~~~~~~~~~
    clear; python -m unittest discover -v

"""
from algorithms import knapsack
import unittest


class TestSequenceFunctions(unittest.TestCase):

    def _test_q1_naive(self):
        file_name = './data/a3/knapsack1.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        max_value = knapsack.knapsack_naive(knapsack_size, items)
        correct_answer = 2493893
        self.assertEquals(max_value, correct_answer)

    def _test_q2_naive(self):
        file_name = './data/a3/knapsack_big.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        max_value = knapsack.knapsack_naive(knapsack_size, items)
        correct_answer = 4243395
        self.assertEquals(max_value, correct_answer)

    def test_q1_smart(self):
        file_name = './data/a3/knapsack1.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        max_value = knapsack.knapsack_smart(knapsack_size, items)
        correct_answer = 2493893
        self.assertEquals(max_value, correct_answer)

    def test_q2_smart(self):
        file_name = './data/a3/knapsack_big.txt'
        knapsack_size, items = knapsack.load_data(file_name)
        max_value = knapsack.knapsack_smart(knapsack_size, items)
        correct_answer = 4243395
        self.assertEquals(max_value, correct_answer)
