"""Implementation of the Bubble sort alogrithm

"""
__author__ = "Jakob Greiling"
__date__ = "2021-02"


# function


def sort(array_in):
    '''Bubble sort Algorithm to sort array in ascending order

    Parameters:
    -----------
    array_in: 
        array to be sorted by this function

    Returns:
    array_in: 
        sorted array

    '''

    len_array = len(array_in)
    for i in range(len_array):
        for j in range(len_array - (i + 1)):
            if(array_in[j] > array_in[j + 1]):
                array_in[j], array_in[j + 1] = array_in[j + 1], array_in[j]


# main Method
if __name__ == '__main__':
    array = [1, -3, 2, 7, 1]
    print(f"Array before sorting:\n {array}\n")
    sort(array)
    print(f"Array after sorting:\n {array}\n")

