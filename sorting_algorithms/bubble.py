"""Implementation of the Bubble sort alogrithm

"""
__author__ = "Jakob Greiling"
__date__ = "2021-02"

import numpy as np

# function


def sort(array: np.ndarray) -> np.ndarray:
    '''Bubble sort Algorithm to sort array in ascending order

    Parameters:
    -----------
    array: np.array
        array to be sorted by this function

    Returns:
    array: np.array
        sorted array

    '''
    len_array = array.size
    for i in range(len_array):
        for j in range(len_array - (i + 1)):
            if(array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# main Method
if __name__ == '__main__':
    array = np.array([1, -3, 2, 7, 1], np.int32)
    print(f"Array before sortig:\n {array}\n")
    array = sort(array)
    print(f"Array after sorting:\n {array}\n")

