#!/usr/bin/env python

"""
    test_a1.py
    ~~~~~~~~~~~~
    For Programming Assignment #1, Algorithms: Design and Analysis Part 2 (https://class.coursera.org/algo2-003)

    Implements a job scheduler by minimizing weighted completion time according to a either a difference or ratio of weight to job length; nothing fancy.

    runtime:
    real    0m0.643s
    user    0m0.610s
    sys     0m0.029s
"""

import numpy
import unittest
from algorithms import prim
from collections import Counter, defaultdict


def load_data(file_name, skiprows=1):
    job_matrix = numpy.loadtxt(file_name, skiprows=skiprows)
    num_jobs = job_matrix.shape[0]
    return num_jobs, job_matrix


def compute_weighted_completion_times(sorted_job_matrix):
    weighted_completion_time = 0
    num_jobs = len(sorted_job_matrix)
    completion_time = 0
    for index, job in enumerate(sorted_job_matrix):
        weight = job[0]
        completion_time += job[1]
        weighted_completion_time += weight * completion_time

    return weighted_completion_time


def schedule_jobs(job_matrix, mode='ratio'):
    job_weight = job_matrix[:, 0]
    job_length = job_matrix[:, 1]
    if mode == 'difference':
        job_metric = numpy.subtract(job_weight, job_length)
        job_matrix = numpy.vstack((job_weight, job_length, job_metric)).T
        job_matrix = job_matrix[job_matrix[:, 2].argsort()]
        job_matrix = numpy.flipud(job_matrix)

        metric_value_freq = Counter(job_matrix[:, 2])

        # Break ties between jobs using weight (i.e. higher weight goes first)
        i = 0
        for key in sorted(metric_value_freq.keys(), reverse=True):
            subarray = job_matrix[i:i + metric_value_freq[key]]
            sorted_subarray = subarray[subarray[:, 0].argsort()]
            sorted_subarray = numpy.flipud(sorted_subarray)
            job_matrix[i:i + metric_value_freq[key]] = sorted_subarray
            i += metric_value_freq[key]

    elif mode == 'ratio':
        job_metric = numpy.divide(job_weight, job_length)

        job_matrix = numpy.vstack((job_weight, job_length, job_metric)).T
        job_matrix = job_matrix[job_matrix[:, 2].argsort()]
        job_matrix = numpy.flipud(job_matrix)

    return job_matrix

def load_data_q3(file_name, skiprows=1):
    """ Returns matrix of  node and edges from edges.txt"""
    with open(file_name, 'r') as f:
        num_nodes, num_edges = [int(n) for n in f.readline().strip().split()]

    node_matrix = numpy.loadtxt(file_name, skiprows=skiprows)

    return node_matrix


def generate_graph(node_matrix):
    """Takes as input a matrix where rows are edges and columns are [node1 node2 weight]"""
    graph = defaultdict(dict)

    for item in node_matrix:
        node1, node2, weight = [int(n) for n in item]
        graph[node1][node2] = weight
        graph[node2][node1] = weight

    return graph


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.num_jobs, self.job_matrix = load_data('./data/a1/jobs.txt')

    def test_q1(self):
        mode = 'difference'
        sorted_job_matrix = schedule_jobs(self.job_matrix, mode=mode)
        weighted_completion_time = compute_weighted_completion_times(sorted_job_matrix)
        correct_answer = 69119377652
        self.assertEquals(weighted_completion_time, correct_answer)

    def test_q2(self):
        mode = 'ratio'
        sorted_job_matrix = schedule_jobs(self.job_matrix, mode=mode)
        weighted_completion_time = compute_weighted_completion_times(sorted_job_matrix)
        correct_answer = 67311454237
        self.assertEquals(weighted_completion_time, correct_answer)

    def test_q3(self):
        self.node_matrix = load_data_q3('./data/a1/edges.txt')
        self.graph = generate_graph(self.node_matrix)
        minimum_spanning_tree = prim.prim(self.graph)
        total_cost = 0
        for node in minimum_spanning_tree.keys():
            total_cost += sum(minimum_spanning_tree[node].values())

        # Divide total by 2 so that we don't double count
        total_cost = total_cost / 2
        correct_answer = -3612829
        self.assertEquals(total_cost, correct_answer)
