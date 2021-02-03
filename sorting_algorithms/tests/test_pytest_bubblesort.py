"""Test file for bubble.py using pytest"""

import sys
import os

my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(my_path, '..', ))

import bubble
import numpy as np

__author__ = "Jakob Greiling"
__date__ = "2021-02"


def test_sorting():
    '''Test if Array is being sorted'''
    array_in = np.array([2, 5, 1])
    array_out = np.array([1, 2, 5])

    assert (array_out.all() == bubble.sort(array_in).all())


def test_negative():
    '''Handling of negative numbers'''
    array_in = np.array([2, -5, 1])
    array_out = np.array([-5, 1, 2])

    assert (array_out == bubble.sort(array_in)).all()


def test_double_entry():
    '''Handling of repeating numbers'''
    array_in = np.array([2, 5, 2])
    array_out = np.array([2, 2, 5])

    assert (array_out == bubble.sort(array_in)).all()


def test_single_entry():
    '''Handling 1 number'''
    array_in = np.array([2])
    array_out = np.array([2])

    assert (array_out == bubble.sort(array_in)).all()


def test_doubles():
    '''Handling of double values'''
    array_in = np.array([3.2, 2.9, 2.1])
    array_out = np.array([2.1, 2.9, 2, 3.2])

    assert (array_out == bubble.sort(array_in)).all()




