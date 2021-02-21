def binary_search(array, item, begin=0, end=None):
    if end is None:
        end = len(array)-1

    if begin > end:
        return None

    middle = (begin + end) // 2

    if array[middle] == item:
        return middle
    if item < array[middle]:
        return binary_search(array, item, begin, middle-1)
    return binary_search(array, item, middle+1, end)
