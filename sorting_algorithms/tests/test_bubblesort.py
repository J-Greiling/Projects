"""Test file for bubble_sort.py"""
import sys
import os

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(my_path, '..', ))


import bubble_sort
import numpy as np


def test_sorting():
    '''Test if Array is being sorted'''
    array_in = np.array([2, 5, 1], np.int32)
    array_out = np.array([1, 2, 5], np.int32)

    assert (array_out == bubble_sort.sort(array_in)).all()



