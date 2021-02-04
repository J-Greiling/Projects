"""Test file for merge.py using pytest"""

import sys
import os

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', ))

import merge

__author__ = "Jakob Greiling"
__date__ = "2021-02"


def test_sorting():
    '''Test if Array is being sorted'''
    array = [2, 5, 1]
    merge.sort(array)

    assert all(array[x] <= array[x + 1] for x in range(len(array) - 1))


def test_negative():
    '''Handling of negative numbers'''
    array = [2, -5, 1]
    merge.sort(array)

    assert all(array[x] <= array[x + 1] for x in range(len(array) - 1))


def test_double_entry():
    '''Handling of repeating numbers'''
    array = [2, 5, 2]
    merge.sort(array)

    assert all(array[x] <= array[x + 1] for x in range(len(array) - 1))


def test_single_entry():
    '''Handling 1 number'''
    array = [2]
    merge.sort(array)

    assert all(array[x] <= array[x + 1] for x in range(len(array) - 1))


def test_doubles():
    '''Handling of double values'''
    array = [3.1, 2.9, 2.4]
    merge.sort(array)

    assert all(array[x] <= array[x + 1] for x in range(len(array) - 1))




