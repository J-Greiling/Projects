"""Testing for bubble.py using unittest"""
import unittest
import sys
import os
import numpy as np

__author__ = "Jakob Greiling"
__date__ = "2021-02"

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', ))

import bubble


class TestFunctions(unittest.TestCase):
    def test_sort_simple(self):
        '''Test if Array is being sorted'''
        array_in = np.array([2, 5, 1])
        array_out = np.array([1, 2, 5])

        self.assertEqual(array_out.all(), bubble.sort(array_in).all())

    def test_negative_numbers(self):
        '''Test sorting behaviour with negative Numbers'''
        array_in = np.array([-2, 5, 1])
        array_out = np.array([-2, 1, 5])

        self.assertEqual(array_out.all(), bubble.sort(array_in).all())

    def test_double_entries(self):
        '''Test sorting behaviour with double entries'''
        array_in = np.array([2, 5, 2])
        array_out = np.array([2, 2, 5])

        self.assertEqual(array_out.all(), bubble.sort(array_in).all())

    def test_single_entry(self):
        array_in = np.array([2])
        array_out = np.array([2])

        self.assertEqual(array_out.all(), bubble.sort(array_in).all())
