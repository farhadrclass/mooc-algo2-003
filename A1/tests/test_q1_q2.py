#!/usr/bin/env python

"""
    test_q1_q2.py
    ~~~~~~~~~~~~
    For Programming Assignment #1, Algorithms: Design and Analysis Part 2 (https://class.coursera.org/algo2-003)

    Implements a job scheduler by minimizing weighted completion time according to a either a difference or ratio of weight to job length; nothing fancy.
"""

import numpy
import unittest
from collections import Counter


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


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.num_jobs, self.job_matrix = load_data('./data/jobs.txt')


    def test_schedule_jobs_by_difference(self):
        mode = 'difference'
        sorted_job_matrix = schedule_jobs(self.job_matrix, mode=mode)
        weighted_completion_time = compute_weighted_completion_times(
            sorted_job_matrix)

        print "Weighted completion time with (weight - job length) metric: {}".format(weighted_completion_time)


    def test_schedule_jobs_by_ratio(self):
        mode = 'ratio'
        sorted_job_matrix = schedule_jobs(self.job_matrix, mode=mode)
        weighted_completion_time = compute_weighted_completion_times(
            sorted_job_matrix)
        print "Weighted completion time with (weight/job length) metric: {}".format(weighted_completion_time)

