import random
import insertion_sort
import merge_sort
import counting_sort

TEST_LIST = [random.random() for _ in range(0, 10000)]
MAX_TEST_LIST = max(TEST_LIST)

def insertion_sort_test():
    return insertion_sort.insertionSort(TEST_LIST)

def merge_sort_test():
    return merge_sort.mergeSort(TEST_LIST)

def counting_sort_test():
    return counting_sort.countingSort(TEST_LIST, MAX_TEST_LIST)
