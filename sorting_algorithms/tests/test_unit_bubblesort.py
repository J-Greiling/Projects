"""Testing for bubble.py using unittest"""
import unittest
import sys
import os


__author__ = "Jakob Greiling"
__date__ = "2021-02"

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', ))

import bubble


class TestFunctions(unittest.TestCase):
    def test_sort_simple(self):
        '''Test if Array is being sorted'''
        array = [2, 5, 1]
        bubble.sort(array)

        self.assertTrue(all(array[x] <= array[x + 1]
                            for x in range(len(array) - 1)))

    def test_negative_numbers(self):
        '''Test sorting behaviour with negative Numbers'''
        array = [-2, 5, 1]
        bubble.sort(array)

        self.assertTrue(all(array[x] <= array[x + 1]
                            for x in range(len(array) - 1)))

    def test_double_entries(self):
        '''Test sorting behaviour with double entries'''
        array = [2, 5, 2]
        bubble.sort(array)

        self.assertTrue(all(array[x] <= array[x + 1]
                            for x in range(len(array) - 1)))

    def test_single_entry(self):
        array = [2]
        bubble.sort(array)

        self.assertTrue(all(array[x] <= array[x + 1]
                            for x in range(len(array) - 1)))
