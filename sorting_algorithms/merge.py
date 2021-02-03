''' Implementation of merge sort'''

__author__ = "Jakob Greiling"
__date__ = "2021-02"


def sort(array):
    '''Implementation of Merge Sort using recursion

    parameters:
    array:
       array which should be sorted
    '''
    if len(array) > 1:
        mid = int(len(array) / 2)
        array_left = array[:mid]
        array_right = array[mid:]

        # recursive calls
        sort(array_left)
        sort(array_right)

        #sorting and remerge
        i = j = k = 0

        while i < len(array_left) and j < len(array_right):
            if array_left[i] < array_right[j]:
                array[k] = array_left[i]
                i += 1
            else:
                array[k] = array_right[j]
                j += 1
            k += 1

        while i < len(array_left):
            array[k] = array_left[i]
            i += 1
            k += 1

        while j < len(array_right):
            array[k] = array_right[j]
            j += 1
            k += 1


if __name__ == "__main__":
    array = [1, -3, 2, 2, 1]
    print(f"Array before sorting:\n {array}\n")
    sort(array)
    print(f"Array after sorting:\n {array}\n")





